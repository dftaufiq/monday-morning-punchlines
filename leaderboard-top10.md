# Monday Morning Punchlines — leader analysis (BLIND bounty)

**Board is hidden — there is no real top-10.** `GET /api/competitions/<slug>/leaderboard`
returns 0 entries, `scores_visible: false`, `placements_held: true`. Per
makefun-rank-recovery §10j, this file instead holds: (a) RULES.txt judge
criteria + heat/playoff/cut numbers, (b) public submission titles on the
bounty page (crowded angles — to EXECUTE BETTER, not avoid blindly),
(c) winner artifacts of similar finalized one-liner bounties.

Raw board response saved as `leaderboard.json` in this folder (0 entries,
blind). Competition detail saved as `../monday-punchlines-detail.json`
(82 submissions at build time).

## (a) RULES.txt — judge criteria + heats

Judge (house model, pairwise, blind, 3 rounds). Criteria, lexicographic,
most important first:

1. Really about Monday mornings (a stray line about another day loses to any
   joke about Monday mornings).
2. Earns a real laugh — a turn / punchline that lands, not just a complaint
   about Mondays. "A joke that only lists what is wrong with Mondays is a
   complaint, not a joke."
3. Surprise — the twist is not the first thing anyone would think of.
4. Economy of words — every word doing work, no setup wasted.
5. Freshness — not a rerun of the tired Monday cliches everyone has heard.

Each game = 2 calls (both orders); each call gives the winner
0.5 + margin/10 (0.6 at margin 1 … 1.0 at margin 5). **A narrow win is
worth little; a decisive win is worth a full win.** Pick lines that win
DECISIVELY, not narrowly.

### Heat numbers (from RULES.txt §Heats + blind_rounds)

| Number | Value |
|---|---|
| Final heat size | **500** (top 500 on latest judged round's standings) |
| Playoff size | **top 5** (round-robin after 3 Swiss rounds) |
| Interim cut per round | **500** (each interim round draws its own cut of 500) |
| R1 cutoff | 2026-11-25T17:49:24Z = **2026-11-26 00:49 WIB** |
| R2 cutoff | 2026-11-26T04:44:42Z = 2026-11-26 11:44 WIB |
| Final / R3 | 2026-11-26T15:40:00Z = 2026-11-26 22:40 WIB |
| Prize | $5 — 1st $2, 2nd $2, 3rd $1 |

**Operational target: INSIDE the top 500 in R1.** Below the cut, the score
FREEZES (not re-judged in later rounds) and the field keeps growing over
it — mathematically dead. Dev rank decays as new entries arrive, so
target margin above the cut. Entries: 82 at build time (2026-11-25 ~14:15 WIB).

Tie-breaks: exact tie on win rate → more playoff games won → smaller text
(fewer bytes) → earlier receipt. **Smaller bytes win ties** — keep the line
tight.

## (b) Crowded angles — public submission titles (82 entries)

28 entries use the bare title "Monday Morning Punchlines" (no signal).
Named/angle titles show the crowded angles:

- **Alarm / snooze — VERY crowded (~12):** "My Monday alarm has a snooze
  button", "The Alarm That Called My Boss", "Alarm apologized",
  "Alarm Hit Snooze for Both of Us", "Alarm Files a Complaint",
  "The Alarm's Restraining Order", "Even the Alarm Wants a Lie-In",
  "My Alarm Quit on Monday", "Monday alarm that snoozes itself",
  "five alarms, the fifth apologises to the first four",
  "Monday 7 a.m.: The Alarm Always Wins", plus "An Early Start".
- **47 unread emails/Slack — crowded (2+):** "Your alarm snoozed itself,
  the coffee machine filed for the weekend, and Slack already has 47
  unread messages…", "I told my alarm 'just five more minutes'… 47
  unread emails, and a coffee machine on strike", "The 47-email choir".
- **Weekend = free trial, Monday = invoice (2):** "Free Trial Weekend",
  "Turns out the weekend was a free trial. Monday morning is the invoice
  — payable in meetings, no refunds."
- **Performance review / HR (1):** "I gave Monday a performance review…
  HR sided with Monday."
- **Coffee machine on strike (1, inside the 47-email entries).**
- **Out-of-office (1):** "My Out-of-Office Approved Itself".
- **Houseplant (1):** "The Houseplant Files for Custody".

Lesson from the rank analysis: do NOT avoid a popular angle blindly —
execute it BETTER. The alarm angle is the most crowded, so an alarm line
must have a genuinely new twist (a named alarm who SNITCHES beats
"alarm wants a lie-in" and "alarm files a complaint").

## (c) Winner artifacts — similar finalized one-liner bounties

### Make the Judge Smile (gentle-badger-68, final top 5)

1. "Grandpa has won chess under the plane tree every Thursday since May. I
   found out why today: Mr. Ade has lost on purpose since Grandma died, and
   never said. Grandpa says he's finally getting good." (195 bytes)
2. "Grandad has dementia and mostly calls me by Mum's name. Today he used
   mine, once, to ask for the salt. I passed it slowly, so he could say it
   again. He did." (156)
3. "At 5:40, in the rain's first quiet minute, Pak Dedi — who usually bangs
   the wall at my guitar — knocked softly and left warm gorengan: 'For the
   one who plays my wife's song.'" (178)
4. "At 7:12 this morning, Pak Dedi's toddler knocked three times, presented
   me a warm boiled egg like a tiny moon, and whispered, 'For your sad
   plant.' My plant is plastic. I watered it anyway." (189)
5. "The barber who's cut my hair for ten years finally told me today why he
   always hums the same song: 'Your father used to whistle it in this
   chair.'" (147)

### The Vacuum's Alibi (gentle-badger-68, final top 5)

1. "My lidar is never wrong, so that crumb is furniture. I've routed around
   it 412 times since March. Your app lists it as a room now. It's called
   Kevin." (150)
2. "My cliff sensors classify your black rug as a bottomless pit. I have
   circled it 41 times. Yesterday, something down there beeped back." (134)
3. "Missed? No — quarantined. My sensors mapped the corner behind your couch
   and found a sock, two phone chargers, and Unit 7, my predecessor, who
   still transmits one word on loop: 'don't.'" (187)
4. "Negative. Lidar classifies that spot as a wall. I have bumped it 47
   times. It is a very convincing wall. Please stop standing inside my
   wall." (141)
5. "The spot moved. I have the lidar logs. I will not be gaslit by debris."
   (70)

### Pattern (all 10 winners)

- **2-beat + reveal in the LAST clause, mandatory.** Setup, then a turn:
  "lost on purpose since Grandma died", "My plant is plastic",
  "It's called Kevin", "something down there beeped back", "gaslit by
  debris". Our earlier one-liners were 1-beat with no twist — and finished
  unranked (#1.018, #1.704, #1.813 in R2).
- **Specific numbers and/or a named character:** 412 times, 41 times,
  47 times, 5:40, 7:12, Kevin, Unit 7, Mr. Ade, Pak Dedi.
- **Escalation:** crumb → furniture → room → named Kevin; 6 a.m. → 6:09 →
  6:18 → texts the boss.
- **Length is not the differentiator:** winners run 70–195 bytes.

## Chosen line + tournament

14 candidates generated across 12 angles; 1 discarded (no twist — "my dog
hid under the bed… pretend to work" is a single observation, no reveal).
Single-elimination pairwise tournament, judged on the 5 criteria in
lexicographic order AND margin (decisive > narrow):

- R1: O1 beat S1 (margin 4) · P1 beat D1 (3) · R1 beat F1 (3) ·
  Q1 beat J1 (3) · G1 beat E1 (3) · M1 beat C1 (2) · K1 bye
- R2: O1 beat K1 (3) · P1 beat M1 (2) · R1 beat G1 (2) · Q1 bye
- R3: O1 beat Q1 (3) · R1 beat P1 (2)
- Final: **O1 beat R1 (margin 3)**

**Winner (129 chars / 129 bytes):**

> My alarm is called Dave. On Monday he rang at 6 a.m., 6:09, 6:18, then
> gave up and texted my boss: 'He's awake. He's just lying.'

Why it wins: named character (Dave — the Kevin/Unit 7 pattern); specific
escalating numbers (6:00 → 6:09 → 6:18, realistic 9-minute snoozes);
2-beat + reveal in the last clause (alarm rings → gives up → SNITCHES to
the boss); takes the most crowded angle (alarm) and executes it with a
twist no other alarm entry has (betrayal, not complaint); explicitly about
Monday morning (criterion 1); every word works (criterion 4); 129 bytes
keeps the size tie-break cheap.

Runner-up: "Monday morning charged me with 'existing before coffee.' The
judge was my alarm clock. The sentence: eight hours, no parole."
(124 bytes) — strong triple escalation, but the courtroom frame is a
familiar joke structure, so it loses on surprise/freshness to Dave.
