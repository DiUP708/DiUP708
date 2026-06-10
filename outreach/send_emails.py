#!/usr/bin/env python3
"""Drošs e-pastu sūtītājs melnrakstiem no outreach/drafts/.

DROŠĪBAS NOTEIKUMI (iebūvēti, nemaini bez vajadzības):
  * Noklusējums ir --dry-run: tikai parāda, ko sūtītu. Īstai sūtīšanai vajag --send.
  * Dienas limits (noklusēti 15) — skaitās no sent_log.csv.
  * Nejauša pauze 60–180 s starp e-pastiem (neizskatās pēc robota, saudzē reputāciju).
  * Atsakās sūtīt melnrakstu bez "STOP" atteikšanās rindas (likuma prasība — sk. plans/02).
  * Adreses no outreach/atteikumi.txt nekad netiek izmantotas.

Pirms pirmās sūtīšanas:
  1. Ieteikums: pirmās 1–2 nedēļas sūti MANUĀLI no sava e-pasta (labāka piegādājamība,
     jauns domēns "jāiesilda" pakāpeniski).
  2. Sakārto domēnam SPF + DKIM ierakstus (e-pasta hostinga instrukcijā).
  3. Vides mainīgie: SMTP_HOST, SMTP_PORT (587), SMTP_USER, SMTP_PASS, FROM_EMAIL, FROM_NAME.

Lietošana:
    python3 outreach/send_emails.py                 # dry-run, parāda ko sūtītu
    python3 outreach/send_emails.py --send          # sūta (ar limitu un pauzēm)
"""

import argparse
import csv
import os
import random
import re
import smtplib
import sys
import time
from datetime import date, datetime
from email.message import EmailMessage
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DRAFTS = ROOT / "drafts"
SENT_DIR = ROOT / "sent"
LOG = ROOT / "sent_log.csv"
SUPPRESSION = ROOT / "atteikumi.txt"


def parse_draft(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        return None
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2).strip()


def sent_today() -> int:
    if not LOG.exists():
        return 0
    today = date.today().isoformat()
    with open(LOG, newline="", encoding="utf-8") as f:
        return sum(1 for r in csv.reader(f) if r and r[0].startswith(today))


def log_sent(email: str, company: str, subject: str) -> None:
    new = not LOG.exists()
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["laiks", "epasts", "uznemums", "temats"])
        w.writerow([datetime.now().isoformat(timespec="seconds"), email, company, subject])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--send", action="store_true", help="tiešām sūtīt (bez šī — dry-run)")
    ap.add_argument("--daily-limit", type=int, default=15)
    args = ap.parse_args()

    suppression = set()
    if SUPPRESSION.exists():
        suppression = {l.strip().lower() for l in SUPPRESSION.read_text().splitlines() if l.strip()}

    drafts = sorted(DRAFTS.glob("*.md")) if DRAFTS.exists() else []
    if not drafts:
        print("Nav melnrakstu mapē outreach/drafts/ — vispirms palaid lead_personalizer.py")
        return 1

    already = sent_today()
    budget = max(0, args.daily_limit - already)
    print(f"Šodien jau nosūtīti: {already}; atlikušais limits: {budget}; melnraksti rindā: {len(drafts)}")
    if budget == 0:
        print("Dienas limits sasniegts — turpini rīt. (Lēni un stabili uzvar.)")
        return 0

    smtp = None
    if args.send:
        try:
            host, port = os.environ["SMTP_HOST"], int(os.environ.get("SMTP_PORT", "587"))
            user, pwd = os.environ["SMTP_USER"], os.environ["SMTP_PASS"]
            from_email = os.environ["FROM_EMAIL"]
            from_name = os.environ.get("FROM_NAME", "Atbilde24")
        except KeyError as e:
            print(f"Trūkst vides mainīgā: {e}. Sk. faila sākuma instrukciju.")
            return 1
        smtp = smtplib.SMTP(host, port, timeout=30)
        smtp.starttls()
        smtp.login(user, pwd)

    SENT_DIR.mkdir(exist_ok=True)
    sent = 0
    for path in drafts:
        if sent >= budget:
            break
        parsed = parse_draft(path)
        if not parsed:
            print(f"  ⨯ {path.name}: nesalasāms formāts, izlaižam")
            continue
        meta, body = parsed
        email = meta.get("epasts", "").lower()
        company, subject = meta.get("uznemums", "?"), meta.get("temats", "Atbilde24")

        if not email or "@" not in email:
            print(f"  ⨯ {company}: nav derīga e-pasta, izlaižam")
            continue
        if email in suppression:
            print(f"  ⨯ {company}: atteikumu sarakstā, izlaižam")
            continue
        if "STOP" not in body:
            print(f"  ⨯ {company}: melnrakstā nav atteikšanās rindas (STOP) — nesūtu. Pielabo!")
            continue

        if not args.send:
            print(f"  [dry-run] {email} ({company}) — '{subject}'")
            sent += 1
            continue

        msg = EmailMessage()
        msg["From"] = f"{from_name} <{from_email}>"
        msg["To"] = email
        msg["Subject"] = subject
        msg.set_content(body)
        smtp.send_message(msg)
        log_sent(email, company, subject)
        path.rename(SENT_DIR / path.name)
        sent += 1
        print(f"  ✓ nosūtīts: {email} ({company})")
        if sent < budget:
            pause = random.randint(60, 180)
            print(f"    ... pauze {pause}s")
            time.sleep(pause)

    if smtp:
        smtp.quit()
    print(f"\n{'Nosūtīti' if args.send else 'Dry-run apskatīti'}: {sent}")
    if not args.send:
        print("Lai tiešām sūtītu: python3 outreach/send_emails.py --send")
    return 0


if __name__ == "__main__":
    sys.exit(main())
