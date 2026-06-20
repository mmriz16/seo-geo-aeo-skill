# SEO、GEO、AEO & LLMO — 完全最適化フレームワーク

**v2.0.0** · 1,599 行 · 70KB

**Python ≥ 3.7** が必要です。`pip install` は不要 — すべてのスクリプトは標準ライブラリのみを使用します。

**🌐 他の言語：** [English](../README.md) · [Bahasa Indonesia](README.id.md) · [中文](README.zh.md) · [Español](README.es.md) · [日本語](README.ja.md)

**フルスタック検索可視性** のための包括的なスキル — クローラビリティやサイトマップから AI 引用準備、将来のエージェント対応インフラまで。5 つの重複する発見レイヤーをカバーします：

```
SEO ↔ Entity SEO ↔ GEO ↔ AEO ↔ LLMO
```

## カバレッジ

| レイヤー | 焦点 | スコア次元 |
|---------|------|:---------:|
| **SEO** | 技術的クローラビリティ、オンページ、コンテンツハブ、バックリンク、E-E-A-T | 技術 + コンテンツ |
| **Entity SEO** | 知識グラフ、Wikidata QID、sameAs、ナレッジパネル | エンティティ |
| **GEO** | AI 引用 (ChatGPT、Perplexity、Gemini)、llms.txt、pricing.md、クエリファンアウト | GEO 準備性 |
| **AEO** | 注目のスニペット（段落/リスト/表）、PAA、音声検索、speakable スキーマ | AEO 準備性 |
| **LLMO** | セマンティックの深さ、ハブアンドスポーク権威、信頼シグナル、コンテンツの鮮度 | 信頼 |
| **将来** | エージェント対応インフラ、OKF、UCP、AGENTS.md、セマンティック DOM | — |

## 主な機能

- **ROSTIDO-SCORE** — 6 次元 × 72 項目、加重スコアリング 0-100、全体スコアを制限する 7 つの拒否権項目
- **スキル契約とハンドオフ** — 監査 → 最適化 → 作成ワークフローを連鎖させる標準化された YAML 出力
- **AEO の深さ** — 3 つのスニペットバリアント（段落 40-55 語、リスト ≤9 項目、表 ≤4 列）+ PAA + 音声 + speakable スキーマ
- **クエリファンアウトフレームワーク** — 4 カテゴリにわたる 30+ のクエリテンプレート、ステップバイステップのマッピングガイド
- **月次 AI 可視性トラッカー** — ChatGPT、Perplexity、Gemini、AI Overviews 全体の引用を追跡するテンプレート
- **優先順位ティア** — P0（拒否権項目）→ P3（継続中）、スコア次元にマッピング
- **8 つの実用的 Python スクリプト**（1,623 行）— 標準ライブラリのみ、すぐに実行可能：セキュリティヘッダー、robots.txt、CWV、スキーマ、llms.txt、サイトマップ、HTML レポート、AI 可視性トラッカー
- **22 の公式リファレンスリンク** — Google Search Central ドキュメントへの直接 href

## システム要件

- **Python ≥ 3.7** — すべてのスクリプトは標準ライブラリのみを使用（`pip install` 不要）
- **インターネット** — スクリプトはターゲット URL と Google API からライブデータを取得
- **OS** — Windows 10/11 でテスト済み、Linux/macOS でも動作するはず

## 使用方法

### クイックスタート：3 コマンドで完全監査

```bash
# 1. リポジトリをクローン
git clone https://github.com/mmriz16/seo-geo-aeo-skill.git
cd seo-geo-aeo-skill

# 2. すべての個別チェックを実行
python3 scripts/check_security_headers.py https://example.com
python3 scripts/check_robots_txt.py https://example.com
python3 scripts/check_llms_files.py https://example.com
python3 scripts/check_schema.py https://example.com
python3 scripts/check_sitemap.py https://example.com
python3 scripts/check_core_web_vitals.py https://example.com

# 3. HTML レポートを生成（すべての結果を集約）
python3 scripts/generate_score_report.py https://example.com --output report.html --open
```

### 高速単一クエリチェック

```bash
# ヘッダーのみ
python3 scripts/check_security_headers.py https://example.com

# ヘッダーを JSON として出力（他のツールにパイプ）
python3 scripts/check_security_headers.py https://example.com --json | jq .score

# AI 可視性（対話式）
python3 scripts/check_ai_visibility.py
```

### CLI エージェントスキルとして（Claude Code、Cursor、Codex など）

```bash
# エージェントのスキルディレクトリにコピー
cp -r SKILL.md scripts/ ~/.agents/skills/seo-geo-aeo/
```

その後、エージェントで次のように使用：

```
"AUDIT https://example.com using ROSTIDO-SCORE — run all scripts and generate HTML report"
"Check GEO readiness for rostido.termicons.com"
"Create an AEO-optimized FAQ section with speakable schema"
"Map query fan-out for 'social media automation'"
```

### リファレンスドキュメントとして

`SKILL.md` を開いてナビゲート：

- **§1-2** → テクニカル SEO + エンティティ SEO（基礎）
- **§3** → GEO：引用価値、llms.txt、ファンアウト
- **§4** → AEO：スニペット、PAA、音声、speakable
- **§5** → LLMO：セマンティックの深さ、信頼シグナル
- **§6** → 月次測定トラッカー
- **§8** → ROSTIDO-SCORE フレームワーク（完全スコアリング）
- **§9** → スキル契約とハンドオフプロトコル
- **§10** → クエリファンアウトテンプレート
- **§12** → 優先順位ティア P0-P3
- **`scripts/`** → 8 つの実用的 Python スクリプト

## スクリプトリファレンス

| スクリプト | チェック内容 | 終了コード | 出力 |
|-----------|------------|:---------:|------|
| `check_security_headers.py` | HSTS、CSP、X-Frame-Options、X-Content-Type-Options、Referrer-Policy、Permissions-Policy、HTTPS | 0=合格, 1=不合格 | スコア 0-100 + ヘッダーごとのステータス |
| `check_robots_txt.py` | robots.txt の存在、Sitemap ディレクティブ、AI クローラールール（10 ボット） | 0=あり, 1=なし | スコア 0-100 + ボットごとの許可/ブロック |
| `check_core_web_vitals.py` | Google PageSpeed Insights 経由の LCP、INP、CLS、TTFB、FCP | 0=正常, 1=エラー | スコア 0-100 + メトリック値 + 改善機会 |
| `check_schema.py` | すべての JSON-LD ブロック、10 の推奨スキーマタイプの検証 | 0=スコア≥50, 1=<50 | スコア 0-100 + 見つかったスキーマ + 推奨事項 |
| `check_llms_files.py` | /llms.txt、/pricing.md、/AGENTS.md — HTTP ステータス + コンテンツ品質 | 0=スコア≥50, 1=<50 | スコア 0-100 + ファイルごとの統計 + プレビュー |
| `check_sitemap.py` | XML サイトマップ、ネストされたインデックスサポート、最終更新日カバレッジ | 0=あり, 1=なし | スコア 0-100 + URL 数 + サンプル URL |
| `generate_score_report.py` | すべてのチェックを集約 → ROSTIDO-SCORE HTML ダッシュボード | 0=正常, 1=エラー | 棒グラフ + 優先順位付きの自己完結型 HTML ファイル |
| `check_ai_visibility.py` | 対話式 ChatGPT/Perplexity/Gemini/AI Overviews 追跡 | 0=正常 | JSON + ai_visibility_tracker.json に保存 |

### 共通フラグ（全スクリプト）

| フラグ | 効果 |
|-------|------|
| `--json` | 人間が読める形式ではなく JSON を出力 |
| `-h` / `--help` | 使い方を表示 |

### 完全監査ワークフロー

```bash
# ステップ 1：すべてのチェックを実行（JSON 結果を保存）
python3 scripts/check_security_headers.py https://example.com --json > /tmp/seo-headers.json
python3 scripts/check_robots_txt.py https://example.com --json > /tmp/seo-robots.json
python3 scripts/check_llms_files.py https://example.com --json > /tmp/seo-llms.json
python3 scripts/check_schema.py https://example.com --json > /tmp/seo-schema.json
python3 scripts/check_sitemap.py https://example.com --json > /tmp/seo-sitemap.json

# ステップ 2：レポートを生成
python3 scripts/generate_score_report.py https://example.com --output rostido-report.html
```

### 制限事項

これらのスクリプトは以下を**チェックしません**：
- 内部リンク構造やリンク切れ
- クロール深度や孤立ページ
- キーワード配置、コンテンツ品質、可読性
- Core Web Vitals **フィールドデータ**（PSI のラボデータを使用 — CrUX の実際のユーザーデータに近いが同一ではない）
- INP を直接（PSI は一部のオリジンで試験的メトリックとして提供）
- ソーシャルメディアの存在、バックリンクプロファイル、ブランド言及分析
- JS レンダリングコンテンツ（生の HTML のみを取得）

これらのチェックには、Screaming Frog、Ahrefs、Google Search Console などの専用ツールを使用してください。

## スコアリングシステム

**ROSTIDO-SCORE** は 6 つの次元を評価します：

| 次元 | 重み | 最大 | 拒否権項目 |
|------|:----:|:---:|:---------:|
| **T** — 技術 | 20% | 120 | sitemap、canonical、HTTPS |
| **C** — コンテンツ | 20% | 120 | — |
| **E** — エンティティ | 15% | 120 | Org スキーマ |
| **G** — GEO 準備性 | 20% | 120 | llms.txt |
| **A** — AEO 準備性 | 15% | 120 | FAQPage スキーマ |
| **R** — 信頼 | 10% | 120 | スキーマの有効性 |

各項目は 0（欠落）、5（部分的）、または 10（完全実装）でスコアリングされます。拒否権項目は全体スコアを最大 50 に制限します。

## 情報源

- Google Search Central — AI 最適化ガイド (2026)
- Princeton GEO 研究 — KDD 2024
- Lumar — GEO/AEO 戦略ガイド 2026
- HubSpot — AEO の現状 2026
- Digital Applied — GEO、LLMO、エンティティ SEO ガイド
- schema.org — 構造化データドキュメント
- llmstxt.org — LLMs.txt 仕様
- Ahrefs — ブランド言及とバックリンクの比較研究 (2025年12月)
- Search Engine Land — エンティティホームの概念 (Jason Barnard / Kalicube)

## API キーとレート制限

一部のスクリプトは外部 API を呼び出し、無料の API キーを使用することでレート制限を回避できます：

| スクリプト | API | 制限（キーなし） | 制限（キーあり） | キーの取得方法 |
|-----------|-----|:--------------:|:--------------:|--------------|
| `check_core_web_vitals.py` | **Google PageSpeed Insights** | 1日あたり240クエリ/IP | 1日あたり25,000クエリ | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) → API キーを作成 → PageSpeed Insights API を有効化 → `PAGESPEED_API_KEY` 環境変数を設定 |

### API キーの設定

```bash
# オプション 1：環境変数（セッションごと）
export PAGESPEED_API_KEY=AIzaSy...

# オプション 2：プロジェクトルートの .env ファイル
echo "PAGESPEED_API_KEY=AIzaSy..." >> .env

# オプション 3：インラインで渡す
PAGESPEED_API_KEY=AIzaSy... python3 scripts/check_core_web_vitals.py https://example.com
```

すべてのスクリプトは API キーがなくても正常に動作します — 機能しますが、大量使用時にはレート制限に達する可能性があります。

## ライセンス

Apache-2.0
