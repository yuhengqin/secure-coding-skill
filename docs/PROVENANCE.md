# 来源核验记录

核验日期：**2026-10-13（Asia/Shanghai）**。

官方仓库：[Tencent/secguide](https://github.com/Tencent/secguide)。本次读取的默认分支为 `main`，固定核验提交为 [`bfda087142e3bb3f5840cbc6af82c1982d1d14e4`](https://github.com/Tencent/secguide/tree/bfda087142e3bb3f5840cbc6af82c1982d1d14e4)。分支未来可能移动，本记录及来源链接使用固定提交。

## 核验方法

通过公开 Git refs 确定默认分支与提交，读取固定提交下各文件的原始字节，计算 SHA-256 与本地快照比较。未做换行、BOM 或编码规范化。五份指南均与最初本地技能包逐字节相同，且匹配上述提交；这不证明最初下载时使用的历史提交。

GitHub 匿名 REST API 在核验时限流，因此提交识别使用 Git 协议，内容使用固定提交的 raw URL；未记录未经核实的提交日期。

## 分发快照

以下六份文件位于 `skills/secure-coding/sources/`，目前均与固定提交中的同名文件逐字节一致。

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| Python安全指南.md | 20622 | `b1d1f0b779b4e6352667a95e4bf28e59eb96e3ff05c20bf43e772cc8c1048eed` |
| JavaScript安全指南.md | 34435 | `ca377face9a0c04fdcf9e12afa8769eee8fdd911f6d48b18c8322498c11d2c27` |
| Java安全指南.md | 29096 | `3798229da5f5d5c07b163016fa09140a9d4bc596d8b1bbd9d8e4f0c49f85ca20` |
| Go安全指南.md | 28143 | `95c020a29e40061ed0d4e6d5f7ea5a6c4029b4512eb0b3b43d98b6a9c1f459fe` |
| C,C++安全指南.md | 47584 | `8a1880e65b833ec95e6a4d10c2c08dc9efea67c5bef8e2fe8f572fd374be25ab` |
| README.md | 1254 | `01282422dc68a1a0448c66c068204dad253b802644e9923a47a46b1a16d6f7bd` |

原本导入的本地 README 为 442 字节，SHA-256 为 `425aa5567f6db0a65aeb149322dd27ea4e59dc5bf711669e180b15435e68a190`，只有简介、理念与实践部分。在这次独立仓库整理中，已替换为固定提交的完整 README，补回索引、贡献与许可信息；原工作区中的旧文件未改动。没有进行历史提交搜索，不推断旧 README 的作者或形成时间。

上游完整 LICENSE 为 17537 字节，SHA-256 为 `317408f36f0b43b11f5aa82ef4a9bb8a5b246fb49baf4f3b6244e0b819ab304e`，逐字节保存在仓库根和技能目录。为保留原 README 的本地贡献指南链接，还收录了同一提交的 `CONTRIBUTING.md`；其实际哈希记录在 `sources/provenance.json` 的附加文件清单。

## 许可与封装变化

上游 LICENSE 第 2 行明确为 **CC-BY-SA-4.0**，第 4 行保留 THL A29 Limited 的版权声明。上游 README 的文字标签不一致，详情见 [第三方声明](../THIRD_PARTY_NOTICES.md)。

原始五份指南保持不变；本仓库增加的指令、索引、解释、工具与文档同样按 CC BY-SA 4.0 提供。新增解释不是对原文的静默替换。完整署名、修改说明和免责条款随独立技能目录保留。

## 维护边界

`manifest.json` 的六份清单用于工具校验；`provenance.json` 另行记录固定来源、许可和本次封装变化。`guide.py check` 不会联网证明远程出处，也不会校验该额外来源记录的全部字段。

每次更新快照，应重新核实提交和逐文件哈希，并同步文档。不能因为旧来源记录存在，就声称新导入的文件已经核实。流程见 [维护说明](MAINTENANCE.md)。
