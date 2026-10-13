# 贡献指南

欢迎报告规则定位错误、过时建议、解释依据不足、安装问题和工具缺陷。

## 报告问题

请提供：规则 ID、涉及的语言/框架/版本、可定位的规则原文或代码片段、预期行为与实际行为。工具问题请附命令、Python 版本和错误输出；提交前移除真实凭据及项目私密信息。

对现时安全建议的更正，请优先提供官方文档或可复现的最小案例。原指南的历史表述与工具实现缺陷应分别说明。

## 修改约定

- `sources/` 保存可追溯的原文快照，更新流程见 [维护说明](docs/MAINTENANCE.md)。
- `references/overrides.json` 是适用性解释的编辑入口。新增解释应包含规则 ID、原文观察、适用条件、核实日期、证据和来源哈希。
- `references/rules.json`、五份语言索引、`references/interpretations.md` 是生成文件，请使用 `guide.py build` 更新。
- 技能指令保持简短，按任务读取相关内容；新增支持范围需要对应的真实资料及验证。
- 工具改动应补充能够捕获真实回归的检查。纯文档修改无需增加镜像式测试。

提交前从仓库根目录运行：

```sh
python skills/secure-coding/scripts/guide.py check
python -B -m unittest discover -s skills/secure-coding/tests -p test_guide.py -v
python -B -m unittest discover -s examples/order-query -p test_orders.py -v
git diff --check
```

涉及生成文件时还应运行 `build` 并检查 diff。说明实际运行结果、未验证的平台及已知限制，避免把包校验表述为业务安全认证。

## 许可

本项目内容按 [CC BY-SA 4.0](LICENSE) 分发。请保留原作和贡献者署名、来源及修改说明；仅提交你有权按该许可提供的内容。原指南作者的许可不代表其为本项目背书。
