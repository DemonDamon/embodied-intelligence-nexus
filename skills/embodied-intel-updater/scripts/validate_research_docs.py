#!/usr/bin/env python3
"""Validate embodied-intelligence-nexus research documentation quality."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = {
    "1. 结论与证据等级",
    "2. 问题设定、符号与假设",
    "3. 方法与完整推导",
    "4. 训练和推理算法",
    "5. 实验设计、基线与结果",
    "6. 失败模式、局限性与复现条件",
    "7. 代码、模型、数据与许可证",
    "8. 参考资料",
}
INLINE_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
REFERENCE_USE = re.compile(r"(?<!\!)\[(\d+)\]")
REFERENCE_DEF = re.compile(r"^\[(\d+)\]:\s+https?://\S+", re.M)
URL = re.compile(r"https?://[^\s)>\]]+")


def validate(path: Path, root: Path, strict: bool) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    rel = path.relative_to(root)
    if not text.lstrip().startswith("#"):
        issues.append(f"{rel}: 缺少一级标题")
    if "作者：Damon Li" not in text:
        issues.append(f"{rel}: 缺少作者署名")
    if not re.search(r"更新日期：\d{4}年\d{1,2}月\d{1,2}日", text):
        issues.append(f"{rel}: 缺少标准更新日期")

    if path.name != "README.md" and strict:
        for heading in REQUIRED_HEADINGS:
            if f"## {heading}" not in text:
                issues.append(f"{rel}: 缺少必需章节“{heading}”")
        if "证据状态：" not in text:
            issues.append(f"{rel}: 缺少证据状态声明")
        if "$$" not in text:
            issues.append(f"{rel}: 缺少块级数学推导公式")
        if "|" not in text:
            issues.append(f"{rel}: 缺少实验设计或资源审计表")
        if not URL.search(text):
            issues.append(f"{rel}: 缺少外部资源 URL")
        used = set(REFERENCE_USE.findall(text))
        defined = set(REFERENCE_DEF.findall(text))
        missing = used - defined
        if missing:
            issues.append(f"{rel}: 未定义参考编号 {sorted(missing)}")

    for href in INLINE_LINK.findall(text):
        href = href.strip()
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = (path.parent / href.split("#", 1)[0]).resolve()
        if not target.exists():
            issues.append(f"{rel}: 内部链接不存在 -> {href}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path, help="要检查的文档文件或目录")
    parser.add_argument("--root", type=Path, default=None, help="内部链接的仓库根目录")
    parser.add_argument("--strict", action="store_true", help="对非 README 文档要求完整研究模板")
    args = parser.parse_args()

    target = args.target.resolve()
    root = (args.root or target).resolve()
    docs = [target] if target.is_file() else sorted(target.rglob("*.md"))
    if not docs:
        print("未找到 Markdown 文档。", file=sys.stderr)
        return 2

    issues: list[str] = []
    for doc in docs:
        issues.extend(validate(doc, root, args.strict))
    print(f"检查文档数：{len(docs)}")
    if issues:
        print("质量检查失败：")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("质量检查通过：署名、日期、章节、资源、引文和内部链接符合要求。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
