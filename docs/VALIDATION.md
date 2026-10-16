# 发布准备验证记录

日期：**2026-10-13（Asia/Shanghai）**。环境：Windows、Python **3.14.2**。这份记录覆盖本次独立仓库的发布准备；后续版本变更后应重新验证。

## 已执行检查

| 检查 | 结果与范围 |
|---|---|
| 上游逐字节比对 | 五份指南匹配固定提交；将原简略 README 补全后，分发包的六份来源全部匹配。完整记录见 PROVENANCE.md |
| `guide.py check` | 退出 0；225 条规则、6 份来源、10 项适用性解释及相关生成内容/引用通过 |
| 原有单元测试 | 7 项通过，进程退出 0；包括规则解析边界、无效 ID、来源漂移、引用缺失及跨目录读取 |
| Skill 基础格式 | skill-creator 的 `quick_validate.py` 退出 0，返回 `Skill is valid!` |
| 独立安装 | 完整复制技能的 25 个文件到临时项目 `.agents/skills/secure-coding/`；逐文件哈希一致，LICENSE / NOTICE.md 随包保留 |
| 安装后使用 | 从临时项目根运行 `check`、`show PY-BACKEND-1.2.1` 和 `list --language go` 全部退出 0；Go 为 37 条 |
| Git 暂存内容导出 | 从 Git tree 导出 ZIP 并解压后，7 份来源/附加文件记录及两个许可证副本的哈希均一致；包校验退出 0 |
| 确定性生成 | 在 Git 导出目录执行 `build` 退出 0；生成前后技能内全部文件哈希不变 |
| Git 格式检查 | `git diff --cached --check` 退出 0；原文空白和已有生成文件末尾空行通过明确的路径属性保留 |
| CI 配置 | YAML 解析及事件、只读权限、平台/版本矩阵核对通过；所用 actions 引用固定提交 |
| 文档 | 新增文档的相对文件链接检查及独立发布材料核对完成；项目入口模板的路径按目标项目解释 |

## 首页与案例更新复验

同日，在上述 Windows / Python 3.14.2 环境中完成：

| 检查 | 实际结果 |
|---|---|
| 规则包与工具回归 | `guide.py check` 退出 0；原有 7 项测试全部通过 |
| 订单查询案例 | 6 项测试全部通过，退出 0；覆盖归属限制、参数绑定、缺失身份和输入边界，使用 SQLite 内存数据库 |
| 文档代码片段 | 首页查询片段与案例函数末尾的 AST 一致；案例文档实现与 `orders.py` 去掉说明性 docstring 后的 AST 一致 |
| 文档本地链接 | 11 份入口/说明文档中的 45 个本地文件或锚点链接均可定位；不包含上游原文及项目入口模板中的目标项目路径 |
| CI 配置更新 | YAML 解析、触发事件、只读权限、版本矩阵、固定 action 提交及新增案例测试命令核对通过 |
| Git 格式 | `git diff --check` 退出 0 |

本次增加的是安装交接文档与可运行案例；技能运行指令、指南原文和规则库未改动。`README_AI.md` 的客户端发现/调用步骤仍须在实际目标客户端执行，文件与脚本验证不替代该步骤。

## 可复现的主要命令

在仓库根目录运行：

```sh
python -B skills/secure-coding/scripts/guide.py check
python -B -m unittest discover -s skills/secure-coding/tests -p test_guide.py -v
python -B -m unittest discover -s examples/order-query -p test_orders.py -v
python -B skills/secure-coding/scripts/guide.py list --language go
python -B skills/secure-coding/scripts/guide.py show PY-BACKEND-1.2.1
git diff --check
```

检查生成结果前应先保存工作目录：运行 `guide.py build` 后检查 `git diff`。未修改来源或解释时不应产生变化。

`quick_validate.py` 是检查时环境已有的辅助工具，不随本仓库分发，也不是安装或 CI 的依赖。工具只检查技能基础格式，不能证明模型的实际决策质量。

## 未验证范围

- GitHub 远程 Actions 的四个矩阵 job 尚未执行；已配置 Windows / Ubuntu × Python 3.10 / 3.14 的矩阵，本次本地运行仅为 Windows / Python 3.14.2。首次运行结果见下方补记。
- 未验证当前或其他客户端的自动发现、自动触发，也未验证插件渠道安装。
- 未运行任何目标业务项目的安全扫描、集成测试或部署检查。
- 未对全部 225 条历史建议完成现代化审计；10 项解释只能说明其明确覆盖的范围。

本次包校验及静态使用结果不证明 AI 的安全能力相对无 Skill 基线有所提升，也不保证生成的业务代码没有漏洞。

## 2026-10-15 补记（Asia/Shanghai）

[首次 GitHub Actions 运行](https://github.com/yuhengqin/secure-coding-skill/actions/runs/38339001315)已触发，但四个矩阵 job 均显示“账户因计费问题被锁定，job 未启动”的注释；没有任何工作流步骤得到远程执行。账户所有者处理 GitHub Billing 后仍需重跑，再按实际 job 结果更新验证状态。

同日在 Windows / Python 3.14.2 重新运行 `guide.py check`、7 项工具测试、6 项订单案例测试和 `git diff --check`，均退出 0。这些结果只证明本地规则包与案例检查通过，不代替远程矩阵或客户端端到端验证。

## 2026-10-16 补记（Asia/Shanghai）

对首页新增的 skills CLI 安装路径做了实测（Windows、Node.js v24.14.0、npx 11.15.0、Python 3.14.2）：

| 检查 | 实际结果 |
|---|---|
| 技能发现 | `npx skills add yuhengqin/secure-coding-skill --list` 退出 0，列出 `secure-coding` |
| 完整安装 | `npx skills add yuhengqin/secure-coding-skill -a opencode --copy -y` 安装到临时项目 `.agents/skills/secure-coding/`；与仓库 `skills/secure-coding/` 逐文件比对，文件清单与 SHA-256 全部一致（25/25） |
| 安装后校验 | 对安装副本运行 `guide.py check`，退出 0：225 条规则、6 份来源、10 项解释 |

说明：实测针对 GitHub 公开仓库当前 main 状态；skills CLI 支持的其余客户端（Claude Code、Cursor 等）未逐一端到端验证，实际安装目录以该工具检测结果为准。远程 CI 矩阵仍未执行，首页暂以文字说明其状态，待首个绿色远程运行后恢复 CI 徽章。

## 2026-10-16 首页重排与手动安装复验

本轮同步调整中英文首页，将案例提前，并把详细手动安装集中到 [INSTALLATION.md](INSTALLATION.md)。技能包、原始规则与案例实现均未修改。

| 检查 | 实际结果与范围 |
|---|---|
| 文档结构与链接 | 中英文显式锚点及顺序、shell 命令一致；改动文档中的本地文件与锚点链接可定位，折叠区和代码围栏配对完整 |
| 首页案例 | 两份首页中修正查询片段的 AST 均与 `orders.py` 最后一个 return 一致；6 项案例测试通过 |
| 规则包 | `python -X utf8 -B skills/secure-coding/scripts/guide.py check` 退出 0，225 条规则、6 份来源、10 项解释 |
| 隔离安装场景 | 原样抽取手动安装代码块，在含空格和方括号的临时项目目录中验证正常安装、克隆失败、已有目标、父级目录联接；PowerShell 7.6.5、Windows PowerShell 5.1.19041.6093 和 Git Bash 5.2.37 均通过各自四个场景 |
| 安装完整性与保护 | 成功场景的 25 个文件 SHA-256 与源包一致，安装副本 `check` 通过；克隆失败不产生目标安装，独占临时 checkout 清理；原有 `.tmp-skill` 哨兵保留；已有目标及目录联接场景在调用 Git 前拒绝，外部目录未变 |
| 真实 Git 安装 | 在 PowerShell 5.1 和 7 下分别执行文档原样命令，经 HTTPS 克隆公开仓库并完成安装；各 25 个文件与本地源包哈希一致，临时 checkout 均已清理 |
| Git 格式 | `git diff --check` 通过 |

隔离场景使用临时 Git 函数模拟成功或部分克隆后失败，以验证控制流和已有数据保护；真实 Git 安装另行执行，不把模拟结果当作联网安装证明。验证中发现 PowerShell 5.1 在方括号路径下读取 `Get-Item -LiteralPath '.'` 会失败，已改用 `(Get-Location).ProviderPath` 并复验通过。

Bash 的执行环境为 Windows 上的 Git Bash，未实测原生 Linux、macOS 或 WSL。以上结果不覆盖客户端自动发现／调用，也未验证业务安全能力提升；验证脚本及隔离项目仅作为本次系统临时目录中的检查产物，不随技能分发。

## 2026-10-16 端到端调用补记（OpenCode，Asia/Shanghai）

同日在 Windows / Python 3.14.2 / Node.js v24.14.0 环境中，首次完成 OpenCode 客户端的端到端验证（显式调用，非自动触发）：

| 检查 | 实际结果与范围 |
|---|---|
| 客户端加载技能 | 在 OpenCode 会话中显式调用 `skill({"id":"secure-coding"})`，返回加载成功，技能 Base 目录为 `D:\chat\.agents\skills\secure-coding` |
| 活跃安装同步 | 将该安装目录与仓库 `skills/secure-coding/` 逐文件比对：25/25 文件 SHA-256 一致（补齐 LICENSE、NOTICE.md、sources/CONTRIBUTING.md、sources/provenance.json，并同步 3 个旧版文件）；对安装副本运行 `guide.py check` 退出 0，7 项工具测试通过 |
| 全新安装复验 | 在全新临时目录执行 `npx -y skills add yuhengqin/secure-coding-skill -a opencode --copy -y`；安装副本 25/25 文件与仓库哈希一致，`check`、`show PY-BACKEND-1.2.1`、`list` 均退出 0 |
| 真实规则调用 | 按技能工作流读取 `references/common.md`、`index.md`、`review.md`，对 `examples/order-query/orders.py` 完成规则审查：定位 `PY-BACKEND-1.1.1`（类型/长度校验）、`PY-BACKEND-1.2.1`（参数绑定）、`PY-BACKEND-1.8.1`（默认鉴权）、`PY-BACKEND-1.8.3`（对象归属）四条适用规则及对应代码位置；6 项案例测试通过（退出 0） |
| 退出码复核 | `check`、7 项工具测试、6 项案例测试的实际进程退出码均确认为 0 |

说明：验证为**显式调用**技能；客户端的自动发现、自动触发仍未验证。审查覆盖示例代码的规则适用性，不构成对业务项目的安全审计。其余客户端（Claude Code、Codex、Cursor 等）仍未逐一端到端验证。

## 2026-10-16 首页文案与证据分层复验

本轮同步优化中英文首页：保留首屏安装、三步流程、案例对话与状态数字，将代码对比、详细输出及目录树折叠；对话标明为案例编排，历史安装记录与本轮本地检查分开说明。规则包、来源快照和案例代码未改动。

| 检查 | 实际结果与范围 |
|---|---|
| 包完整性 | `python -X utf8 -B skills/secure-coding/scripts/guide.py check` 退出 0；225 条规则、6 份来源、10 项解释 |
| 工具与案例测试 | 分别运行 `python -X utf8 -B -m unittest discover -s skills/secure-coding/tests -v` 和 `python -X utf8 -B -m unittest discover -s examples/order-query -p test_orders.py -v`；7 + 6 项通过，均退出 0 |
| 规则数字 | 从 `references/rules.json` 统计：188 条必须、27 条建议、10 条推荐；五类语言为 45 / 45 / 49 / 37 / 49 条，总计 225 |
| 首页结构 | 122 处本地文件或锚点引用可定位；中英文显式锚点顺序、命令一致；折叠区和代码围栏配对完整 |
| 查询示意 | 两份 README 的 diff 新增代码 AST 均与 `orders.py` 最后一个 return 一致；`show PY-BACKEND-1.2.1` 的标题、原文行段与哈希前缀复核一致 |
| Python 缓存 | `git ls-files -- '*.pyc' '*/__pycache__/*'` 无输出；`.gitignore` 已有 `__pycache__/` 和 `*.py[cod]`，无需移除已跟踪文件 |

本轮未重新安装或调用 OpenCode，相关声明引用上方已记录的端到端验证。GitHub About、最新 Actions 与 Release 的公开 API 查询受到未认证请求频率限制，未获得可用结果；未修改远程设置、未添加 CI 通过徽章、未发布 Release。About 与 Topics 的可复制建议已更新到 [RELEASING.md](RELEASING.md)。
