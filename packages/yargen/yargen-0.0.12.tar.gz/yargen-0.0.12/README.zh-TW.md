[English](README.md) | 繁體中文 

# Yargen 插件用於 IDA Pro

## 簡介
Yargen 是一款為 IDA Pro 設計的創新插件，旨在簡化 YARA 分析過程。通過整合 CAPA 框架的功能，Yargen 為執行檔案的能力檢測和文件化提供了一種無縫且高效的體驗。透過簡單的 `Alt+Y` 快捷方式激活，Yargen 為新手和經驗豐富的分析師提供了一個簡化的分析工作流程。

## 功能特性
- **簡化 YARA 分析**：簡化了將 YARA 規則應用於二進制文件的過程，使分析更易於訪問。
- **NetNode 探索**：自動掃描並在 IDA Pro 中顯示 CAPA netnodes，突出關鍵的分析發現。
- **數據序列化**：提供自定義的 JSON 序列化以增強數據處理，允許清晰呈現分析結果。
- **結果導出**：促進將分析結果導出為 JSON 和 Excel 格式，使深入檢查和文件化成為可能。
- **用戶路徑選擇**：提供在保存文件時的靈活性，允許用戶選擇將文件保存到桌面或插件特定的緩存目錄。

## 安裝
1. 確保您的系統上安裝了 IDA Pro 8.3 版和 CAPA 7.0.1 版。
2. 克隆或下載 Yargen 插件倉庫到您的本地機器。
3. 將 `yargen.py` 文件複製到您的 IDA Pro 安裝目錄下的 `plugins` 目錄中。
4. 重新啟動 IDA Pro 自動加載插件。

## 使用方法
要啟動 Yargen 插件，請打開一個執行檔案與 IDA Pro 並按下 `Alt+Y`。遵循直觀的界面來進行 YARA 分析，探索 netnodes，並輕鬆導出分析結果。

## 原理
Yargen 插件致力於通過整合 CAPA 框架使 IDA Pro 中的 YARA 分析更容易接近。它利用 Python 腳本和 IDA Pro 的廣泛 API 提供了一種用戶友好的二進制分析方法、數據序列化和結果導出，增強了整體的分析工作流程。

## 貢獻
我們歡迎貢獻以改善 Yargen 插件。請隨意 Fork 倉庫，進行您的修改，並提交 Pull 請求。對於討論和建議，請在倉庫中開啟一個問題。

## 許可證
Yargen 根據 [MIT 許可證](LICENSE) 提供。此許可證允許廣泛使用，促進插件的開放使用、修改和分發。更多細節，請查看倉庫中的 LICENSE 文件。

## 聯繫方式
- Zhao-Xinn: zhaoxinzhang0429@gmail.com
- Tsai, YA-HSUAN: aooood456@gmail.com
- Ting0525: zg45154551@gmail.com
