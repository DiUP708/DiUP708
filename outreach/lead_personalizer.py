#!/usr/bin/env python3
"""Personalizētu pirmā kontakta e-pastu ģenerēšana no outreach/leads.csv.

Katram CSV ierakstam ar statusu "jauns" uzģenerē individuālu e-pasta melnrakstu
(Claude API) un saglabā outreach/drafts/<uznemums>.md. NEKO nesūta — sūtīšanai
izmanto send_emails.py vai (ieteicams sākumā) sūti manuāli no sava e-pasta.

Lietošana:
    export ANTHROPIC_API_KEY=sk-ant-...
    python3 outreach/lead_personalizer.py --limit 15

Sūtītāja dati: vai nu vides mainīgajos (SENDER_NAME, SENDER_PHONE, DEMO_URL,
SENDER_LEGAL), vai aizpildi noklusējumus zemāk.
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parent
DRAFTS = ROOT / "drafts"
SUPPRESSION = ROOT / "atteikumi.txt"

SENDER_NAME = os.environ.get("SENDER_NAME", "[Tavs vārds]")
SENDER_PHONE = os.environ.get("SENDER_PHONE", "[+371 ...]")
DEMO_URL = os.environ.get("DEMO_URL", "[demo links]")
SENDER_LEGAL = os.environ.get(
    "SENDER_LEGAL", "[Vārds Uzvārds, saimn. darbības veicējs, reģ. nr. ..., adrese]"
)

MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-4-8")

SYSTEM = f"""Tu raksti īsus, personiskus B2B pirmā kontakta e-pastus latviešu valodā
uzņēmuma "Atbilde24" vārdā. Atbilde24 uzstāda mazajiem pakalpojumu uzņēmumiem AI
klientu asistentu (čats mājaslapā + WhatsApp/Messenger/Instagram), kas 24/7 atbild
klientiem latviski/krieviski/angliski, atbild uz biežākajiem jautājumiem, piesaka
vizītes un atsūta īpašniekam klientu kontaktus. Cena: uzstādīšana no €290 + no €97/mēn,
14 dienu naudas atgriešanas garantija.

PRASĪBAS E-PASTAM:
1. Maksimums 120 vārdu pamattekstā. Viena doma, viens aicinājums (apskatīt demo vai 15 min zvans).
2. Sākums OBLIGĀTI ar konkrētu, ticamu novērojumu par šo uzņēmumu (no dotajiem datiem,
   neizdomā faktus, ko nezini). Nekādu "Cienījamais uzņēmum!" vai tukšu glaimu.
3. Valoda dabiska, cilvēcīga, bez pārdošanas klišejām ("unikāla iespēja", "nepalaidiet garām")
   un bez spam-vārdiem. Uzruna "jūs".
4. Beigās paraksts: {SENDER_NAME} | Atbilde24 | {SENDER_PHONE}
   Tad rinda: {SENDER_LEGAL}
   Tad rinda: Ja nevēlaties saņemt manus e-pastus, atbildiet ar "STOP" — vairs nerakstīšu.
5. Demo links: {DEMO_URL}
6. Tēmas rinda: īsa, konkrēta, bez clickbait, ar uzņēmuma vārdu vai nozari.

ATBILDES FORMĀTS (tieši šāds, bez citiem komentāriem):
TEMA: <tēmas rinda>
---
<e-pasta pamatteksts ar parakstu>"""


def slugify(name: str) -> str:
    s = re.sub(r"[^\w\s-]", "", name.lower()).strip()
    return re.sub(r"[\s_-]+", "-", s)[:60] or "uznemums"


def load_suppression() -> set:
    if SUPPRESSION.exists():
        return {l.strip().lower() for l in SUPPRESSION.read_text().splitlines() if l.strip()}
    return set()


def generate(client: anthropic.Anthropic, row: dict) -> str:
    info = "\n".join(f"{k}: {v}" for k, v in row.items() if v and v.strip())
    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        system=SYSTEM,
        messages=[{
            "role": "user",
            "content": f"Uzraksti pirmā kontakta e-pastu šim uzņēmumam:\n\n{info}",
        }],
    )
    return next(b.text for b in response.content if b.type == "text")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=str(ROOT / "leads.csv"))
    ap.add_argument("--limit", type=int, default=15, help="maks. melnrakstu skaits reizē")
    ap.add_argument("--status", default="jauns", help="kuram statusam ģenerēt")
    args = ap.parse_args()

    suppression = load_suppression()
    DRAFTS.mkdir(exist_ok=True)
    client = anthropic.Anthropic()  # ANTHROPIC_API_KEY no vides

    done = 0
    with open(args.csv, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if done >= args.limit:
                break
            name = (row.get("uznemums") or "").strip()
            email = (row.get("epasts") or "").strip().lower()
            if not name or name.startswith("PIEMĒRS"):
                continue
            if (row.get("statuss") or "").strip() != args.status:
                continue
            if email in suppression:
                print(f"  ⨯ {name}: atteikumu sarakstā, izlaižam")
                continue
            out = DRAFTS / f"{slugify(name)}.md"
            if out.exists():
                continue

            print(f"  → ģenerēju: {name}")
            text = generate(client, row)
            m = re.match(r"TEMA:\s*(.+?)\s*\n---\s*\n(.*)", text, re.S)
            subject, body = (m.group(1), m.group(2)) if m else (f"Jautājums par {name}", text)
            out.write_text(
                f"---\nuznemums: {name}\nepasts: {email}\ntemats: {subject}\n---\n{body.strip()}\n",
                encoding="utf-8",
            )
            done += 1

    print(f"\nGatavi {done} melnraksti mapē {DRAFTS}/")
    print("OBLIGĀTI izlasi un vajadzības gadījumā pielabo katru pirms sūtīšanas!")


if __name__ == "__main__":
    sys.exit(main())
