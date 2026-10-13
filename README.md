# Secure Coding Skill

将 [Tencent/secguide](https://github.com/Tencent/secguide) 的安全编码指南封装为可按需读取的 Agent Skill，帮助 AI 在编码前选择规则、实现时检查适用条件、交付前验证改动。

当前包含 **5 种语言、225 条规则、10 项带出处的适用性解释**。原指南、规则索引、解释和检索工具随包提供，可以离线读取和检索。

本项目是独立的社区封装，未获得腾讯官方背书。指南及本仓库内容采用 **CC BY-SA 4.0**；来源和修改情况见 [第三方声明](THIRD_PARTY_NOTICES.md)。

## 支持范围

| 语言 | 规则数 | 场景 |
|---|---:|---|
| Python | 45 | 通用、服务端 |
| JavaScript | 45 | 浏览器、Node.js |
| Java | 49 | Android、服务端 |
| Go | 37 | 通用、服务端 |
| C/C++ | 49 | 通用安全编码 |

TypeScript 可复用适用的 JavaScript 运行时规则；本包没有独立的 TypeScript 规则库。原文中的“必须／建议／推荐”保持原级别。

## 安装

先克隆或下载本仓库。在 GitHub 仓库页面使用 **Code → Clone / Download ZIP**，解压后找到 `skills/secure-coding/`。

### 安装到单个项目

将 **整个** `skills/secure-coding/` 目录复制到目标项目的 `.agents/skills/secure-coding/`：

```text
your-project/
├── .agents/
│   └── skills/
│       └── secure-coding/
│           ├── SKILL.md
│           ├── LICENSE
│           ├── NOTICE.md
│           ├── references/
│           ├── sources/
│           ├── scripts/
│           └── tests/
└── AGENTS.md
```

若该目录已经存在，先对比版本和本地修改，再更新。可将 [examples/AGENTS.md](examples/AGENTS.md) 的段落合并进目标项目已有的 `AGENTS.md`，保留其他指令。

希望技能适用于个人所有项目时，可将同一完整目录放到 `~/.agents/skills/secure-coding/`；Windows 对应 `%USERPROFILE%\.agents\skills\secure-coding\`。避免在同一环境重复安装相同名称的技能。

Codex 的技能目录和发现方式见 [官方文档](https://learn.chatgpt.com/docs/build-skills)。本仓库的 `skills/` 是分发目录；克隆仓库不会自动把它安装到其他业务项目。

### 通过 Skill Installer 安装

在提供 `skill-installer` 的 Codex 环境中，将本仓库 GitHub 地址交给它，并明确路径：

> 使用 skill-installer，从我提供的 GitHub 仓库安装 skills/secure-coding 目录中的技能。

也可始终采用上述手动复制方式。新技能未出现时，重新打开项目或重启客户端。其他支持 Agent Skills 的助手需按其官方文档配置发现路径；本仓库未逐一验证这些客户端。

## 快速使用

在安装后的项目中发送：

> 请使用 secure-coding 技能完成这次 Go 接口改动。根据涉及的输入、数据库和文件操作读取适用规则，并在完成后说明规则 ID、处理结果及实际执行的验证。

Codex CLI / IDE 支持显式提及 `$secure-coding`。自动选用取决于客户端、技能描述与任务上下文；不能仅凭复制成功就认定自动触发已生效。

期望交付包含：适用规则及其对应的代码位置、已处理的问题、实际执行的检查、仍未验证的事项。可参考 [使用示例](examples/USAGE.md)。

## 如何按需加载

1. 发现技能时读取名称与描述。
2. 使用技能时读取 `SKILL.md`、共性入口和场景路由。
3. 按本次任务选择语言索引，读取相关规则正文及适用性解释。
4. 交付前按验证约定检查改动。

只处理 Go 时无需把其他语言指南全文放进上下文。按需选择由助手执行，并非程序强制的访问隔离。检索脚本会在本地校验完整规则库，但只向模型返回请求的结果。

**目前需要安装完整包。** 不要直接删除其他语言文件；来源清单和校验仍依赖全部指南。当前未提供单语言导出功能。

## 依赖与命令

- 直接阅读 Markdown：不需要 Python。
- 使用检索、构建及校验工具：Python 3.10+，仅标准库，无第三方包依赖。
- `list`、`show`、`check` 不修改文件、不联网、不执行指南中的代码示例。
- `build` 用于维护，会写入生成文件；普通使用者无需执行。

以下命令在**本仓库根目录**运行：

```sh
python skills/secure-coding/scripts/guide.py list --language go
python skills/secure-coding/scripts/guide.py list --language java --query SQL
python skills/secure-coding/scripts/guide.py show PY-BACKEND-1.2.1
python skills/secure-coding/scripts/guide.py check
python -B -m unittest discover -s skills/secure-coding/tests -p test_guide.py -v
```

安装到业务项目后，将命令前缀 `skills/secure-coding/` 改为 `.agents/skills/secure-coding/`，或使用技能的绝对路径。`show` 返回原文行号、来源哈希及关联解释。关键词零命中不能证明没有适用规则。

## 验证与局限

`guide.py check` 校验来源哈希、225 条规则、10 项解释、生成文件及技能内部引用；单元测试检查规则边界、无效 ID、来源漂移和跨工作目录检索等行为。

这些是**规则包完整性检查**，不是业务代码安全扫描。它们也不证明 AI 自动触发或始终遵守指南。项目安全测试、静态分析和合并门禁仍需使用目标项目的工具。

原指南中的版本、密码、加密、框架及正反示例含有历史背景；10 项解释只覆盖部分高影响条目，不能视为全部 225 条规则已经完成现代化审计。迁移示例前应核验当前 API 和运行环境。

本地验证环境、实际结果及未覆盖范围见 [验证记录](docs/VALIDATION.md)。仓库提供 Windows / Ubuntu、Python 3.10 / 3.14 的 GitHub Actions 配置；远程结果以实际运行记录为准。

## 仓库结构与维护

```text
secure-coding-skill/
├── README.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/                    # 来源、维护、验证、发布说明
├── examples/                # 项目入口与提示词示例
├── .github/workflows/       # 规则包 CI
└── skills/secure-coding/    # 可独立复制的完整技能包
    ├── SKILL.md
    ├── LICENSE
    ├── NOTICE.md
    ├── references/
    ├── sources/
    ├── scripts/
    └── tests/
```

更新指南和解释请遵循 [维护说明](docs/MAINTENANCE.md)；提交问题或改进见 [贡献指南](CONTRIBUTING.md)；创建 GitHub 仓库和发布版本见 [发布步骤](docs/RELEASING.md)。

## 来源与许可

原作：**Secure Coding Guide**，作者及版权方 **THL A29 Limited, a Tencent company**，Copyright (C) 2021。原仓库：[Tencent/secguide](https://github.com/Tencent/secguide)。

本仓库按 **Creative Commons Attribution-ShareAlike 4.0 International（CC BY-SA 4.0）** 分发，保留上游版权声明和完整 [LICENSE](LICENSE)。封装增加了技能指令、索引、适用性解释、工具及文档；具体快照对应关系和变化见 [来源记录](docs/PROVENANCE.md)。复制单个技能目录时，请同时保留其中的 `LICENSE`、`NOTICE.md` 及来源文件。

上游 README 的链接标签写作“CC BY 4.0”，但其目标链接和 `LICENSE` 全文是 **CC BY-SA 4.0**；本项目依照许可证全文标注。
