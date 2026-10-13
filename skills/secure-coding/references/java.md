# java 规则索引

共 49 条。由 scripts/guide.py 生成。

先读适用的完整规则正文和解释；标题及原文级别不等于已验证的当前实现。
使用 `python scripts/guide.py show <ID>` 取得带行号正文及本技能解释。
脚本路径以技能目录为基准；没有 Python 时，按下表行号直接读取 sources 文件。


## 安卓类 / I. 代码实现 / 1.1 异常捕获处理

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-ANDROID-1.1.1 | 必须 | 序列化异常捕获 | [32–48](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-1.1.2 | 必须 | NullPointerException 异常捕获 | [49–66](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-1.1.3 | 必须 | ClassCastException 异常捕获 | [67–82](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-1.1.4 | 必须 | ClassNotFoundException 异常捕获 | [83–84](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 安卓类 / I. 代码实现 / 1.2 数据泄露

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-ANDROID-1.2.1 | 必须 | logcat 输出限制 | [88–102](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 安卓类 / I. 代码实现 / 1.3 webview 组件安全

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-ANDROID-1.3.1 | 必须 | addJavaScriptInterface 方法调用 | [106–120](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-1.3.2 | 建议 | setJavaScriptEnabled 方法调用 | [121–133](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-1.3.3 | 建议 | setAllowFileAccess 方法调用 | [134–146](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-1.3.4 | 建议 | setSavePassword 方法调用 | [147–159](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-1.3.5 | 必须 | onReceivedSslError 方法调用 | [160–179](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 安卓类 / I. 代码实现 / 1.4 传输安全

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-ANDROID-1.4.1 | 必须 | 自定义 HostnameVerifier 类 | [182–200](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-1.4.2 | 必须 | 自定义 X509TrustManager 类 | [201–218](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-1.4.3 | 必须 | setHostnameVerifier 方法调用 | [219–233](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 安卓类 / II. 配置&环境 / 2.1 AndroidManifest.xml 配置

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-ANDROID-2.1.1 | 必须 | PermissionGroup 属性设置 | [239–240](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-2.1.2 | 必须 | protectionLevel 属性设置 | [241–242](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-2.1.3 | 建议 | sharedUserId 权限设置 | [243–244](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-2.1.4 | 建议 | allowBackup 备份设置 | [245–250](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-ANDROID-2.1.5 | 必须 | debuggable 调试设置 | [251–256](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.1 数据持久化

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.1.1 | 必须 | SQL语句默认使用预编译并绑定变量 | [266–291](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.1.2 | 必须 | 白名单过滤 | [293–301](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.2 文件操作

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.2.1 | 必须 | 文件类型限制 | [306–331](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.2.2 | 必须 | 禁止外部文件存储于可执行目录 | [333–335](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.2.3 | 建议 | 避免路径拼接 | [337–339](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.2.4 | 必须 | 避免路径穿越 | [341–343](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.3 网络访问

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.3.1 | 必须 | 避免直接访问不可信地址 | [348–369](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.4 XML读写

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.4.1 | 必须 | XML解析器关闭DTD解析 | [374–421](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.5 响应输出

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.5.1 | 必须 | 设置正确的HTTP响应包类型 | [427–429](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.5.2 | 建议 | 设置安全的HTTP响应头 | [431–459](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.5.3 | 必须 | 外部输入拼接到response页面前进行编码处理 | [463–484](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-XSS-CONTEXT](interpretations.md#int-xss-context) |
| JAVA-BACKEND-1.5.4 | 必须 | 外部输入拼接到HTTP响应头中需进行过滤 | [486–488](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.5.5 | 必须 | 避免不可信域名的302跳转 | [490–513](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.5.6 | 必须 | 避免通过Jsonp传输非公开敏感信息 | [517–519](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.5.7 | 必须 | 限定JSONP接口的callback字符集范围 | [521–523](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.5.8 | 必须 | 屏蔽异常栈 | [525–527](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.5.9 | 必须 | 模板&表达式 | [529–554](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.6 OS命令执行

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.6.1 | 建议 | 避免不可信数据拼接操作系统命令 | [559–561](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.6.2 | 必须 | 避免创建SHELL操作 | [563–580](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.7 会话管理

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.7.1 | 必须 | 非一次有效身份凭证禁止在URL中传输 | [585–587](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.7.2 | 必须 | 避免未经校验的数据直接给会话赋值 | [589–591](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.8 加解密

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.8.1 | 建议 | 对称加密 | [596–602](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-AEAD](interpretations.md#int-aead) |
| JAVA-BACKEND-1.8.2 | 建议 | 非对称加密 | [604–606](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.8.3 | 建议 | 哈希算法 | [608–610](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.8.4 | 建议 | 密码存储策略 | [612–614](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | [INT-PASSWORD-STORAGE](interpretations.md#int-password-storage) |

## 后台类 / I. 代码实现 / 1.9 查询业务

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.9.1 | 必须 | 返回信息最小化 | [619–621](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.9.2 | 必须 | 个人敏感信息脱敏展示 | [623–631](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.9.3 | 必须 | 数据权限校验 | [633–639](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |

## 后台类 / I. 代码实现 / 1.10 操作业务

| ID | 原文级别 | 规则 | 原文行号 | 解释 |
|---|---|---|---|---|
| JAVA-BACKEND-1.10.1 | 必须 | 部署CSRF防御机制 | [644–689](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.10.2 | 必须 | 权限校验 | [691–698](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
| JAVA-BACKEND-1.10.3 | 建议 | 加锁操作 | [700–702](../sources/Java%E5%AE%89%E5%85%A8%E6%8C%87%E5%8D%97.md) | — |
