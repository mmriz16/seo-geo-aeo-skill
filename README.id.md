# SEO, GEO, AEO & LLMO — Kerangka Optimasi Lengkap

**v2.0.0** · 1.599 baris · 70KB

**Python ≥ 3.7** diperlukan untuk skrip. Tidak perlu `pip install` — semua skrip hanya menggunakan stdlib.

**🌐 Baca dalam bahasa lain:** [English](README.md) · [Bahasa Indonesia](README.id.md) · [中文](README.zh.md) · [Español](README.es.md) · [日本語](README.ja.md)

Skill komprehensif untuk **visibilitas pencarian full-stack** — dari crawlability dan sitemap hingga kesiapan kutipan AI dan infrastruktur agent-ready di masa depan. Mencakup lima lapisan penemuan yang saling tumpang tindih:

```
SEO ↔ Entity SEO ↔ GEO ↔ AEO ↔ LLMO
```

## Cakupan

| Lapisan | Fokus | Dimensi Skor |
|---------|-------|:------------:|
| **SEO** | Crawlability teknis, on-page, hub konten, backlink, E-E-A-T | Teknis + Konten |
| **Entity SEO** | Knowledge Graph, Wikidata QID, sameAs, Knowledge Panel | Entitas |
| **GEO** | Kutipan AI (ChatGPT, Perplexity, Gemini), llms.txt, pricing.md, query fan-out | Kesiapan GEO |
| **AEO** | Featured snippets (paragraf/daftar/tabel), PAA, penelusuran suara, speakable schema | Kesiapan AEO |
| **LLMO** | Kedalaman semantik, hub-and-spoke authority, sinyal kepercayaan, kesegaran konten | Kepercayaan |
| **Masa Depan** | Infra agent-ready, OKF, UCP, AGENTS.md, DOM semantik | — |

## Fitur Utama

- **ROSTIDO-SCORE** — 6 dimensi × 72 item, skor tertimbang 0-100, 7 item veto yang membatasi skor keseluruhan
- **Skill Contract & Handoff** — output YAML standar untuk merangkai alur audit → optimasi → pembuatan
- **AEO Depth** — 3 varian cuplikan (paragraf 40-55 kata, daftar ≤9 item, tabel ≤4 kolom) + PAA + suara + speakable schema
- **Query Fan-Out Framework** — 30+ template kueri di 4 kategori, panduan pemetaan langkah demi langkah
- **Pelacak Visibilitas AI Bulanan** — template untuk melacak kutipan di ChatGPT, Perplexity, Gemini, AI Overviews
- **Tingkat Prioritas** — P0 (item veto) → P3 (berkelanjutan), dipetakan ke dimensi skor
- **8 Skrip Python Nyata** (1.623 baris) — stdlib-only, siap jalan: security headers, robots.txt, CWV, schema, llms.txt, sitemap, laporan HTML, pelacak visibilitas AI
- **22 Tautan Referensi Resmi** — href langsung ke dokumentasi Google Search Central di seluruh dokumen

## Persyaratan

- **Python ≥ 3.7** — semua skrip hanya menggunakan stdlib (tidak perlu `pip install`)
- **Internet** — skrip mengambil data langsung dari URL target dan Google APIs
- **Sistem Operasi** — teruji di Windows 10/11, seharusnya berfungsi di Linux/macOS

## Cara Menggunakan

### Mulai cepat: audit penuh dalam 3 perintah

```bash
# 1. Clone repositori
git clone https://github.com/mmriz16/seo-geo-aeo-skill.git
cd seo-geo-aeo-skill

# 2. Jalankan semua pemeriksaan individual
python3 scripts/check_security_headers.py https://example.com
python3 scripts/check_robots_txt.py https://example.com
python3 scripts/check_llms_files.py https://example.com
python3 scripts/check_schema.py https://example.com
python3 scripts/check_sitemap.py https://example.com
python3 scripts/check_core_web_vitals.py https://example.com

# 3. Generate laporan HTML (gabungkan semua hasil)
python3 scripts/generate_score_report.py https://example.com --output report.html --open
```

### Pemeriksaan cepat satu perintah

```bash
# Header saja
python3 scripts/check_security_headers.py https://example.com

# Header sebagai JSON (untuk diproses alat lain)
python3 scripts/check_security_headers.py https://example.com --json | jq .score

# Visibilitas AI (interaktif)
python3 scripts/check_ai_visibility.py
```

### Sebagai skill agent CLI (Claude Code, Cursor, Codex, dll.)

```bash
# Salin ke direktori skills agent Anda
cp -r SKILL.md scripts/ ~/.agents/skills/seo-geo-aeo/
```

Kemudian di agent Anda:

```
"AUDIT https://example.com using ROSTIDO-SCORE — run all scripts and generate HTML report"
"Check GEO readiness for rostido.termicons.com"
"Create an AEO-optimized FAQ section with speakable schema"
"Map query fan-out for 'social media automation'"
```

### Sebagai dokumen referensi

Buka `SKILL.md` dan navigasi:

- **§1-2** → SEO Teknis + Entity SEO (fondasi)
- **§3** → GEO: kelayakan kutipan, llms.txt, fan-out
- **§4** → AEO: cuplikan, PAA, suara, speakable
- **§5** → LLMO: kedalaman semantik, sinyal kepercayaan
- **§6** → Pelacak pengukuran bulanan
- **§8** → Kerangka ROSTIDO-SCORE (skoring lengkap)
- **§9** → Skill contract & handoff protocol
- **§10** → Template query fan-out
- **§12** → Tingkat prioritas P0-P3
- **`scripts/`** → 8 skrip Python nyata

## Referensi Skrip

| Skrip | Pemeriksaan | Kode Keluar | Output |
|-------|-------------|:-----------:|--------|
| `check_security_headers.py` | HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, HTTPS | 0=lulus, 1=gagal | Skor 0-100 + status per-header |
| `check_robots_txt.py` | robots.txt ada, Sitemap directive, aturan crawler AI (10 bot) | 0=ditemukan, 1=tidak ditemukan | Skor 0-100 + izin/blok per-bot |
| `check_core_web_vitals.py` | LCP, INP, CLS, TTFB, FCP via Google PageSpeed Insights | 0=ok, 1=error | Skor 0-100 + nilai metrik + peluang |
| `check_schema.py` | Semua blok JSON-LD, validasi 10 tipe schema yang direkomendasikan | 0=skor≥50, 1=<50 | Skor 0-100 + schema ditemukan + rekomendasi |
| `check_llms_files.py` | /llms.txt, /pricing.md, /AGENTS.md — status HTTP + kualitas konten | 0=skor≥50, 1=<50 | Skor 0-100 + statistik per-file + pratinjau |
| `check_sitemap.py` | Sitemap XML, dukungan indeks bersarang, cakupan lastmod | 0=ditemukan, 1=tidak ditemukan | Skor 0-100 + jumlah URL + contoh URL |
| `generate_score_report.py` | Menggabungkan semua pemeriksaan → dashboard HTML ROSTIDO-SCORE | 0=ok, 1=error | File HTML mandiri dengan diagram batang + prioritas |
| `check_ai_visibility.py` | Pelacakan interaktif ChatGPT/Perplexity/Gemini/AI Overviews | 0=ok | JSON + simpan ke ai_visibility_tracker.json |

### Flag umum (semua skrip)

| Flag | Efek |
|------|------|
| `--json` | Output JSON alih-alih format terbaca manusia |
| `-h` / `--help` | Tampilkan penggunaan |

### Alur audit penuh

```bash
# Langkah 1: Jalankan semua pemeriksaan (simpan hasil JSON)
python3 scripts/check_security_headers.py https://example.com --json > /tmp/seo-headers.json
python3 scripts/check_robots_txt.py https://example.com --json > /tmp/seo-robots.json
python3 scripts/check_llms_files.py https://example.com --json > /tmp/seo-llms.json
python3 scripts/check_schema.py https://example.com --json > /tmp/seo-schema.json
python3 scripts/check_sitemap.py https://example.com --json > /tmp/seo-sitemap.json

# Langkah 2: Generate laporan
python3 scripts/generate_score_report.py https://example.com --output rostido-report.html
```

### Keterbatasan

Skrip ini **TIDAK** memeriksa:
- Struktur tautan internal atau tautan rusak
- Kedalaman crawl atau halaman yatim piatu
- Penempatan kata kunci, kualitas konten, atau keterbacaan
- Core Web Vitals **data lapangan** (menggunakan data lab dari PSI — mendekati tapi bukan data nyata CrUX)
- INP secara langsung (PSI menyediakannya sebagai metrik eksperimental untuk beberapa origin)
- Keberadaan media sosial, profil backlink, atau analisis mention merek
- Konten yang dirender JS (hanya mengambil HTML mentah)

Untuk pemeriksaan tersebut, gunakan alat khusus seperti Screaming Frog, Ahrefs, atau Google Search Console.

## Sistem Skoring

**ROSTIDO-SCORE** mengevaluasi 6 dimensi:

| Dimensi | Bobot | Maks | Item Veto |
|---------|:-----:|:----:|:---------:|
| **T** — Teknis | 20% | 120 | sitemap, canonical, HTTPS |
| **C** — Konten | 20% | 120 | — |
| **E** — Entitas | 15% | 120 | Skema Org |
| **G** — Kesiapan GEO | 20% | 120 | llms.txt |
| **A** — Kesiapan AEO | 15% | 120 | Skema FAQPage |
| **R** — Kepercayaan | 10% | 120 | Validitas skema |

Setiap item mendapat skor 0 (hilang), 5 (sebagian), atau 10 (terimplementasi penuh). Item veto membatasi skor keseluruhan maksimal 50.

## Sumber

- Google Search Central — Panduan Optimasi AI (2026)
- Riset GEO Princeton — KDD 2024
- Lumar — Panduan Strategi GEO/AEO 2026
- HubSpot — State of AEO 2026
- Digital Applied — Panduan GEO, LLMO, Entity SEO
- schema.org — Dokumentasi Data Terstruktur
- llmstxt.org — Spesifikasi LLMs.txt
- Ahrefs — Studi Brand Mentions vs Backlinks (Des 2025)
- Search Engine Land — Konsep Entity Home (Jason Barnard / Kalicube)

## Kunci API & Batas Kecepatan

Beberapa skrip memanggil API eksternal dan mendapat manfaat dari kunci API gratis untuk menghindari batas kecepatan:

| Skrip | API | Batas (tanpa kunci) | Batas (dengan kunci) | Cara Mendapatkan Kunci |
|-------|-----|:-------------------:|:--------------------:|------------------------|
| `check_core_web_vitals.py` | **Google PageSpeed Insights** | 240 kueri/hari per IP | 25.000 kueri/hari | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) → Buat API Key → Aktifkan PageSpeed Insights API → Setel `PAGESPEED_API_KEY` env var |

### Mengatur Kunci API

```bash
# Opsi 1: Variabel lingkungan (per sesi)
export PAGESPEED_API_KEY=AIzaSy...

# Opsi 2: File .env di root proyek
echo "PAGESPEED_API_KEY=AIzaSy..." >> .env

# Opsi 3: Lewati inline
PAGESPEED_API_KEY=AIzaSy... python3 scripts/check_core_web_vitals.py https://example.com
```

Semua skrip bekerja dengan baik tanpa kunci API — tetap berfungsi namun mungkin terkena batas kecepatan jika digunakan berat.

## Lisensi

Apache-2.0
