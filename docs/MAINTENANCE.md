# 维护说明

## 日常使用与生成文件

`list`、`show`、`check` 为只读命令。`build` 会写入规则目录和生成的 Markdown；仅维护者需要执行。

仅修改解释时：编辑 `skills/secure-coding/references/overrides.json`，核对每项关联规则、证据、日期和适用条件，然后运行：

```sh
python skills/secure-coding/scripts/guide.py build
python skills/secure-coding/scripts/guide.py check
python -B -m unittest discover -s skills/secure-coding/tests -p test_guide.py -v
git diff --check
```

`build` 不会自动刷新网络来源；原文不变时，结果应是确定的。检查生成 diff，不要手工修补生成文件。

## 更新上游快照

1. 在本仓库之外取得 [Tencent/secguide](https://github.com/Tencent/secguide) 的目标版本，固定完整提交 SHA，并检查该提交的许可证和所有拟导入文件。
2. 确保当前工作已提交或另行保存。审阅五份指南及 README 的变化，尤其是规则编号、语义、版本和例子。
3. 从仓库根目录运行下述命令，将 `UPSTREAM_DIRECTORY` 替换为已审阅的本地上游目录路径：

   ```sh
   python skills/secure-coding/scripts/guide.py build --source-dir UPSTREAM_DIRECTORY
   ```

   该命令先导入六份 Markdown 及清单，再构建索引。来源变化后，哈希绑定的解释可能导致构建停止；此时六份快照可能已经更新，操作不是整体事务。不要将失败状态直接发布。

4. 对所有失效解释重新核查正文、行号、版本条件及证据，再修改 `overrides.json`。不要只替换哈希来绕过复核；重新运行 `build`。
5. 更新 `sources/manifest.json` 的 `origin`、`upstream_revision` 及来源说明。导入命令会将这些字段重置为本地快照和 `null`，因为它无法证明本地目录对应哪个远程提交。
6. 同步更新 `sources/provenance.json`、技能内 `NOTICE.md`、仓库 `THIRD_PARTY_NOTICES.md` 和 `docs/PROVENANCE.md`。为每份来源保留实际哈希、固定版本链接及任何差异，不能把未经核实的本地内容标成远程原件。
7. 检查上游许可证变化；同步保存上游完整 `LICENSE` 到仓库根和技能目录，并同步目标提交的 `sources/CONTRIBUTING.md` 及其附加文件哈希。`guide.py` 不会替你同步或审计许可证、署名及来源说明。
8. 运行包校验和测试；如果全部六份快照确实与上游目录逐字节一致，可追加 `check --upstream UPSTREAM_DIRECTORY`。有历史或编辑版文件时，以来源记录中的逐文件比对为准。

## 保持字节与可移植性

`sources/` 的哈希对换行和 BOM 敏感。`.gitattributes` 对来源文件关闭文本转换；不要用编辑器批量规范化来源文件。生成文件使用 UTF-8 / LF。

在 Windows 和其他系统间分发后，运行 `guide.py check`。发布前还应从 Git 导出的干净内容或独立克隆运行检查，避免只验证工作目录而漏掉 Git 换行转换。

## 验证边界

`guide.py check` 验证六份来源、规则/解释绑定、生成内容和技能内部 Markdown 链接。它不验证远程来源真实性、许可合规、当前 API 正确性、README 的全部链接，也不扫描业务代码。来源文件 `provenance.json` 是维护者的证据记录；其更新仍需人工核对。
