# GraphwalkerRunner
    說明：以Graphwalker的核心架構下，新增特殊功能的整合工具。
    增添功能： 1.圖形合併 2. 圖形完整性驗證 3. Grapgwalker運行 4. 錯誤續跑機制
    
    注：What is GraphWalker?
        It's a Model-Based testing tool built in Java. 
        It reads models in the shape of finite-state diagrams, or directed graphs, and generate tests from the models, either offline or online.
    
# Install 

1. 下載執行檔:下載Graphwalker_Runner(執行檔)
    1. 下載Graphwalker_Runner.py
    2. 執行檔Download URL:https://justup.9ifriend.com/share.html?id=cc9139b0-8094-4ba0-8d03-72dc6e483ff4

2. 建立Graphwalker Runner環境

    Step：
    1. clone graphwalker工具 (from github)
    2. 於本地端建立執行環境 (path:/usr/local/GraphwalkerRunner)
    3. 下載graphwalker-cli-SNAPSHOT.jar    (ps：如果下載失敗，請手動下載，URL：https://justup.9ifriend.com/share.html?id=c84d674b-c645-4a2b-a5f0-8afd931b005e，並放置在：/usr/local/GraphwalkerRunner/lib)

Install command：$ sudo ./Graphwalker_Runner


# How to Run：

    usage: Graphwalker_Runner [-h] [-u UPDATE] [-m MODEL] [-c] [-r]
    optional arguments:
    -h, --help            show this help message and exit
    -u UPDATE, --update UPDATE update graphwalker source code
    -m MODEL, --model MODEL merge graph ,please input graph folder
    -c, --check           Check graphical integrity
    -r, --run             running graphwalker

#### merge graph
    example：./Graphwalker_Runner -m 'graphml folder path'
#### Check graphical integrity
    example：./Graphwalker_Runner -c
#### running graphwalker
    example：./Graphwalker_Runner -r

# Reference
    graphwalker：http://graphwalker.org/
