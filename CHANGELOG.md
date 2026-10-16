# Changelog

## Unreleased

- 中文首页设为默认：`README.md` 为中文，英文首页移至 `README_EN.md`（原 `README.zh-CN.md` 不再使用），双语互链与 `docs/` 内引用同步更新。
- 双语首页重构：新增 SVG 视觉锚点（`assets/banner.svg`）、GitHub Stars 动态徽章、AI 代理前置入口、2026-10-16 真实端到端实测输出（技能加载、skills CLI 安装 25/25、`check`/`show` 真实输出、7+6 测试证据）、场景路由表与仓库结构树。
- 增加 `AGENTS.md` 与 `CLAUDE.md`：面向来访 AI 代理的仓库导航与红线（sources 只读、`build` 唯一会写文件的命令、如实报告未验证项）。
- 记录 OpenCode 端到端调用验证（2026-10-16）：显式调用 `secure-coding` 加载成功；活跃安装与仓库 25/25 哈希一致；按技能工作流完成订单案例规则审查；详见 `docs/VALIDATION.md`。
- 同步重排中英文 README：提前展示订单查询案例，将上手主流程压缩为安装与调用两步，补充任务场景、客户端验证表和按读者需求组织的文档入口。
- 手动安装移入双语 `docs/INSTALLATION.md`：独立临时目录、克隆失败即停止、拒绝覆盖现有安装或沿链接路径写入，只清理本次创建的临时目录。
- 首页接入 skills CLI 一行安装（`npx skills add yuhengqin/secure-coding-skill`），克隆复制降为备选，并补充更新/卸载命令与客户端覆盖说明；中英文首页同步补齐实战案例、验证边界、路线图、文档索引与仓库结构。
- 实测 skills CLI 安装链路（2026-10-16）：技能可被发现、完整安装的 25 个文件与仓库 SHA-256 一致、安装副本 `guide.py check` 通过；记录见 `docs/VALIDATION.md`。
- 修正首页验证状态表述：原“Windows / Ubuntu 及 Python 3.10 ~ 3.14 已通过”与验证记录不符，改为按实际证据表述（Windows / Python 3.14.2 本地验证；远程 CI 因账户计费锁定待重跑）；CI 徽章暂时移除，待首个绿色远程运行后恢复。
- 重写中文首页，先说明用途、适用人群和工作方式，再提供两种安装方式、可运行案例、验证边界与路线图。
- 默认提供英文首页 `README.md`，中文完整首页调整为 `README.zh-CN.md`，并在两份首页中说明原规则正文仍为中文。
- 增加工具问题与规则更正的 Issue 模板，以及私密漏洞报告说明 `SECURITY.md`。
- 记录 GitHub Actions 首次运行因账户计费锁定而未启动；远程矩阵仍待验证。
- 增加 `README_AI.md` 安装交接及 `docs/USAGE.md` 命令手册。
- 增加 Python / SQLite 订单查询案例、规则对应说明和 6 项行为测试，并接入 CI。
- 将安全编码 Skill 整理为独立仓库，提供可完整复制的 `skills/secure-coding/`。
- 收录五种语言、225 条规则及 10 项有来源的适用性解释。
- 提供规则检索、正文读取、来源哈希和生成内容校验，以及 7 项回归检查。
- 补充安装、使用、维护、来源、贡献及 GitHub 发布文档。
- 保留 Tencent/secguide 的 CC BY-SA 4.0 许可证及署名；来源比对详情见 `docs/PROVENANCE.md`。
- 增加 Git 换行策略及 Windows / Ubuntu 的包校验工作流。
