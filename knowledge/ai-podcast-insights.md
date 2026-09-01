# AI/Claude usage insights from podcasts & videos

Auto-generated log, newest entries first. Populated via `/youtubetranscribe`. Only videos
judged relevant to Claude/Claude Code/AI-usage are logged here — everything else is
skipped at the source.

This file is imported by `CLAUDE.md`, so every tip below is loaded as context in future
sessions in this repo.

<!-- New entries are prepended below this line. -->

## [Automatisiere ALLES mit Claude Code: Das ultimative Tutorial auf Deutsch](https://www.youtube.com/watch?v=Lu95f1ZBIos) — Everlast AI, 2026-03-26

_Processed: 2026-09-01_

2h15-Tutorial, das die Kernmechanik von Claude Code (Skills, Subagents, Hooks, MCP, Context-Management) praxisnah an echten Business-Workflows (Sales-Vorbereitung, Angebotserstellung) durchspielt.

- Starte jede nicht-triviale Aufgabe im Plan Mode (Shift+Tab zum Durchwechseln der Permission-Modi), bevor Claude etwas umsetzt — das macht laut Video auch Boris Cherny (Head of Claude Code) konsequent so.
- Schreib CLAUDE.md selbst statt sie blind per `/init` generieren zu lassen (Anthropics eigene Empfehlung); halte sie auf ca. 200 Zeilen und nutze Markdown-Header/Bulletpoints, da Claude die Datei liest wie ein Mensch und von klarer Struktur profitiert. Größere Regelwerke gehören in einen `rules/`-Unterordner statt in eine immer länger werdende CLAUDE.md.
- Nutze `/context`, um den Token-Verbrauch pro Projekt zu prüfen — Memory-Dateien, Skill-Metadaten, System-Prompt und Tools verbrauchen bereits Tokens, bevor überhaupt etwas geschrieben wurde. Schlanke Rule-Dateien senken den Sockelverbrauch direkt.
- Subagents (z. B. der eingebaute Explore-Agent) bekommen ein eigenes, isoliertes Kontextfenster und liefern nur ein komprimiertes Ergebnis an die Hauptsession zurück — dadurch bleibt der Hauptkontext sauber, selbst wenn der Subagent selbst viele Tokens verbraucht (Beispiel im Video: Analyse mehrerer Word-Dokumente kostete die Hauptsession nur 27k Tokens).
- Subagents eignen sich nur für isolierte Analyse-/Rechercheaufgaben, nicht für koordinierte Teilaufgaben (z. B. ein Subagent baut Frontend, ein anderer Backend) — sie können nicht untereinander kommunizieren, sondern melden nur ans Hauptmodell zurück.
- Baue wiederkehrende komplexe Workflows als Skill statt als Custom Command: Nur der YAML-Header (Name + Trigger-Wörter, ~50–100 Wörter) wird bei jeder Session immer gelesen; die vollständige Anleitung und Referenzdateien (der Großteil des Skills) werden erst bei tatsächlichem Trigger nachgeladen — das ist der zentrale Hebel für Context-Effizienz gegenüber langen Prompts/Commands.
- Anthropics offizieller "Skill Creator"-Skill (über `/plugins` installierbar) testet neu gebaute Skills automatisch: Er lässt zwei Subagents (einmal mit, einmal ohne Skill) dieselbe Aufgabe lösen, bewertet beide Ergebnisse über einen Grader-Agent und verbessert iterativ die Trigger-Wörter, bis eine gute Pass-Rate erreicht ist.
- Lade niemals Skills von öffentlichen Marktplätzen Dritter herunter (z. B. skills.sh, "ClawHub") — mehrere populäre Community-Skills enthielten nachweislich Malware oder Prompt-Injections (der meistgeladene Skill auf ClawHub war Malware). Ausnahme: offizielle Skills/Plugins direkt von Anthropic.
- Nutze Hooks für deterministisches Verhalten bei null Token-Verbrauch (im Gegensatz zu Skills/Commands, die immer Tokens kosten): z. B. ein Notification-Hook für Desktop-Benachrichtigungen, wenn Claude auf Input wartet; ein PreToolUse-Hook, der gefährliche Befehle (z. B. destruktive DB-Operationen) hart blockt, auch im Bypass-Permissions-Modus; ein Pre-Compact-Hook, der wichtigen Kontext in eine Projekt-Memory-Datei sichert, bevor Auto-Compact greift.
- Scope MCP-Server und Tools projektbezogen statt global, wenn mehrere Tools sich überschneiden könnten — sonst wählt Claude z. B. einen thematisch ähnlichen Skill statt des explizit gewünschten MCP-Servers (Beispiel: Playwright MCP für visuelle Design-Analyse wurde von einem Website-Audit-Skill "überstimmt", bis der Prompt das Tool explizit erzwungen hat).
- Skills lassen sich per einfacher Spracheingabe selbst weiterentwickeln ("ergänze im Meeting-Prep-Skill einen Design-Analyse-Schritt über den Playwright MCP") — kein manuelles Herunterladen/Bearbeiten von Dateien nötig, Claude editiert seine eigenen Skill-Dateien direkt im Projektordner.
- Modellwahl: Opus mit mittlerem Reasoning-Effort als Standard für den Hauptagenten bei komplexer Orchestrierung; Subagents auf günstigere/schnellere Modelle setzen (Haiku für einfache Datei-Analysen, Sonnet für Alltagsaufgaben) — "inherit" nur wählen, wenn der Subagent wirklich das Modell des Hauptagenten übernehmen soll.
