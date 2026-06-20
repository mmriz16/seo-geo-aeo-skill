# SEO、GEO、AEO 与 LLMO — 完整优化框架

**v2.0.0** · 1,599 行 · 70KB

**需要 Python ≥ 3.7**。无需 pip 安装 — 所有脚本仅使用标准库。

**🌐 其他语言版本：** [English](../README.md) · [Bahasa Indonesia](README.id.md) · [中文](README.zh.md) · [Español](README.es.md) · [日本語](README.ja.md)

一个全面的 **全栈搜索可见性** 技能 — 从可爬取性和站点地图到 AI 引用准备度和面向代理的未来基础设施。涵盖五个相互重叠的发现层：

```
SEO ↔ Entity SEO ↔ GEO ↔ AEO ↔ LLMO
```

## 覆盖范围

| 层级 | 焦点 | 评分维度 |
|------|------|:--------:|
| **SEO** | 技术可爬取性、页面优化、内容中心、外链、E-E-A-T | 技术 + 内容 |
| **Entity SEO** | 知识图谱、Wikidata QID、sameAs、知识面板 | 实体 |
| **GEO** | AI 引用（ChatGPT、Perplexity、Gemini）、llms.txt、pricing.md、查询扩展 | GEO 就绪度 |
| **AEO** | 精选摘要（段落/列表/表格）、PAA、语音搜索、speakable schema | AEO 就绪度 |
| **LLMO** | 语义深度、中心辐射权威性、信任信号、内容新鲜度 | 信任 |
| **未来** | 面向代理的基础设施、OKF、UCP、AGENTS.md、语义 DOM | — |

## 主要特点

- **ROSTIDO-SCORE** — 6 个维度 × 72 个项目，加权评分 0-100，7 个否决项限制总分
- **技能合约与交接** — 标准化 YAML 输出，用于串联审计 → 优化 → 创建工作流
- **AEO 深度** — 3 种摘要变体（段落 40-55 词、列表 ≤9 项、表格 ≤4 列）+ PAA + 语音 + speakable schema
- **查询扩展框架** — 4 个类别中 30+ 个查询模板，逐步映射指南
- **月度 AI 可见性追踪器** — 追踪 ChatGPT、Perplexity、Gemini、AI Overviews 引用的模板
- **优先级层级** — P0（否决项）→ P3（持续进行），映射到评分维度
- **8 个真实 Python 脚本**（1,623 行）— 仅标准库，随时可用：安全标头、robots.txt、CWV、schema、llms.txt、站点地图、HTML 报告、AI 可见性追踪器
- **22 个官方参考链接** — 全文直接链接到 Google Search Central 文档

## 系统要求

- **Python ≥ 3.7** — 所有脚本仅使用标准库（无需 `pip install`）
- **互联网** — 脚本从目标 URL 和 Google API 实时获取数据
- **操作系统** — 已在 Windows 10/11 测试，应在 Linux/macOS 上正常工作

## 使用方法

### 快速入门：3 条命令完成完整审计

```bash
# 1. 克隆仓库
git clone https://github.com/mmriz16/seo-geo-aeo-skill.git
cd seo-geo-aeo-skill

# 2. 运行所有单个检查
python3 scripts/check_security_headers.py https://example.com
python3 scripts/check_robots_txt.py https://example.com
python3 scripts/check_llms_files.py https://example.com
python3 scripts/check_schema.py https://example.com
python3 scripts/check_sitemap.py https://example.com
python3 scripts/check_core_web_vitals.py https://example.com

# 3. 生成 HTML 报告（汇总所有结果）
python3 scripts/generate_score_report.py https://example.com --output report.html --open
```

### 快速单查询检查

```bash
# 仅检查标头
python3 scripts/check_security_headers.py https://example.com

# 标头输出为 JSON（供其他工具处理）
python3 scripts/check_security_headers.py https://example.com --json | jq .score

# AI 可见性（交互式）
python3 scripts/check_ai_visibility.py
```

### 作为 CLI 代理技能使用（Claude Code、Cursor、Codex 等）

```bash
# 复制到您的代理技能目录
cp -r SKILL.md scripts/ ~/.agents/skills/seo-geo-aeo/
```

然后在您的代理中使用：

```
"AUDIT https://example.com using ROSTIDO-SCORE — run all scripts and generate HTML report"
"Check GEO readiness for rostido.termicons.com"
"Create an AEO-optimized FAQ section with speakable schema"
"Map query fan-out for 'social media automation'"
```

### 作为参考文档

打开 `SKILL.md` 并导航：

- **§1-2** → 技术 SEO + 实体 SEO（基础）
- **§3** → GEO：引用价值、llms.txt、查询扩展
- **§4** → AEO：摘要、PAA、语音、speakable
- **§5** → LLMO：语义深度、信任信号
- **§6** → 月度测量追踪器
- **§8** → ROSTIDO-SCORE 框架（完整评分）
- **§9** → 技能合约与交接协议
- **§10** → 查询扩展模板
- **§12** → 优先级层级 P0-P3
- **`scripts/`** → 8 个真实 Python 脚本

## 脚本参考

| 脚本 | 检查内容 | 退出码 | 输出 |
|------|---------|:------:|------|
| `check_security_headers.py` | HSTS、CSP、X-Frame-Options、X-Content-Type-Options、Referrer-Policy、Permissions-Policy、HTTPS | 0=通过, 1=失败 | 评分 0-100 + 每个标头的状态 |
| `check_robots_txt.py` | robots.txt 是否存在、Sitemap 指令、AI 爬虫规则（10 个爬虫） | 0=找到, 1=未找到 | 评分 0-100 + 每个爬虫的允许/阻止 |
| `check_core_web_vitals.py` | 通过 Google PageSpeed Insights 获取 LCP、INP、CLS、TTFB、FCP | 0=正常, 1=错误 | 评分 0-100 + 指标值 + 优化机会 |
| `check_schema.py` | 所有 JSON-LD 块、10 个推荐 schema 类型的验证 | 0=评分≥50, 1=<50 | 评分 0-100 + 找到的 schema + 建议 |
| `check_llms_files.py` | /llms.txt、/pricing.md、/AGENTS.md — HTTP 状态 + 内容质量 | 0=评分≥50, 1=<50 | 评分 0-100 + 每个文件的统计 + 预览 |
| `check_sitemap.py` | XML 站点地图、嵌套索引支持、lastmod 覆盖 | 0=找到, 1=未找到 | 评分 0-100 + URL 数量 + 示例 URL |
| `generate_score_report.py` | 汇总所有检查 → ROSTIDO-SCORE HTML 仪表板 | 0=正常, 1=错误 | 包含柱状图和优先级的独立 HTML 文件 |
| `check_ai_visibility.py` | 交互式 ChatGPT/Perplexity/Gemini/AI Overviews 追踪 | 0=正常 | JSON + 保存到 ai_visibility_tracker.json |

### 通用标志（所有脚本）

| 标志 | 效果 |
|------|------|
| `--json` | 输出 JSON 而不是人类可读格式 |
| `-h` / `--help` | 显示帮助信息 |

### 完整审计工作流

```bash
# 步骤 1：运行所有检查（保存 JSON 结果）
python3 scripts/check_security_headers.py https://example.com --json > /tmp/seo-headers.json
python3 scripts/check_robots_txt.py https://example.com --json > /tmp/seo-robots.json
python3 scripts/check_llms_files.py https://example.com --json > /tmp/seo-llms.json
python3 scripts/check_schema.py https://example.com --json > /tmp/seo-schema.json
python3 scripts/check_sitemap.py https://example.com --json > /tmp/seo-sitemap.json

# 步骤 2：生成报告
python3 scripts/generate_score_report.py https://example.com --output rostido-report.html
```

### 局限性

这些脚本**不**检查：
- 内部链接结构或损坏的链接
- 爬取深度或孤立页面
- 关键词放置、内容质量或可读性
- Core Web Vitals **现场数据**（使用 PSI 的实验室数据 — 接近但非 CrUX 真实用户数据）
- 直接 INP（PSI 将其作为某些来源的实验性指标提供）
- 社交媒体存在、外链概况或品牌提及分析
- JS 渲染内容（仅获取原始 HTML）

如需这些检查，请使用 Screaming Frog、Ahrefs 或 Google Search Console 等专用工具。

## 评分系统

**ROSTIDO-SCORE** 评估 6 个维度：

| 维度 | 权重 | 最高分 | 否决项 |
|------|:----:|:-----:|:------:|
| **T** — 技术 | 20% | 120 | sitemap、canonical、HTTPS |
| **C** — 内容 | 20% | 120 | — |
| **E** — 实体 | 15% | 120 | Org schema |
| **G** — GEO 就绪度 | 20% | 120 | llms.txt |
| **A** — AEO 就绪度 | 15% | 120 | FAQPage schema |
| **R** — 信任 | 10% | 120 | Schema 有效性 |

每个项目评分 0（缺失）、5（部分）或 10（完全实现）。否决项将总分上限设为 50 分。

## 来源

- Google Search Central — AI 优化指南 (2026)
- Princeton GEO 研究 — KDD 2024
- Lumar — GEO/AEO 策略指南 2026
- HubSpot — AEO 现状 2026
- Digital Applied — GEO、LLMO、实体 SEO 指南
- schema.org — 结构化数据文档
- llmstxt.org — LLMs.txt 规范
- Ahrefs — 品牌提及与外链研究 (2025年12月)
- Search Engine Land — 实体首页概念 (Jason Barnard / Kalicube)

## API 密钥与速率限制

部分脚本调用外部 API，使用免费 API 密钥可避免速率限制：

| 脚本 | API | 无限额限制 | 有密钥限制 | 如何获取密钥 |
|------|-----|:----------:|:----------:|-------------|
| `check_core_web_vitals.py` | **Google PageSpeed Insights** | 每天 240 次/IP | 每天 25,000 次 | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) → 创建 API 密钥 → 启用 PageSpeed Insights API → 设置 `PAGESPEED_API_KEY` 环境变量 |

### 设置 API 密钥

```bash
# 选项 1：环境变量（每次会话）
export PAGESPEED_API_KEY=AIzaSy...

# 选项 2：项目根目录下的 .env 文件
echo "PAGESPEED_API_KEY=AIzaSy..." >> .env

# 选项 3：内联传递
PAGESPEED_API_KEY=AIzaSy... python3 scripts/check_core_web_vitals.py https://example.com
```

所有脚本在没有 API 密钥的情况下也能优雅降级 — 它们仍可工作，但在大量使用时可能达到速率限制。

## 许可证

Apache-2.0
