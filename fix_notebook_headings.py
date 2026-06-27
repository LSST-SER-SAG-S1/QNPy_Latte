#!/usr/bin/env python3
"""Make Jupyter notebooks render cleanly in Sphinx/myst-nb:
  * one H1 title per notebook (derived from the file name)
  * every other heading flattened to H2 (no skipped levels, tidy table of contents)
Usage:  python3 fix_notebook_headings.py [folder]   (default: docs/source/tutorials)
"""
import sys, os, re, glob, json

def title_from_filename(path):
    name = os.path.splitext(os.path.basename(path))[0]
    m = re.match(r'^(\d+)[._\-\s]+(.*)$', name)   # leading "1_" / "1." -> "1. "
    num = ""
    if m:
        num, name = m.group(1) + ". ", m.group(2)
    return num + name.replace("_", " ").strip()

def fix_notebook(path):
    with open(path, encoding="utf-8") as fh:
        nb = json.load(fh)
    title = title_from_filename(path)
    title_set = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = cell.get("source", "")
        text = "".join(src) if isinstance(src, list) else src
        out = []
        for line in text.split("\n"):
            m = re.match(r'^(#{1,6})\s+(.*)$', line.rstrip("\r"))
            if m:
                heading_text = m.group(2).strip()
                if not title_set:
                    out.append("# " + title)        # the one H1 title
                    title_set = True
                else:
                    out.append("## " + heading_text)  # all sections -> H2
            else:
                out.append(line)
        cell["source"] = "\n".join(out)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(nb, fh, indent=1, ensure_ascii=False)

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "docs/source/tutorials"
    files = [f for f in glob.glob(os.path.join(root, "**", "*.ipynb"), recursive=True)
             if ".ipynb_checkpoints" not in f]
    for f in sorted(files):
        fix_notebook(f); print("fixed:", os.path.relpath(f, root))
    print(f"\nDone - {len(files)} notebook(s) updated.")
