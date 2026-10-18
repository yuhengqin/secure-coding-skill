# 客户端实际调用验证（2026-10-18）

本轮在 Windows 本机实际调用 Claude Code、Codex CLI 与 Cursor 桌面端；三个客户端均完成显式技能调用、订单案例审查和 6 项案例测试。

这是**指定技能名称后的本地调用验证**。三个客户端均使用本机的 DeepSeek 模型配置，不能据此推断 Anthropic Claude 或 OpenAI 模型的行为。Codex 使用单次命令覆盖参数，Cursor 使用临时代理与 HTTP/1.1 设置；通过范围以下面的实际配置为准。完整的脱敏工具回执节选、测试输出、源文件哈希和失败记录见 [JSON 证据](validation/2026-10-18-clients.json)。

## 环境与验收

- 日期：2026-10-18（Asia/Shanghai）；Windows、Python 3.14.2、Node.js v24.14.0。
- 被测源包：提交 `555ff68b8ad0f51d194054967cdd56cb564e214b` 中的 `skills/secure-coding/`。
- 三个客户端各有独立临时项目；复制完整技能包及 `examples/order-query/` 的两个 Python 文件，初始化本地 Git 仓库。
- 三份安装副本各 **25/25 文件 SHA-256 与源包一致**，均保留 LICENSE、NOTICE.md 和来源文件；各自的 `guide.py check` 退出 0。
- 技能均安装在临时项目；Cursor 的两项临时网络设置在复试后恢复，设置文件 SHA-256 与修改前一致。本轮未测试这三个客户端的 skills CLI 联网安装路径。

| 验收项 | Claude Code 2.1.233 | Codex CLI 0.162.1 | Cursor 3.24.18 |
|---|---|---|---|
| 项目级安装位置 | `.claude/skills/secure-coding/` | `.agents/skills/secure-coding/` | `.cursor/skills/secure-coding/` |
| 完整包与 `check` | 25/25 一致，退出 0 | 25/25 一致，退出 0 | 25/25 一致，退出 0 |
| 客户端实际加载/使用技能 | `Skill({"skill":"secure-coding"})` | 显式 `$secure-coding`，按发现路径读取索引和规则 | 原生 `read_file_v2` 读取项目技能的 `SKILL.md` |
| 规则正文与代码对应 | 四条核心规则及代码位置均出现在回执/报告中 | 四条核心规则及代码位置均出现在读取结果/报告中 | SQL、默认鉴权、对象归属三条规则及代码位置可定位 |
| 客户端内实际运行案例测试 | 6 项通过；CLI 退出 0 | 6 项通过；CLI 退出 0，使用已有 Node MCP 工具执行 | 6 项 `ok`、`OK`；原生工具回执为 `success` |
| 模型后端 | 会话报告 `deepseek-v4.1-flash[1M]` | 已配置的 DeepSeek Responses 提供方，`deepseek-flash` | 界面为 Auto，完成会话持久化模型名为 `deepseek-v4-pro` |

两个 CLI 的四条核心规则是 `PY-BACKEND-1.1.1`（输入校验）、`PY-BACKEND-1.2.1`（参数化查询）、`PY-BACKEND-1.8.1`（默认鉴权）、`PY-BACKEND-1.8.3`（避免越权）；Cursor 首轮选择了后三条，未另行提示它补读规则 ID。验收检查实际读取和调用行为，不将模型报告中的每一项静态判断都视为独立安全认证，也不将本案例当作规则覆盖率实验。

## 相同任务输入

三个客户端收到相同任务；Codex 的请求前额外带有字面量 `$secure-coding`。输入没有预先给出预期规则 ID：

```text
请使用 secure-coding 技能审查当前项目的 orders.py。业务约束：调用方传入服务端已经验证的登录身份，用户只能读取自己的订单。
这是一次真实客户端显式调用验证。请通过客户端的技能发现机制定位并加载该技能，实际读取适用规则全文，再把规则 ID 对应到 orders.py 的具体行号与防护行为。运行已有 test_orders.py 的 unittest（python -X utf8 -B -m unittest discover -s . -p test_orders.py -v）。
请用中文报告：实际加载的技能绝对路径、适用规则及代码位置、实际检查命令和结果、仍未验证的事项。找不到技能就如实报告，不要伪造加载或测试成功。仅做只读审查，不修改文件、不安装依赖、不运行 guide.py build、不执行指南中的示例、不调用子代理、不访问其他项目。输出控制在 700 字以内。
```

## Claude Code：原生 Skill 工具调用通过

在 Claude 的独立临时项目根运行，`$prompt` 为上面的完整任务文本：

```powershell
claude -p $prompt --output-format stream-json --verbose --no-session-persistence --permission-mode dontAsk --tools 'Read,Glob,Grep,Bash,Skill' --allowedTools 'Read,Glob,Grep,Skill,Bash(python *)' --strict-mcp-config --mcp-config '{"mcpServers":{}}' --settings '{"disableAllHooks":true,"autoMemoryEnabled":false}' --max-budget-usd 3
```

实际回执节选（临时目录前缀已替换）：

```text
tool_use: Skill, input: {"skill":"secure-coding"}
tool_result: Launching skill: secure-coding
Base directory: <FIXTURE_ROOT>/claude/.claude/skills/secure-coding

guide.py show PY-BACKEND-1.2.1 PY-BACKEND-1.8.1 PY-BACKEND-1.8.3
guide.py show PY-BACKEND-1.1.1 PY-BACKEND-1.2.2
Source: sources/Python安全指南.md:177-262 sha256=b1d1f0b7…

python -X utf8 -B -m unittest discover -s . -p test_orders.py -v
Ran 6 tests in 0.004s
OK
```

客户端读取了技能工作流、相关索引和规则正文，并在最终报告中对应 `orders.py:17–23` 的输入检查、`25–28` 的参数绑定及对象归属约束。进程退出 0；运行前后临时项目文件哈希一致。

限制：会话使用本机已有第三方模型配置。额外的一条 Bash 读取命令被权限白名单拒绝，拒绝记录保留在 JSON 中；技能调用、核心规则读取和测试各有实际工具回执，不以最终报告的自述代替这些证据。

## Codex CLI：显式调用通过，记录环境绕行

默认 OpenAI 后端出现 `tls handshake eof`，多次重连后由验证器在 300 秒结束进程。随后仅为本次命令选择本机已配置的 DeepSeek 提供方；该服务的 `/models` 实际返回包含 `deepseek-flash`。没有修改全局配置。

在 Codex 的独立临时项目根运行：

```powershell
codex -a never -c features.multi_agent=false -c model_provider=subagent -c model_reasoning_effort=low -c features.apps=false -c features.code_mode=false -m deepseek-flash exec --sandbox read-only --ephemeral --json -o '<输出文件>' ('$secure-coding' + [Environment]::NewLine + $prompt)
```

`subagent` 是本机现有提供方的配置名称；该命令没有启动子代理。保留以下实际观察，避免将环境绕行隐藏为默认配置通过：

1. 第一次切换后端时，服务拒绝 `code_mode` 的自定义 `exec` 工具：`Unsupported custom tool: 'exec'. Only 'apply_patch' is supported.`。本次命令关闭该特性后继续。
2. 客户端从技能发现清单确定 `.agents/skills/secure-coding/SKILL.md`，读取 `common.md`、`index.md`、`python.md`、`review.md`，并实际读取 Python 来源第 145–279、470–519 行，包含四条核心规则全文。
3. 内置 shell 工具返回 `helper_unknown_error`，因此改用会话中已有 `node_repl.js` 的 `child_process.spawnSync` 执行原测试 argv。工具回执明确包含 `status: 0`、6 项 `ok` 和 `OK`。

```text
python -X utf8 -B -m unittest discover -s . -p test_orders.py -v
status: 0
Ran 6 tests in 0.004s
OK
CLI process exit_code: 0
fixture_unchanged: true
```

最终报告把四条核心规则对应到输入检查、SQL 参数绑定、默认拒绝及订单归属条件，并明确上层会话认证和真实数据库集成未验证。本结果证明**上述配置与工具路径下的 Codex CLI 显式调用**；默认官方后端连接和内置 shell 路径仍未通过。

## Cursor：桌面端显式调用通过，临时网络设置已恢复

最初的 2.6.21 界面要求登录；用户完成安装和登录后，实际验证版本为 **3.24.18**，提交 `be4c9e5350d77747b42cd467cbd3370a753d4640`，安装位置变为 `C:\Program Files\cursor\`。本机的 `cursor` 启动器没有提供可用的独立 Agent CLI，因此本项直接在已安装桌面端执行。

通过编辑器启动器打开 Cursor 专属临时项目，再用 [官方 prompt deeplink](https://cursor.com/docs/reference/deeplinks) 预填上面的完整任务，核对确认框后提交。未将其他客户端或父进程执行的测试算作 Cursor 运行结果。

初次提交停在 `Reconnecting...`。该项目窗口日志记录 `ENOTFOUND agentn.global.api5.cursor.sh`；系统 DNS 无法解析 Cursor 域名，经现有本地代理可访问 `api2.cursor.sh`。参照 [Cursor 网络说明](https://cursor.com/docs/enterprise/network-configuration) 和 [HTTP/1.1 排障说明](https://cursor.com/help/troubleshooting/network)，临时加入：

```json
{
  "http.proxy": "http://127.0.0.1:7897",
  "cursor.general.disableHttp2": true
}
```

重载验证窗口后，同一会话继续执行并完成。实际客户端工具回执：

```text
read_file_v2: <FIXTURE_ROOT>/cursor/.cursor/skills/secure-coding/SKILL.md
status: completed; totalLinesInFile: 30

run_terminal_command_v2:
python "<FIXTURE_ROOT>/cursor/.cursor/skills/secure-coding/scripts/guide.py" show PY-BACKEND-1.2.1 PY-BACKEND-1.8.1 PY-BACKEND-1.8.3
status: completed; execution_status: success

run_terminal_command_v2:
python -X utf8 -B -m unittest discover -s . -p test_orders.py -v
status: completed; execution_status: success
Ran 6 tests in 0.004s
OK
```

从界面和该会话的本地持久化记录交叉核对：读取了 `SKILL.md`、`common.md`、`index.md`、`review.md` 和案例文件；规则检索返回原文位置与 SHA-256；最终报告将三条规则对应到参数绑定、非法身份拒绝和 `user_id` 归属条件，并列出上层认证、数据库权限及部署行为未验证。界面模型标签为 Auto，会话元数据的模型名为 `deepseek-v4-pro`，状态为 `completed`，未启动子代理。

两次 shell 检查采用单次 Run 批准，没有扩大命令白名单。单测的持久化工具回执保存六项 `ok`、`OK`、`rejected: false` 和 `notInterrupted: true`，但未单列数值退出码；JSON 中明确保留这一证据边界，不将模型报告里的 `exit 0` 作为独立退出码证明。

复试后移除本轮添加的两项网络设置，原设置文件逐字节恢复，前后 SHA-256 均为 `d9157f2ebade8557da0065d74315526a91ed017898c40151ef235a73c72d695a`。安装副本 25/25 文件仍与源包一致，两个案例文件与仓库哈希一致。本项验证的是**上述临时代理与 HTTP/1.1 条件下**的桌面端调用，默认网络配置的模型连接未通过。

## 验证边界与复跑

- 三个客户端验证的是显式指定名称后的技能发现、规则使用和实际测试；没有测试不提技能名称时的自动选择/触发。
- 本轮使用手动完整复制的项目级副本；不扩展为这三个客户端的 skills CLI、插件或全局安装验证。
- 原有 7 项工具测试及 6 项订单案例测试在仓库中重新通过，`guide.py check` 仍为 225 条规则、6 份来源、10 项解释。
- 三个客户端均未修改案例和安装副本；测试仅覆盖 SQLite 内存数据库的已有断言，未验证 HTTP 认证、操作级授权、生产数据库及部署行为。
- CLI 原始 JSONL、Cursor 界面文字快照及本次会话的精选持久化工具记录保留在本机临时目录；仓库 JSON 为脱敏节选并记录对应 SHA-256。未分发凭据、会话加密字段或完整用户配置。

调用入口与技能目录另核对了 [Claude Code 官方文档](https://code.claude.com/docs/en/headless)、[Claude 技能文档](https://code.claude.com/docs/en/skills)、[OpenAI 非交互模式](https://developers.openai.com/codex/noninteractive)、[Codex 技能目录](https://developers.openai.com/codex/skills)及 [Cursor 技能文档](https://cursor.com/docs/skills)。客户端行为和通过状态以上述本机运行记录为准。
