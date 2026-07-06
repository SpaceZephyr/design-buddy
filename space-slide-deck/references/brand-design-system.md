# Brand Design System for Slide Decks

Use this reference when a deck should use real brand-inspired visual systems from `getdesign.md`, or when the user wants intelligent brand style recommendations before making a PPT.

## Core Rule

Treat brand styles as **design systems**, not logos or trademark imitation.

- Use color tokens, typography behavior, spacing, density, surfaces, and component rhythm.
- Do not place brand logos, official product screenshots, or imply endorsement.
- Keep slide readability above brand mimicry.
- For every selected brand, fetch the live `DESIGN.md` before final outline generation.

## Recommendation Flow

When user gives content without an explicit style:

1. Run `scripts/recommend_brand_styles.py` with the source content.
2. Show exactly 6 options:
   - Options 1-5: content-matched brand styles, randomized among strong matches.
   - Option 6: `智能匹配` using the script's top-ranked `smart_match`.
3. Each option must include the brand slug/name and one sentence explaining why it fits the content.
4. If the user chooses `智能匹配`, use the `smart_match.slug`.

When user names a brand directly:

1. Map the brand name or alias to a `slug` from `references/brand-style-registry.json`.
2. Skip the 5+1 recommendation unless the user asks for alternatives.

When user wants mixed styles:

1. Use the first named brand as the primary style.
2. Fetch all selected brands.
3. Keep the primary brand's layout, typography rhythm, and density.
4. Borrow only 1-2 dimensions from secondary brands, usually accent colors, surface treatment, or visual motifs.

## Fetching DESIGN.md

Fetch each selected brand in a temporary isolated directory:

```bash
tmpdir="$(mktemp -d /tmp/slide-brand-design.XXXXXX)"
cd "$tmpdir"
npx getdesign@latest add <slug>
cat DESIGN.md
```

If fetching several brands, use separate temp directories or rename each file to `DESIGN-<slug>.md`.

## Converting DESIGN.md to Slide STYLE_INSTRUCTIONS

Extract the following from the fetched `DESIGN.md` and put it inside the outline's `<STYLE_INSTRUCTIONS>` block.

```markdown
Brand Design System:
  Primary Brand: <slug>
  Secondary Brands: <slug list or none>
  Source: getdesign.md DESIGN.md

Design Aesthetic:
  <2-3 sentences describing the brand-inspired slide system>

Background:
  <base surface color, gradient, texture, and slide canvas behavior>

Typography:
  Headlines: <visual description + exact values when available>
  Body: <visual description + exact values when available>

Color Palette:
  Primary Text: <token/value> - <usage>
  Background: <token/value> - <usage>
  Accent 1: <token/value> - <usage>
  Accent 2: <token/value> - <usage>

Layout & Spacing:
  <grid, margins, whitespace, density, section rhythm>

Visual Elements:
  - <brand-specific but logo-free shape, surface, chart, card, or illustration style>
  - <data visualization treatment>
  - <icon/diagram treatment>

Density Guidelines:
  <content per slide and whitespace rules>

Style Rules:
  Do: <specific brand-derived rules>
  Don't: <anti-patterns, including logo/trademark overuse>
```

## Matching Heuristics

Use registry tags and content intent:

| Content Signal | Strong Style Families |
| --- | --- |
| AI, Agent, model, automation | `claude`, `cursor`, `vercel`, `raycast`, `together.ai`, `voltagent`, `composio` |
| Developer tools, API, infra | `vercel`, `supabase`, `stripe`, `warp`, `mintlify`, `hashicorp`, `sentry` |
| Knowledge work, productivity | `notion`, `linear.app`, `raycast`, `superhuman`, `cal`, `airtable` |
| Product metrics, growth, SaaS | `stripe`, `posthog`, `clay`, `shopify`, `intercom`, `webflow` |
| Finance, crypto, payment | `stripe`, `wise`, `revolut`, `coinbase`, `binance`, `kraken` |
| Consumer, lifestyle, travel | `airbnb`, `spotify`, `pinterest`, `nike`, `uber` |
| Premium hardware, vehicle, launch | `apple`, `tesla`, `bmw`, `ferrari`, `lamborghini`, `spacex` |
| Research, enterprise, governance | `ibm`, `cohere`, `mistral.ai`, `nvidia`, `clickhouse` |
| Design, workshop, creativity | `figma`, `miro`, `framer`, `webflow`, `pinterest` |

## Fallback

If `npx getdesign` fails:

1. Use the registry `description`, `tags`, and category as a fallback style direction.
2. Tell the user the full DESIGN.md could not be fetched.
3. Continue with a clearly marked "fallback brand-inspired style" rather than blocking the deck.
