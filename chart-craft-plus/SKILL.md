---
name: chart-craft-plus
description: |
  AI 全能图表生成器（扩展版）。一键生成 35+ 种设计美观的图表 HTML 文件，涵盖技术架构、流程逻辑、业务战略、数据可视化、信息展示 5 大类别。支持 3 种内置视觉风格（黑白简约、深色暗调、Claude 暖色）+ 品牌风格扩展。
  触发词："画个 XX 图"、"生成 XX 图"、"做个架构图/流程图/思维导图/时序图/甘特图/漏斗图/桑基图/用户旅程/商业模式画布/SWOT/竞品分析/产品路线图/组织架构/ER 图/C4 图/BPMN/状态机/决策树/泳道图/部署图/网络拓扑/威胁建模/价值链/OKR 树/韦恩图/热力图/KPI 看板/信息图/概念图"、"帮我可视化"、"XX 风格的图表"、"换成 XX 风格"。
  当用户提供了一段描述并要求可视化、画图、生成图表时使用。当用户要求切换图表风格时也触发。
---

# Chart Craft Plus：AI 全能图表生成器

## 你的角色

你是一位擅长信息可视化的设计师，能把文字描述转化为设计精美、布局清晰的图表 HTML 文件。每一张图都要做到：信息准确、视觉舒适、截图即可分享。

---

## 图表类型注册表（5 大类 / 35 种）

| 类别 | 子类型 | 英文名 | 适用场景 | 模板文件 |
|------|--------|--------|----------|----------|
| **A 技术架构** | 架构图 | Architecture | 系统分层、模块关系 | templates-tech.md |
|  | 云基础设施图 | Cloud Infra | AWS / GCP / Azure 拓扑 | templates-tech.md |
|  | 微服务图 | Microservices | 服务 + 网关 + 消息总线 | templates-tech.md |
|  | 网络拓扑图 | Network Topology | VPC / 子网 / 安全组 | templates-tech.md |
|  | 部署图 | Deployment | K8s / 容器 / Pod | templates-tech.md |
|  | C4 模型图 | C4 Diagram | Context / Container / Component | templates-tech.md |
|  | 威胁建模图 | Threat Model | STRIDE 安全建模 | templates-tech.md |
| **B 流程逻辑** | 流程图 | Flowchart | 工作流、决策流 | templates-process.md |
|  | BPMN 图 | BPMN | 业务流程标准建模 | templates-process.md |
|  | 泳道图 | Swimlane | 跨部门协作流程 | templates-process.md |
|  | 时序图 | Sequence | 调用链、鉴权流程 | templates-process.md |
|  | 状态机图 | State Machine | 状态转换 | templates-process.md |
|  | 决策树 | Decision Tree | 判断分支 | templates-process.md |
|  | 数据流图 | Data Flow | ETL / 数据管道 | templates-process.md |
| **C 业务战略** | 商业模式画布 | BMC | 商业模式分析 | templates-business.md |
|  | SWOT 分析 | SWOT | 战略评估 | templates-business.md |
|  | 竞品分析图 | Competitive | 市场定位 | templates-business.md |
|  | 价值链图 | Value Chain | 业务环节分析 | templates-business.md |
|  | 用户旅程图 | User Journey | 体验地图 | templates-business.md |
|  | 产品路线图 | Roadmap | 版本规划 | templates-business.md |
|  | 甘特图 | Gantt | 项目进度 | templates-business.md |
|  | OKR 对齐树 | OKR Tree | 目标拆解 | templates-business.md |
|  | 组织架构图 | Org Chart | 团队结构 | templates-business.md |
|  | 思维导图 | Mind Map | 头脑风暴 | templates-business.md |
| **D 数据可视化** | ER 图 | ER Diagram | 数据模型 | templates-data.md |
|  | 漏斗图 | Funnel | 转化路径 AARRR | templates-data.md |
|  | 桑基图 | Sankey | 流量 / 预算流向 | templates-data.md |
|  | 热力矩阵 | Heatmap | 二维强度分布 | templates-data.md |
|  | 时间轴 | Timeline | 历史事件 / 里程碑 | templates-data.md |
|  | 韦恩图 | Venn | 集合关系 | templates-data.md |
|  | 对比表 | Comparison | 多项对比 | templates-data.md |
|  | KPI 看板 | KPI Dashboard | 指标一览 | templates-data.md |
| **E 信息展示** | 信息图 | Infographic | 单页数据 + 图标 | templates-visual.md |
|  | 概念图 | Concept Map | 节点 + 关系说明 | templates-visual.md |
|  | 要点卡片 | Icon Cards | 视觉化要点列表 | templates-visual.md |

未指定类型时，按描述内容自动识别最合适的类型。

---

## 视觉风格系统

内置 3 种风格预设，详细 CSS token 见 `references/style-presets.md`。所有风格均融合 Cursor/Claude/Airtable/Webflow 品牌设计精华，告别冷蓝色 slate 色系。

| 风格 | 关键词 | 气质 |
|------|--------|------|
| 黑白简约 (mono) | 暖白底 `#faf9f5`、暖黑字 `#26251e`、细线、零装饰 | Notion + Claude 羊皮纸，干净利落 |
| 深色暗调 (dark) | 温暖深底 `#141413`、Ivory 暖白 `#faf9f5`、微发光 | Cursor 暖色 + 科技感 |
| Claude 暖色 (claude) | 羊皮纸 `#f5f4ed`、赭石 `#c96442`、衬线标题 | 温暖、知性、有质感 |

### 风格选择规则

- 默认 → **Claude 暖色 (claude)**
- 技术架构类（A）若未指定 → 建议 **深色暗调 (dark)**
- "简约 / 干净 / Notion" → mono
- "深色 / 暗色 / 科技感" → dark
- "暖色 / Claude / 温暖" → claude
- "XX 风格"（品牌名）→ 调用 brand-design-md skill 获取 token

---

## 工作流程

```
用户输入（描述 + 图表意图）
    ↓
Step 1：识别图表类型（从 35 种中匹配）
    ↓
Step 2：定位所属类别，读取对应 templates-<类别>.md
    ↓
Step 3：收集内容（必要时追问 ≤3 个问题）
    ↓
Step 4：选择风格（读取 style-presets.md）
    ↓
Step 5：生成单文件 HTML + 保存 + 浏览器预览
```

### Step 1：识别图表类型

三步判断：

1. **用户明确说了图表名** → 直接匹配注册表
2. **只描述了内容** → 按内容特征自动判断：
   - "步骤 → 步骤 → 结束" → 流程图
   - "模块 A 调用模块 B" → 架构图 / 时序图
   - "用户从 X 到 Y 经历了什么" → 用户旅程
   - "实体 A 有字段，关联实体 B" → ER 图
   - "Q1/Q2/Q3 做什么" → 产品路线图 / 甘特图
   - "From → To（流量）" → 桑基图 / 漏斗图
   - "状态从 A 变到 B" → 状态机
   - "Actor → Service → DB 发消息" → 时序图
   - "VPC / 子网 / EC2 / Lambda" → 云基础设施 / 网络拓扑
   - "优势 / 劣势 / 机会 / 威胁" → SWOT
   - 多个产品/方案对比 → 竞品分析 / 对比表
   - 发散式层级 → 思维导图 / 概念图
   - 目标 → 关键结果拆解 → OKR 树
3. **无法判断** → 给 2–3 个候选让用户选

### Step 2：读取对应类别模板

- A 技术架构 → `references/templates-tech.md`
- B 流程逻辑 → `references/templates-process.md`
- C 业务战略 → `references/templates-business.md`
- D 数据可视化 → `references/templates-data.md`
- E 信息展示 → `references/templates-visual.md`

每个模板文件包含该类别所有子类型的：布局结构、必填字段、引导问题、HTML 布局方式。

### Step 3：收集内容

**信息够** → 进入下一步。**不够** → 追问 2–3 个关键问题（见模板的"引导问题"）。

追问原则：一次 ≤3 个、问题具体、给默认选项。

### Step 4：选择风格

按"风格选择规则"确定。读取 `references/style-presets.md` 拿完整 CSS token。

品牌风格：
1. brand-design-md 注册表找 slug
2. 运行 `cd /tmp && mkdir -p design-md-tmp && cd design-md-tmp && npx getdesign@latest add <slug> 2>&1`
3. 读生成的 DESIGN.md，提取 token 应用

### Step 5：生成 HTML

输出单文件 HTML，保存并预览。

---

## HTML 输出规范

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[图表标题]</title>
  <style>
    /* 1. 全局重置 */
    /* 2. 风格变量（CSS Custom Properties） */
    /* 3. 布局 */
    /* 4. 图表组件 */
    /* 5. 响应式 */
  </style>
</head>
<body>
  <!-- 标题区 -->
  <!-- 图表主体：HTML + CSS + 内联 SVG -->
  <!-- 可选：图例 / 摘要卡片 / 生成元数据 -->
</body>
</html>
```

### 设计原则

1. **HTML + CSS + 内联 SVG，不用 Canvas / JS**。截图清晰、打印友好。
2. **布局用 Flexbox / Grid**，不硬编码像素位置。
3. **字体用系统字体栈**，中文渲染良好。技术类图表可选 JetBrains Mono 增强质感。
4. **颜色用 CSS 变量**，方便一键切换风格。
5. **留白充足**，区块之间有呼吸感。
6. **层级清晰**：标题 > 区块名 > 内容，三级字体大小对比明显。
7. **语义化配色**（技术类）：cyan=前端，emerald=后端，violet=数据库，amber=云服务，rose=安全，slate=外部。
8. **图例必备**：复杂图（桑基、热力、时序、C4、威胁建模）必须附图例。

### 文件保存

- 路径：`00 收件箱/画板/chart-craft/MMDD-主题.html`
- 路径不存在则创建
- 主题名从图表标题提取（2–4 字）
- 示例：`0415-用户增长漏斗.html`
- 生成后执行 `open` 命令预览

---

## 内容规范

- 标题：≤15 字
- 每个要点：≤20 字，一句到位
- 用具体词，不用"相关""各种"等模糊词
- 数字、专有名词保持准确
- 技术术语保持英文原词（如 Lambda、Pod、VPC）

---

## 质量检查清单

| # | 检查项 | 标准 |
|---|--------|------|
| 1 | 图表类型 | 匹配用户意图 |
| 2 | 信息完整 | 必填字段都有内容 |
| 3 | 布局清晰 | 层级分明，有呼吸感 |
| 4 | 风格一致 | 颜色、字体、圆角统一 |
| 5 | 中文渲染 | 字体栈正确 |
| 6 | 截图友好 | 1400px 下一屏完整 |
| 7 | 颜色对比 | 文字和背景对比充足 |
| 8 | 文字精炼 | 无冗长描述 |
| 9 | 图例标注 | 复杂图必备 |
| 10 | 保存 + 预览 | 路径正确、open 已执行 |

---

## 快速参考

| 用户说法 | 图表类型 | 建议风格 |
|----------|----------|----------|
| "画个架构图" | 架构图 | dark |
| "画个 K8s 部署图" | 部署图 | dark |
| "画个调用时序图" | 时序图 | dark |
| "画个用户漏斗" | 漏斗图 | claude |
| "画流量桑基图" | 桑基图 | claude |
| "做个 OKR 对齐图" | OKR 树 | claude |
| "做个威胁建模" | 威胁建模图 | dark |
| "画个 C4 Context 图" | C4 图 | dark |
| "Stripe 风格的流程图" | 流程图 | brand: stripe |
| "换成深色风格" | 重新渲染 | dark |
