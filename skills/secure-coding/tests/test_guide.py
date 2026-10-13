"""Regression checks for rule boundaries, provenance and portable retrieval."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("guide", ROOT / "scripts" / "guide.py")
guide = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guide)


class ParserTests(unittest.TestCase):
    def test_rule_ids_include_scenario_and_ignore_toc_and_code(self):
        text = "\n".join([
            "* [1.1.1 【必须】目录](#toc)",
            "# 通用类", "## I. 实现", "### 1.1 内存",
            "#### 1.1.1【必须】检查长度", "正文", "```python",
            "# 后台类", "#### 9.9.9【必须】代码中的伪标题", "```", "",
            "# 后台类", "## I. 实现", "### 1.1 输入",
            "#### 1.1.1 【建议】检查输入", "第二段", "",
        ])
        rules = guide.parse_source(text, "python", "sources/example.md")
        self.assertEqual([r["id"] for r in rules],
                         ["PY-COMMON-1.1.1", "PY-BACKEND-1.1.1"])
        self.assertEqual(rules[0]["source"]["start_line"], 5)
        self.assertEqual(rules[0]["source"]["end_line"], 10)
        self.assertEqual(rules[1]["source"]["start_line"], 15)
        self.assertEqual(rules[1]["requirement"], "建议")

    def test_bold_js_rules_stop_at_the_next_section(self):
        text = "\n".join([
            "## JavaScript页面类", "### I. 代码实现", "#### 1.1 DOM",
            "**1.1.1【必须】安全文本**", "示例", "~~~js",
            "**7.7.7【必须】伪标题**", "~~~", "",
            '<a id="next"></a>', "#### 1.2 框架",
            "**1.2.1【推荐】框架规则**", "第二段", "",
            "## Node.js后台类", "### I. 实现", "#### 1.1 输入",
            "**1.1.1【必须】校验**", "第三段",
        ])
        rules = guide.parse_source(text, "javascript", "sources/example.md")
        self.assertEqual([r["id"] for r in rules],
                         ["JS-BROWSER-1.1.1", "JS-BROWSER-1.2.1", "JS-NODE-1.1.1"])
        self.assertEqual(rules[0]["source"]["end_line"], 8)
        self.assertEqual(rules[1]["section"],
                         ["JavaScript页面类", "I. 代码实现", "1.2 框架"])

    def test_duplicate_ids_and_unknown_scenarios_fail_closed(self):
        for text in [
            "# 通用类\n#### 1.1【必须】A\n#### 1.1【必须】B",
            "# 新场景\n#### 1.1【必须】A",
        ]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                guide.parse_source(text, "python", "sources/example.md")


class PackageTests(unittest.TestCase):
    def run_tool(self, root, *args):
        return subprocess.run([sys.executable, str(root / "scripts" / "guide.py"), *args],
                              cwd=tempfile.gettempdir(), capture_output=True,
                              text=True, encoding="utf-8")

    def test_real_rule_returns_its_body_from_an_unrelated_directory(self):
        result = self.run_tool(ROOT, "show", "PY-BACKEND-1.2.1")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('cur.execute("SELECT', result.stdout)
        self.assertIn("PY-BACKEND-1.2.1", result.stdout)

    def test_unknown_rule_is_an_error(self):
        result = self.run_tool(ROOT, "show", "NOT-A-RULE")
        self.assertNotEqual(result.returncode, 0)

    def test_source_drift_is_rejected_before_display(self):
        with tempfile.TemporaryDirectory() as folder:
            copied = Path(folder) / "secure-coding"
            shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns("__pycache__"))
            source = copied / "sources" / "Python安全指南.md"
            source.write_bytes(source.read_bytes() + b"\nchanged\n")
            result = self.run_tool(copied, "show", "PY-BACKEND-1.2.1")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("hash", result.stderr.lower())

    def test_missing_rule_and_broken_reference_fail_validation(self):
        with tempfile.TemporaryDirectory() as folder:
            copied = Path(folder) / "secure-coding"
            shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns("__pycache__"))
            catalog = copied / "references" / "rules.json"
            data = json.loads(catalog.read_text(encoding="utf-8"))
            data["rules"].pop()
            catalog.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            result = self.run_tool(copied, "check")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("catalog", result.stderr.lower())
        with tempfile.TemporaryDirectory() as folder:
            copied = Path(folder) / "secure-coding"
            shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns("__pycache__"))
            with (copied / "SKILL.md").open("a", encoding="utf-8") as stream:
                stream.write("\n[Missing](references/does-not-exist.md)\n")
            result = self.run_tool(copied, "check")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("does-not-exist", result.stderr)


if __name__ == "__main__":
    unittest.main()
