<h1 align="center">Design Buddy</h1>

<p align="center"><code>design-buddy.skill</code></p>

<p align="center"><em>「你想做的下一张图，何必从空白画布开始」</em></p>

<p align="center">
  <img alt="License MIT" src="https://img.shields.io/badge/License-MIT-c8a500?style=for-the-badge">
  <img alt="Agent Skills Standard" src="https://img.shields.io/badge/Agent%20Skills-Standard-5aa524?style=for-the-badge">
  <img alt="skills.sh Compatible" src="https://img.shields.io/badge/skills.sh-Compatible-1888c8?style=for-the-badge">
  <img alt="Runtime" src="https://img.shields.io/badge/Runtime-Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20Cursor%20%C2%B7%20OpenClaw%20%C2%B7%20Hermes-7b2bd9?style=for-the-badge">
</p>

<p align="center">
  公众号 / 小红书 / B站 / 知乎：<strong>空格的键盘</strong> ｜ <a href="mailto:wzfh520@gmail.com">wzfh520@gmail.com</a>
</p>

Design Buddy 是一套给内容创作者、产品经理、独立开发者和设计协作者用的视觉生产 Skill 集合。

它帮你把文章、观点、产品逻辑、品牌概念、故事脚本和数据结构，转成封面、配图、信息图、逻辑图、架构图、Logo、故事板、幻灯片、公众号排版和社交媒体图片。

基于开放的 Agent Skills 协议，可在 Claude Code、Codex、Cursor、OpenClaw、Hermes Agent、CodeBuddy、Workbuddy、Gemini CLI、OpenCode 等兼容 runtime 中运行。

不是让 AI 随机画一张“看起来还行”的图。

是先判断内容要表达什么，再选择合适的视觉结构、画面比例、设计风格和输出格式：

- 文章应该配概念图、流程图，还是场景图
- 产品逻辑应该画架构图、旅程图，还是路线图
- 小红书内容应该拆成几页、用什么版式
- 公众号文章应该用什么排版风格、怎样复制到编辑器
- 一段故事应该切成哪些关键分镜
- 一个品牌应该生成哪些 Logo 方向
- 一份 Markdown 应该生成单张图、批量配图，还是整套幻灯片
- 一份 Markdown 应该怎样变成可分享海报

看效果 · 安装 · 它能做什么 · 使用方式 · 工作原理 · 诚实边界

## 效果示例

```text
用户      ❯ 给这篇文章做一张公众号封面

助手      ❯ 已分析文章主题：AI 生产力系统 / 上下文管理 / 个人工作流

            推荐封面方向：
            1. conceptual + warm editorial：适合个人品牌文章
            2. blueprint + technical schematic：适合方法论/系统感
            3. flat-vector + high contrast：适合社交媒体传播

            将生成 16:9 封面，并保留标题可读区。
```

再看内容可视化：

```text
用户      ❯ 把这段产品逻辑画成一张图

助手      ❯ 已识别为“多角色协作流程”，建议使用泳道图。

            结构：
            - 用户输入需求
            - Agent 判断任务类型
            - 分支 Skill 执行
            - 输出报告 / 图片 / HTML
            - 用户反馈后迭代

            将生成可截图分享的 HTML 图表。
```

再看社交媒体图片：

```text
用户      ❯ 把这篇文章拆成小红书 6 页图

助手      ❯ 已拆成 6 张图：

            1. 封面：一句话钩子
            2. 痛点：为什么普通提示词不够
            3. 框架：上下文系统四层结构
            4. 案例：写作/运营/产品怎么用
            5. 清单：搭建步骤
            6. 结尾：保存引导

            推荐风格：notion + dense layout。
```

Design Buddy 不是只负责“生成图片”。  
它负责把内容变成更容易理解、更容易传播、更适合平台的视觉表达和排版交付。

## 安装

Design Buddy 基于开放的 Agent Skills 协议，可在任何 skills-compatible 的 AI agent runtime 中运行。

### 方式一：一行命令（推荐，跨 runtime）

打开你正在用的 agent（Claude Code、Codex、Cursor、OpenClaw、Hermes、CodeBuddy、Workbuddy、Gemini CLI、OpenCode 等），告诉它：

```text
帮我安装这个 skill：https://github.com/SpaceZephyr/design-buddy
```

或者用通用 CLI 安装器（vercel-labs/skills，支持多 runtime）：

```bash
npx skills add SpaceZephyr/design-buddy
```

它会自动识别你当前的 runtime 并把 skill 放到正确目录。需要指定时可加 runtime 参数，例如 `-a codex` / `-a claude-code` / `-a cursor`。

### 方式二：手动安装

克隆仓库后，把需要的 skill 目录复制到你的 runtime skills 目录：

```bash
git clone https://github.com/SpaceZephyr/design-buddy.git
```

仓库结构：

```text
algorithmic-art/
architecture-diagram-zh/
article-batch-illustration/
canvas-design/
chart-craft/
chart-craft-plus/
gemini-image/
image-skill-builder/
logo-batch-generator/
markdown-to-image/
mermaid-generator/
space-article-batch-illustration/
space-chart-image/
space-image-studio/
space-slide-deck/
storyboard-generator/
text-logic-diagram/
wechat-official-account-layout/
```

每个子目录都是一个独立 Skill。

### 方式三：作为参考资料使用

即使你的 runtime 不支持 Agent Skills 自动加载，也可以直接打开对应目录里的 `SKILL.md`，把内容粘贴进对话。  
它本质是一份 markdown + YAML frontmatter + 可运行脚本或工作流说明。

## 使用

装好后，可以直接告诉 agent：

```text
给这篇文章生成一张封面图
```

```text
把这段内容做成小红书 6 页图片
```

```text
把这个系统画成架构图
```

```text
帮我设计 10 个 Logo 方向
```

```text
用 image-studio 做一张小红书封面
```

```text
把这份 Markdown 转成 12 页幻灯片
```

```text
把这份 Markdown 转成分享海报
```

```text
把这篇文章排成公众号可复制 HTML
```

```text
把这个故事拆成分镜并生成故事板
```

如果你想手动运行脚本，也可以进入对应 Skill 目录查看 `SKILL.md` 和 `scripts/`。

## 它能做什么

| Skill | 解决的问题 | 输出 |
| --- | --- | --- |
| `gemini-image` | Gemini 文生图、图生图、多图参考生成 | 图片 |
| `article-batch-illustration` | Markdown 文章批量配图并插入文档 | 图片 + 更新后的文章 |
| `markdown-to-image` | Markdown 转社交媒体分享海报 | PNG |
| `logo-batch-generator` | 品牌 Logo 批量生成和方向探索 | Logo 图片 |
| `storyboard-generator` | 故事润色、分镜拆解、故事板生成 | 分镜表 + 图片 |
| `chart-craft` | 流程图、架构图、ER 图、旅程图等 10 类图表 | HTML 图表 |
| `chart-craft-plus` | 35+ 类图表，覆盖技术、流程、战略、数据和信息展示 | HTML 图表 |
| `space-chart-image` | 使用 GPT-image-2 生成流程图、架构图、SWOT、路线图等图片图表 | PNG |
| `architecture-diagram-zh` | 中文系统架构图、部署图、网络拓扑图 | HTML / SVG |
| `text-logic-diagram` | 把文章或论述拆成递进、流程、层次、对比等逻辑图 | HTML / SVG |
| `mermaid-generator` | 文本、工作流、系统关系转 Mermaid 图 | Mermaid / Markdown |
| `space-image-studio` | 小红书封面、PPT 配图、图表、文章逻辑图的 GPT-image-2 总控工作室 | PNG |
| `space-article-batch-illustration` | GPT-image-2 / Gemini 文章批量配图，带中文图表提示词 | 多张 PNG + 更新后的文章 |
| `space-slide-deck` | Markdown / 长文生成整套幻灯片图片，并可导出 PPTX / PDF | 多张 PNG + PPTX / PDF |
| `wechat-official-account-layout` | 微信公众号文章排版，生成本地预览页和可复制富 HTML | HTML 预览页 |
| `canvas-design` | 海报、静态艺术、视觉作品的设计哲学与画布生成 | PNG / PDF / MD |
| `algorithmic-art` | p5.js 生成艺术、粒子、流场、交互参数探索 | HTML / JS / MD |
| `image-skill-builder` | 零代码创建自定义批量生图 Skill | 新 Skill 目录 |

## 使用方式

你可以用自然语言直接触发，也可以点名调用单个 Skill。

| 方式 | 示例 | 会触发什么 |
| --- | --- | --- |
| 内容 + 目标 | `把这篇文章配图`、`给这个观点做成信息图` | 自动判断封面、插图、信息图或逻辑图 |
| 图表类型 | `画一个架构图`、`做个用户旅程图`、`生成商业模式画布` | 调用图表类 Skill 输出 HTML / SVG / Mermaid |
| 平台图片 | `做小红书 6 页图`、`生成公众号封面`、`转成分享海报` | 按平台比例和阅读场景生成图片 |
| 品牌设计 | `设计 Logo`、`给这个产品做 10 个 Logo 方向` | 收集品牌信息并批量生成视觉方向 |
| GPT-image-2 工作室 | `用 image-studio 做封面`、`画一个高质感 SWOT 图片` | 调用 LabNana / GPT-image-2 生成高质量 PNG |
| 幻灯片生成 | `把这份 Markdown 做成 PPT`、`生成 12 页 deck` | 生成大纲、逐页图片，并合并 PPTX / PDF |
| 公众号排版 | `把这篇文章排成公众号`、`生成可复制 HTML` | 生成本地预览页，复制富 HTML 到公众号编辑器 |
| 故事分镜 | `把这个故事做成分镜`、`生成故事板` | 拆故事线、生成镜头表和连续图片 |
| 风格控制 | `用蓝图风`、`做成手绘感`、`更极简一点` | 调整 palette、rendering、layout、style 等参数 |
| 输出指定 | `输出 HTML`、`给我 PNG`、`保存到 Obsidian 图片目录` | 按目标格式和目录组织结果 |

## 工作原理

Design Buddy 不是一个单一画图脚本，而是一组视觉生产 Skill。

它把设计任务拆成四层：

| 层次 | 说明 |
| --- | --- |
| 内容理解 | 读取文章、需求、故事、产品逻辑或数据结构，判断真正要表达的信息 |
| 视觉决策 | 选择图像类型、图表结构、平台比例、风格系统和输出媒介 |
| 资产生成 | 调用图像模型、GPT-image-2、HTML/SVG 模板、Mermaid、p5.js、公众号排版模板或本地脚本生成结果 |
| 交付整理 | 保存图片、HTML、PDF、Markdown，必要时回写文章或生成批量文件 |

常见分支：

- 文章配图：先拆段落和观点，再决定每一处适合概念图、流程图、对比图还是场景图。
- 图表生成：先识别信息关系，再选择流程图、架构图、矩阵、旅程图、路线图等结构。
- 社交图片：先按平台阅读场景拆页，再控制封面钩子、信息密度、比例和留白。
- GPT-image-2 出图：先用类型规范和风格库约束提示词，再调用 LabNana / GPT-image-2 生成 PNG。
- 幻灯片生成：先生成大纲和逐页提示词，再批量生成幻灯片图片并合并为 PPTX / PDF。
- 公众号排版：先保留原文意义，再按 Claude / OpenAI / Google 风格生成可复制富 HTML。
- 品牌视觉：先抽取品牌属性，再批量探索 Logo、色彩和图形方向。
- 生成艺术：先建立视觉哲学，再通过代码表达可复现的生成系统。

## 适合谁

- 自媒体作者：做封面、配图、知识卡片、小红书多页图、公众号排版
- 产品经理：画流程图、用户旅程、路线图、商业模式画布
- 技术团队：画系统架构、部署拓扑、时序图、数据流图
- 独立开发者：做 Logo、落地页素材、产品说明图
- 课程创作者：把文稿变成课件图、摘要图、传播海报和整套幻灯片
- 设计协作者：把粗糙想法快速变成可讨论的视觉稿

## 风控与安全性说明

Design Buddy 的定位是视觉生产和内容可视化，不是素材搬运或版权规避工具。

- 原创优先：生成图像、图表和视觉风格应基于用户内容，不复制在世艺术家或现成品牌的受保护风格。
- 授权清晰：使用参考图、品牌素材、字体、Logo 或第三方图片前，应确认你拥有使用权。
- 凭据不入库：OpenAI、Google、DashScope、Gemini、LabNana 等 API Key 只放在环境变量或本地配置中，不提交到仓库。
- 本地配置保护：`.labnana.env`、`.env` 已加入忽略规则，仓库只保留 `.labnana.env.example` 模板。
- 本地文件谨慎处理：文章、客户 brief、未发布产品图和私有数据只在本机处理，分享报告前先脱敏。
- 商用前复核：Logo、封面、海报、信息图用于商业发布前，应人工检查版权、事实、人物肖像和品牌合规。
- 不伪造背书：不要生成暗示名人、机构、品牌授权或真实新闻事件的误导性素材。
- 标注 AI 参与：当平台、客户或团队规范要求披露 AI 生成内容时，应按规则标注。

## 诚实边界

每个设计工具都应该说明自己做不到什么。

- 它不是专业设计师的完整替代：能快速出方向，但最终品味、取舍和品牌一致性仍需要人判断。
- 图像模型可能不稳定：文字、手指、复杂结构、中文排版和细节一致性可能需要多轮修正。
- 图表不等于事实：如果输入逻辑有误，生成的图也会把错误画得更漂亮。
- Logo 不能自动保证可注册：商标近似、行业冲突和法律可用性需要单独检索。
- 平台比例不是万能模板：小红书、公众号、B站、课程封面都需要结合具体发布场景调整。
- 生成结果不自动拥有版权安全：商用前仍需检查训练模型、参考素材、字体和图形授权边界。

一个不告诉你边界在哪的设计工具，不值得信任。

## 参考

Design Buddy 汇集并整理了多个视觉生产 Skill，涵盖 AI 生图、文章配图、图表生成、品牌视觉、生成艺术和社交媒体图片工作流。

其中部分 Skill 使用 OpenAI、Google、DashScope、Gemini 等模型或服务，具体依赖以各目录的 `SKILL.md` 和 `scripts/` 为准。

## 许可证

MIT
