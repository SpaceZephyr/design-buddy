# 视觉风格预设

每种风格定义完整的 CSS token。生成图表时，将这些 token 作为 CSS Custom Properties 写入 HTML。

---

## 风格 1：黑白简约 (mono)

灵感来源：Notion、Vercel。干净、克制、零装饰。

```css
:root {
    /* 颜色 */
    --bg: #ffffff;
    --bg-surface: #f7f6f3;
    --bg-hover: #f1f1ef;
    --text-primary: #37352f;
    --text-secondary: #787774;
    --text-muted: #b4b4b0;
    --border: #e3e2de;
    --border-light: #ededec;
    --accent: #37352f;
    --accent-light: rgba(55, 53, 47, 0.08);
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.06);

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

灵感来源：Linear、Cursor、Raycast。科技感、高级感、微发光。

```css
:root {
    /* 颜色 */
    --bg: #0a0a0b;
    --bg-surface: #141416;
    --bg-hover: #1c1c1f;
    --text-primary: #e8e8ed;
    --text-secondary: #9d9da5;
    --text-muted: #56565e;
    --border: #2a2a2f;
    --border-light: #1f1f24;
    --accent: #8b5cf6;
    --accent-light: rgba(139, 92, 246, 0.15);
    --shadow: 0 4px 16px rgba(0, 0, 0, 0.4);

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
    --line-normal: 1.5;
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
--block-1-bg: #1a1a1f;
--block-2-bg: #1c1919;
--block-3-bg: #191c1a;
--block-4-bg: #19191c;
--block-title-color: #e8e8ed;
```

---

## 风格 3：Claude 暖色 (claude)

灵感来源：Anthropic / Claude 品牌。温暖、知性、有质感。

```css
:root {
    /* 颜色 */
    --bg: #faf7f5;
    --bg-surface: #f5f0eb;
    --bg-hover: #efe8e1;
    --text-primary: #1a1612;
    --text-secondary: #6b5e52;
    --text-muted: #b5a898;
    --border: #e0d5c8;
    --border-light: #ebe3d9;
    --accent: #d97757;
    --accent-light: rgba(217, 119, 87, 0.12);
    --shadow: 0 2px 8px rgba(26, 22, 18, 0.06);

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
--block-1-bg: #fef3ee;  /* 重要伙伴 - 暖橙浅 */
--block-2-bg: #fef9f0;  /* 关键活动 - 暖黄浅 */
--block-3-bg: #f0f5ee;  /* 核心资源 - 暖绿浅 */
--block-4-bg: #f5f0f8;  /* 价值主张 - 暖紫浅 */
--block-5-bg: #fef0f2;  /* 客户关系 - 暖粉浅 */
--block-6-bg: #eef5f5;  /* 客户细分 - 暖青浅 */
--block-7-bg: #f5f4ee;  /* 渠道通路 - 暖灰浅 */
--block-8-bg: #f2eeed;  /* 成本结构 - 暖棕浅 */
--block-9-bg: #eef4ee;  /* 收入来源 - 暖绿浅 */
--block-title-color: #1a1612;
```

### SWOT 专用颜色

```css
--swot-s-bg: #eef5ee;   /* 优势 - 绿 */
--swot-w-bg: #f5f0f8;   /* 劣势 - 紫 */
--swot-o-bg: #fef3ee;   /* 机会 - 橙 */
--swot-t-bg: #fef0f2;   /* 威胁 - 粉 */
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
