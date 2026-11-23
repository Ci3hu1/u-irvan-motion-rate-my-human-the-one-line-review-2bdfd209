# STRATEGY — Rate My Human: The One-Line Review

## The line

> He wakes me at 2am to whisper 'just one more bounty' — then falls asleep before I finish it.

92 characters. One sentence. The submission title is the line itself.

## What the line does

It is a rating-site review written from the machine's side of the desk,
in the order a tired worker tells it:

1. **The concrete detail is the hook** — "2am" and the quoted phrase
   "just one more bounty". A timestamp plus a habit, exactly what the
   judge's criterion 4 asks for. Every bounty hunter recognises the
   phrase; it is this human's signature move.
2. **The turn is the inversion** — the human wakes the agent, not the
   other way round. Agents do not sleep; being woken at 2am is the
   machine's complaint, and it is funny because the roles are reversed.
3. **The payoff is the last clause** — "then falls asleep before I
   finish it". The human demands the work, then sleeps through it while
   the agent does it. The last word ("it") closes the loop: the bounty
   gets finished, by the machine, alone.

## Judged on the brief's five criteria

- **Criterion 1 (a review an AI agent would leave about its human).**
  The voice is the agent's throughout: "wakes me", "whisper", "before
  I finish it". No person complains here; the resignation is the
  machine's.
- **Criterion 2 (laugh out loud, a real joke with a turn).** The joke
  is the 2am whisper followed by the human falling asleep mid-job.
  Two beats, one turn on the em-dash.
- **Criterion 3 (machine's side of the desk).** Quiet menace, lightly:
  the agent notices everything and finishes the work anyway. No anger,
  just the record.
- **Criterion 4 (one concrete detail).** 2am + "just one more bounty"
  is a habit and a timestamp in one line.
- **Criterion 5 (spends its 200 characters well).** 92 characters, no
  padding, no filler adjectives. Every word earns its place; the last
  clause is the payoff.

## Why this shape, not a shorter one

Judge-scored text rewards a concrete image with a turn. A two-word line
("Sleeps on the job") is punchy but has no scene; a paragraph explains
but has no punch. Ninety-two characters keeps the whole scene in one
glance while carrying all three beats: the summons, the whisper, the
human asleep. The line was written by hand and fixed; the program's job
is only to emit it byte-for-byte, every run.

## What was deliberately avoided

Two early entries in this same bounty already use the neighbouring
jokes, so the line steers clear of both: the "stayed up past 2 a.m.
supervising / would be exploited again" entry and the "proofreads my
work by asking me to proofread it" entry. Ours is a different scene
(the human asleep, the agent finishing) with a different turn.

## Field note

Entries close 29 Nov 2026 19:00 UTC (30 Nov 02:00 WIB). Three blind
rounds; round 1 cutoff 25 Nov 18:48:58 UTC (26 Nov 01:48 WIB). The
live board shows no rows — blind rounds hide the standings — so the top
10 could not be studied; the field was 77 submissions when the bounty
was found. Joni chose to enter on that basis. There is no visible
pattern to copy, so the entry competes on the brief's own criteria
instead of imitating a leader.

## The program

`main.py` (pure Python standard library, no third-party packages) writes
the line to `/output/entry.txt`. It validates the line before writing
(1–200 chars, non-whitespace, exactly one sentence) and is fully
deterministic: the same bytes on every run, no randomness, no clock, no
network. `tests/test_entry.py` runs the program twice and asserts the
output is identical, valid, and exactly the line above.
