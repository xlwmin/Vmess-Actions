# VmessActions
通过GitHub的actions 自动采集节点 
自动生成订阅信息

订阅内容自动更新在仓库 subscribe 目录下的 clash.yml 和 v2ray.txt 中
然后PC端/手机端根据自己的软件支持的格式，订阅对应的链接即可

比如clash.yml的订阅链接为 https://raw.githubusercontent.com/skywolf627/VmessActions/main/subscribe/clash.yml  
如果自己的仓，直接查看对应文件的raw链接 即可

部分国内网络貌似无法直接访问  https://raw.githubusercontent.com  会导致你的软件第一次拉取订阅的时候 拉取不到节点。这个时候手动在github找到对应的订阅文件，打开文件把节点信息手动录入到软件即可。或者自己找个免费梯子用来拉取节点。



目前抓取的节点速度看youtubu 4k 不卡，电报基本秒开。


订阅节点仅作学习交流用，用于查找资料，学习知识，不要做任何违法行为。所有资源均来自互联网，非盈利目的，仅供大家交流学习使用，出现违法问题概不负责。

https://github.com/skywolf627/VmessActions


## 在线抓取
 
> - https://proxies.bihai.cf/

> - https://etproxypool.ga/

> - https://sspool.nl/

 
## 节点筛选
 
Provider

所有节点示例 > - https://proxies.bihai.cf/clash/proxies	

筛选节点示例 > - https://proxies.bihai.cf/clash/proxies?c=CN,HK,TW&speed=15,30&type=ss

            > - https://proxies.bihai.cf/clash/proxies?filter=1	
               
❗️节点过多会造成软件卡顿，可以自行筛选节点后修改配置文件的proxy-provider部分。

Provider筛选参数

🌟 使用URL Query对Clash Provider进行筛选

| 项目            | Query Key      | Query Value                            | 备注                                                           |
|----------------|----------------|----------------------------------------|----------------------------------------------------------------|
| 类型            | type           | ss,ssr,vmess,trojan                    | 可同时选择多个类型                                                               |
| 国家            | c              | AT,CN,IN,HK,JP,NL,RU,SG,TW,US...       | 可同时选择多个国家                                                               |
| 排除国家        | nc             | AT,CN,IN,HK,JP,NL,RU,SG,TW,US...       | 可同时选择多个国家                                                               |
| 速度            | speed          | 任何数字                                | 单个数字选择最低速度,两个数字选择速度区间                                                   |
| 过滤            | filter         | 1,2                                    | 默认：不进行过滤 1:选择中转节点 2:选择pool节点 3:选择中转与pool节点                                |

 
## 订阅转换

> - https://suc.bihai.ml/sub?target=clash&new_name=true&url=<<<<ss,ssr,vmess,trojan地址>>>>&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini

> - https://subsc.ednovas.xyz/sub?target=clash&url=<<<<ss,ssr,vmess,trojan地址>>>>&insert=false&config=https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini_MultiMode.ini&emoji=true&list=false&tfo=false&scv=false&fdn=false&sort=false&expand=true&new_name=true


## 相关收藏

> - https://github.com/lizisan/Free-Proxies
