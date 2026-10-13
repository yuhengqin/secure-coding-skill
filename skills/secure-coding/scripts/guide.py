"""Build, validate and query a pinned, portable secguide reference package.

No network calls, external dependencies, or execution of guide examples.
Only `build` writes files; all other commands are read-only.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, quote


ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {
    "python": ("PY", "Python安全指南.md"),
    "javascript": ("JS", "JavaScript安全指南.md"),
    "java": ("JAVA", "Java安全指南.md"),
    "go": ("GO", "Go安全指南.md"),
    "cpp": ("CPP", "C,C++安全指南.md"),
}
SCENARIOS = {
    "通用类": "COMMON", "通用安全指南": "COMMON", "后台类": "BACKEND",
    "JavaScript页面类": "BROWSER", "Node.js后台类": "NODE", "安卓类": "ANDROID",
}
RULE = re.compile(r"^(\d+(?:\.\d+)+)\s*【(必须|建议|推荐)】\s*(.+?)\s*$")
HEADING = re.compile(r"^\s*(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
ANCHOR = re.compile(r'^\s*<a\s+id=[^>]+></a>\s*$')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def parse_source(text, language, source_path):
    """Extract numbered policy headings, excluding TOCs and fenced examples."""
    prefix = LANGUAGES[language][0]
    lines = text.splitlines()
    stack, rules = [], []
    fence = None
    current = None
    seen = set()

    def finish(stop):
        nonlocal current
        if current is None:
            return
        # Remove spacing and a following section's HTML anchor from the excerpt.
        while stop >= current["source"]["start_line"]:
            if lines[stop - 1].strip() and not ANCHOR.match(lines[stop - 1]):
                break
            stop -= 1
        current["source"]["end_line"] = stop
        current.pop("_depth")
        rules.append(current)
        current = None

    for number, line in enumerate(lines, 1):
        match_fence = FENCE.match(line)
        if fence:
            if (match_fence and not match_fence[2].strip()
                    and match_fence[1][0] == fence[0]
                    and len(match_fence[1]) >= fence[1]):
                fence = None
            continue
        if match_fence:
            fence = (match_fence[1][0], len(match_fence[1]))
            continue
        heading = HEADING.match(line)
        bold = re.match(r"^\s*\*\*(.+?)\*\*\s*$", line)
        title = heading[2] if heading else bold[1] if bold else ""
        rule = RULE.match(title)
        depth = len(heading[1]) if heading else (stack[-1][0] + 1 if stack else 1)
        if rule:
            finish(number - 1)
            parents = [name for level, name in stack if level < depth]
            scenario = next((SCENARIOS[name] for name in parents if name in SCENARIOS), None)
            if not scenario:
                raise ValueError(f"Unknown scenario: {source_path}:{number}")
            rule_id = f"{prefix}-{scenario}-{rule[1]}"
            if rule_id in seen:
                raise ValueError(f"Duplicate rule id: {rule_id}")
            seen.add(rule_id)
            current = {
                "id": rule_id, "language": language, "scenario": scenario.lower(),
                "original_number": rule[1], "requirement": rule[2],
                "title": rule[3], "section": parents,
                "source": {"path": source_path, "start_line": number}, "_depth": depth,
            }
        elif heading:
            if current and depth <= current["_depth"]:
                finish(number - 1)
            stack = [(level, name) for level, name in stack if level < depth]
            stack.append((depth, title))
    if fence:
        raise ValueError(f"Unclosed code fence: {source_path}")
    finish(len(lines))
    if not rules:
        raise ValueError(f"No rules found: {source_path}")
    return rules


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def snapshot(root, source_dir):
    # Read and parse every input before modifying the package.
    names = [name for _, name in LANGUAGES.values()] + ["README.md"]
    payloads = {name: (source_dir / name).read_bytes() for name in names}
    for language, (_, name) in LANGUAGES.items():
        parse_source(payloads[name].decode("utf-8-sig"), language, "sources/" + name)
    destination = root / "sources"
    destination.mkdir(parents=True, exist_ok=True)
    manifest = {"schema_version": 1, "origin": "user-provided secguide-main local snapshot",
                "upstream_revision": None, "files": []}
    for name, data in payloads.items():
        (destination / name).write_bytes(data)
        manifest["files"].append({"path": "sources/" + name, "sha256": digest(data),
                                  "bytes": len(data)})
    (destination / "manifest.json").write_text(json_text(manifest), encoding="utf-8")


def verified_sources(root, upstream=None):
    manifest = load_json(root / "sources" / "manifest.json")
    expected = {"sources/" + name for _, name in LANGUAGES.values()} | {"sources/README.md"}
    records = manifest["files"]
    if len(records) != len(expected) or {item["path"] for item in records} != expected:
        raise ValueError("Source manifest file inventory mismatch")
    result = {}
    for item in records:
        data = (root / item["path"]).read_bytes()
        if digest(data) != item["sha256"] or len(data) != item["bytes"]:
            raise ValueError(f"Source hash mismatch: {item['path']}; review the source update first")
        if upstream is not None:
            original = (upstream / Path(item["path"]).name).read_bytes()
            if original != data:
                raise ValueError(f"Upstream hash mismatch: {item['path']}")
        result[item["path"]] = (data, item["sha256"])
    return result


def interpretations(root):
    return load_json(root / "references" / "overrides.json")["interpretations"]


def compile_catalog(root):
    sources = verified_sources(root)
    rules = []
    for language, (_, name) in LANGUAGES.items():
        path = "sources/" + name
        data, sha = sources[path]
        batch = parse_source(data.decode("utf-8-sig"), language, path)
        for rule in batch:
            rule["source"]["sha256"] = sha
            rule["interpretations"] = []
        rules.extend(batch)
    by_id = {rule["id"]: rule for rule in rules}
    seen = set()
    for item in interpretations(root):
        if item["id"] in seen:
            raise ValueError(f"Duplicate interpretation: {item['id']}")
        seen.add(item["id"])
        if not item["guidance"] or not item["evidence"] or not item["rules"]:
            raise ValueError(f"Incomplete interpretation: {item['id']}")
        for rule_id in item["rules"]:
            if rule_id not in by_id:
                raise ValueError(f"Unknown interpretation rule: {rule_id}")
            rule = by_id[rule_id]
            # A source revision invalidates the interpretation until its citations are rechecked.
            pinned = item["source_hashes"].get(rule["source"]["path"])
            if pinned != rule["source"]["sha256"]:
                raise ValueError(f"Interpretation source hash needs review: {item['id']} / {rule_id}")
            rule["interpretations"].append(item["id"])
    return {"schema_version": 1, "rules": rules}


def generated_pages(root, catalog):
    pages = {"references/rules.json": json_text(catalog)}
    for language in LANGUAGES:
        rows = [r for r in catalog["rules"] if r["language"] == language]
        chunks = [f"# {language} 规则索引", "", f"共 {len(rows)} 条。由 scripts/guide.py 生成。",
                  "", "先读适用的完整规则正文和解释；标题及原文级别不等于已验证的当前实现。",
                  "使用 `python scripts/guide.py show <ID>` 取得带行号正文及本技能解释。",
                  "脚本路径以技能目录为基准；没有 Python 时，按下表行号直接读取 sources 文件。", ""]
        previous = None
        for rule in rows:
            section = " / ".join(rule["section"])
            if section != previous:
                chunks.extend(["", f"## {section}", "", "| ID | 原文级别 | 规则 | 原文行号 | 解释 |",
                               "|---|---|---|---|---|"])
                previous = section
            src = rule["source"]
            link = "../" + quote(src["path"], safe="/,+")
            notes = ", ".join(f"[{i}](interpretations.md#{i.lower()})" for i in rule["interpretations"]) or "—"
            title = rule["title"].replace("|", "\\|")
            chunks.append(f"| {rule['id']} | {rule['requirement']} | {title} | "
                          f"[{src['start_line']}–{src['end_line']}]({link}) | {notes} |")
        pages[f"references/{language}.md"] = "\n".join(chunks) + "\n"
    chunks = ["# 本技能的适用性解释", "", "由 overrides.json 生成；原文快照保持不变。",
              "这些解释是有出处的补充或纠偏，不代表全部历史指南已完成现代化审计。",
              "解释适用于列出的规则；用户明确要求和项目已批准的安全政策仍需遵循，冲突要说明。", ""]
    for item in interpretations(root):
        chunks.extend([f"<a id=\"{item['id'].lower()}\"></a>",
                       f"## {item['id']} · {item['title']}", "",
                       "适用规则：" + ", ".join(item["rules"]), "",
                       f"核实日期：{item['verified_on']}。范围：{item['review_scope']}。", "",
                       "原文情况：" + item["original_observation"], "",
                       "本技能采用：" + item["guidance"], "", "依据："])
        for evidence in item["evidence"]:
            chunks.append(f"- [{evidence['title']}]({evidence['url']})")
        chunks.append("")
    pages["references/interpretations.md"] = "\n".join(chunks) + "\n"
    return pages


def check_links(root):
    # Only local file targets; original articles contain upstream URLs/anchors outside our control.
    files = [root / "SKILL.md"] + list((root / "references").glob("*.md"))
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)\)", text):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            raw, _, anchor = unquote(target).partition("#")
            resolved = (path.parent / raw).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                raise ValueError(f"Broken local reference: {path.name}: {target}")
            if anchor and resolved.name == "interpretations.md":
                if f'id="{anchor}"' not in resolved.read_text(encoding="utf-8"):
                    raise ValueError(f"Broken interpretation anchor: {target}")


def checked_catalog(root):
    expected = compile_catalog(root)
    actual = load_json(root / "references" / "rules.json")
    if actual != expected:
        raise ValueError("Rule catalog mismatch: rebuild and validate the package")
    return actual


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build", help="Regenerate indexes; optionally import an explicitly reviewed snapshot")
    build.add_argument("--source-dir", type=Path, help="Copy the six original Markdown files byte-for-byte")
    check = sub.add_parser("check", help="Validate source hashes, rule coverage, generated pages and local links")
    check.add_argument("--upstream", type=Path, help="Also compare sources with the original secguide-main folder")
    listing = sub.add_parser("list", help="Filter rule metadata; query matches title, section and original body")
    listing.add_argument("--language", choices=list(LANGUAGES))
    listing.add_argument("--scenario", choices=sorted({s.lower() for s in SCENARIOS.values()}))
    listing.add_argument("--query", default="")
    listing.add_argument("--json", action="store_true")
    show = sub.add_parser("show", help="Print effective interpretations and complete original rule excerpts")
    show.add_argument("ids", nargs="+")
    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            if args.source_dir:
                snapshot(ROOT, args.source_dir)
            catalog = compile_catalog(ROOT)
            for name, text in generated_pages(ROOT, catalog).items():
                destination = ROOT / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(text, encoding="utf-8", newline="\n")
            print(f"Built {len(catalog['rules'])} rules from {len(LANGUAGES)} guides.")
            return 0
        catalog = checked_catalog(ROOT)
        if args.command == "check":
            verified_sources(ROOT, args.upstream)
            for name, text in generated_pages(ROOT, catalog).items():
                if (ROOT / name).read_text(encoding="utf-8") != text:
                    raise ValueError(f"Generated catalog/page mismatch: {name}")
            check_links(ROOT)
            counts = dict(Counter(r["language"] for r in catalog["rules"]))
            print(json_text({"status": "ok", "rules": len(catalog["rules"]), "by_language": counts,
                             "sources": 6, "interpretations": len(interpretations(ROOT)),
                             "scope": "package integrity only; not a target-code security scan"}), end="")
            return 0
        rules = catalog["rules"]
        if args.command == "list":
            filtered = []
            for rule in rules:
                if args.language and rule["language"] != args.language:
                    continue
                if args.scenario and rule["scenario"] != args.scenario:
                    continue
                src = rule["source"]
                body = (ROOT / src["path"]).read_text(encoding="utf-8-sig").splitlines()
                haystack = " ".join([rule["id"], rule["title"], *rule["section"],
                                      *body[src["start_line"] - 1:src["end_line"]]])
                if args.query.casefold() not in haystack.casefold():
                    continue
                filtered.append(rule)
            if args.json:
                print(json_text(filtered), end="")
            else:
                for rule in filtered:
                    flags = ",".join(rule["interpretations"]) or "-"
                    print(f"{rule['id']} [{rule['requirement']}] {rule['title']} | explanations={flags}")
                print(f"Matched {len(filtered)} rules. Zero matches do not prove no applicable rule exists.")
        elif args.command == "show":
            by_id = {r["id"]: r for r in rules}
            missing = [rule_id for rule_id in args.ids if rule_id not in by_id]
            if missing:
                raise ValueError("Unknown rule: " + ", ".join(missing))
            overrides = {i["id"]: i for i in interpretations(ROOT)}
            for rule_id in args.ids:
                rule = by_id[rule_id]
                src = rule["source"]
                print(f"\n# {rule_id} [{rule['requirement']}] {rule['title']}")
                print("Context: " + " / ".join(rule["section"]))
                print(f"Source: {src['path']}:{src['start_line']}-{src['end_line']} sha256={src['sha256']}")
                for override_id in rule["interpretations"]:
                    item = overrides[override_id]
                    print(f"\nInterpretation {override_id} ({item['verified_on']}): {item['guidance']}")
                    for evidence in item["evidence"]:
                        print(f"  {evidence['title']}: {evidence['url']}")
                print("\nOriginal excerpt (historical examples; apply interpretations and verify applicability):")
                lines = (ROOT / src["path"]).read_text(encoding="utf-8-sig").splitlines()
                for index in range(src["start_line"] - 1, src["end_line"]):
                    print(f"{index + 1}\t{lines[index]}")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    raise SystemExit(main())
