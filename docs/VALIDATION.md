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
