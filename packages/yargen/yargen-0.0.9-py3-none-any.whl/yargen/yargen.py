import re
import idaapi
import ida_netnode
import ida_kernwin
import json
import pandas as pd
from pathlib import Path
import capa.ida.helpers
from datetime import datetime
import idautils
import ida_lines
from ida_lines import GENDSM_REMOVE_TAGS

class YargenPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "Yargen Plugin for IDA Pro"
    help = "Yargen Plugin"
    wanted_name = "Yargen"
    wanted_hotkey = "Alt-Y"

    def init(self):
        print("Yargen plugin initialized")
        return idaapi.PLUGIN_OK

    def term(self):
        print("Yargen plugin terminated")

    def get_cache_dir(self):
        plugin_dir = Path(__file__).parent
        cache_dir = plugin_dir / "yargen_cache"
        cache_dir.mkdir(exist_ok=True)
        return cache_dir

    def custom_json_serializer(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

    def explore_netnodes(self):
        n = ida_netnode.netnode()
        if n.start():
            while True:
                name = n.get_name()
                if name and "$ com.mandiant.capa" in name:
                    print("Found CAPA netnode:", name)
                if not n.next():
                    break

    def pretty_dump(self, save_path):
        result_document = capa.ida.helpers.load_and_verify_cached_results()
        if result_document:
            json_data = json.dumps(result_document.model_dump(), default=self.custom_json_serializer, indent=4,
                                   ensure_ascii=False)
            output_file_path = save_path / 'result_document_pretty.json'
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(json_data)
            print(f"ResultDocument 已保存到 {output_file_path}")
        else:
            print("未找到 CAPA 結果或加載失敗。")

    def ask_user_for_path(self):
        desktop_path = Path.home() / 'Desktop'
        choice = ida_kernwin.ask_buttons("Desktop", "Cache", None, 1, "Choose the destination for the Excel file.")
        return desktop_path if choice == 1 else self.get_cache_dir()

    def extract_data_with_address(self, rule_name, matches, collected_data):
        for match_list in matches:
            for match in match_list:
                if match.get('type') == 'absolute':
                    match_value = match.get('value', 0)
                    match_value_hex = hex(int(match_value)) if match_value else '0x0'
                    instructions = self.get_instructions_for_address(int(match_value))
                    collected_data.append({
                        'Rule Name': rule_name,
                        'Match Type': match.get('type', ''),
                        'Value': match_value,
                        'Address': match_value_hex,
                        'Instructions': instructions
                    })

    def get_instructions_for_address(self, addr):
        func = idaapi.get_func(addr)
        if not func:
            return f"Address 0x{addr:X} does not belong to any function."

        fci = idaapi.FlowChart(func)
        instructions = []
        for b in fci:
            if b.start_ea <= addr < b.end_ea:
                for head in idautils.Heads(b.start_ea, b.end_ea):
                    disasm_line = ida_lines.generate_disasm_line(head, GENDSM_REMOVE_TAGS)
                    if disasm_line:
                        instructions.append(f"0x{head:X}: {disasm_line}")
        return instructions

    def run(self, arg):
        self.explore_netnodes()

        # 獲取用戶選擇的保存路徑
        save_path = self.ask_user_for_path()

        # 在 cache 目錄下創建 sample_instructions 子資料夾
        sample_instructions_path = self.get_cache_dir() / "sample_instructions"
        sample_instructions_path.mkdir(exist_ok=True)

        # 根據用戶選擇的保存路徑生成 pretty dump
        self.pretty_dump(save_path)

        json_file_path = save_path / "result_document_pretty.json"

        # 使用idautils獲取當前分析檔案的MD5 hash
        md5_hash = idautils.GetInputFileMD5().hex()

        if json_file_path.is_file():
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            all_data = []
            if data and 'rules' in data:
                for rule_name, rule_details in data['rules'].items():
                    if 'matches' in rule_details:
                        self.extract_data_with_address(rule_name, rule_details['matches'], all_data)

            # 使用md5 hash值作為文件名，並保存在 sample_instructions 子資料夾中
            instructions_json_path = sample_instructions_path / f"{md5_hash}.json"
            with instructions_json_path.open('w', encoding='utf-8') as f:
                json.dump(all_data, f, ensure_ascii=False, indent=4)

            print(f"指令集已導出到 {instructions_json_path}")
        else:
            print(f"未能生成或找到 JSON 文件: {json_file_path}")

def PLUGIN_ENTRY():
    return YargenPlugin()
