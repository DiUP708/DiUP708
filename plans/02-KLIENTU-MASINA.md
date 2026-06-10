# 02 — Klientu mašīna (piesaiste, kas strādā Latvijā)

## Piltuve

```
Saraksts (es) → Pirmais kontakts (tu: zvans/e-pasts/DM) → 2 min demo (site/demo.html)
→ 14 dienu izmēģinājums → Maksājošs klients (Stripe abonements) → Ieteikumi
```

Konversijas pieņēmumi (kalibrē pēc pirmajām 2 nedēļām ar reāliem skaitļiem):
**100 mērķēti kontakti → ~30 sarunas → ~10 demo → 2–4 klienti.**
Tātad €5k mērķim (~26 klienti) kopā vajag ~800–1300 kontaktu 6–12 mēnešos =
**~10 kontaktu darba dienā.** Tas ir 45–60 min dienā. Pilnīgi izdarāms.

## Kanāli prioritārā secībā (LV specifika)

### 1. Telefons (galvenais kanāls, konversija ~10× pret e-pastu)
Latvijā mazo uzņēmumu īpašnieki paši ceļ klausuli. 10 zvani dienā.
- Skripts un iebildumu lapa: `outreach/templates-lv.md`.
- Atvērums (15 sek): *"Labdien! [Vārds] no Atbilde24. Redzēju, ka jums [klīnika X] —
  īss jautājums: kas atbild jūsu klientiem vakaros un brīvdienās, kad zvana pēc
  pieraksta?"* → klausies → piedāvā 2 min demo.
- Mērķis NAV pārdot pa telefonu. Mērķis = norunāt 15 min demo video-zvanu vai nosūtīt
  demo linku WhatsApp.

### 2. Personisks e-pasts (uzņēmuma adresēm, mazos apjomos)
- Es uzģenerēju katram uzņēmumam individuālu e-pastu (`outreach/lead_personalizer.py`
  vai vienkārši sesijā ar mani). Nekādu masu sūtīšanu.
- Sekvence: 1. e-pasts (novērojums + demo links) → +3 dienas: atgādinājums ar vērtību
  ("šādi tas izskatītos tieši jūsu lapā") → +4 dienas: "noslēdzu tēmu" e-pasts. Viss šablonos.

### 3. Facebook/Instagram DM + vietējās grupas
LV mazais bizness dzīvo Facebook. Raksti lapām, kurām cilvēki komentāros jautā cenas,
bet atbildes nav. DM šablons ir `outreach/templates-lv.md`.

### 4. Partneri (sviras efekts — 1 partneris = klientu plūsma)
Web izstrādātāji, mārketinga aģentūras, grāmatveži, kases sistēmu pārdevēji: viņiem ir
klienti, tev ir produkts. Piedāvā **20% no pirmā gada maksājumiem** par katru atvesto
klientu. 10 e-pasti partneriem nedēļā.

### 5. Ienākošie (sāk strādāt no ~2. mēneša)
- Mājaslapa + Google Business Profile "Atbilde24" (bezmaksas).
- 2 īsi video nedēļā (TikTok/Reels/Shorts): ekrāna ieraksts "Skaties, kā zobārstniecības
  bots piesaka vizīti 30 sekundēs". Scenārijus rakstu es.
- Katram apmierinātam klientam 2. mēnesī palūdz Google atsauksmi + 1 ieteikumu
  (par ieteikumu — €50 atlaide nākamajam rēķinam).

### 6. Maksas reklāma (TIKAI ja ir budžets un >5 klienti)
FB lead ads uz demo lapu, €5–10/dienā tests. Ne agrāk par 2. mēnesi — vispirms organika.

## Likumība (svarīgi, lasi!)

- **Zvani B2B** — atļauti. Ja lūdz vairs nezvanīt → ieraksti `outreach/atteikumi.txt`.
- **E-pasti:** Latvijā komercziņojumus regulē Informācijas sabiedrības pakalpojumu
  likuma 9. pants un GDPR. Drošā prakse, ko izmantojam:
  - sūtām **individuālus, personalizētus** e-pastus uz **uzņēmumu publiskajām adresēm**
    (info@..., nevis privātpersonu adresēm) ar leģitīmo interesi (B2B piedāvājums,
    saistīts ar saņēmēja saimniecisko darbību);
  - katrā e-pastā: kas tu esi (vārds, uzņēmums/SD reģ., adrese) + skaidra iespēja
    atteikties ("atbildi STOP, un vairs nerakstīšu") + atteikumus ievēro mūžīgi;
  - nekādu pirktu datubāžu, nekādu masu sūtījumu tūkstošos. 10–15 dienā, katrs unikāls.
  - Esošajiem klientiem drīkst sūtīt par līdzīgiem pakalpojumiem (soft opt-in), kamēr
    viņi nav atteikušies.
- **GDPR savāktajiem kontaktiem:** glabā tikai biznesa info (uzņēmums, publiskais
  tālrunis/e-pasts), dzēs pēc atteikuma. CRM tabula `outreach/leads.csv`.
- Sods par spamu LV var sasniegt četrciparu summas un, galvenais, sagrauj reputāciju
  mazā tirgū. Tāpēc: kvalitāte, ne kvantitāte.

## Demo — tavs galvenais ierocis

`site/demo.html` ir interaktīvs bots fiktīvai zobārstniecībai un autoservisam.
Pārdošanas gājiens: atver telefonā/ekrānā klienta priekšā → "Uzrakstiet tam jebko, ko
jūsu klients jautātu" → bots atbild latviski un paprasa kontaktu → "Tieši šādu, tikai ar
JŪSU cenām un pakalpojumiem, es uzlikšu jūsu lapai līdz piektdienai. €490 un €167 mēnesī.
Pirmās 14 dienas — ja nepatīk, atgriežu naudu."

Pirms svarīga demo pasaki man uzņēmuma nosaukumu un mājaslapu — es 10 minūtēs uzģenerēšu
personalizētu demo konfigurāciju tieši viņa biznesam (`tools/klienta-konfig-sablons.yaml`).

## Nedēļas ritms (kopā ~6 h)

| Diena | Darbs | Laiks |
|---|---|---|
| Pirmdiena | Sesija ar mani: 50 jauni mērķi + visi melnraksti gatavi | 45 min |
| O–T–C | 10 zvani + e-pastu sūtīšana/atbildes (atbildes rakstu es) | 3×45 min |
| Piektdiena | Demo zvani + uzstādīšanas darbi jaunajiem | 1–2 h |
| Sestdiena | 2 īsie video (scenāriji no manis) | 40 min |

## Mērījumi (pildi `outreach/leads.csv` katru dienu)

Zvani / sasniegti / demo norunāti / demo notikuši / izmēģinājumi / klienti / MRR.
Reizi nedēļā parādi man skaitļus — es pateikšu, kura piltuves daļa buksē un ko mainīt.

→ Tālāk: `plans/03-PIEGADE.md` — ko darīt, kad klients pateica "jā".
