# AI/Claude usage insights from podcasts & videos

Auto-generated log, newest entries first. Populated via `/youtubetranscribe`. Only videos
judged relevant to Claude/Claude Code/AI-usage are logged here — everything else is
skipped at the source.

This file is imported by `CLAUDE.md`, so every tip below is loaded as context in future
sessions in this repo.

<!-- New entries are prepended below this line. -->

## [Nie wieder Claude-Limits: 12 Tipps für 20x mehr Leistung aus deinem Claude-Plan!](https://www.youtube.com/watch?v=KZAJeq5n-m8) — Everlast AI, 2026-08-25

_Processed: 2026-09-02_

Dichter 12-Punkte-Guide, komplett fokussiert auf Token-/Kosten-Optimierung in Claude Code — direkt umsetzbare Hebel, keine Grundlagenwiederholung.

- Arbeite für produktive Aufgaben nie in der normalen Claude-Webapp (claude.ai) oder in Cowork — nur Claude Code (bevorzugt im Terminal, nicht Desktop-App) gibt dir überhaupt die Hebel, um Tokenverbrauch zu steuern.
- Mach den Kontextfenster-Füllstand sichtbar: Im Terminal wird er standardmäßig NICHT angezeigt (anders als Web-/Desktop-App) — lass dir eine Statusline einrichten, die den Füllstand laufend zeigt, und nutze `/context`, um zu sehen, was genau das Fenster füllt (System-Prompt, Tools, Nachrichten, MCP, Memory Files, Skills).
- Mentales Modell fürs Kontextfenster: BASE = **B**asis (System-Prompt/Tools/Umgebung — nicht beeinflussbar), **A**npassungen (CLAUDE.md, Skills, MCP, Memory Files — voll kontrollierbar), **S**itzung (wächst mit jeder Nachricht/jedem Tool-Ergebnis — der mit Abstand größte Posten), **E**ingabe (deine aktuelle Nachricht/Screenshots). Der A-Teil ist der einzige Hebel, den du direkt und dauerhaft steuerst.
- Halte CLAUDE.md und Skills so schlank wie möglich — jede zusätzliche Zeile wird bei praktisch jeder Anfrage neu ins Kontextfenster geladen und kostet Tokens, unabhängig davon ob sie gerade gebraucht wird.
- Schreib und arbeite auf Englisch statt Deutsch, wo immer möglich (CLAUDE.md, Skills, Doku, Prompts) — der Tokenizer ist stärker auf englischen Text trainiert, deutsche Wörter zerfallen häufiger in mehrere Bruchstücke; gleicher Inhalt kostet auf Deutsch ca. ein Drittel mehr Tokens.
- Nutze Prompt Caching bewusst: Anthropic cached die bisherige Konversation, ein Cache-Read kostet nur ~1/10 einer Neuberechnung. Der Cache verfällt nach einer Stunde Inaktivität — dann wird die komplette Historie beim nächsten Prompt wieder voll (teuer) neu berechnet. Besonders tückisch bei Remote Control vom Handy aus, wo diese 1h-Grenze leicht gerissen wird.
- Vermeide `/clear` (löscht die Session komplett) und warte nicht auf automatisches Compacting (kommt strukturell zu spät, ist der teuerste Moment) — nutze stattdessen einen selbstgebauten Handoff-Skill, der eine Zusammenfassung als Markdown-Datei auf die Platte schreibt statt sie im Kontextfenster zu kompaktieren.
- Wähle Modell und Reasoning-Effort bewusst pro Aufgabe statt immer das stärkste Modell zu nehmen: Sonnet verbraucht ca. 3x, Opus 5x, das stärkste Modell ca. 10x so viel Kontingent wie das kleinste Modell für dieselbe Aufgabe. Höherer Reasoning-Effort ist nicht automatisch besser (Benchmark-Beispiel: Medium-Effort schlägt High/Extra-High bei deutlich geringeren Kosten) — Modell/Effort vorher festlegen, ein Wechsel mitten in der Session verwirft sofort den Prompt-Cache.
- Bau dir Subagents mit explizit im Dateikopf festgelegtem (günstigerem) Modell für Delegationsaufgaben — jeder Subagent bekommt ein eigenes Kontextfenster, der teure Hauptagent bleibt schlank. Umgekehrt geht's auch: günstiges Modell als Hauptagent, das per `/advisor` nur bei Bedarf ein teureres Modell als Berater hinzuzieht.
- Bei großen Workspaces mit vielen Dateien: Nutze "Prime Commands" (eigene Slash-Commands wie `/prime` oder projektspezifische Varianten), die zu Sessionbeginn gezielt nur die wirklich relevanten Dateien laden, statt Claude pauschal alles lesen zu lassen.
- Automatisiere Handoff-Dateien per Hook bei einer selbst gewählten Kontextfenster-Schwelle (z. B. 80%). Das Handoff-Template sollte NICHT nach Arbeitsschritten fragen (die stehen ohnehin in Git-Historie/Code), sondern gezielt nach Learnings, Fehlannahmen und Stellen, die besser hätten laufen können — und diese global statt nur projektbezogen sammeln, damit sich Claude über die Zeit aus eigenen Fehlern verbessert.
- Räume regelmäßig mit einem Doctor-artigen Check auf: ungenutzte Skills/MCP-Server/Plugins und veraltete Hooks kosten trotzdem in jeder Session Kontext, auch wenn sie nie aktiv gebraucht werden — und kürze CLAUDE.md um alles, was Claude ohnehin aus dem Code selbst able­iten kann.

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
