# 命令与使用手册

首次使用见 [两步极速上手](../README.zh-CN.md#quickstart)；安装助手见 [README_AI.md](../README_AI.md)。以下命令均从**本仓库根目录**执行，需 Python 3.10+，无第三方包依赖。

## 检索与读取

```sh
python skills/secure-coding/scripts/guide.py list --language go
python skills/secure-coding/scripts/guide.py list --language java --query SQL
python skills/secure-coding/scripts/guide.py show PY-BACKEND-1.2.1
```

`show` 支持多个规则 ID，返回完整正文、原文行号、来源哈希和关联解释。先从语言索引与场景路由选规则，再读取正文；关键词零命中不能证明没有适用规则。

安装到业务项目后，将前缀 `skills/secure-coding/` 改为 `.agents/skills/secure-coding/`，或使用技能的绝对路径。脚本根据自身位置定位规则文件，不要求工作目录恰好是技能目录。

没有 Python 时，直接阅读 [SKILL.md](../skills/secure-coding/SKILL.md)、[场景路由](../skills/secure-coding/references/index.md) 和语言索引，按索引行号打开原文，并读取关联解释。Markdown 使用不依赖检索脚本。

## 校验与测试

```sh
python skills/secure-coding/scripts/guide.py check
python -B -m unittest discover -s skills/secure-coding/tests -p test_guide.py -v
python -B -m unittest discover -s examples/order-query -p test_orders.py -v
```

第一条检查规则包完整性；第二条运行 7 项工具回归测试；第三条运行 6 项 [订单查询示例测试](../examples/order-query/README.md)。订单案例随本仓库提供，位于可复制技能目录之外；只安装技能后，应回到本仓库运行案例。

`list`、`show`、`check` 不修改文件、不联网、不执行指南中的示例。单元测试使用临时文件或内存数据库，不需要业务数据。这些检查不会扫描目标项目，也不能证明客户端已自动发现或执行技能。

## 维护生成内容

```sh
python skills/secure-coding/scripts/guide.py build
git diff --check
git diff
```

`build` 会写入规则索引等生成文件，普通安装和使用无需执行。维护者应先保存工作目录，再按 [维护说明](MAINTENANCE.md) 修改来源或解释、重建并审阅 diff。

## 在业务项目中交付

使用 [提示词示例](../examples/USAGE.md) 请求开发、修复或只读审查。交付内容应将适用规则 ID 与实际代码位置对应，并区分静态判断、执行过的项目检查和未验证事项。

工具故障请附命令、Python 版本与错误输出；规则建议与当前框架不符时请附规则 ID 和官方依据，见 [贡献指南](../CONTRIBUTING.md)。
