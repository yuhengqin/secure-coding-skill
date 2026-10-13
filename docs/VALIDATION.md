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

## 可复现的主要命令

在仓库根目录运行：

```sh
python -B skills/secure-coding/scripts/guide.py check
python -B -m unittest discover -s skills/secure-coding/tests -p test_guide.py -v
python -B skills/secure-coding/scripts/guide.py list --language go
python -B skills/secure-coding/scripts/guide.py show PY-BACKEND-1.2.1
git diff --check
```

检查生成结果前应先保存工作目录：运行 `guide.py build` 后检查 `git diff`。未修改来源或解释时不应产生变化。

`quick_validate.py` 是检查时环境已有的辅助工具，不随本仓库分发，也不是安装或 CI 的依赖。工具只检查技能基础格式，不能证明模型的实际决策质量。

## 未验证范围

- GitHub 远程 Actions 尚未运行；已配置 Windows / Ubuntu × Python 3.10 / 3.14 的矩阵，本次本地运行仅为 Windows / Python 3.14.2。
- 未验证当前或其他客户端的自动发现、自动触发，也未验证插件渠道安装。
- 未运行任何目标业务项目的安全扫描、集成测试或部署检查。
- 未对全部 225 条历史建议完成现代化审计；10 项解释只能说明其明确覆盖的范围。

本次包校验及静态使用结果不证明 AI 的安全能力相对无 Skill 基线有所提升，也不保证生成的业务代码没有漏洞。
