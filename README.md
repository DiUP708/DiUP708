# Atbilde24 — tavs biznesa komplekts

**Bizness:** AI klientu asistenti (čatboti) Latvijas mazajiem pakalpojumu uzņēmumiem.
**Modelis:** vienreizēja uzstādīšanas maksa + ikmēneša abonements (atkārtoti ieņēmumi).
**Mērķis:** €5 000/mēnesī. Reālistisks termiņš: 6–12 mēneši konsekventa darba.

> ⚠️ Vispirms izlasi `plans/00-SAKUMS-LASI-VISPIRMS.md` — tur ir godīgā daļa par to,
> kas šeit ir un kas nav iespējams. Bez tās pārējais nestrādās.

---

## Kas ir šajā repozitorijā

| Fails | Kas tas ir |
|---|---|
| `plans/00-SAKUMS-LASI-VISPIRMS.md` | Godīgs ievads: realitāte, ceļa karte, pasivitātes kāpnes |
| `plans/01-BIZNESS-UN-NISA.md` | Niša, piedāvājums, cenas, matemātika līdz €5k/mēn |
| `plans/02-KLIENTU-MASINA.md` | Klientu piesaistes sistēma: kanāli, skripti, likumība |
| `plans/03-PIEGADE.md` | Kā tehniski piegādāt pakalpojumu (platformas, process) |
| `plans/04-NAUDA-NODOKLI-LIKUMI.md` | VID, nodokļi, Stripe, līgumi, GDPR |
| `plans/05-30-DIENU-PLANS.md` | Diena pa dienai — pirmās 30 dienas |
| `plans/06-FAZE2-PASIVA-NAUDA.md` | Pasīvākie virzieni vēlāk (YouTube u.c., ar vidIQ datiem) |
| `site/index.html` | Gatava mājaslapa (publicējama šodien) |
| `site/demo.html` | Interaktīvs demo bots — tavs galvenais pārdošanas ierocis |
| `site/privatums.html` | Privātuma politikas sagatave |
| `outreach/` | E-pastu/zvanu šabloni (LV+EN), CRM tabula, automatizācijas skripti |
| `tools/` | Klienta anketa, piedāvājuma šablons, bota konfigurācijas šablons |

---

## Ko izdarīt ŠODIEN (~3 stundas)

1. **Izlasi** `plans/00` un `plans/01` (30 min).
2. **Reģistrē saimniecisko darbību** VID EDS sistēmā — bezmaksas, ~20 min tiešsaistē
   (sk. `plans/04`).
3. **Izveido Stripe kontu** (stripe.com) — lai vari pieņemt kartes un abonementus (~30 min).
4. **Nopērc domēnu** `atbilde24.lv` (vai citu — sk. `plans/01`) un izveido e-pastu
   `info@...` (~30 min).
5. **Publicē lapu** (15 min): bezmaksas variants — Cloudflare Pages vai GitHub Pages:
   - GitHub: izveido jaunu repo `atbilde24`, ielādē `site/` saturu, Settings → Pages → ieslēdz.
   - Nomaini `site/index.html` failā e-pastu/telefonu uz savējiem (meklē `TODO`).
6. **Atver demo** `site/demo.html` pārlūkā un izmēģini — šo tu rādīsi klientiem.
7. **Atgriezies pie manis (Claude)** ar tekstu: *"Sagatavo pirmos 50 mērķa uzņēmumus
   un personalizētus zvanu/e-pastu melnrakstus pēc outreach/ šabloniem"* — un sāc.

## Kā mēs strādājam tālāk (nedēļas ritms)

- **Pirmdiena (30–60 min ar mani):** es sagatavoju nedēļas mērķu sarakstu, personalizētus
  e-pastus un zvanu piezīmes; tu tikai apstiprini un nosūti.
- **Otrdiena–ceturtdiena (45 min/dienā):** 10 zvani dienā pēc skripta + atbildes uz e-pastiem
  (atbildes ģenerēju es — tu iekopē sarunu, es uzrakstu atbildi).
- **Piektdiena:** demo zvani interesentiem (15 min katrs, skripts `outreach/templates-lv.md`).
- **Klients pateica "jā":** aizpildi `tools/klienta-anketa.md` kopā ar viņu, iedod man —
  es uzģenerēju visu bota saturu un konfigurāciju (`plans/03`).

Nauda ienāk caur Stripe abonementiem automātiski. Mans darbs ir ~80% no satura un
domāšanas; tavs — zvani, paraksti un nauda.
