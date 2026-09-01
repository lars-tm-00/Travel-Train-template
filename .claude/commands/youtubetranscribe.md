---
description: Transcribe a YouTube video, check AI/Claude relevance, and log actionable tips into the knowledge base
argument-hint: <youtube-url>
---

You are running the `/youtubetranscribe` workflow. The goal: turn one YouTube video into
durable, actionable knowledge in this repo — but only if the video is actually about
AI/Claude usage, not e.g. robotics or unrelated tech news.

Input URL: `$ARGUMENTS`

Follow these steps:

## 1. Validate input
If `$ARGUMENTS` is empty or not a YouTube URL, ask the user to paste one and stop.
Otherwise extract the video ID from the URL.

## 2. Fetch metadata + captions
Try the automated path first:

1. Check `which yt-dlp`; if missing, install it with `pip3 install -q -U yt-dlp`.
2. Fetch metadata:
   `yt-dlp --skip-download --print "%(id)s|||%(title)s|||%(channel)s|||%(upload_date)s|||%(description)s" "<url>"`
3. Fetch captions (prefer manual subs, fall back to auto-generated, prefer German/English):
   `yt-dlp --skip-download --write-sub --write-auto-sub --sub-lang "de,en,en-orig" --sub-format vtt -o "/tmp/yt_%(id)s" "<url>"`
4. Find the resulting `.vtt` file(s) in `/tmp`, pick the best match, and convert it to plain
   text with `python3 scripts/youtube/vtt_to_text.py <file.vtt>`.
5. Delete the temp `.vtt`/metadata files afterwards.

**If this fails** (network/proxy block, no captions available, video restricted, tool
missing and uninstallable — e.g. this is expected in sandboxed environments where
youtube.com is blocked by egress policy): tell the user plainly what failed, then ask them
to paste the transcript manually (YouTube → "..." → "Show transcript" → copy all) or at
least the video description/show notes, plus the title. Continue with whatever text they
provide instead of aborting.

## 3. Relevance filter
Read the title, description, and transcript. Decide: is this video substantively about
**Claude, Claude Code, AI coding assistants, LLM usage, prompting techniques, or AI-driven
productivity workflows**?

- If it's about something else (robotics, hardware, general tech/business news, unrelated
  interviews, etc.) → report "Video ist nicht Claude/AI-Usage-relevant, wird übersprungen"
  with a one-line reason, and **stop here** — do not write anything to the knowledge file.
- If it's borderline (e.g. mostly unrelated but with one relevant segment) → extract only
  the relevant segment's tips, note the rest was skipped.

## 4. Extract actionable tips
For a relevant video, extract concrete, actionable takeaways — prioritize in this order:
1. Anything about Claude Code specifically (skills, commands, hooks, MCP, workflows).
2. Concrete prompting/context techniques.
3. Token/cost reduction strategies.
4. General AI coding-workflow productivity tips.

Write each tip as a short, imperative, self-contained instruction (something Claude can
actually act on later), not a vague paraphrase of "he talked about X".

## 5. Log to the knowledge base
Prepend a new entry (newest first) to `knowledge/ai-podcast-insights.md`, creating the file
from the template at the top of it if this is the first entry. Use this format:

```markdown
## [Video title](https://youtube.com/watch?v=VIDEO_ID) — Channel, YYYY-MM-DD
_Processed: <today's date>_

<one-sentence summary of why this is relevant>

- <actionable tip 1>
- <actionable tip 2>
```

## 6. Commit and push
Stage `knowledge/ai-podcast-insights.md` (and any script changes), commit with a message
like `Add insights from "<video title>"`, and push to the current branch with
`git push -u origin <branch>`. This is how the knowledge persists across sessions and
environments — mention to the user that this happened.

If the video was skipped as irrelevant in step 3, skip this step — there's nothing to
commit.

## 7. Summarize
Give the user a short summary: relevant or skipped, and if relevant, the tips that were
added (not just "done").
