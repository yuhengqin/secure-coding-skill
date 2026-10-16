# 🛡️ Secure Coding Skill

<p align="center">
  <b>让 AI 编码助手告别安全漏洞。<br>先检索规则，再构筑防线，最后拿证据说话。</b>
</p>

<p align="center">
  <a href="./README.md">English</a> · <b>简体中文</b>
</p>

<p align="center">
  <a href="#case">先看效果</a> •
  <a href="#quickstart">极速上手</a> •
  <a href="#use-cases">适用场景</a> •
  <a href="#features">核心特性</a> •
  <a href="#compatibility">客户端兼容</a> •
  <a href="#faq">常见问题</a>
</p>

<p align="center">
  <a href="#languages"><img src="https://img.shields.io/badge/安全规则-225_条-blue.svg" alt="225 Rules"></a>
  <a href="#languages"><img src="https://img.shields.io/badge/覆盖语言-5_种主流语言-brightgreen.svg" alt="5 Languages"></a>
  <img src="https://img.shields.io/badge/CLI-仅需_Python_标准库-orange.svg" alt="Python Standard Library Only">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg" alt="License"></a>
</p>

**把 225 条安全规则，变成 AI 编码时随叫随到的安全火力。** Secure Coding Skill 将 [Tencent/secguide](https://github.com/Tencent/secguide) 封装为 Agent Skill：让编码助手先检索适用规则，再落实防护，交付时说明规则 ID、代码位置和实际检查结果。日常开发、缺陷修复、重构、代码审查，都能用上。

> **文档语言：** 原始规则与大部分配套文档为中文；中英文 README 提供相同的入门流程，CLI 界面为英文。

<span id="case"></span>
## 🧪 先看效果：订单只能自己查

**一个真实开发需求：**“用 Python 实现订单查询，沿用已有登录态，用户只能读取自己的订单；检查输入、SQL 和权限边界。”

[可运行的订单查询案例](examples/order-query/README.md) 把这条链路串了起来：**需求 → 规则 → 实现 → 测试**。

```diff
# 查询写法示意；完整输入校验见 orders.py。

- # 风险写法：直接拼接 SQL，没有订单归属限制
- return connection.execute(f"SELECT * FROM orders WHERE id = '{order_id}'").fetchone()

+ # PY-BACKEND-1.2.1 + PY-BACKEND-1.8.3：参数绑定 + 对象归属检查
+ return connection.execute(
+     "SELECT id, note FROM orders WHERE id = ? AND user_id = ?",
+     (order_id, authenticated_user_id),
+ ).fetchone()
```

| 你会得到什么 | 在这个案例中 |
| :--- | :--- |
| **有依据的规则选择** | `PY-BACKEND-1.1.1` 输入校验；`PY-BACKEND-1.2.1` 参数绑定；`PY-BACKEND-1.8.1` 默认鉴权；`PY-BACKEND-1.8.3` 对象归属 |
| **落到代码里的防护** | 输入检查 + SQL 参数绑定 + 基于服务端已验证身份的订单归属限制 |
| **能亲手复跑的证据** | 6 项测试覆盖本人／他人／不存在的订单、注入形态输入与合法单引号、无效身份值及非法订单 ID |

**直接跑起来**——在本仓库根目录执行，需要 Python 3.10+ 与标准库 `sqlite3`：

```bash
python -B -m unittest discover -s examples/order-query -p test_orders.py -v
```

案例的 6 项测试已在本地通过。上方对比用于演示规则，并非模型 A/B 实测；调用方须先完成用户认证，HTTP 认证、操作级权限和真实数据库集成不在案例范围内。[查看完整实现与测试范围 →](examples/order-query/README.md)

<span id="quickstart"></span>
## 🚀 两步极速上手

### 1. 安装

在**目标业务项目根目录**运行，按提示选择编码助手。需要带 `npx` 的 Node.js；直接读取 Markdown 规则不需要 Python。

```bash
npx skills add yuhengqin/secure-coding-skill
```

### 2. 开始干活

把技能带进一个实际任务。如果项目涉及订单查询，可以直接对助手说：

```text
请使用 secure-coding 技能实现或审查本项目的订单查询。
用户只能读取自己的订单。先检索相关的输入校验、SQL 与权限规则，
完成后说明规则 ID、对应代码位置、防护措施、实际执行的检查及未验证事项。
```

**如何判断用上了：**助手读取了适用规则，并把结论对应到代码和检查。也可以先让它定位 `secure-coding` 并读取 `PY-BACKEND-1.2.1`；若找不到技能，核对安装目录后重新打开项目。建议显式指定技能名称调用。

<details>
<summary><b>可选：检查安装后的规则包</b></summary>

有 Python 3.10+ 时，在业务项目根目录运行。若客户端使用其他目录，请替换为实际安装路径。

```bash
python .agents/skills/secure-coding/scripts/guide.py check
```

预期返回 `"status": "ok"`，包含 **225 条规则、6 份来源、10 项解释**。这验证包完整性；客户端是否成功调用需单独确认。

</details>

<details>
<summary><b>更多安装方式、更新与卸载</b></summary>

| 你的需求 | 命令或入口 |
| :--- | :--- |
| 先看看有哪些技能 | `npx skills add yuhengqin/secure-coding-skill --list` |
| 指定客户端 | `npx skills add yuhengqin/secure-coding-skill --agent codex --agent claude-code` |
| 本机所有项目可用 | `npx skills add yuhengqin/secure-coding-skill -g` |
| 更新／卸载项目级安装 | `npx skills update secure-coding` / `npx skills remove secure-coding` |
| 更新／卸载全局安装 | 在更新或卸载命令中追加 `-g` |
| 没有 Node.js | [手动安装：Linux、macOS 与 PowerShell](docs/INSTALLATION.md) |
| 让助手完成安装 | [AI 安装交接指南](README_AI.md) |

[skills CLI](https://github.com/vercel-labs/skills) 会处理各客户端的安装位置。手动安装须保留完整 `skills/secure-coding/`，包括许可证和来源文件。更新手动副本前先比较并保留本地修改，更新后运行 `guide.py check`。

</details>

<span id="use-cases"></span>
## 🎯 这些场景，直接叫上它

| 你正在做什么 | 带进改动的规则与检查 |
| :--- | :--- |
| 写 API、查数据库 | 输入校验、参数化查询、身份认证与对象归属 |
| 做上传下载、访问用户提供的 URL | 路径边界、文件约束、SSRF 与重定向处理 |
| 渲染 HTML、修改浏览器行为 | XSS、输出上下文、DOM 操作与浏览器安全边界 |
| 启动进程、反序列化数据 | 命令参数、执行边界与不可信输入 |
| 重构或审查已有代码 | 适用规则 ID、代码证据、针对性检查与未覆盖事项 |

<span id="why"></span>
<span id="features"></span>
## ⚡ 为什么选它？安全火力，随用随取

AI 写码飞快，输入边界、SQL 参数和对象权限也该从第一处改动就跟上。**把安全作战手册，直接送到编码助手手边。**

- 🎯 **225 条工业级规则，一次装齐。** Python、JavaScript/TypeScript、Java、Go、C/C++，五大语言收进一个技能包。
- ⚡ **安全火力全开，上下文轻装上阵。** 渐进式披露，沿语言与任务索引按需读取规则正文，无需一开始载入五份指南全文。
- 🔍 **每条规则，都有出处。** 原文、行号、来源 SHA-256 完整可查，另附 10 项带依据的历史建议适用性解释。
- 🔌 **CLI 零第三方依赖。** Python 3.10+ 标准库即可完成本地检索与完整性校验，不联网、不采集代码。
- 🧪 **拿检查结果说话。** 7 项工具回归测试 + 6 项可运行案例测试，执行命令公开，随时亲手复验。

<span id="how-it-works"></span>
### 从需求到证据

```mermaid
flowchart LR
    A["你的编码任务"] --> B["语言与场景索引"]
    B --> C["适用规则与解释"]
    C --> D["实现或审查"]
    D --> E["规则 ID + 代码位置 + 检查结果"]
```

模型负责选择适用规则，`guide.py` 负责在本地检索正文与出处。应用历史示例时，技能还要求核对当前 API 和项目约束。[查看完整工作流 →](skills/secure-coding/SKILL.md)

<span id="languages"></span>
## 📊 语言与覆盖范围

| 语言 | 规则数 | 环境与防御重点 |
| :--- | :---: | :--- |
| **Python** | 45 | 脚本与服务端：SQL 注入、SSRF、反序列化、访问控制 |
| **JavaScript / TypeScript** | 45 | 浏览器与 Node.js：XSS、DOM 安全、原型链污染、CORS |
| **Java** | 49 | 服务端与 Android：表达式注入、XXE、密码学应用 |
| **Go** | 37 | 后端与系统代码：路径、命令、并发与资源限制 |
| **C / C++** | 49 | 原生代码：缓冲区与整数溢出、格式化字符串、内存生命周期 |

TypeScript 复用 JavaScript 运行时规则。原文的**必须／建议／推荐**级别保留；10 项适用性解释针对特定历史建议，全部规则尚未完成现代化审计。

<span id="compatibility"></span>
## 🔌 客户端兼容情况

| 客户端／安装途径 | 规则包安装 | 技能发现与实际调用 |
| :--- | :--- | :--- |
| **OpenCode，经 skills CLI** | Windows，2026-10-16 实测：`-a opencode --copy -y`；25/25 文件一致，安装副本 `check` 通过 | 尚未端到端验证 |
| **Codex、Claude Code、Cursor、GitHub Copilot 等 skills CLI 客户端** | 上游 CLI 提供安装适配，本仓库未逐一实测 | 尚未端到端验证 |
| **手动复制** | 已验证完整包复制及安装后的 CLI 使用；目录遵循目标客户端约定 | 取决于客户端加载机制 |

以安装器报告的位置为准。共享项目级路径通常为 `.agents/skills/secure-coding/`，不同客户端可能使用专用路径。[安装详情 →](docs/INSTALLATION.md) · [验证记录 →](docs/VALIDATION.md)

<span id="validation"></span>
## ✅ 验证结果，公开可查

| 检查项 | 已记录结果 |
| :--- | :--- |
| 规则包 | **本地通过：**225 条规则、6 份来源、10 项解释 |
| 工具与案例测试 | Windows / Python 3.14.2 下 **7 + 6 项通过** |
| 远程 CI | 已配置 Windows / Ubuntu × Python 3.10 / 3.14；账户计费问题阻止运行，仍待执行 |
| 模型安全能力提升 | 尚未开展与无技能基线的受控对比 |

包校验和案例测试仅覆盖各自声明的范围；业务项目仍需运行自身的测试、扫描与审查。[执行命令与完整证据 →](docs/VALIDATION.md)

<span id="faq"></span>
## ❓ 常见问题

<details>
<summary><b>业务项目必须使用 Python 吗？</b></summary>

不必。助手可以直接读取 Markdown 规则；Python 3.10+ 只用于本地检索、包校验与测试。

</details>

<details>
<summary><b>会占用多少上下文？</b></summary>

技能按渐进式披露组织：发现时提供元数据，调用后读取指令、索引和适用规则。实际 token 消耗取决于客户端和任务，本仓库尚未公布实测预算。

</details>

<details>
<summary><b>能替代安全扫描器，或让 AI 客户端完全离线吗？</b></summary>

它指导生成与审查；请保留项目原有的静态分析、动态测试和人工审查。本地 CLI 不联网，编码助手的模型调用和数据处理仍遵循客户端设置及服务商条款。

</details>

<details>
<summary><b>能只安装一种语言吗？</b></summary>

目前请保留完整包，完整性校验覆盖整个规则库；助手仍可选择性读取。单语言导出已列入路线图。

</details>

<span id="roadmap"></span>
## 🤝 一起完善它

欢迎提交**客户端验证记录**、**有当前依据的规则更正**、**包含有效测试的可运行案例**。从[贡献指南](CONTRIBUTING.md)开始；可利用的工具缺陷请按[安全报告说明](SECURITY.md)提交。

- 完成客户端实际调用验证，补充真实使用演示。
- 跑通首个远程 CI，发布带版本号的 Release。
- 扩充有来源的适用性解释与可运行案例。
- 探索单语言导出和更多客户端适配。

## 📚 继续探索

| 你想了解什么 | 从这里开始 |
| :--- | :--- |
| 手动安装 | [安装指南](docs/INSTALLATION.md) |
| 检索规则、执行检查 | [命令与使用手册](docs/USAGE.md) |
| 更多开发与审查提示词 | [使用示例](examples/USAGE.md) |
| 原始来源与封装修改 | [来源追溯](docs/PROVENANCE.md) · [第三方声明](THIRD_PARTY_NOTICES.md) |
| 维护与发布 | [维护说明](docs/MAINTENANCE.md) · [发布步骤](docs/RELEASING.md) · [更新记录](CHANGELOG.md) |

可安装的完整技能包位于 `skills/secure-coding/`，可运行案例位于 `examples/order-query/`。大部分配套文档使用中文。

## 📜 来源与开源协议

基于 **THL A29 Limited, a Tencent company** 的 **Secure Coding Guide**，Copyright (C) 2021。按 **[CC BY-SA 4.0](LICENSE)** 分发，保留原作署名与修改说明。本项目为独立社区封装，未获得腾讯官方背书。安装包须保留 `LICENSE`、`NOTICE.md` 及来源文件。

<p align="center">
  下一次让 AI 写代码，就把安全一起带上。<br>
  如果它帮到了你，欢迎点亮 ⭐️ <b>Star</b>、分享真实案例，或<a href="https://github.com/yuhengqin/secure-coding-skill/issues/new/choose">提交问题</a>。
</p>
