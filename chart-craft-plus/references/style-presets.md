# 视觉风格预设

每种风格定义完整的 CSS token。生成图表时，将这些 token 作为 CSS Custom Properties 写入 HTML。

---

## 风格 1：黑白简约 (mono)

灵感来源：Notion、Vercel + Claude 羊皮纸。干净、克制、零装饰。

```css
:root {
    /* 颜色 */
    --bg: #faf9f5;
    --bg-surface: #f5f4ed;
    --bg-hover: #f0eee6;
    --text-primary: #26251e;
    --text-secondary: #6b6a62;
    --text-muted: #a3a199;
    --border: #e0ddd4;
    --border-light: #ebe9e2;
    --accent: #26251e;
    --accent-light: rgba(38, 37, 30, 0.08);
    --shadow: rgba(0,0,0,0.05) 0px 4px 24px, rgba(38,37,30,0.08) 0px 0px 0px 1px;

    /* 字体 */
    --font-body: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    --font-title: Georgia, "Noto Serif SC", "Songti SC", serif;
    --font-mono: "JetBrains Mono", "Fira Code", monospace;

    /* 字号 */
    --text-xs: 12px;
    --text-sm: 14px;
    --text-base: 16px;
    --text-lg: 20px;
    --text-xl: 28px;
    --text-2xl: 36px;

    /* 字重 */
    --weight-normal: 400;
    --weight-medium: 500;
    --weight-bold: 700;

    /* 行高 */
    --line-tight: 1.3;
    --line-normal: 1.5;
    --line-loose: 1.8;

    /* 圆角 */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;

    /* 间距 */
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 24px;
    --space-xl: 32px;
    --space-2xl: 48px;

    /* 线条 */
    --line-width: 1px;
    --line-style: solid;

    /* 特殊效果 */
    --gradient: none;
    --glow: none;
}
```

### 区块颜色（用于商业模式画布、SWOT 等）

```css
--block-1-bg: #f7f6f3;
--block-2-bg: #f7f6f3;
--block-3-bg: #f7f6f3;
--block-4-bg: #f7f6f3;
--block-title-color: #37352f;
```

---

## 风格 2：深色暗调 (dark)

灵感来源：Linear、Cursor、Raycast + Claude 温暖深色。科技感、高级感、暖色底蕴。

```css
:root {
    /* 颜色 */
    --bg: #141413;
    --bg-surface: #1a1a18;
    --bg-hover: #222220;
    --text-primary: #faf9f5;
    --text-secondary: #b0aea5;
    --text-muted: #6b6a62;
    --border: rgba(38, 37, 30, 0.25);
    --border-light: rgba(38, 37, 30, 0.12);
    --accent: #8b5cf6;
    --accent-light: rgba(139, 92, 246, 0.15);
    --shadow: rgba(0,0,0,0.14) 0px 4px 16px, rgba(38,37,30,0.1) 0px 0px 0px 1px;

    /* 字体 */
    --font-body: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    --font-title: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    --font-mono: "JetBrains Mono", "Fira Code", monospace;

    /* 字号 */
    --text-xs: 12px;
    --text-sm: 14px;
    --text-base: 16px;
    --text-lg: 20px;
    --text-xl: 28px;
    --text-2xl: 36px;

    /* 字重 */
    --weight-normal: 400;
    --weight-medium: 500;
    --weight-bold: 600;

    /* 行高 */
    --line-tight: 1.3;
    --line-normal: 1.6;
    --line-loose: 1.8;

    /* 圆角 */
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;

    /* 间距 */
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 24px;
    --space-xl: 32px;
    --space-2xl: 48px;

    /* 线条 */
    --line-width: 1px;
    --line-style: solid;

    /* 特殊效果 */
    --gradient: linear-gradient(135deg, #8b5cf6, #6366f1);
    --glow: 0 0 20px rgba(139, 92, 246, 0.2);
}
```

### 区块颜色

```css
--block-1-bg: #1e1e1c;
--block-2-bg: #201e1a;
--block-3-bg: #1c1e1a;
--block-4-bg: #1e1c20;
--block-title-color: #faf9f5;
```

---

## 风格 3：Claude 暖色 (claude)

灵感来源：Anthropic / Claude 品牌 + Cursor 暖面 + Airtable 干净感。温暖、知性、有质感。

```css
:root {
    /* 颜色 */
    --bg: #f5f4ed;
    --bg-surface: #faf9f5;
    --bg-hover: #f0eee6;
    --text-primary: #141413;
    --text-secondary: #5e5d59;
    --text-muted: #87867f;
    --border: #e0ddd4;
    --border-light: #f0eee6;
    --accent: #c96442;
    --accent-light: rgba(201, 100, 66, 0.12);
    --shadow: rgba(0,0,0,0.05) 0px 4px 24px, rgba(38,37,30,0.08) 0px 0px 0px 1px;

    /* 字体 */
    --font-body: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    --font-title: Georgia, "Noto Serif SC", "Songti SC", serif;
    --font-mono: "JetBrains Mono", "Fira Code", monospace;

    /* 字号 */
    --text-xs: 12px;
    --text-sm: 14px;
    --text-base: 16px;
    --text-lg: 20px;
    --text-xl: 28px;
    --text-2xl: 36px;

    /* 字重 */
    --weight-normal: 400;
    --weight-medium: 500;
    --weight-bold: 700;

    /* 行高 */
    --line-tight: 1.3;
    --line-normal: 1.5;
    --line-loose: 1.8;

    /* 圆角 */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;

    /* 间距 */
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 24px;
    --space-xl: 32px;
    --space-2xl: 48px;

    /* 线条 */
    --line-width: 1px;
    --line-style: solid;

    /* 特殊效果 */
    --gradient: none;
    --glow: none;
}
```

### 区块颜色（商业模式画布专用）

```css
--block-1-bg: #f8f0ea;  /* 重要伙伴 - 暖赭浅 */
--block-2-bg: #faf5ec;  /* 关键活动 - 暖黄浅 */
--block-3-bg: #edf2eb;  /* 核心资源 - 暖绿浅 */
--block-4-bg: #f2edf5;  /* 价值主张 - 暖紫浅 */
--block-5-bg: #f8eaed;  /* 客户关系 - 暖粉浅 */
--block-6-bg: #eaf2f0;  /* 客户细分 - 暖青浅 */
--block-7-bg: #f5f3ec;  /* 渠道通路 - 暖灰浅 */
--block-8-bg: #f0edeb;  /* 成本结构 - 暖棕浅 */
--block-9-bg: #ecf2eb;  /* 收入来源 - 暖绿浅 */
--block-title-color: #141413;
```

### SWOT 专用颜色

```css
--swot-s-bg: #edf2eb;   /* 优势 - 绿 */
--swot-w-bg: #f2edf5;   /* 劣势 - 紫 */
--swot-o-bg: #f8f0ea;   /* 机会 - 赭 */
--swot-t-bg: #f8eaed;   /* 威胁 - 粉 */
```

---

## 品牌风格扩展

当用户指定品牌风格时（如"Stripe 风格"），通过 brand-design-md skill 获取 DESIGN.md，提取以下 token 替换：

| CSS 变量 | DESIGN.md 对应字段 |
|----------|-------------------|
| `--bg` | 背景色 |
| `--text-primary` | 文字色 |
| `--accent` | 强调色 |
| `--border` | 边框色 |
| `--font-body` | 字体家族 |
| `--radius-md` | 圆角 |
| `--shadow` | 阴影 |

无法从 DESIGN.md 获取的变量（如字号层级、间距），沿用 Claude 暖色预设的值作为基础。

---

## 风格应用示例

HTML 中统一用 CSS 变量，切换风格只改 `:root` 的值：

```html
<style>
:root {
    /* 这里放选定风格的 token */
    --bg: #faf7f5;
    --text-primary: #1a1612;
    /* ... */
}

body {
    background: var(--bg);
    color: var(--text-primary);
    font-family: var(--font-body);
}

.card {
    background: var(--bg-surface);
    border: var(--line-width) var(--line-style) var(--border);
    border-radius: var(--radius-md);
    padding: var(--space-md);
}

.card-title {
    font-family: var(--font-title);
    font-size: var(--text-lg);
    font-weight: var(--weight-bold);
    color: var(--accent);
}
</style>
```
