# lorawan-parser  
## 介绍 :smile: 
此工具是方便解析LoRaWAN PHY解析器，基于开源帧解析项目[lorawan-parse](https://github.com/tanupoo/lorawan-parse)制作。
使用pyqt5窗体应用，方便小白直接使用。无需使用原项目的命令行形式。
## 截图
[![截图](https://s1.ax1x.com/2022/08/17/vBYwGD.md.png)](https://imgtu.com/i/vBYwGD)
## 功能
1. 解析入网请求00包   :white_check_mark: 
2. 解析入网回复20包  :white_check_mark: 
3. 解析confirm up类型80包  :white_check_mark: 
4. 解析unconfirm down类型60包  :white_check_mark: 
5. 解析unconfirm up类型40包  :white_check_mark: 
6. 解析confirm down类型A0包  :white_check_mark: 
7. 批量解析报文文件，暂未实现    :x: 

## 注意
解析部分报文时需要appkey、nwkskey、appskey，否则可能无法完全解析成功。
## 感谢
[tanupoo](https://github.com/tanupoo)
[lorawan-parse](https://github.com/tanupoo/lorawan-parse)