# 本技能的适用性解释

由 overrides.json 生成；原文快照保持不变。
这些解释是有出处的补充或纠偏，不代表全部历史指南已完成现代化审计。
解释适用于列出的规则；用户明确要求和项目已批准的安全政策仍需遵循，冲突要说明。

<a id="int-runtime"></a>
## INT-RUNTIME · 运行时维护状态

适用规则：PY-COMMON-2.1.1

核实日期：2026-10-12。范围：原文静态核对与已打开的一手文档；未运行完整业务示例。

原文情况：Python 原文 123–129 行将新项目下限写为 Python 3.6+。官方已列明 Python 3.6 于 2021-12-23 结束支持。

本技能采用：不要以满足 3.6+ 作为新项目选型充分条件。核对实际运行时、依赖兼容性与支持周期，选仍获安全更新的稳定分支及其补丁版本。既有项目升级需评估兼容性，不能擅自大版本升级。

依据：
- [Python 官方版本维护状态](https://devguide.python.org/versions/)

<a id="int-password-storage"></a>
## INT-PASSWORD-STORAGE · 采用密码专用哈希

适用规则：PY-COMMON-1.3.3, JAVA-BACKEND-1.8.4

核实日期：2026-10-12。范围：原文静态核对与已打开的一手文档；未运行完整业务示例。

原文情况：Python 109–113 行要求不可逆算法和随机盐，Java 612–614 行建议随机盐及多轮哈希；这些表述未指定密码专用算法及成本。

本技能采用：通过维护中的密码哈希库保存密码，优先考虑 Argon2id；受平台或合规约束时按当前文档选择 scrypt、PBKDF2 等适合方案。配置成本、独立盐、验证和逐步升级策略。不要自行循环快速 SHA-256 或用可逆加密代替密码哈希；迁移旧哈希要保留兼容验证并在成功登录后升级。

依据：
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

<a id="int-aead"></a>
## INT-AEAD · 加密完整性和 nonce 唯一性

适用规则：PY-COMMON-1.1.1, JAVA-BACKEND-1.8.1

核实日期：2026-10-12。范围：原文静态核对与已打开的一手文档；未运行完整业务示例。

原文情况：Python 75–77 行建议使用 AES；Java 596–602 行已推荐 GCM，并要求 CBC 随机 IV、GCM 随机 nonce。

本技能采用：选用成熟库的认证加密方案，并按该库要求管理密钥和 nonce。GCM 的同一密钥下 nonce 必须不重复，不能只以“调用随机函数”证明这一点；随机生成还需匹配长度、调用量和碰撞风险约束。CBC 的随机 IV 不提供消息完整性，使用时还需可靠认证方案。不要自研组合。

依据：
- [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [MDN AesGcmParams](https://developer.mozilla.org/en-US/docs/Web/API/AesGcmParams)

<a id="int-xss-context"></a>
## INT-XSS-CONTEXT · 按输出上下文处理数据

适用规则：JS-BROWSER-1.1.1, JS-BROWSER-1.1.2, JS-NODE-1.6.3, JAVA-BACKEND-1.5.3, PY-BACKEND-1.6.3

核实日期：2026-10-12。范围：原文静态核对与已打开的一手文档；未运行完整业务示例。

原文情况：指南包含 DOM 安全 API、按上下文编码和协议限制；JS 541 行及 Java 470–473 行的表格仍可能把 URL/style 属性理解成普通属性。

本技能采用：普通文本优先通过文本 API 或框架默认转义输出。需要富文本时使用维护中的、配置恰当的净化器。HTML 文本、属性、URL、CSS 和 JavaScript 分别处理；完整 URL 的协议/目标允许列表校验不能由编码替代。URL 参数编码后嵌入 HTML 属性仍需属性编码。不要把通用 htmlEncode 或字符串替换用于所有上下文。

依据：
- [OWASP Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

<a id="int-command"></a>
## INT-COMMAND · 命令字符黑名单不能建立完整边界

适用规则：PY-BACKEND-1.3.2, JS-NODE-1.2.1

核实日期：2026-10-12。范围：原文静态核对与已打开的一手文档；未运行完整业务示例。

原文情况：Python 284–300 行删除字符后调用 os.system；JS 391–400 行标为 good 的示例删除部分字符后仍拼接 exec 命令。未验证这些示例在具体平台上的安全性。

本技能采用：优先业务库。必须启动程序时固定可执行文件、使用参数数组、关闭 shell，并校验各参数的业务类型、允许值和选项注入风险。不要只删几个符号后拼接 shell 命令。Windows .bat/.cmd 等依赖 shell 的场景需单独分析，不能套用普通可执行文件结论；已有平台约束必须明确保留。

依据：
- [Node.js child_process](https://nodejs.org/api/child_process.html)
- [OWASP OS Command Injection Defense](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)

<a id="int-password-policy"></a>
## INT-PASSWORD-POLICY · 口令组成要求受政策适用范围约束

适用规则：PY-COMMON-1.3.2

核实日期：2026-10-12。范围：原文静态核对与已打开的一手文档；未运行完整业务示例。

原文情况：Python 100–107 行要求大小写、数字、特殊字符及最近六次不重复。NIST SP 800-63B-4 对其适用的远程身份认证系统不要求这类强制字符组合。

本技能采用：先确认项目适用的认证政策，不直接把原文字符组合要求复制为所有项目的统一规则。采用 NIST SP 800-63B-4 时，应按其单因素/多因素场景设置长度、弱口令阻断和尝试限速，并遵循其不强制字符组合的要求。不要借本说明擅自改掉项目已批准的密码政策；发现冲突要指出并给出依据。

依据：
- [NIST SP 800-63B-4 Password Verifiers](https://pages.nist.gov/800-63-4/sp800-63b.html)

<a id="int-go-loop"></a>
## INT-GO-LOOP · 循环变量捕获取决于 Go 语言版本

适用规则：GO-BACKEND-1.9.1

核实日期：2026-10-12。范围：原文静态核对与已打开的一手文档；未运行完整业务示例。

原文情况：Go 980–1019 行将循环内闭包直接引用循环变量一概标为错误。

本技能采用：检查 go.mod 的 go 版本、文件构建约束以及循环变量声明方式。Go 1.22 起，按新语义在循环中声明的变量每轮独立，不能仅据闭包引用就判定数据竞争。旧语义、循环外变量赋值及共享可变对象仍需检查；显式传参是可选手段，不能用机械改写替代并发分析。

依据：
- [Go 1.22 Release Notes](https://go.dev/doc/go1.22)
- [Fixing For Loops in Go 1.22](https://go.dev/blog/loopvar-preview)

<a id="int-frame"></a>
## INT-FRAME · 不使用已废弃的 ALLOW-FROM

适用规则：PY-BACKEND-1.6.2

核实日期：2026-10-12。范围：原文静态核对与已打开的一手文档；未运行完整业务示例。

原文情况：Python 422 行仍把 X-Frame-Options: ALLOW-FROM origin 列作有效可选值。

本技能采用：按嵌入需求使用 CSP frame-ancestors；需要 X-Frame-Options 兼容措施时使用有效的 DENY 或 SAMEORIGIN。不要使用 ALLOW-FROM，现代浏览器可能直接忽略含该指令的整个响应头。配置是否生效需用目标响应和浏览器验证。

依据：
- [MDN X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options)

<a id="int-cpp-lifetime"></a>
## INT-CPP-LIFETIME · 标题不能取代生命周期和边界检查

适用规则：CPP-COMMON-2.4

核实日期：2026-10-12。范围：原文静态分析；未运行 C++ 示例。

原文情况：C/C++ 589 行标题是“返回栈上变量的地址”，591 行正文实际禁止此行为。607–617 行的 Good 示例分配 300 字节后使用未充分约束的 len 作索引。

本技能采用：执行正文要求：不能返回已经失效的局部栈对象地址。优先返回有明确所有权的 string/vector 等值类型；若使用缓冲区，另外检查长度上下界、分配失败、初始化及释放责任。不要复制该 Good 示例作为已证明安全的实现；例如 len=300 时写 a[len] 已超出所分配数组。

依据：
- [原始 C/C++ 指南 589–623 行（静态证据）](../sources/C,C++安全指南.md)

<a id="int-upload-ext"></a>
## INT-UPLOAD-EXT · 扩展名示例的点号不匹配

适用规则：PY-BACKEND-1.4.1

核实日期：2026-10-12。范围：原文静态核对与已打开的一手文档；未运行完整业务示例。

原文情况：Python 315 行允许列表是 txt/jpg/png，320 行却直接与 os.path.splitext(filename)[1] 比较；后者正常返回带前导点的扩展名。

本技能采用：将扩展名及允许列表规范化为同一种格式，例如统一保留前导点并小写。保留文件大小和类型范围要求；扩展名校验不能证明文件内容安全，应按业务检查内容、保存位置及访问权限。原示例会拒绝通常应允许的 a.jpg，不应原样复制。

依据：
- [Python os.path.splitext](https://docs.python.org/3/library/os.path.html#os.path.splitext)
- [原始 Python 指南 308–324 行](../sources/Python安全指南.md)

