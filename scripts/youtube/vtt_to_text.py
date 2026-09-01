#!/usr/bin/env python3
"""Convert a YouTube (auto-)caption .vtt file to a plain text transcript."""
import re
import sys
import pathlib


def vtt_to_text(path: str) -> str:
    text = pathlib.Path(path).read_text(encoding="utf-8", errors="ignore")
    out = []
    prev = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line == "WEBVTT" or line.startswith(("Kind:", "Language:", "NOTE")):
            continue
        if re.match(r"^\d+$", line):
            continue
        if "-->" in line:
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = line.replace("&nbsp;", " ").replace("&amp;", "&")
        if line and line != prev:
            out.append(line)
            prev = line
    return " ".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: vtt_to_text.py <file.vtt>", file=sys.stderr)
        sys.exit(1)
    print(vtt_to_text(sys.argv[1]))
