# GraphwalkerRunner
    說明：以Graphwalker的核心架構下，新增特殊功能的整合工具。
    增添功能： 1.圖形合併 2. 圖形完整性驗證 3. Grapgwalker運行 4. 錯誤續跑機制 5. 畫面截圖。
    
    注：What is GraphWalker?
        It's a Model-Based testing tool built in Java. 
        It reads models in the shape of finite-state diagrams, or directed graphs, 
        and generate tests from the models, either offline or online.
    
# 安裝

### 下載執行檔並執行

說明：此執行檔為單個可執行的程式，不需要另外安裝所需library，安裝指令如下方"Install command"中，執行完後，即可於全域執行。

*   下載：[Ubuntu executable](https://justup.9ifriend.com/share.html?id=cc9139b0-8094-4ba0-8d03-72dc6e483ff4)
*   更新：[runner_update](https://justup.co/share.html?id=88fab911-0ee0-4614-8702-f30b812487cf)

    註：備用執行程式：Graphwalker_Runner.py，此方式需要安裝所需的lib。

### 安裝指令
*    `$ sudo ./Graphwalker_Runner`

*   註：如果執行檔權限不足，請修改它的權限(chmod 775 Graphwalker)

# How to Run：

## 全域執行：
*   `Graphwalker [arguments]`

## 指令說明：

    usage: Graphwalker_Runner [-h] [-u UPDATE] [-m MODEL] [-c] [-r]
    optional arguments:
        -h, --help            show this help message and exit
        -i, --init            Rebuild graphwalker environment ,syntax：Graphwalker_Runner -i
        -u, --update          Pull graphwalker source code from github,syntax：Graphwalker_Runner -u
        -m, --model           MODEL Merge graphml files in folder ,folderpattern: graphml folder path,syntax：Graphwalker_Runner -m <folderpattern>
        -c, --check           Check graphical integrity, output Not visited points file (Not_visited_points.txt),syntax：Graphwalker_Runner -c
        -r, --run             Running graphwalker, syntax：Graphwalker_Runner -r
        -s, --shot SHOT  Screenshot when graphwalker running, TestDevice: 'pc' or 'mobile' , syntax: Graphwalker_Runner -r -s <TestDevice>
        -S, --Stop STOP  Set stop condition, default StopCondition:'random(edge_coverage(100))' , syntax:Graphwalker_Runner -r -S <StopCondition>
        -v, --version         Show current version number and change notes
        -vv, --ChangeNotes    Show all version number and change notes


## 建立初始環境
    說明：移除現有環境，並重新於本地端建立一個全新的Graphwalker tool。
        自動建立Graphwalker Runner環境的流程如下：
            1. clone graphwalker工具 (from github)
            2. 於本地端建立執行環境 (path:/usr/local/GraphwalkerRunner)
            3. 下載graphwalker-cli-SNAPSHOT.jar
            註：如果下載失敗，請手動下載，並放置在：/usr/local/GraphwalkerRunner/lib。
        
    syntax：
        `Graphwalker_Runner -i`
    example:
        `$ sudo Graphwalker_Runner -i  `
        `git clone code...`
        `[sudo] password for jeremy: `
        `remote: Counting objects: 822, done.`
        `remote: Compressing objects: 100% (10/10), done.`
        `remote: Total 822 (delta 3), reused 0 (delta 0), pack-reused 812`
        `   .   `
        `   .  `
        `   .   `
        `chmod folder...`

## 版本
    說明：查詢目前版本，回傳"版號"與"Change note"，如果runner版本過舊也會顯示提示更新訊息。
    syntax：
        `Graphwalker_Runner -v`
    example:
        `$ sudo Graphwalker_Runner -v`
        `Current Version: 1.0.5`
        `Change log：`
        `    1 ： 修改logging config 初始化錯誤`
        `                                                   `
        `****************** Warning ********************`
        `                                                   `
        `Runner has new version : 1.0.1`
        `                                                   `
        `please update by runner_update (Ubuntu executable) `
        `                                                   `
        `runner_update download URL : https://justup.co/share.html?id=88fab911-0ee0-4614-8702-f30b812487cf`
        `                                                   `
        `***********************************************`
            
## 變更歷程
    說明：查詢所有版本，回傳"版號"與"Change note"。。
    syntax：
        `Graphwalker_Runner -vv`
    example:
        `$ sudo Graphwalker_Runner -vv`
        `Current Version: 1.0.5`
        `Change log：`
        `    1 ： 修改logging config 初始化錯誤`
        `Version: 1.0.4`
        `Change log：`
        `    1 ： 新增Log Record`
        `    2 ： 新增測試報告`
        `    . ` 
        `    .`
        `    .`
        `Version: 1.0.0`
        `Change log：`
        `    1 ： 修復合圖問題`
        `    2 ： 新增版本與更新細節清單`
          
## 更新工具
    說明：從github拉新的code。
    syntax：
        `Graphwalker_Runner -u`
    example:
        `$ ./Graphwalker_Runner -u`
        `INFO : update...`
        `INFO : Updating 0fe0936..fdb732c`
        `Fast-forward`
        ` README.md |   21 +++++++++++++++++++--`
        ` 1 file changed, 19 insertions(+), 2 deletions(-)`
        `INFO : get "Runner" downloadURL...`
        `INFO : Download Runner...`
        `INFO : successful`
        `INFO : chmod folder...`
        `INFO : successful`
        `INFO : chmod runner...`
        `INFO : successful`
    
## 圖形合併
    說明：合併資料夾內所有Graphml子圖。
    syntax：
        `Graphwalker_Runner -m 'graphml folder path'`
    example:
        `$ Graphwalker_Runner -m ./graph_folder`
        `INFO : merge graph...`
        `INFO : successful`
        `INFO : graphml -> dot... (merged.dot)`
        `INFO : successful`
        `INFO : dot -> png... (merged.png)`
        `INFO : successful`
        `INFO : output merged.py`
        `INFO : Generate python stub source code & graphwalker Runner ... (script.py)`
        `INFO : successful`
        `INFO : del dot`
        `INFO : successful`

## 確認圖形完整性
    說明：確認script.py內所有的function是否均被執行到。
         回傳值：True(全部已執行); False(有function未執行，或執行步數達到限制條件Stop condition：(edge+vertex)^2)
    syntax：
        `Graphwalker_Runner -c`
    example:
        `$ Graphwalker_Runner -c`
        `INFO : Check graphical integrity`
        `INFO : Run Websocket...`
        `    二月 03, 2016 5:48:26 下午 com.sun.jersey.server.impl.application.WebApplicationImpl _initiate`
        `    資訊: Initiating Jersey application, version 'Jersey: 1.18.3 12/01/2014 08:23 AM'`
        `    二月 03, 2016 5:48:26 下午 org.glassfish.grizzly.http.server.NetworkListener start`
        `    資訊: Started listener bound to [0.0.0.0:8887]`
        `    二月 03, 2016 5:48:26 下午 org.glassfish.grizzly.http.server.HttpServer start`
        `    資訊: [HttpServer] Started.`
        `INFO : Cheching every point by online`
        `INFO : ===========Result=============`
        `INFO : Visited complete graphics`
        `INFO : ==============================`
    
## 執行graphwlaker測試
    說明：執行Graphewalker測試。測試會先計算平均十次的步數作為陷入無窮回圈時的停止條件，再進行Graphwalker的運行。
    syntax：
        `Graphwalker_Runner -r`
    example:
        `$ Graphwalker_Runner -r`
        `INFO : graphwalker running`
        `INFO : successful`
        `INFO : Get average count...`
        `    The 1st times step:12`
        `    The 2nd times step:18`
        `   The 3rd times step:12`
        `    The 4th times step:30`
        `    The 5th times step:12`
        `    The 6th times step:24`
        `    The 7th times step:18`
        `    The 8th times step:18`
        `    The 9th times step:12`
        `    The 10th times step:12`
        `    Step List:[12, 18, 12, 30, 12, 24, 18, 18, 12, 12]`
        `    Max:30`
        `    Min:12`
        `    Stop Condition:54`
        `Run Testing...`
        `kill pid : 6821`
        `Run websocket...`
        `    二月 03, 2016 5:56:23 下午 com.sun.jersey.server.impl.application.WebApplicationImpl _initiate`
        `    資訊: Initiating Jersey application, version 'Jersey: 1.18.3 12/01/2014 08:23 AM'`
        `    二月 03, 2016 5:56:23 下午 org.glassfish.grizzly.http.server.NetworkListener start`
        `    資訊: Started listener bound to [0.0.0.0:8887]`
        `    二月 03, 2016 5:56:23 下午 org.glassfish.grizzly.http.server.HttpServer start`
        `    資訊: [HttpServer] Started.`
        `e_init`
        `v_3`
        `e_3_2`
        `v_2`
        `e_2_1_1`
        `v_1_edit`
        `e_1__2_3`
        `Action error on e_1__2_3`
        `Error message:`
        `(<type 'exceptions.AssertionError'>, AssertionError(), <traceback object at 0x29196c8>)`
        ``
        ``
        `Run Testing...`
        `    .`
        `    .`
        `    .`
        `*********************`
        `Full Completion`
        `*********************`
        `*********************`
        `{}`
        `*********************`
        `2016-02-03 17:56:37,041 - INFO : Generate Test Report`
        `2016-02-03 17:56:37,060 - INFO : Generate XML`
        `kill pid : 6869`
        `kill pid : 6870`
        `已砍掉`
        
    
### Screenshot when testing 
    說明：執行Graphewalker測試與錯誤發生時照下當前畫面，並存在screenshot目錄內(依照每一次測試結果分類)
         參數：pc(當前測試裝置為桌電) or mobile(當前測試裝置為行動裝置)。
    syntax：
        `Graphwalker_Runner -r -s [ pc | mobile ]`
    example:
         `$ Graphwalker_Runner -r -s pc`
         
### Set stop condition
    說明：設置停止條件，預設為"random(edge_coverage(100))"。
         更多停止條件用法請參考下方"Stop conditions Documentation"
    syntax：
        `Graphwalker_Runner -r -S "stop condition"`
    example:
        `$ Graphwalker_Runner -r -S "random(edge_coverage(10))"`
    
# 問與答
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

# 資料來源

*   [Graphwalker官網](http://graphwalker.org/)
*   下載 [graphwalker-cli-SNAPSHOT.jar](https://justup.9ifriend.com/share.html?id=c84d674b-c645-4a2b-a5f0-8afd931b005e)
*   [Stop conditions Documentation](http://graphwalker.org/docs/path_generators_and_stop_conditions)
