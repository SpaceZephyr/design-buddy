# 提示词组装模板

每张图的 prompt 由以下 4 块拼装而成。最终用英文+中文混合（中文用于图内文字、英文用于风格描述），写入 `/tmp/space-image-studio-prompt.txt`。

```
Create a {TYPE_NAME} image with aspect ratio {ASPECT}.

## Type Specification
{TYPE_SPEC}
（来自 references/types/{type}.md：用途定位、信息密度、必填字段规则）

## Visual Style: {STYLE_NAME}
{STYLE_SPEC}
（来自 references/styles/{style}.md：背景、字体、配色 hex、视觉元素、Do/Don't）

## Content
Title (中文): {TITLE}
Subtitle (中文): {SUBTITLE}
Key elements (中文):
- {ELEMENT_1}
- {ELEMENT_2}
- {ELEMENT_3}
Visual metaphor: {METAPHOR}
Layout: {LAYOUT}

## Universal Constraints
- All Chinese text must render with correct, complete characters — no garbled glyphs.
- No page numbers, no logos, no watermarks, no signatures.
- Generous whitespace — never overcrowd.
- One clear focal point; subject must not be cropped at edges.
- Color palette strictly limited to the hex codes listed above; no extra colors.
- Typography exactly matches the style specification — no realistic photo overlays unless style allows.
- Punctuation matches Chinese (full-width 。，！？「」) for Chinese text.
- Avoid AI clichés: no glowing orbs, no abstract data swirls, no generic "tech" backgrounds unless style demands.
```

## 类型 → TYPE_NAME / ASPECT 映射

| 类型 | TYPE_NAME | ASPECT |
|------|-----------|--------|
| 小红书封面 | "Xiaohongshu cover poster" | 3:4 |
| PPT 配图 | "Presentation slide illustration" | 16:9 |
| 流程图 | "Flowchart diagram" | 16:9 |
| 架构图 | "System architecture diagram" | 16:9 |
| ER 图 | "Entity-relationship diagram" | 16:9 |
| 思维导图 | "Mind map diagram" | 4:3 |
| 用户旅程图 | "User journey map" | 16:9 |
| 商业模式画布 | "Business model canvas (9-grid)" | 1:1 |
| SWOT | "SWOT analysis 2x2 matrix" | 1:1 |
| 竞品分析图 | "Competitive analysis chart" | 16:9 |
| 产品路线图 | "Product roadmap timeline" | 16:9 |
| 组织架构图 | "Organizational hierarchy chart" | 4:3 |
| 热力图 | "Heatmap matrix visualization" | 16:9 |
| 统计图 | "Statistical chart" | 16:9 |
| 文章逻辑图 | "Article logic diagram" | 16:9 |

## 拼装伪代码

```python
prompt = f"""Create a {type_name} image with aspect ratio {aspect}.

## Type Specification
{open(f'references/types/{type_slug}.md').read()}

## Visual Style: {style_name}
{open(f'references/styles/{style_slug}.md').read()}

## Content
{user_content_block}

## Universal Constraints
{universal_constraints}
"""

Path('/tmp/space-image-studio-prompt.txt').write_text(prompt)
```

## 注意

- 提示词总长不超 4000 字符（GPT-image-2 限制）
- 中文内容字段必须完整保留中文，不翻译
- Style 文件只读取一次，写入提示词后不再回读
