---
name: brand-design-md
description: 根据品牌名称从 getdesign.md 自动获取设计规范并生成匹配风格的 UI 代码。支持 62 个顶级品牌风格（苹果/Apple、Notion、Claude、Stripe 等），支持中英文品牌名、混搭风格。当用户提到"XX风格"、"做成XX的感觉"、"参考XX设计"时触发。
---

# Brand Design MD Skill

当用户提到某个品牌的设计风格，你需要：

1. 识别品牌名称并映射到正确的 slug
2. 通过 `npx getdesign@latest add <slug>` 获取完整的 DESIGN.md 规范
3. 读取内容，作为设计上下文生成 UI 代码

## 品牌 Slug 注册表

### 科技 / AI 产品

| 用户可能说的 | Slug |
|---|---|
| 苹果、Apple | `apple` |
| Claude、Anthropic、Claude AI | `claude` |
| Cursor、AI编辑器 | `cursor` |
| ElevenLabs、11Labs、语音AI | `elevenlabs` |
| Figma、设计工具 | `figma` |
| Framer、建站工具 | `framer` |
| Lovable | `lovable` |
| Meta、Facebook | `meta` |
| MiniMax | `minimax` |
| Mintlify、文档平台 | `mintlify` |
| Mistral、Mistral AI | `mistral.ai` |
| Notion、笔记工具 | `notion` |
| Ollama | `ollama` |
| OpenCode | `opencode.ai` |
| PostHog | `posthog` |
| Raycast | `raycast` |
| Replicate | `replicate` |
| Resend | `resend` |
| Runway、RunwayML、AI视频 | `runwayml` |
| Sanity、CMS | `sanity` |
| Sentry | `sentry` |
| Supabase | `supabase` |
| Superhuman、邮件客户端 | `superhuman` |
| Together AI、together | `together.ai` |
| Vercel | `vercel` |
| VoltAgent | `voltagent` |
| Warp、终端 | `warp` |
| Webflow | `webflow` |
| X.AI、Grok | `x.ai` |
| Zapier | `zapier` |

### 开发者工具 / 基础设施

| 用户可能说的 | Slug |
|---|---|
| Airtable | `airtable` |
| Cal.com、Cal | `cal` |
| Clay | `clay` |
| ClickHouse | `clickhouse` |
| Cohere | `cohere` |
| Composio | `composio` |
| Expo | `expo` |
| HashiCorp | `hashicorp` |
| IBM | `ibm` |
| Intercom | `intercom` |
| Linear、项目管理 | `linear.app` |
| Miro、在线白板 | `miro` |
| MongoDB | `mongodb` |
| NVIDIA、英伟达 | `nvidia` |
| Pinterest | `pinterest` |
| Stripe、支付 | `stripe` |

### 金融 / 加密

| 用户可能说的 | Slug |
|---|---|
| Binance、币安 | `binance` |
| Coinbase | `coinbase` |
| Kraken | `kraken` |
| Revolut | `revolut` |
| Wise | `wise` |

### 消费品 / 汽车

| 用户可能说的 | Slug |
|---|---|
| Airbnb、爱彼迎 | `airbnb` |
| BMW、宝马 | `bmw` |
| Ferrari、法拉利 | `ferrari` |
| Lamborghini、兰博基尼 | `lamborghini` |
| Nike、耐克 | `nike` |
| Renault、雷诺 | `renault` |
| Shopify | `shopify` |
| SpaceX | `spacex` |
| Spotify | `spotify` |
| Tesla、特斯拉 | `tesla` |
| Uber | `uber` |

## 操作步骤

### Step 1：识别品牌

从用户的输入中识别品牌名称，对照上方注册表找到对应的 slug。

- 用户说「苹果风格」→ slug = `apple`
- 用户说「Notion 那种感觉」→ slug = `notion`
- 用户说「做成 Stripe 的极简风」→ slug = `stripe`
- 用户说「BMW + Linear 混搭」→ slugs = `bmw`, `linear.app`（多品牌混搭）

如果品牌名无法识别，直接告知用户并列出可用品牌列表。

### Step 2：获取 DESIGN.md

在终端运行以下命令（在临时目录中执行，避免污染用户项目）：

```bash
cd /tmp && mkdir -p design-md-tmp && cd design-md-tmp && npx getdesign@latest add <slug> 2>&1
```

然后读取生成的 DESIGN.md 文件：

```bash
cat /tmp/design-md-tmp/DESIGN.md
```

如果是多品牌混搭，依次获取每个品牌的 DESIGN.md，合并关键设计 token。

### Step 3：解析设计规范

从 DESIGN.md 中提取关键信息：

- **颜色系统**：背景色、文字色、强调色、边框色
- **字体规范**：字体家族、字号层级、字重、行高、字间距
- **组件样式**：按钮、卡片、导航、输入框的具体 CSS 值
- **间距系统**：基础单位和比例
- **圆角体系**：各组件的 border-radius 值
- **阴影系统**：各层级的 box-shadow 值

### Step 4：生成 UI

根据提取的设计规范，生成用户请求的 UI 代码（HTML/CSS/React/Vue 等）。

**严格执行规范中的具体数值**，不要自由发挥或用近似值替代。如果规范中写的是 `rgba(0,0,0,0.95)` 就不要用 `#000000`，如果字间距是 `-2.125px` 就不要四舍五入。

## 混搭风格指南

当用户要求混搭多个品牌风格时：

1. 分别获取各品牌的 DESIGN.md
2. 以用户指定的主品牌为基础
3. 从副品牌中提取指定维度（颜色/排版/布局/组件）进行融合
4. 在生成代码中注释说明哪部分来自哪个品牌

示例混搭逻辑：
- "Notion 暖色 + Linear 极简排版" → 用 Notion 的颜色 token + Linear 的字体排版规则
- "Apple 留白 + Claude 暖橙强调色" → 用 Apple 的间距系统 + Claude 的 `#d97757` 强调色

## 输出格式

- 默认输出完整的单文件 HTML（含内联 CSS）
- 用户明确指定 React/Vue 时输出对应格式
- 代码顶部注释品牌来源和关键设计 token，方便后续维护
- 可选：是否将 DESIGN.md 保存到用户的项目目录（询问用户）

## 错误处理

- **npx 命令失败**：提示用户确认 Node.js 环境，或手动访问 https://getdesign.md 查看规范
- **品牌不存在**：列出所有可用品牌，建议最相近的替代方案
- **网络问题**：使用品牌注册表中的简要描述作为降级设计方向

## 快速参考：各品牌风格一句话描述

```
apple      → 极致留白 + SF Pro + 电影质感
notion     → 暖色极简 + 衬线标题 + 柔和表面
claude     → 赭石强调色 + 编辑排版 + 温暖智识感
stripe     → 紫色渐变 + 300 字重优雅 + 精致细节
linear     → 超级极简 + 精准 + 紫色强调
figma      → 多彩活泼 + 专业 + 协作感
cursor     → 深色 + 渐变强调 + AI原生
spotify    → 深色底 + 荧光绿 + 音乐封面驱动
tesla      → 激进减法 + 全屏摄影 + 近零UI
ferrari    → 黑底电影感 + Ferrari红 + 奢华排版
vercel     → 黑白精准 + Geist字体 + 极简
supabase   → 深色翠绿 + 代码优先 + 开发者感
raycast    → 深色铬面 + 渐变强调 + 效率感
airbnb     → 珊瑚暖色 + 摄影驱动 + 圆润UI
stripe     → 紫色渐变 + 精致 + 金融质感
nike       → 单色 + 大写字体 + 全出血摄影
bmw        → 深色溢价面 + 精准德式美学
shopify    → 深色电影感 + 荧光绿 + 超细字重
```
