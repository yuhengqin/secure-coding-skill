# javascript 规则索引

共 45 条。由 scripts/guide.py 生成。

先读适用的完整规则正文和解释；标题及原文级别不等于已验证的当前实现。
使用 `python scripts/guide.py show <ID>` 取得带行号正文及本技能解释。
脚本路径以技能目录为基准；没有 Python 时，按下表行号直接读取 sources 文件。


## JavaScript页面类 / I. 代码实现 / 1.1 原生DOM API的安全操作

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-BROWSER-1.1.1 | 必须 | HTML标签操作，限定/过滤传入变量值 | [49–80](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-XSS-CONTEXT](interpretations.md#int-xss-context) |
| JS-BROWSER-1.1.2 | 必须 | HTML属性操作，限定/过滤传入变量值 | [82–106](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-XSS-CONTEXT](interpretations.md#int-xss-context) |

## JavaScript页面类 / I. 代码实现 / 1.2 流行框架/库的安全操作

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-BROWSER-1.2.1 | 必须 | 限定/过滤传入jQuery不安全函数的变量值 | [111–143](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-BROWSER-1.2.2 | 必须 | 限定/过滤传入Vue.js不安全函数的变量值 | [145–193](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## JavaScript页面类 / I. 代码实现 / 1.3 页面重定向

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-BROWSER-1.3.1 | 必须 | 限定跳转目标地址 | [198–222](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## JavaScript页面类 / I. 代码实现 / 1.4 JSON解析/动态执行

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-BROWSER-1.4.1 | 必须 | 使用安全的JSON解析方式 | [227–248](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## JavaScript页面类 / I. 代码实现 / 1.5 跨域通讯

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-BROWSER-1.5.1 | 必须 | 使用安全的前端跨域通信方式 | [253–255](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-BROWSER-1.5.2 | 必须 | 使用postMessage应限定Origin | [257–279](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## JavaScript页面类 / II. 配置&环境 / 2.1 敏感/配置信息

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-BROWSER-2.1.1 | 必须 | 禁止明文硬编码AK/SK | [287–289](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## JavaScript页面类 / II. 配置&环境 / 2.2 第三方组件/资源

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-BROWSER-2.2.1 | 必须 | 使用可信范围内的统计组件 | [294–294](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-BROWSER-2.2.2 | 必须 | 禁止引入非可信来源的第三方JS | [296–296](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## JavaScript页面类 / II. 配置&环境 / 2.3 纵深安全防护

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-BROWSER-2.3.1 | 推荐 | 部署CSP，并启用严格模式 | [301–301](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.1 输入验证

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.1.1 | 必须 | 按类型进行数据校验 | [312–342](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.2 执行命令

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.2.1 | 必须 | 使用child_process执行系统命令，应限定或校验命令和参数的内容 | [347–414](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-COMMAND](interpretations.md#int-command) |

## Node.js后台类 / I. 代码实现 / 1.3 文件操作

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.3.1 | 必须 | 限定文件操作的后缀范围 | [419–421](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.3.2 | 必须 | 校验并限定文件路径范围 | [423–465](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.3.3 | 必须 | 安全地处理上传文件名 | [467–470](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.3.4 | 必须 | 敏感资源文件，应有加密、鉴权和水印等加固措施 | [472–477](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.4 网络请求

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.4.1 | 必须 | 限定访问网络资源地址范围 | [482–493](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.4.2 | 推荐 | 请求网络资源，应加密传输 | [495–499](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.5 数据输出

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.5.1 | 必须 | 高敏感信息禁止存储、展示 | [504–507](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.5.2 | 必须 | 一般敏感信息脱敏展示 | [509–514](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.5.3 | 推荐 | 返回的字段按业务需要输出 | [516–521](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.6 响应输出

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.6.1 | 必须 | 设置正确的HTTP响应包类型 | [526–528](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.6.2 | 必须 | 添加安全响应头 | [530–534](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.6.3 | 必须 | 外部输入拼接到响应页面前，进行编码处理 | [536–544](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-XSS-CONTEXT](interpretations.md#int-xss-context) |
| JS-NODE-1.6.4 | 必须 | 响应禁止展示物理资源、程序内部代码逻辑等敏感信息 | [546–553](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.6.5 | 推荐 | 添加安全纵深防御措施 | [555–575](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.7 执行代码

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.7.1 | 必须 | 安全的代码执行方式 | [580–586](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.8 Web跨域

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.8.1 | 必须 | 限定JSONP接口的callback字符集范围 | [591–593](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.8.2 | 必须 | 安全的CORS配置 | [595–607](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.9 SQL操作

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.9.1 | 必须 | SQL语句默认使用预编译并绑定变量 | [612–680](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.9.2 | 必须 | 安全的ORM操作 | [682–720](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.10 NoSQL操作

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.10.1 | 必须 | 校验参数值类型 | [725–759](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.10.2 | 必须 | NoSQL操作前，应校验权限/角色 | [761–783](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.11 服务器端渲染（SSR）

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.11.1 | 必须 | 安全的Vue服务器端渲染(Vue SSR) | [788–813](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.11.2 | 必须 | 安全地使用EJS、LoDash、UnderScore进行服务器端渲染 | [815–839](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-1.11.3 | 必须 | 在自行实现状态存储容器并将其JSON.Stringify序列化后注入到HTML时，必须进行安全过滤 | [841–841](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.12 URL跳转

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.12.1 | 必须 | 限定跳转目标地址 | [846–896](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / I. 代码实现 / 1.13 Cookie与登录态

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-1.13.1 | 推荐 | 为Cookies中存储的关键登录态信息添加http-only保护 | [901–903](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / II. 配置&环境 / 2.1 依赖库

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-2.1.1 | 必须 | 使用安全的依赖库 | [911–913](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / II. 配置&环境 / 2.2 运行环境

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-2.2.1 | 必须 | 使用非root用户运行Node.js | [918–918](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## Node.js后台类 / II. 配置&环境 / 2.3 配置信息

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JS-NODE-2.3.1 | 必须 | 禁止硬编码认证凭证 | [923–926](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-2.3.2 | 必须 | 禁止硬编码IP配置 | [928–932](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JS-NODE-2.3.3 | 必须 | 禁止硬编码员工敏感信息 | [934–936](../sources/JavaScript%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
