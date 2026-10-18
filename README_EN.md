<p align="center">
  <img src="./assets/banner.png" alt="Secure Coding Skill — Rules → Code → Evidence; 225 rules, 5 languages" width="100%">
</p>

<h1 align="center">🛡️ Secure Coding Skill</h1>

<p align="center">
  <b>Give your AI coding assistant rules to check and evidence to show.<br>225 rules · 5 programming languages · From request to evidence</b>
</p>

<p align="center">
  <a href="./README.md">简体中文</a> · <b>English</b>
</p>

<p align="center">
  <a href="#quickstart">Quickstart</a> · <a href="#case">See It in Action</a> · <a href="#evidence">Evidence</a> · <a href="#use-cases">Use Cases</a> · <a href="#features">Features</a> · <a href="#compatibility">Compatibility</a> · <a href="#repo">Layout</a> · <a href="#faq">FAQ</a> · <a href="#roadmap">Roadmap</a>
</p>

<p align="center">
  <a href="https://github.com/yuhengqin/secure-coding-skill/stargazers"><img src="https://img.shields.io/github/stars/yuhengqin/secure-coding-skill.svg?label=%E2%AD%90%20Stars" alt="GitHub Stars"></a>
  <a href="#languages"><img src="https://img.shields.io/badge/rules-225-blue.svg" alt="225 Rules"></a>
  <a href="#languages"><img src="https://img.shields.io/badge/languages-5-brightgreen.svg" alt="5 Languages"></a>
  <img src="https://img.shields.io/badge/CLI-Python_3.10%2B_stdlib_only-orange.svg" alt="Python Standard Library Only">
  <a href="./docs/VALIDATION.md"><img src="https://img.shields.io/badge/rule_package%20check-ok-green.svg" alt="Rule package check: ok"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent_Skills-format-6366f1.svg" alt="Agent Skills format specification"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/yuhengqin/secure-coding-skill.svg" alt="License: CC BY-SA 4.0"></a>
</p>

**Put 225 security rules from Tencent/secguide into your AI coding assistant.** Retrieve relevant rules by language and task, then tie implementation and review to **rule IDs, code locations, and checks actually performed**.

Run in your **target project's root** and select your coding agent:

```bash
npx skills add yuhengqin/secure-coding-skill
```

Requires Node.js with `npx`. You can also [ask an assistant to install it](./README_AI.md) or [copy the complete package manually](./docs/INSTALLATION.md). Explicit invocation is verified in OpenCode; see [compatibility](#compatibility) for other clients.

**① Install → ② Ask for a task using `secure-coding` → ③ Check the rules, code, and evidence in the result.** [Try your first task →](#quickstart)

| Security rules | programming Languages | Applicability notes | Regression tests | CLI third-party deps |
| :---: | :---: | :---: | :---: | :---: |
| **225** | **5** | **10** | **13 (7 + 6)** | **0** |

Covers **Python · JavaScript/TypeScript · Java · Go · C/C++**, preserving the original MUST / SHOULD / RECOMMENDED levels. See [validation records](./docs/VALIDATION.md) for the counts and local checks; the `check ok` badge refers to a recorded local package check.

**Working code can still miss an authorization boundary.** An order lookup can pass a functional test while missing parameter binding or an ownership condition. This skill brings the relevant rules into implementation and asks the assistant to state what it checked and what remains unverified.

<span id="case"></span>

## 🧪 See It in Action: Only Read Your Own Orders

The [runnable order-query example](./examples/order-query/README.md) follows **request → rules → implementation → tests**. This is a **staged dialogue based on the example, not a verbatim transcript or model A/B test**. Actual install and invocation records are in [evidence](#evidence).

```text
You  ❯ Use secure-coding to implement a Python order lookup. Reuse the existing
       authenticated identity; users may only read their own orders.

AI   ❯ Reads 4 applicable rules:
       PY-BACKEND-1.1.1 input validation · PY-BACKEND-1.2.1 parameterized query
       PY-BACKEND-1.8.1 default authorization · PY-BACKEND-1.8.3 object ownership
       The caller must authenticate, check operation-level permissions,
       and supply a server-verified identity.

You  ❯ Where did the code change, and what did you check?

AI   ❯ orders.py:17–23 validates input; 25–28 binds values and checks ownership.
       6 tests pass: own orders are readable; other and missing orders return
       None; injection-shaped input cannot widen the query; invalid identity
       values and order IDs are rejected.
       Unverified: HTTP auth, operation-level permissions, real DB integration.
```

[Implementation: `orders.py`](./examples/order-query/orders.py#L17-L28) · [The 6 tests](./examples/order-query/test_orders.py) · [Rule-to-code mapping](./examples/order-query/README.md#从规则到实现)

<details>
<summary><b>Expand: query comparison and rule mapping</b></summary>

```diff
# Illustrative query comparison; full input checks are in orders.py.

- # Unsafe pattern: SQL string interpolation, no ownership constraint
- return connection.execute(f"SELECT * FROM orders WHERE id = '{order_id}'").fetchone()

+ # PY-BACKEND-1.2.1 + PY-BACKEND-1.8.3: bind values and constrain ownership
+ return connection.execute(
+     "SELECT id, note FROM orders WHERE id = ? AND user_id = ?",
+     (order_id, authenticated_user_id),
+ ).fetchone()
```

| What you get | In this example |
| :--- | :--- |
| **Rules with a reason** | `PY-BACKEND-1.1.1` input validation; `PY-BACKEND-1.2.1` parameter binding; `PY-BACKEND-1.8.1` default authorization; `PY-BACKEND-1.8.3` object ownership |
| **Concrete defenses** | Input checks + SQL parameters + an ownership condition using a server-verified identity |
| **Executable evidence** | 6 tests covering own/other/missing orders, injection-shaped input and literal quotes, invalid identity values, and invalid order IDs |

</details>

**Try the evidence yourself** — from this repository root, with Python 3.10+ and standard-library `sqlite3`:

```bash
python -B -m unittest discover -s examples/order-query -p test_orders.py -v
```

The example uses an in-memory SQLite database and passes all 6 tests locally. Validating an identity's numeric value is not authentication. [Full implementation and boundaries →](./examples/order-query/README.md)

<span id="evidence"></span>

## 📡 Evidence: What Has Actually Run

These are **2026-10-16 Windows** validation records and output excerpts. OpenCode invocation and fresh installation refer to the [existing end-to-end record](./docs/VALIDATION.md#2026-10-16-端到端调用补记opencodeasiashanghai); the package check and all 13 tests passed again during this README update.

| Check | Result | What it establishes |
| :--- | :--- | :--- |
| `guide.py check` | **ok**: 225 rules, 6 sources, 10 interpretations | Package integrity |
| Tool and example tests | **7 + 6 pass** | CLI regressions and order-query behavior |
| Fresh skills CLI installation | **25/25 SHA-256 hashes match** | The recorded installation matches its source package |
| Explicit OpenCode invocation | **Skill loaded; example reviewed against its rules** | That client's explicitly requested invocation path |

<details>
<summary><b>Expand: installation, integrity, rule lookup, and test evidence</b></summary>

**① Explicit skill invocation in OpenCode, loaded successfully:**

```
⏺ skill({"id":"secure-coding"})
  ⏺ Skill "secure-coding" loaded successfully
    Base directory: D:\chat\.agents\skills\secure-coding
```

**② Fresh install via skills CLI — 25/25 files match the repository:**

```bash
npx -y skills add yuhengqin/secure-coding-skill -a opencode --copy -y
```

The recorded installed copy matched the repository at the time, file by file by SHA-256, and passed the integrity check.

**③ Integrity check (`guide.py check`):**

```console
$ python skills/secure-coding/scripts/guide.py check
{
  "status": "ok",
  "rules": 225,
  "by_language": {
    "python": 45,
    "javascript": 45,
    "java": 49,
    "go": 37,
    "cpp": 49
  },
  "sources": 6,
  "interpretations": 10,
  "scope": "package integrity only; not a target-code security scan"
}
```

**④ Rule lookup (`guide.py show`) with source line numbers and hash (excerpt; hash abbreviated):**

```console
$ python skills/secure-coding/scripts/guide.py show PY-BACKEND-1.2.1
# PY-BACKEND-1.2.1 [必须] 使用参数化查询
Context: 后台类 / I. 代码实现 / 1.2 SQL操作
Source: sources/Python安全指南.md:177-262 sha256=b1d1f0b7…

Original excerpt (historical examples; apply interpretations and verify applicability):
177  #### 1.2.1 【必须】使用参数化查询
179  - 使用参数化SQL语句，强制区分数据和命令，避免产生SQL注入漏洞。
…
```

**⑤ Test evidence (result summary; individual cases and timings omitted):**

```console
$ python -B -m unittest discover -s skills/secure-coding/tests -v
Ran 7 tests
OK

$ python -B -m unittest discover -s examples/order-query -p test_orders.py -v
Ran 6 tests
OK
```

</details>

**Boundaries:** a package check does not establish business-code security; successful explicit invocation does not establish automatic triggering. No controlled experiment has measured an improvement in model security. See [validation scope](#validation) for remote CI status.

<span id="quickstart"></span>

## 🚀 Installed? Try a Task

After installing with the command above, ask your assistant to apply the skill to a real task. For a project with order queries, try:

```text
Use the secure-coding skill to implement or review the order lookup in this project.
Users must only read their own orders. Retrieve the relevant input validation,
SQL, and authorization rules first. Then report rule IDs, code locations,
defenses, checks actually run, and anything still unverified.
```

**What to look for:** the assistant reads applicable rules and ties its result to code and checks. To confirm discovery separately, ask it to locate `secure-coding` and read `PY-BACKEND-1.2.1`. If it cannot find the skill, check the installation directory and reopen the project. Explicit invocation is recommended.

<details>
<summary><b>Optional: verify the installed rule package</b></summary>

With Python 3.10+, run this from your project root. Replace the path with the actual installed location if your agent uses another directory.

```bash
python .agents/skills/secure-coding/scripts/guide.py check
```

Expected: `"status": "ok"`, **225 rules, 6 sources, 10 interpretations**. This checks package integrity; client invocation is a separate check (see the end-to-end evidence above).

</details>

<details>
<summary><b>More install options, updates, and removal</b></summary>

| Need | Command or guide |
| :--- | :--- |
| Preview available skills | `npx skills add yuhengqin/secure-coding-skill --list` |
| Choose agents explicitly | `npx skills add yuhengqin/secure-coding-skill --agent codex --agent claude-code` |
| Install for all your projects | `npx skills add yuhengqin/secure-coding-skill -g` |
| Update / remove a project install | `npx skills update secure-coding` / `npx skills remove secure-coding` |
| Update / remove a global install | Add `-g` to the update or remove command |
| Install without Node.js | [Manual installation: Linux, macOS, and PowerShell](./docs/INSTALLATION.md) |
| Let an assistant install it | [AI installation handoff guide](./README_AI.md) (Chinese) |

The [skills CLI](https://github.com/vercel-labs/skills) handles agent-specific destinations. Manual installs must keep the entire `skills/secure-coding/` package, including its license and sources. Before replacing a manual installation, compare and preserve local changes; run `guide.py check` after updating.

</details>

<span id="routing"></span>

<details>
<summary><b>🧭 Find the right entry point for your role</b></summary>

| You are… | You want to… | Go here |
| :--- | :--- | :--- |
| 🤖 AI agent | Install, verify, first call | [`README_AI.md`](./README_AI.md) |
| 🤖 AI agent | Understand repo layout & guardrails | [`AGENTS.md`](./AGENTS.md) / [`CLAUDE.md`](./CLAUDE.md) |
| 👤 Human (first visit) | Try a first task | [Quickstart](#quickstart) |
| 👤 Human (on OpenCode) | End-to-end workflow | [`docs/USAGE.md`](./docs/USAGE.md) |
| 🔧 Manual install | Pick agent & platform | [`docs/INSTALLATION.md`](./docs/INSTALLATION.md) |
| 📖 Looking up a rule | Exact rule lookup | `guide.py show <rule-id>` |
| 🔍 Verifying rule sources | Check hashes & provenance | [`docs/PROVENANCE.md`](./docs/PROVENANCE.md) · [`docs/VALIDATION.md`](./docs/VALIDATION.md) |
| 🧩 Maintaining or releasing | Build & release process | [`docs/MAINTENANCE.md`](./docs/MAINTENANCE.md) · [`docs/RELEASING.md`](./docs/RELEASING.md) |
| 🤝 Contributing | Open an issue / PR | [`CONTRIBUTING.md`](./CONTRIBUTING.md) · [Issue templates](./.github/ISSUE_TEMPLATE) |

</details>

<span id="use-cases"></span>

## 🎯 When to Reach for It

| Your task | Rules and checks to bring into the change |
| :--- | :--- |
| Build an API or database query | Input validation, parameter binding, authentication and object ownership |
| Handle uploads, downloads, or user-provided URLs | Path boundaries, file constraints, SSRF and redirect handling |
| Render HTML or change browser behavior | XSS, output context, DOM operations and browser security boundaries |
| Start processes or deserialize data | Command arguments, execution boundaries and untrusted input |
| Refactor or review existing code | Relevant rule IDs, code evidence, targeted checks and remaining gaps |

<span id="features"></span>

## 🔍 Why Package the Rules as a Skill?

- 🎯 **225 rules, one skill.** Python, JavaScript/TypeScript, Java, Go, and C/C++ in a single installable package.
- 🪶 **Read on demand.** Language and task indexes lead to relevant rules without loading five full guides up front. Token savings have not been measured.
- 🔍 **Every rule has a trail.** Original text, line numbers, and source SHA-256 hashes, plus 10 sourced applicability notes for selected historical guidance.
- 🔌 **Zero third-party CLI dependencies.** Python 3.10+ standard library handles local lookup and integrity checks — no network requests, no code collection.
- 🧪 **Show the checks.** 7 tool regression tests and 6 runnable example tests, with commands you can repeat yourself.

<details>
<summary><b>Expand: the retrieval workflow from task to evidence</b></summary>

```mermaid
flowchart LR
    A["Your coding task"] --> B["Language + scenario indexes"]
    B --> C["Relevant rules + applicability notes"]
    C --> D["Implementation or review"]
    D --> E["Rule IDs + code locations + checks"]
```

The model selects applicable rules; `guide.py` retrieves their text and provenance locally. The skill also asks the assistant to check current APIs and project constraints when applying historical examples. [Explore the workflow →](./skills/secure-coding/SKILL.md)

</details>

<span id="languages"></span>

## 📊 Languages & Coverage

| Language | Rules | Environments and focus |
| :--- | :---: | :--- |
| **Python** | 45 | Scripts and backend services: SQLi, SSRF, deserialization, access control |
| **JavaScript / TypeScript** | 45 | Browsers and Node.js: XSS, DOM security, prototype pollution, CORS |
| **Java** | 49 | Backend services and Android: expression injection, XXE, cryptography |
| **Go** | 37 | Backend and systems code: paths, commands, concurrency, resource limits |
| **C / C++** | 49 | Native code: buffer and integer overflows, format strings, memory lifetime |

TypeScript uses the JavaScript runtime rules. The total includes **188 MUST, 27 SHOULD, and 10 RECOMMENDED rules**, not 225 vulnerability classes. The 10 applicability notes address specific historical recommendations; the full rule set has not undergone a complete modernization audit. Source: [Tencent/secguide](https://github.com/Tencent/secguide).

<span id="compatibility"></span>

## 🔌 Client Compatibility

| Client / installation route | Package installation | Discovery and actual invocation |
| :--- | :--- | :--- |
| **OpenCode via skills CLI** | Windows, 2026-10-16: `-a opencode --copy -y`; 25/25 files match; installed package passes `check` | ✅ End-to-end verified (2026-10-16, explicit invocation loaded successfully — see [evidence](#evidence)) |
| **Codex, Claude Code, Cursor, GitHub Copilot, other skills CLI agents** | Installation routes provided by the upstream CLI; not individually tested here | Not yet verified end-to-end; verification records welcome |
| **Manual copy** | Complete-package copying and installed CLI use verified; use your client's documented directory | Depends on the client's loading mechanism |

Use the installer's reported location. The shared project path is commonly `.agents/skills/secure-coding/`; agent-specific paths can differ. [Installation details →](./docs/INSTALLATION.md) · [Validation records →](./docs/VALIDATION.md)

<span id="validation"></span>

## ✅ Validation You Can Inspect

| Check | Recorded result |
| :--- | :--- |
| Rule package integrity | **Pass locally:** 225 rules, 6 sources, 10 interpretations (hashes, coverage, generated files all consistent) |
| Tool and example tests | **7 + 6 passed** on Windows / Python 3.14.2 |
| OpenCode end-to-end invocation | **Verified:** explicit `secure-coding` invocation loaded successfully (2026-10-16) |
| Fresh install via skills CLI | **Verified:** 25/25 file hashes match; installed package passes `check` (2026-10-16) |
| Remote CI | Windows / Ubuntu × Python 3.10 / 3.14 configured; the [recorded first run](https://github.com/yuhengqin/secure-coding-skill/actions/runs/38339001315) could not start jobs due to account billing; no passing run recorded |
| Model security improvement | No controlled comparison against an unassisted baseline yet |

Package integrity and example tests cover their stated scope. Project security still needs project tests, scanners, and review. [Commands and full evidence →](./docs/VALIDATION.md)

<span id="repo"></span>

## 🗂️ Repository Layout

<details>
<summary><b>Expand: skill package, example, and maintenance docs</b></summary>

```
secure-coding-skill/
├── README.md                  ← Chinese README (default homepage)
├── README_EN.md               ← this file (English)
├── README_AI.md               ← AI-agent installation handoff (Chinese)
├── AGENTS.md / CLAUDE.md      ← agent navigation (Claude / Codex / OpenCode / Cursor)
├── assets/banner.png          ← visual anchor
├── skills/secure-coding/      ← the installable skill package
│   ├── SKILL.md               ← skill entry (agents read this first)
│   ├── scripts/guide.py       ← zero-dep CLI: check / show / list / build
│   ├── references/            ← language indexes, scenario routing, rule metadata
│   ├── sources/               ← vendored source snapshots + provenance manifests
│   └── tests/                 ← 7 tool regression tests
├── examples/order-query/      ← runnable case: order lookup (6 tests)
├── docs/                      ← installation / usage / provenance / validation / maintenance / releasing
├── .github/workflows/         ← remote validation workflow
└── THIRD_PARTY_NOTICES.md     ← third-party notices
```

</details>

<span id="faq"></span>

## ❓ FAQ

<details>
<summary><b>Why not just paste the secguide originals into the AI?</b></summary>

You can. This package adds reusable retrieval and reporting instructions: find rules by language and scenario, trace each to source lines and a SHA-256 hash, and consult 10 applicability notes for selected historical guidance. It asks assistants to map rules to code and distinguish checked items from unverified ones. You do not need all five guides in context at once, but actual token savings have not been measured. You still need to check that the assistant follows these instructions.

</details>

<details>
<summary><b>Does my project need Python?</b></summary>

No. An assistant can read the Markdown rules directly. Python 3.10+ is needed only to run the local lookup, package checks, and tests.

</details>

<details>
<summary><b>How much context does it use?</b></summary>

The skill is organized for progressive disclosure: metadata for discovery, then instructions, indexes, and relevant rules when invoked. Actual token use depends on the client and task; this repository does not publish a measured token budget.

</details>

<details>
<summary><b>Does it replace security scanners or keep my AI client offline?</b></summary>

It guides generation and review; keep your project's static analysis, dynamic tests, and human review. The local CLI makes no network requests. Your coding assistant's model calls and data handling still follow that client's settings and provider terms.

</details>

<details>
<summary><b>Can I install only one language?</b></summary>

Keep the complete package today: integrity checks cover the full rule set. The assistant can still read rules selectively. Single-language export is on the roadmap.

</details>

<details>
<summary><b>Are the rules AI-hallucinated?</b></summary>

No. Rules come from the secguide originals; the repository vendors the source snapshots with SHA-256 hashes, and `guide.py check` verifies every one. Every rule maps back to exact source line numbers. The skill also instructs assistants to report checks and unverified items honestly, never presenting guesses as passes.

</details>

<span id="roadmap"></span>

## 🤝 Contribute & What's Next

Useful contributions include **client verification records**, **rule corrections with current sources**, and **runnable examples with meaningful tests**. Start with [CONTRIBUTING.md](./CONTRIBUTING.md); report exploitable tool defects through [SECURITY.md](./SECURITY.md).

- ✅ OpenCode end-to-end invocation verified (2026-10-16)
- ⬜ End-to-end verification for the remaining clients (Claude Code / Codex / Cursor)
- ⬜ First green remote CI run and a versioned release
- ⬜ More sourced applicability notes and runnable cases
- ⬜ Single-language exports and additional client adapters

## 📚 Go Deeper

| Want to know | Start here |
| :--- | :--- |
| Let an AI assistant install it | [AI handoff guide](./README_AI.md) · [Agent navigation](./AGENTS.md) |
| Install manually | [Installation guide](./docs/INSTALLATION.md) |
| Query rules and run checks | [Command reference](./docs/USAGE.md) |
| More development and review prompts | [Usage examples](./examples/USAGE.md) |
| Inspect original sources and modifications | [Provenance](./docs/PROVENANCE.md) · [Third-party notices](./THIRD_PARTY_NOTICES.md) |
| Maintain or release the package | [Maintenance](./docs/MAINTENANCE.md) · [Releasing](./docs/RELEASING.md) · [Changelog](./CHANGELOG.md) |

The installable package lives in `skills/secure-coding/`; the runnable demo lives in `examples/order-query/`. Most supporting documents are in Chinese.

## 📜 Attribution & License

Based on **Secure Coding Guide** by **THL A29 Limited, a Tencent company**, Copyright (C) 2021. Distributed under **[CC BY-SA 4.0](./LICENSE)** with upstream attribution and modification notices preserved (see [NOTICE](./skills/secure-coding/NOTICE.md)). This is an independent community project, not officially endorsed by Tencent. Keep `LICENSE`, `NOTICE.md`, and source files with the installed package.

<p align="center">
  Bring security into your next AI coding session.<br>
  If it helps, give the project a ⭐️ <b>Star</b>, share a real use case, or <a href="https://github.com/yuhengqin/secure-coding-skill/issues/new/choose">open an issue</a>.
</p>
