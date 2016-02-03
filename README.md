# GraphwalkerRunner
    說明：以Graphwalker的核心架構下，新增特殊功能的整合工具。
    增添功能： 1.圖形合併 2. 圖形完整性驗證 3. Grapgwalker運行 4. 錯誤續跑機制 5. 畫面截圖。
    
    注：What is GraphWalker?
        It's a Model-Based testing tool built in Java. 
        It reads models in the shape of finite-state diagrams, or directed graphs, 
        and generate tests from the models, either offline or online.
    
# Install 

### 下載執行檔並執行

說明：此執行檔為單個可執行的程式，不需要另外安裝所需library，安裝指令如下方"Install command"中，執行完後，即可於全域執行。

*   下載：[Ubuntu executable](https://justup.9ifriend.com/share.html?id=cc9139b0-8094-4ba0-8d03-72dc6e483ff4)
    
    註：備用執行程式：Graphwalker_Runner.py，此方式需要安裝所需的lib。

### Install command
*    `$ sudo ./Graphwalker_Runner`
    
### 全域執行：
*   `Graphwalker [arguments]`

# How to Run：

    usage: Graphwalker_Runner [-h] [-u UPDATE] [-m MODEL] [-c] [-r]
    optional arguments:
        -h , --help     Show this help message and exit
        -i , --init     Init graphwalker environment
        -u , --update   Update graphwalker source code
        -m , --model    It's will merge graphml files in folder ,
                        example：Graphwalker_Runner -m 'folder path'
        -c , --check    Check graphical integrity, output Not visited points file
        -r , --run      Running graphwalker
        -s , --shot     Screenshot when graphwalker running, parameter: 'pc' or 'mobile'
                        example：Graphwalker_Runner -s pc[mobile]
        -S , --Stop     Set stop condition, default parameter：'random(edge_coverage(100))'
                        example：Graphwalker_Runner -S 'random(edge_coverage(100))'
        -v , --version  Show version number and change notes
                        parameter:'new' (show lastest info) or 'all' (show all versioninfo)
                        example: Graphwalker_Runner -v new[all]


#### Init environment

    說明：移除現有環境，並重新於本地端建立一個全新的Graphwalker tool。
        自動建立Graphwalker Runner環境的流程如下：
            1. clone graphwalker工具 (from github)
            2. 於本地端建立執行環境 (path:/usr/local/GraphwalkerRunner)
            3. 下載graphwalker-cli-SNAPSHOT.jar
            註：如果下載失敗，請手動下載，並放置在：/usr/local/GraphwalkerRunner/lib。
        
    syntax：Graphwalker_Runner -i
    example:
    $ sudo ./Graphwalker_Runner
    git clone code...
    [sudo] password for jeremy: 
    remote: Counting objects: 822, done.
    remote: Compressing objects: 100% (10/10), done.
    remote: Total 822 (delta 3), reused 0 (delta 0), pack-reused 812
       .   
       .  
       .   
    chmod folder...

#### Version


    說明：查詢版本，回傳"版號"與"Change note"。
         參數: new (顯示最新版本的資訊) or all (顯示所有版本資訊) 。
    syntax：Graphwalker_Runner -v [ new | all ]
    
#### Update code

    說明：從github拉新的code。
    syntax：Graphwalker_Runner -u
    
#### Merge graph

    說明：合併資料夾內所有Graphml子圖。
    syntax：Graphwalker_Runner -m 'graphml folder path'
    

#### Check graphical integrity

    說明：確認script.py內所有的function是否均被執行到。
         回傳值：True(全部已執行); False(有function未執行，或執行步數達到限制條件Stop condition：(edge+vertex)^2)
    syntax：Graphwalker_Runner -c
#### Running graphwalker

    說明：執行Graphewalker測試。
    syntax：Graphwalker_Runner -r
#### Screenshot when testing

    說明：執行Graphewalker測試與錯誤發生時照下當前畫面
         參數：pc(當前測試裝置為桌電) or mobile(當前測試裝置為行動裝置)。
    syntax：Graphwalker_Runner -r -s [ pc | mobile ]
#### Set stop condition

    說明：設置停止條件，預設為"random(edge_coverage(100))"。
         更多停止條件用法請參考下方"Stop conditions Documentation"
    syntax：Graphwalker_Runner -r -S "stop condition"
    
# Q&A

    1:
        Q：TypeError: argument of type 'NoneType' is not iterable >>
        A：此錯誤為有頂點或邊沒有命名(常見的錯誤：多拉了一條線)
    2:
        Q：Cannot assign requested address    
        A：原因：主要是太頻繁的連接伺服器，由於每次都在很短的時間內結束，導致很多TIME_WAIT，以至於用光可以用的端口。
            所以新的連接無法綁定成功，通過netstat，的確看到很多TIME_WAIT狀態的連接。
           解決方法：執行修改如下兩個內核参数 （需要root權限） 
            sysctl -w net.ipv4.tcp_timestamps=1  開啟對於TCP時間戳的支持,若該項設置為0，則下面一項設置不起作用
            sysctl -w net.ipv4.tcp_tw_recycle=1  標示開啟TCP連接中TIME-WAIT sockets的快速回收

# Reference

*   [Graphwalker官網](http://graphwalker.org/)
*   下載 [graphwalker-cli-SNAPSHOT.jar](https://justup.9ifriend.com/share.html?id=c84d674b-c645-4a2b-a5f0-8afd931b005e)
*   [Stop conditions Documentation](http://graphwalker.org/docs/path_generators_and_stop_conditions)
