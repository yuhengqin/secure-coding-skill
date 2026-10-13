# GitHub 发布步骤

本目录是独立 Git 仓库。以下步骤由仓库维护者在决定公开发布时执行；本地准备不会自动创建 GitHub 仓库、推送或发布 Release。

## 发布前检查

- 核对 [来源记录](PROVENANCE.md)、[第三方声明](../THIRD_PARTY_NOTICES.md) 和两个完整许可证副本。
- 确认 `git status` 和提交内容只包含需要分发的文件；不要加入原工作区、个人配置、环境变量文件或缓存。
- 运行 [使用手册](USAGE.md#校验与测试) 中的包校验、7 项工具测试和 6 项订单案例测试，检查 `git diff --check`。
- 从独立克隆或导出目录运行相同命令，确认五份原指南的字节未被 Git 换行转换。
- 阅读 [验证记录](VALIDATION.md)，保留未验证事项。首次推送后的远程 CI 结果不能提前声明为通过。

## 创建远程并推送

1. 在自己的 GitHub 账户或组织下创建空仓库，建议名称 `secure-coding-skill`。为了保持与本地历史一致，创建时不另行初始化 README、LICENSE 或 `.gitignore`。
2. 在本仓库根目录运行，先将 `YOUR_ACCOUNT` 换成实际账户或组织名称：

   ```sh
   git remote add origin https://github.com/YOUR_ACCOUNT/secure-coding-skill.git
   git push -u origin main
   ```

   如果已存在 `origin`，先用 `git remote -v` 核对，避免直接覆盖或推送到错误目标。

3. 建议仓库描述：`A progressive-loading secure coding skill based on Tencent/secguide, with 225 rules across five languages.`
4. 可选 Topics：`agent-skills`、`secure-coding`、`codex`、`security-guidelines`。
5. 查看 Actions 中的包校验结果；根据团队需要设置分支保护。

## 版本与下载包

首次版本建议 `v0.1.0`。先完成验证，将 `CHANGELOG.md` 的 Unreleased 内容转入实际发布日期，再提交、打标签和推送：

```sh
git add CHANGELOG.md
git commit -m "docs: release v0.1.0"
git tag -a v0.1.0 -m "Initial secure-coding skill release"
git push origin main
git push origin v0.1.0
```

可在 GitHub 的 Releases 页面选择该标签创建版本。GitHub 自带源码 ZIP 包已包含所有文件；使用者只需按 README 复制完整技能目录。

若另行提供仅含技能的压缩包，应保留 `secure-coding/SKILL.md`、`LICENSE`、`NOTICE.md`、所有 references/sources/scripts/tests。制作后重新解压并运行包校验及测试，勿根据文件名判断内容完整。

## 插件分发

当前交付是可安装到技能目录的 Agent Skill 仓库，未附加插件清单或声明插件安装已验证。如果未来需要通过 Codex 插件渠道分发，可依据 [官方说明](https://developers.openai.com/plugins/build/plugins) 增加 `plugin.json` 并单独验证插件安装；这不会改变本包所需的署名和许可证。
