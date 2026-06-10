# 03 — Piegāde: kā tehniski izpildīt solīto

## Platformas izvēle

Tev NAV jāprogrammē bots no nulles. Izmanto gatavu platformu, kurā es uzģenerēju saturu.

| Posms | Platforma | Cena | Kāpēc |
|---|---|---|---|
| **Pirmie 1–5 klienti** | Chatbase / Botpress (free–~$40/mēn) | zema | Ātri (1 vakars), čata logs + zināšanu bāze + widget kods. |
| **Skalēšana (5+ klienti)** | Stammer.ai vai līdzīgs white-label (~$59–197/mēn par VISIEM klientiem) | fiksēta | Tavs zīmols, klientu apakškonti, abonementu pārvaldība; ~$12 izmaksas uz klientu. |
| **WhatsApp/IG/Messenger** | platformas iebūvētie savienojumi vai 360dialog/Twilio | ~€10–30/klients | PRO pakas funkcija. |
| **Vizīšu kalendārs** | Calendly / Google Calendar / SimplyBook.me | free–€10 | Bots iedod pieraksta linku vai pats rezervē. |

Izvēles princips: sāc ar lētāko, kas strādā; migrē uz white-label, kad MRR > €800
(tad platformas fiksētā maksa ir <10% no MRR). Pirms pirkšanas pārbaudi aktuālās cenas —
tās mainās; sesijā ar mani varam salīdzināt konkrētajā dienā.

## Uzstādīšanas process (viens klients, ~2–3 h kopā)

1. **Anketa (30 min ar klientu):** aizpildi `tools/klienta-anketa.md` — pakalpojumi,
   cenas, darba laiki, BUJ, tonis, ko bots NEDRĪKST darīt.
2. **Es ģenerēju (tu tikai iekopē man anketu + viņa mājaslapas tekstu):**
   - bota sistēmas promptu un zināšanu bāzi (LV/RU/EN),
   - atbildes uz 30–50 tipiskākajiem jautājumiem viņa nozarē,
   - eskalācijas noteikumus ("nezinu" → paņem vārdu+telefonu → e-pasts īpašniekam),
   - sagatavi pēc `tools/klienta-konfig-sablons.yaml`.
3. **Tu ievieto platformā (30–60 min):** izveido botu, iekopē promptu/zināšanas,
   nokonfigurē kontaktu formu un e-pasta paziņojumus.
4. **Tests (30 min):** izej cauri `tools/klienta-konfig-sablons.yaml` testa čeklistei
   (20 jautājumi, t.sk. provokatīvie). Kļūdainās atbildes iekopē man — es izlaboju promptu.
5. **Live:** klients (vai tu ar viņa atļauju) ielīmē widget kodu lapā — viena `<script>`
   rinda. WhatsApp/IG savieno caur platformas instrukciju.
6. **Nodošana:** īss video/zvans "kā lasīt sarunas un kontaktus", rēķins/Stripe
   abonements aktīvs, ieraksti atjaunošanas datumu.

## Ikmēneša serviss (kāpēc klients turpina maksāt)

- **Mēneša atskaite** (PRO+): sarunu skaits, savāktie kontakti, top jautājumi,
  ieteikums ("8 cilvēki jautāja par balināšanu — ielieciet cenu lapā"). Es to uzģenerēju
  no platformas eksporta 5 minūtēs. Šī atskaite ir galvenais pret-atbiruma ierocis.
- Zināšanu bāzes atjauninājumi (jaunas cenas, brīvdienu laiki) — 10 min ar mani.
- Reizi ceturksnī: "ko jauno botam pievienot?" zvans → upsell uz augstāku paku.

## Kvalitātes red lines (nekad nepārkāp)

1. Bots nekad nesola medicīnisku/juridisku rezultātu — tikai informē un piesaka.
2. Bots nekad neizdomā cenas — ja nav zināšanu bāzē, saka "precizēšu" un paņem kontaktu.
3. Klienta dati (sarunas, kontakti) pieder klientam; GDPR apstrādes līgums `plans/04`.
4. Ja bots nokļūdās pie klienta klienta — tu atbildi 24 h laikā un izlabo. Serviss ir produkts.

→ Tālāk: `plans/04-NAUDA-NODOKLI-LIKUMI.md`
