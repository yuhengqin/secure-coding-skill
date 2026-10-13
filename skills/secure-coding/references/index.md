# 规则路由

规则以“语言前缀－场景－原编号”为稳定标识；例如 `PY-COMMON-1.1.1` 与 `PY-BACKEND-1.1.1` 是不同规则。编号不连续时保留原样。

| 实际环境 | 索引 | 应加载的场景 |
|---|---|---|
| Python 脚本、服务 | [python.md](python.md) | COMMON；存在接口、数据库、文件/网络等行为时加 BACKEND 的相关章节 |
| 浏览器 JavaScript/TypeScript | [javascript.md](javascript.md) | BROWSER |
| Node.js JavaScript/TypeScript | [javascript.md](javascript.md) | NODE；同时改前端时加 BROWSER |
| Java 服务端 | [java.md](java.md) | BACKEND |
| Android Java；Kotlin 调同类 Android API 时参考 | [java.md](java.md) | ANDROID；Kotlin 语言本身不在本库覆盖范围 |
| Go | [go.md](go.md) | COMMON；服务端加 BACKEND |
| C/C++ | [cpp.md](cpp.md) | COMMON；按内存、进程、线程、文件等章节选取 |

场景名称来自原文，不是适用范围的硬边界：Python 本地脚本访问数据库仍需读 BACKEND 的 SQL 规则。未覆盖的语言沿用项目政策；不要声称本库已覆盖其特有风险。

## 按当前操作定位

| 任务涉及 | 在相关语言索引查找 | 同时考虑 |
|---|---|---|
| 查询／持久化数据 | SQL、数据持久化、ORM、NoSQL | 输入类型、对象归属、返回信息最小化 |
| 登录／鉴权／修改记录 | 权限、访问控制、会话、Cookie、CSRF | 可信身份来源、租户/对象权限、错误输出 |
| HTML／模板／DOM／跳转 | DOM、响应输出、模板、SSR、URL、跨域 | 浏览器与服务端上下文、URL目标限制 |
| 文件上传／下载／本地路径 | 文件、路径、类型、权限 | 文件内容及大小、符号链接、可执行目录、对象权限 |
| 访问用户给定 URL | 网络请求、资源请求过滤验证 | 协议、重定向、解析结果与真实连接目标 |
| 启动程序／动态执行 | 命令、系统接口、执行代码、反序列化 | 参数语义、shell、运行权限、资源限额 |
| 密码／密钥／日志 | 加密、口令、敏感、日志 | 当前算法/参数、密钥生命周期、脱敏 |
| 内存／并发／边界计算 | 内存、指针、数字、多线程、并发 | 生命周期、错误路径、平台/语言版本 |

## 检索与全文读取

先定位技能根目录，将下列 `scripts/guide.py` 替换为其绝对路径，或在技能目录运行：

```sh
python scripts/guide.py list --language python --query SQL
python scripts/guide.py list --language javascript --scenario browser
python scripts/guide.py show PY-BACKEND-1.2.1 PY-BACKEND-1.8.3 JS-BROWSER-1.1.1
```

`--query` 是标题、章节和原文正文的大小写不敏感子串匹配，不是语义检索。无匹配时改用索引和场景，不推断不存在适用规则。`--json` 返回结构化元数据。

完整机器索引为 [rules.json](rules.json)，原文快照清单为 [manifest.json](../sources/manifest.json)。日常编码不需要读取完整 JSON。来源哈希验证失败时先核对更新，不按错位行号继续使用。
