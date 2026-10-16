# Manual installation / 手动安装

[English quickstart](../README.md#quickstart) · [中文快速开始](../README.zh-CN.md#quickstart)

The recommended installation is `npx skills add yuhengqin/secure-coding-skill`. Use the commands below when you have Git but do not want to install Node.js. Run **one complete block** from your **target project's root**, not this distribution repository.

推荐使用 `npx skills add yuhengqin/secure-coding-skill`。已有 Git、不想安装 Node.js 时，可在**目标业务项目根目录**完整执行对应代码块，不要把本分发仓库误当作目标项目。

These commands create a new installation at `.agents/skills/secure-coding/`. They stop if the destination already exists or a skill-path component is a symbolic link/junction. Each run owns a uniquely named temporary directory, stops on clone failure, and cleans up only that directory. Existing installations and local customizations are not overwritten.

以下命令新建 `.agents/skills/secure-coding/`；若目标已存在，或技能路径包含符号链接／目录联接，则停止。每次使用独立临时目录，克隆失败即停止，只清理本次创建的临时目录，不覆盖已有安装或本地定制。

## Linux / macOS — Bash

```bash
(
  set -eu
  project_root=$(pwd -P)
  target="$project_root/.agents/skills/secure-coding"
  for path in "$project_root/.agents" "$project_root/.agents/skills" "$target"; do
    if [ -L "$path" ]; then
      printf 'Refusing a linked skill path: %s\n' "$path" >&2
      exit 1
    fi
  done
  if [ -e "$target" ]; then
    printf 'Already exists; compare local changes before updating: %s\n' "$target" >&2
    exit 1
  fi
  stage=$(mktemp -d "$project_root/.secure-coding-install.XXXXXX")
  trap 'rm -rf -- "$stage"' EXIT
  git clone --depth 1 https://github.com/yuhengqin/secure-coding-skill.git "$stage/repository"
  source_dir="$stage/repository/skills/secure-coding"
  test -f "$source_dir/SKILL.md"
  mkdir -p "$project_root/.agents/skills"
  mkdir "$target"
  cp -R "$source_dir/." "$target/"
  printf 'Installed: %s\n' "$target"
)
```

## Windows — PowerShell 5.1 / 7

```powershell
& {
    $ErrorActionPreference = 'Stop'
    $projectRoot = (Get-Location).ProviderPath
    $skillParent = Join-Path $projectRoot '.agents\skills'
    $target = Join-Path $skillParent 'secure-coding'
    foreach ($path in @((Join-Path $projectRoot '.agents'), $skillParent, $target)) {
        $item = Get-Item -LiteralPath $path -Force -ErrorAction SilentlyContinue
        if ($item -and ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
            throw "Refusing a linked skill path: $path"
        }
    }
    if (Test-Path -LiteralPath $target) {
        throw "Already exists; compare local changes before updating: $target"
    }
    $stageRoot = Join-Path $projectRoot ('.secure-coding-install-' + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $stageRoot | Out-Null
    try {
        git clone --depth 1 https://github.com/yuhengqin/secure-coding-skill.git (Join-Path $stageRoot 'repository')
        if ($LASTEXITCODE -ne 0) { throw "git clone failed (exit $LASTEXITCODE)" }
        $sourceDir = Join-Path $stageRoot 'repository\skills\secure-coding'
        if (-not (Test-Path -LiteralPath (Join-Path $sourceDir 'SKILL.md') -PathType Leaf)) {
            throw 'The cloned repository does not contain the skill package.'
        }
        New-Item -ItemType Directory -Path $skillParent -Force | Out-Null
        New-Item -ItemType Directory -Path $target | Out-Null
        Get-ChildItem -LiteralPath $sourceDir -Force | Copy-Item -Destination $target -Recurse
        Write-Output "Installed: $target"
    }
    finally {
        $stageItem = Get-Item -LiteralPath $stageRoot -Force
        if (($stageItem.Parent.FullName -ne $projectRoot) -or
            ($stageItem.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
            throw "Refusing to clean an unexpected temporary path: $stageRoot"
        }
        Remove-Item -LiteralPath $stageItem.FullName -Recurse -Force
    }
}
```

## Verify and invoke / 校验与调用

With Python 3.10+, run from your target project's root:

有 Python 3.10+ 时，在目标业务项目根目录运行：

```bash
python .agents/skills/secure-coding/scripts/guide.py check
```

Expected: `"status": "ok"`, 225 rules, 6 sources, 10 interpretations. Then ask your client to locate `secure-coding` and read `PY-BACKEND-1.2.1`. Package checks do not prove client discovery or invocation. Without Python, the Markdown rules remain usable.

预期为 `"status": "ok"`、225 条规则、6 份来源、10 项解释。随后让客户端定位 `secure-coding` 并读取 `PY-BACKEND-1.2.1`。包校验不替代客户端发现与调用验证；没有 Python 仍可读取 Markdown 规则。

## Other destinations and updates / 其他目录与更新

- **Other clients:** follow the client's documented skill directory, or let the skills CLI select it. These copy commands target the shared project-level directory only.
- **Global installation:** use `npx skills add yuhengqin/secure-coding-skill -g` to select the appropriate user-level paths.
- **Existing manual installation:** compare the complete package with the new version, preserve local changes, and update deliberately. Do not delete an existing directory merely to make the commands run.
- **Copy failure:** the temporary checkout is cleaned, but a partially copied destination is kept for inspection. Inspect the reported path before repairing or removing it; a retry will refuse to overwrite it.
- **Package contents:** keep `SKILL.md`, `LICENSE`, `NOTICE.md`, `references/`, `sources/`, `scripts/`, and `tests/` together.

其他客户端请按其文档选择技能目录，或交给 skills CLI；上述复制命令只面向共享项目级目录。全局安装使用 `-g`。已有手动安装先比较完整包并保留定制，不要为了重跑命令而直接删除旧目录。若复制失败，可能保留部分目标内容供检查，重试不会覆盖；修复或移除前先核对实际路径。始终保留完整包及许可证。
