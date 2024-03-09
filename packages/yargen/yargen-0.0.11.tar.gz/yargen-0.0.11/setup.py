from setuptools import setup, find_packages

# 使用 with 語句和指定編碼來打開 README.md
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='yargen',
    version='0.0.11',
    author='zhaoxinnZ',
    author_email='zhaoxinzhang0429@gmail.com',
    description='一個簡短的專案描述',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zhaoxinnZ/Yargen',
    packages=find_packages(),
    classifiers=[
        # 看 setuptools 文檔以獲取完整列表
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
    ],
)
