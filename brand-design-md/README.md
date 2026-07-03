# brand-design-md

> A Claude Code Skill powered by [getdesign.md](https://getdesign.md) — give your AI agent the design language of world-class brands, on demand.

![Brands](https://img.shields.io/badge/brands-62-533afd?style=flat-square)
![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-d97757?style=flat-square)
![Last Update](https://img.shields.io/github/last-commit/SpaceZephyr/brand-design-md?style=flat-square&label=last%20update)
![License](https://img.shields.io/github/license/SpaceZephyr/brand-design-md?style=flat-square)

[English](#english) · [中文](#中文)

---

<a name="english"></a>

## The Problem

Vibecoding has a style problem.

You can ask AI to build a landing page in minutes. But the result looks like... AI built it. Random primary colors. System fonts. Buttons that could belong to any company on earth.

The fix isn't better prompting — it's better context. Design systems like Apple's, Notion's, and Stripe's aren't "minimalist" or "clean" in the abstract. They're defined by exact values: `letter-spacing: -2.125px`, `font-weight: 300`, `rgba(50,50,93,0.25) 0px 30px 45px -30px`. That precision is what makes them recognizable.

This skill gives Claude Code access to all of it.

---

## What It Does

This Claude Code Skill wraps [getdesign.md](https://getdesign.md) — a project that distills 62 top brand design systems into structured `DESIGN.md` files — and makes it available as a conversational interface.

**Say this:**
> "Build a login page in Stripe style"
> "Make it look like Linear"
> "Notion warm colors + Linear minimal layout, build a card component"

**The skill will:**
1. Recognize the brand name (Chinese or English)
2. Run `npx getdesign@latest add <slug>` to fetch the latest design spec
3. Extract exact color tokens, typography rules, spacing systems, shadow formulas
4. Generate UI code that strictly follows the spec — no approximations

Because it calls `npx` at runtime, it always fetches the **latest version** of the design spec. If getdesign.md updates a brand's rules, you get the update automatically.

---

## Supported Brands (62 total)

### Tech / AI
Apple · Claude · Cursor · ElevenLabs · Figma · Framer · Lovable · Meta · MiniMax · Mintlify · Mistral · Notion · Ollama · OpenCode · PostHog · Raycast · Replicate · Resend · Runway · Sanity · Sentry · Supabase · Superhuman · Together AI · Vercel · VoltAgent · Warp · Webflow · X.AI · Zapier

### Dev Tools / Infrastructure
Airtable · Cal.com · Clay · ClickHouse · Cohere · Composio · Expo · HashiCorp · IBM · Intercom · Linear · Miro · MongoDB · NVIDIA · Pinterest · Stripe

### Fintech / Crypto
Binance · Coinbase · Kraken · Revolut · Wise

### Consumer / Automotive
Airbnb · BMW · Ferrari · Lamborghini · Nike · Renault · Shopify · SpaceX · Spotify · Tesla · Uber

---

## Quick Reference

```
apple      → extreme whitespace + SF Pro + cinematic quality
notion     → warm minimal + serif headings + soft surfaces
claude     → terracotta accent + editorial layout + warm intellect
stripe     → purple + weight-300 elegance + refined detail
linear     → ultra minimal + precise + purple accent
vercel     → black & white precision + Geist font + pure minimal
cursor     → dark + gradient accent + AI-native
spotify    → dark base + neon green + album-art driven
tesla      → radical reduction + full-bleed photography + near-zero UI
ferrari    → cinematic black + Ferrari red + luxury typography
airbnb     → coral warmth + photography-first + rounded UI
```

---

## Installation

### Prerequisites
- [Claude Code](https://claude.ai/code) installed
- Node.js (for `npx`)

### Install the Skill

```bash
# Clone this repo
git clone https://github.com/SpaceZephyr/brand-design-md.git

# Create the skill directory and copy the file
mkdir -p ~/.claude/skills/brand-design-md
cp brand-design-md/SKILL.md ~/.claude/skills/brand-design-md/SKILL.md
```

Restart Claude Code and the skill is live.

---

## Usage

### Single brand
```
Build a Hero section in Apple style
Make a pricing page that looks like Stripe
Create a Notion-style card component
```

### Multi-brand mix
```
Notion warm colors + Linear minimal layout, build a Feature section
Apple whitespace system + Claude terracotta accent
```

### Output formats
- Default: single-file HTML with inline CSS
- Specify React, Vue, or Tailwind if needed
- Code includes comments showing which brand each token comes from

---

## How It Works

The skill runs `npx getdesign@latest add <slug>` in a temp directory, reads the generated `DESIGN.md`, and uses its contents as the design context for code generation.

This means:
- **No stale specs** — fetches from getdesign.md at runtime
- **No manual file management** — nothing gets committed to your project
- **Exact fidelity** — the spec contains precise CSS values, not vague descriptions

---

## Demo

The following pages were generated using this skill + [getdesign.md](https://getdesign.md):

| Style | Characteristics |
|-------|----------------|
| Apple | 80px hero type, full-bleed Cinematic Band, pill buttons in `#0071e3` |
| Notion | Warm `#fffdf9` background, Georgia serif headings, numbered feature list |
| Claude | `#faf8f5` base, terracotta `#d97757` accent, 720px editorial column |
| Stripe | `sohne-var` font, weight 300, `#533afd` purple, layered blue shadows |

---

## Credits

Design specs sourced from [getdesign.md](https://getdesign.md) by [VoltAgent](https://github.com/VoltAgent/awesome-design-md). This skill is a Claude Code wrapper — all design system content belongs to the respective brand owners.

---

## License

MIT

---

<a name="中文"></a>

## 中文说明

**一个 Claude Code Skill，让你的 AI 直接调用 62 个顶级品牌的设计规范。**

不再是"AI 默认风格"。告诉 Claude Code "用 Stripe 风格做一个登录页"，它会自动拉取真实设计规范，提取精确的设计 Token，生成高度还原的 UI 代码。

### 背景

Vibecoding 有个通病：AI 做出来的 UI 没有风格。

不是写错了，是没有参照物。苹果、Notion、Stripe 的设计系统不是什么"简约"或"精致"的抽象概念，而是一堆精确的数值：`letter-spacing: -2.125px`、`font-weight: 300`、`rgba(50,50,93,0.25) 0px 30px 45px -30px`。正是这些精确值让它们一眼可辨。

这个 Skill 把这些精确值全部交给 Claude Code。

### 工作原理

Skill 在运行时调用 `npx getdesign@latest add <slug>`，实时拉取指定品牌的 `DESIGN.md`，提取颜色、字体、间距、阴影等设计 Token，作为上下文生成 UI。

**因为是实时调用，所以永远获取最新版本的设计规范。**

### 安装

```bash
git clone https://github.com/SpaceZephyr/brand-design-md.git
mkdir -p ~/.claude/skills/brand-design-md
cp brand-design-md/SKILL.md ~/.claude/skills/brand-design-md/SKILL.md
```

重启 Claude Code 即可使用。

### 使用示例

**单品牌**
```
用 Apple 风格帮我做一个 Hero 区块
做一个 Stripe 风格的定价页
Notion 风格的卡片组件
```

**多品牌混搭**
```
Notion 的暖色调 + Linear 的极简排版，做个 Feature 区
用 Apple 的留白系统 + Claude 的橙赭强调色
```

支持中英文品牌名，均可正确识别。

### 支持品牌

共 62 个，覆盖科技、AI、开发工具、金融、消费品、汽车等品类。完整列表及一句话风格描述见上方英文部分。

---

设计规范来源：[getdesign.md](https://getdesign.md) · [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
