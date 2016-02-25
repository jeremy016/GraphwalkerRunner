# GraphwalkerRunner
    說明：以Graphwalker的核心架構下，新增特殊功能的整合工具。
    增添功能： 1.圖形合併 2. 圖形完整性驗證 3. Grapgwalker運行 4. 錯誤續跑機制 5. 畫面截圖。
    
    注：What is GraphWalker?
        It's a Model-Based testing tool built in Java. 
        It reads models in the shape of finite-state diagrams, or directed graphs, 
        and generate tests from the models, either offline or online.

# GraphwalkerRunner流程圖
![Alt text](http://s2.imgs.cc/img/aNHB7SHt.png)
# 預安裝

*   pygraphml
    `$ pip install pygraphml`

*   graphviz
    `$ sudo apt-get install graphviz`

*   numpy
    `$ sudo apt-get install python-numpy`

# 安裝

### 下載執行檔並執行

說明：此執行檔為單個可執行的程式，不需要另外安裝所需library，安裝指令如下方"安裝指令"中，執行完後，即可於全域執行。

*   下載：[Ubuntu executable](https://justup.9ifriend.com/share.html?id=cc9139b0-8094-4ba0-8d03-72dc6e483ff4)

*   註：備用執行程式：Graphwalker_Runner.py，此方式需要安裝所需的lib。

### 安裝指令
*    `$ sudo ./Graphwalker_Runner`

*   註：如果執行檔權限不足，請修改它的權限(chmod 775 Graphwalker)

# 更新

*   Runner：[runner_update](https://justup.co/share.html?id=88fab911-0ee0-4614-8702-f30b812487cf)
*   Library：`$ Graphwalker -u`

# 移除

*   移除執行檔(Ubuntu executable)：[uninstall](https://justup.co/share.html?id=561d951c-27ce-47b1-b40f-a1911ed3a726)

# How to Run：

## 全域執行：
*   `$ Graphwalker [arguments]`

## 指令說明：

    usage: Graphwalker_Runner [-h] [-u UPDATE] [-m MODEL] [-c] [-r]
    optional arguments:
        -h, --help            show this help message and exit
        -i, --init            Rebuild graphwalker environment ,syntax：Graphwalker_Runner -i
        -u, --update          Pull graphwalker source code from github,syntax：Graphwalker_Runner -u
        -m, --model           MODEL Merge graphml files in folder ,folderpattern: graphml folder path,syntax：Graphwalker_Runner -m <folderpattern>
        -c, --check           Check graphical integrity, output Not visited points file (Not_visited_points.txt),syntax：Graphwalker_Runner -c
        -r, --run             Running graphwalker, syntax：Graphwalker_Runner -r
        -s, --shot SHOT       Screenshot when graphwalker running, TestDevice: 'pc' or 'mobile' , syntax: Graphwalker_Runner -r -s <TestDevice>
        -S, --Stop STOP       Set stop condition, default StopCondition:'random(edge_coverage(100))' , syntax:Graphwalker_Runner -r -S <StopCondition>
        -v, --version         Show current version number and change notes
        -vv, --ChangeNotes    Show all version number and change notes
        -p , --path PATH      Visits specific path , syntax: Graphwalker_Runner -p 'path' , path syntax :'point(0)->point(2)->point(3)'


### 建立初始環境
移除現有環境，並重新於本地端建立一個全新的Graphwalker Library。

##### 流程說明：
自動建立Graphwalker Library環境的流程如下 

-   移除本地端Library目錄(path:/usr/local/GraphwalkerRunner)
-   clone graphwalker工具 (from github) 
-   建立本地端Library目錄 (path:/usr/local/GraphwalkerRunner) 
-   下載graphwalker-cli-SNAPSHOT.jar

註：如果下載失敗，請手動下載，並放置在：/usr/local/GraphwalkerRunner/lib

##### Syntax：

`$ Graphwalker_Runner -i`

##### Example：

    $ sudo Graphwalker_Runner -i 
    git clone code...
    [sudo] password for jeremy: 
    remote: Counting objects: 822, done.
    remote: Compressing objects: 100% (10/10), done.
    remote: Total 822 (delta 3), reused 0 (delta 0), pack-reused 812
    .
    .
    .
    chmod folder...

### 版本

  查詢目前版本，回傳"版號"與"Change note"，如果runner版本過舊也會顯示提示更新訊息。

##### Syntax：

`$ Graphwalker_Runner -v`

##### Example:

    $ sudo Graphwalker_Runner -v
    Current Runner Version: 1.0.3
    Current Tool Version: 1.0.6
    Change log：
        1 ： 修改logging config 初始化錯誤
                                                   
    ****************** Warning ********************
                                                       
    Runner has new version : 1.0.4
                                                       
    please update by runner_update (Ubuntu executable) 
                                                               
        runner_update download URL : https://justup.co/share.html?id=88fab911-0ee0-4614-8702-f30b812487cf
                                                           
        ***********************************************
            
### 變更歷程
查詢Runner與Library版本，回傳Runner目前"版號"，Library所有"版號"與"Change note"的相關資訊。

##### Syntax：

`$ Graphwalker_Runner -vv`

##### Example：

    $ sudo Graphwalker_Runner -vv
    Current Runner Version: 1.0.4
    Current Tool Version: 1.0.6
    Change log：
        1 ： 修改logging config 初始化錯誤
    Version: 1.0.4
    Change log：
        1 ： 新增Log Record
        2 ： 新增測試報告
        . 
        .
        .
    Version: 1.0.0
    Change log：
        1 ： 修復合圖問題
        2 ： 新增版本與更新細節清單

### 走訪特定路線
執行指定的路徑，可搭配錯誤報告中的path(格式一致，可直接複製貼上)，進行問題重現。

##### Syntax：

`$ Graphwalker_Runner -p 'path'`

##### Example：

    $ Graphwalker_Runner -p 'e_Init->v_Landing_Page->e_btn_Download_from_Landing'
    2016-02-16 10:41:16,183 - INFO : successful
    2016-02-16 10:41:16,184 - INFO : run script by specific path...
    e_Init
    v_Landing_Page
    e_btn_Download_from_Landing
     
### 更新Library
從github拉新的code。

##### 流程說明：
從Github上pull code至本地端目錄(/usr/local/Graphwalker)

##### Syntax：
    `Graphwalker_Runner -u`
##### Example：

    $ ./Graphwalker_Runner -u
    INFO : update...
    INFO : Updating 0fe0936..fdb732c
    Fast-forward
     README.md |   21 +++++++++++++++++++--
     1 file changed, 19 insertions(+), 2 deletions(-)
    INFO : get "Runner" downloadURL...
    INFO : Download Runner...
    INFO : successful
    INFO : chmod folder...
    INFO : successful
    INFO : chmod runner...
    INFO : successful
    
### 圖形合併
合併資料夾內所有Graphml子圖。

##### 流程說明：
合併graph目錄下所有的圖，並再當前目錄底下產生 1.合併後的圖(merged.graphml), 2.合併後的png檔(merged.png), 3.執行的腳本(script.py)。

##### Syntax：
    `Graphwalker_Runner -m 'graphml folder path'`
    
##### Example：

    $ Graphwalker_Runner -m ./graph_folder
    INFO : merge graph...
    INFO : successful
    INFO : graphml -> dot... (merged.dot)
    INFO : successful
    INFO : dot -> png... (merged.png)
    INFO : successful
    INFO : output merged.py
    INFO : Generate python stub source code & graphwalker Runner ... (script.py)
    INFO : successful
    INFO : del dot
    INFO : successful

### 確認圖形完整性
以線上Graphwalker的方式去走訪合併後的圖形，如失敗，則列出所有沒走訪的點。

*   註:因圖形有可能繪製成無窮回圈的狀況，故另外加一條停止條件機制(當執行到指定步數時時也會停止，並列出未走訪的點和邊)

##### 流程說明：
1. 確認socket server port是否被佔用
2. 啟動Web socket server
3. 以"random(edge_coverage(100))"或"步驟等於(edge+vertex)^2)"作為"停止條件"，以隨機的方式執行script.py內的所有function。
4. 結果：
    -   Pass -> 回饋訊息：Visited complete graphics
    -   Fail -> 回饋訊息：Visited incomplete graphics 與 Not visited points : xx,xx,xx,xx,....

##### Syntax：
    `Graphwalker_Runner -c`

##### Example:

    $ Graphwalker_Runner -c
    INFO : Check graphical integrity
    INFO : Run Websocket...
        二月 03, 2016 5:48:26 下午 com.sun.jersey.server.impl.application.WebApplicationImpl _initiate
        資訊: Initiating Jersey application, version 'Jersey: 1.18.3 12/01/2014 08:23 AM'
        二月 03, 2016 5:48:26 下午 org.glassfish.grizzly.http.server.NetworkListener start
        資訊: Started listener bound to [0.0.0.0:8887]
        二月 03, 2016 5:48:26 下午 org.glassfish.grizzly.http.server.HttpServer start
        資訊: [HttpServer] Started.
    INFO : Cheching every point by online
    INFO : ===========Result=============
    INFO : Visited complete graphics
    INFO : ==============================
    
### 執行graphwlaker測試
此測試在原先graphwalker的運行上，新增了下列幾個功能：
1. 新增停止條件：以平均走訪圖形10次，以(最大值+最小值*2)作為另一停止條件。
2. 錯誤續跑的機制：當遇到錯誤的點時，會自動修改圖形，以mark錯誤的點重新開始走訪，改善了原先遇到錯誤時即停止的問題。

##### 流程說明：
1. 以offline的方式，算出10次走訪完整的圖形所需的步數(作為陷入無窮回圈時的停止條件)
2. 再啟動Web scoket server
3. 以online的方式，開始走訪script.py內的function
4. 當遇到錯誤時會mark住錯誤的點以及相關的點和邊
5. 持續重複步驟3~4，直至走訪完成
6. 結果：產生兩份測試報告，文字檔(test_report.txt)與匯入Jenkins的報告格式(Result.xml)

##### Syntax：
        `Graphwalker_Runner -r`
        
##### Example:

    $ Graphwalker_Runner -r
    INFO : graphwalker running
    INFO : successful
    INFO : Get average count...
        The 1st times step:12
        The 2nd times step:18
        The 3rd times step:12
        The 4th times step:30
        The 5th times step:12
        The 6th times step:24
        The 7th times step:18
        The 8th times step:18
        The 9th times step:12
        The 10th times step:12
        Step List:[12, 18, 12, 30, 12, 24, 18, 18, 12, 12]
        Max:30
        Min:12
        Stop Condition:54
    Run Testing...
    kill pid : 6821
    Run websocket...
        二月 03, 2016 5:56:23 下午 com.sun.jersey.server.impl.application.WebApplicationImpl _initiate
        資訊: Initiating Jersey application, version 'Jersey: 1.18.3 12/01/2014 08:23 AM'
        二月 03, 2016 5:56:23 下午 org.glassfish.grizzly.http.server.NetworkListener start
        資訊: Started listener bound to [0.0.0.0:8887]
        二月 03, 2016 5:56:23 下午 org.glassfish.grizzly.http.server.HttpServer start
        資訊: [HttpServer] Started.
    e_init
    v_3
    e_3_2
    v_2
    e_2_1_1
    v_1_edit
    e_1__2_3
    Action error on e_1__2_3
    Error message:
    (<type 'exceptions.AssertionError'>, AssertionError(), <traceback object at 0x29196c8>)
    Run Testing...
        .
        .
        .
    *********************
    Full Completion
    *********************
    *********************
    {}
    *********************
    2016-02-03 17:56:37,041 - INFO : Generate Test Report
    2016-02-03 17:56:37,060 - INFO : Generate XML
    kill pid : 6869
    kill pid : 6870
    已砍掉
    
#### Screenshot when testing 
此參數為執行graphwlaker測試之可選用參數。同步紀錄執行Graphewalker測試與錯誤發生時的畫面截圖，並存在screenshot目錄內(依照每一次測試結果分類)，目前有兩種模式，分別是pc與mobile。
參數：pc(當前測試裝置為桌電) or mobile(當前測試裝置為行動裝置)。

##### 流程說明：
1. 執行測試時，同步擷取每一個function執行的畫面
2. 擷取的畫面，存放於當前目錄底下的screenshot資料夾
3. 測試進行時，會重複步驟1~2，並以測試次數作為子資料夾名稱

##### Syntax：
    `Graphwalker_Runner -r -s [ pc | mobile ]`

##### Example：

    $ Graphwalker_Runner -r -s pc
    $ cd Screenshot/
    $ ls
        The_1st_times_testing  The_3rd_times_testing  The_5th_times_testing
        The_2nd_times_testing  The_4th_times_testing
    $ cd The_1st_times_testing/
    $ ls
        screen-0-e_Init.png
        screen-100-e_link_System_Bulletin_from_More.png
        screen-101-v_System_Bulletin.png
        .
        .
        .
         
#### Set stop condition
此參數為執行graphwlaker測試之可選用參數。即設置停止條件，預設為"random(edge_coverage(100))"，可依照不同的測試需求，設定不同的停止條件。
    
*   註：更多停止條件用法請參考下方"Stop conditions Documentation"

##### Syntax：
    `Graphwalker_Runner -r -S "stop condition"`
    
##### Example：

    $ Graphwalker_Runner -r -S "random(edge_coverage(10))"
    
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
