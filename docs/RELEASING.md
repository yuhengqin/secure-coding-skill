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

3. GitHub About 建议使用以下双语简介（可直接复制；此文档不代表远程设置已更新）：

   ```text
   把 Tencent/secguide 的 225 条安全规则带进 AI 编码与审查。225 security rules across 5 language families, with source references and repeatable checks.
   ```

4. 建议 Topics：`agent-skills`、`secure-coding`、`claude-code`、`codex`、`ai-agents`、`secguide`、`code-review`、`appsec`、`security-guidelines`。更新时保留已有且相关的标签。
5. 查看 Actions 中的包校验结果；根据团队需要设置分支保护。

## 版本与下载包

首版使用 [`v0.1.0`](https://github.com/yuhengqin/secure-coding-skill/releases/tag/v0.1.0)，首次绿色远程 CI 见 [验证记录](VALIDATION.md#2026-10-18-首个绿色远程-ci-与-v010)。后续版本先将 `CHANGELOG.md` 的 Unreleased 内容转入实际版本和发布日期，更新发布材料，再提交并推送候选提交。下面以首版命令为例，发布新版本时应替换版本号，不覆盖已有标签：

```sh
git add CHANGELOG.md README.md README_EN.md docs/VALIDATION.md docs/RELEASING.md
git commit -m "docs: release v0.1.0"
git push origin main
```

在 Actions 中核对**候选提交的完整 SHA**，确认四个矩阵 job 及所有校验步骤全部成功后，再打标签、推送并创建 Release。本地检查、较早提交的绿色结果或工作流配置正确均不能代替该提交的远程结果。

```sh
git tag -a v0.1.0 -m "Initial secure-coding skill release"
git push origin v0.1.0
```

可在 GitHub 的 Releases 页面选择该标签创建版本。说明中记录完整提交 SHA、该提交的绿色 CI 链接及实际验证范围。GitHub 自带源码 ZIP 包已包含所有文件；使用者只需按 README 复制完整技能目录。发布后应下载该标签的源码归档，核对完整技能目录、来源与两个许可证副本，重新运行包校验及 7 + 6 项测试；不要把本地打包检查描述成远程下载验证。

若另行提供仅含技能的压缩包，应保留 `secure-coding/SKILL.md`、`LICENSE`、`NOTICE.md`、所有 references/sources/scripts/tests。制作后重新解压并运行包校验及测试，勿根据文件名判断内容完整。

## 插件分发

当前交付是可安装到技能目录的 Agent Skill 仓库，未附加插件清单或声明插件安装已验证。如果未来需要通过 Codex 插件渠道分发，可依据 [官方说明](https://developers.openai.com/plugins/build/plugins) 增加 `plugin.json` 并单独验证插件安装；这不会改变本包所需的署名和许可证。
