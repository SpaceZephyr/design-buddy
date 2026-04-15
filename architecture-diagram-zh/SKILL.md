---
name: architecture-diagram-zh
description: 创建专业、支持深色/浅色双主题切换的系统架构图，输出为独立的 HTML 文件（内含 SVG 图形）。当用户需要系统架构图、基础设施拓扑图、云架构可视化、安全架构图、网络拓扑图，或任何展示系统组件及其关系的技术图表时使用此技能。支持中文标注和说明，内置主题切换按钮。
license: MIT
metadata:
  version: "2.1"
  author: Architecture Diagram Skill (中文版)
---

# 架构图生成技能

创建专业的技术架构图，输出为独立的 HTML 文件，包含内联 SVG 图形和 CSS 样式。

## 触发条件

当用户提到以下任何场景时，主动使用此技能：
- "画一个架构图" / "生成架构图" / "画个图"
- "系统架构" / "部署架构" / "技术架构"
- "画一个流程图" / "组件关系图" / "拓扑图"
- "infrastructure diagram" / "architecture diagram"
- 用户粘贴了代码并要求分析架构
- 用户描述了系统组件和它们之间的关系

## 工作流程

### 第一步：收集信息

如果用户没有提供完整的架构描述，主动询问以下信息：
- 系统包含哪些主要组件/服务？
- 组件之间的连接关系和数据流？
- 使用了哪些技术栈和云服务？
- 是否有安全组、网络分区等边界？

如果用户提供了代码库或项目文件，自行分析提取架构信息。

### 第二步：生成架构图

根据收集到的信息，使用本技能的设计规范和模板生成 HTML 文件。

### 第三步：输出结果

输出一个完整的、可直接在浏览器中打开的 `.html` 文件。

## 设计系统

### 主题系统

架构图支持 **深色（Dark）** 和 **浅色（Light）** 两种主题，通过页眉右侧的切换按钮一键切换。用户选择会保存到 localStorage，下次打开自动恢复。

**实现方式：** CSS 自定义属性 + `data-theme` 属性切换。SVG 元素通过 CSS class（`text-primary`、`text-secondary`、`mask-bg`、`grid-line`、`arrowhead-color`）适配主题。

**关键原则：**
- 组件描边色（青/绿/紫/琥珀/玫红/橙）在两种主题下保持不变，确保视觉一致性
- 仅切换背景、文字、网格、边框等基础色
- 使用 CSS `transition` 实现平滑切换动画

#### 深色主题（默认）

融合 Cursor 暖色深底 + Claude 暖白文字。温暖不冰冷，告别冷蓝色 slate。

| 元素 | 颜色 |
|------|------|
| 页面背景 | `#141413` (温暖近黑) |
| 卡片背景 | `rgba(20, 20, 19, 0.5)` |
| 遮罩背景 | `#1a1a18` (暖深色) |
| 边框 | `rgba(38, 37, 30, 0.2)` (oklab 暖边框) |
| 主文字 | `#faf9f5` (Ivory 暖白) |
| 副文字 | `#b0aea5` (暖银) |
| 网格线 | `rgba(38, 37, 30, 0.12)` |
| 箭头头 | `rgba(38, 37, 30, 0.45)` |

#### 浅色主题

融合 Claude 羊皮纸 `#f5f4ed` + Airtable 深海军蓝文字。

| 元素 | 颜色 |
|------|------|
| 页面背景 | `#f5f4ed` (羊皮纸) |
| 卡片背景 | `rgba(250, 249, 245, 0.85)` |
| 遮罩背景 | `#faf9f5` (Ivory) |
| 边框 | `#f0eee6` (暖奶油) |
| 主文字 | `#141413` (暖近黑) |
| 副文字 | `#5e5d59` (橄榄灰) |
| 网格线 | `#f0eee6` (暖奶油) |
| 箭头头 | `#87867f` (石灰) |

### 组件配色方案

按组件类型使用语义化颜色：

| 组件类型 | 填充色 (rgba) | 描边色 | 典型用途 |
|---------|-------------|--------|---------|
| 前端 | `rgba(20, 50, 62, 0.4)` | `#22d3ee` (青色) | 客户端应用、UI、浏览器 |
| 后端 | `rgba(18, 72, 55, 0.4)` | `#34d399` (翡翠绿) | 服务器、API、微服务 |
| 数据库 | `rgba(72, 30, 100, 0.4)` | `#a78bfa` (紫色) | 数据库、存储、缓存 |
| 云服务 | `rgba(110, 50, 18, 0.35)` | `#fbbf24` (琥珀色) | AWS/阿里云/腾讯云服务 |
| 安全组件 | `rgba(130, 25, 50, 0.4)` | `#fb7185` (玫红色) | 认证、安全组、加密 |
| 消息队列 | `rgba(251, 146, 60, 0.3)` | `#fb923c` (橙色) | Kafka、RabbitMQ、事件总线 |
| 外部/通用 | `rgba(38, 37, 30, 0.35)` | `#94a3b8` (石板灰) | 外部系统、第三方服务 |
| AI/智能 | `rgba(80, 30, 120, 0.4)` | `#c084fc` (亮紫) | AI 服务、LLM、模型 |

### 字体规范

所有文字使用 JetBrains Mono 等宽字体（技术风格）：
```html
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
```

排版规范（参考 Cursor 紧凑间距 + Claude 宽松行高）：
- 标题：`letter-spacing: -0.02em`, `line-height: 1.6`
- 副标题：`letter-spacing: 0.04em`
- 字体大小：12px 组件名称，9px 子标签，8px 注释文字，7px 极小标签

### 视觉元素

**背景：** 深色模式 `#141413` (温暖近黑) / 浅色模式 `#f5f4ed` (羊皮纸)，带微妙网格纹理：
```svg
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M 40 0 L 0 0 0 40" fill="none" class="grid-line" stroke-width="0.5"/>
</pattern>
```

**组件方框：** 圆角矩形（`rx="8"`），1.5px 描边，半透明填充。

**阴影系统（Claude ring shadow + Cursor ambient）：**
- 深色模式：`rgba(0,0,0,0.14) 0px 4px 16px, rgba(38,37,30,0.1) 0px 0px 0px 1px`
- 浅色模式：`rgba(0,0,0,0.05) 0px 4px 24px, rgba(38,37,30,0.08) 0px 0px 0px 1px`

**圆角体系：**
- 组件方框：`8px`（Cursor 标准）
- 卡片/图表容器：`12px`（Airtable 按钮 / Claude 舒适圆角）
- 标签徽章：`6px`（Webflow 紧凑）

**安全组：** 虚线描边（`stroke-dasharray="4,4"`），透明填充，玫红色。

**区域边界：** 大虚线描边（`stroke-dasharray="8,4"`），琥珀色，`rx="12"`。

**箭头：** 使用 SVG marker 定义箭头头部：
```svg
<marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
  <polygon points="0 0, 10 3.5, 0 7" class="arrowhead-color" />
</marker>
```

**箭头层级（Z-order）：** 连接箭头要在 SVG 中较早绘制（背景网格之后），这样它们会渲染在组件方框之下。SVG 元素按文档顺序绘制。

**透明填充遮罩技巧：** 组件方框使用半透明填充，箭头在后面会透出来。为了完全遮住箭头，在半透明样式矩形之前绘制一个不透明背景矩形。使用 `class="mask-bg"` 以适配主题：
```svg
<!-- 不透明背景遮盖箭头（自动适配主题） -->
<rect x="X" y="Y" width="W" height="H" rx="6" class="mask-bg"/>
<!-- 半透明样式组件叠加在上面 -->
<rect x="X" y="Y" width="W" height="H" rx="6" fill="rgba(76, 29, 149, 0.4)" stroke="#a78bfa" stroke-width="1.5"/>
```

**认证/安全流：** 玫红色虚线（`#fb7185`）。

**消息队列/事件总线：** 组件间的小型连接元素，橙色（`#fb923c` 描边，`rgba(251, 146, 60, 0.3)` 填充）：
```svg
<rect x="X" y="Y" width="120" height="20" rx="4" fill="rgba(251, 146, 60, 0.3)" stroke="#fb923c" stroke-width="1"/>
<text x="CENTER_X" y="Y+14" fill="#fb923c" font-size="7" text-anchor="middle">Kafka / RabbitMQ</text>
```

### 间距规则

**关键：** 垂直堆叠组件时确保间距正确，避免重叠：

- **标准组件高度：** 服务 60px，较大组件 80-120px
- **组件间最小垂直间距：** 40px
- **内联连接器（消息队列）：** 放在组件间的间隙中，不要重叠

**示例布局：**
```
组件 A: y=70,  height=60  → 结束于 y=130
间隙:    y=130 到 y=170   → 40px 间隙，消息队列放 y=140 (20px 高)
组件 B: y=170, height=60  → 结束于 y=230
```

### 图例放置

**关键：** 图例必须放在所有边界框（区域边界、集群边界、安全组）之外。

- 计算所有边界结束的位置（y 坐标 + 高度）
- 图例至少放在最低边界下方 20px 处
- 如需要则扩展 SVG viewBox 高度

### 页面布局结构

1. **页眉** - 项目标题（带脉冲指示灯动画）、副标题
2. **主 SVG 架构图** - 包含在圆角边框卡片中
3. **信息摘要卡片** - 图表下方的 3 张卡片网格，展示关键架构细节
4. **页脚** - 最小化元数据行

### 组件方框模板

```svg
<!-- 带主题适配的完整组件方框 -->
<rect x="X" y="Y" width="W" height="H" rx="6" class="mask-bg"/>
<rect x="X" y="Y" width="W" height="H" rx="6" fill="FILL_COLOR" stroke="STROKE_COLOR" stroke-width="1.5"/>
<text x="CENTER_X" y="Y+20" class="text-primary" font-size="11" font-weight="600" text-anchor="middle">组件名称</text>
<text x="CENTER_X" y="Y+36" class="text-secondary" font-size="9" text-anchor="middle">技术说明</text>
```

**关键：** 使用 CSS class 而非硬编码颜色值，以支持主题切换：
- `class="mask-bg"` - 不透明遮罩背景（深色: `#1a1a18`，浅色: `#faf9f5`）
- `class="text-primary"` - 主文字（深色: `#faf9f5`，浅色: `#141413`）
- `class="text-secondary"` - 副文字（深色: `#b0aea5`，浅色: `#5e5d59`）
- `class="grid-line"` - 网格线描边
- `class="arrowhead-color"` - 箭头头部填充
- 组件描边色和彩色标签（如 `fill="#22d3ee"`）**不使用 class**，在两种主题下保持不变

### 信息摘要卡片模板

```html
<div class="card">
  <div class="card-header">
    <div class="card-dot COLOR"></div>
    <h3>卡片标题</h3>
  </div>
  <ul>
    <li>- 要点一</li>
    <li>- 要点二</li>
  </ul>
</div>
```

## 中文适配规则

### 文本排版
- 所有组件标签、注释、卡片内容使用中文
- 技术专有名词保留英文（如 PostgreSQL、Kubernetes、OAuth 2.0）
- 混合排版时，中文字符之间无空格，中英文之间加空格

### 文字宽度
- 中文字符宽度约为英文的 2 倍，组件方框宽度需相应增加
- 标准中文标签组件宽度建议：140-180px（英文为 110-140px）
- 使用 `text-anchor="middle"` 居中对齐

### 图表标题
- 页眉标题格式："【项目名】系统架构" 或 "【项目名】部署架构"
- 副标题简要说明系统类型和关键特征

### 信息卡片
- 三张卡片分别展示：
  1. 技术栈概要（核心技术选型）
  2. 关键设计决策（架构特点）
  3. 安全与运维要点（安全、监控等）

## 使用模板

复制并自定义 `assets/template.html` 模板。关键自定义点：

1. 更新 `<title>` 和页眉文字
2. 根据需要调整 SVG viewBox 尺寸（默认：`1000 x 680`）
3. 添加/删除/重新定位组件方框
4. 绘制组件间的连接箭头
5. 更新三张摘要卡片
6. 更新页脚元数据

## 输出要求

始终生成一个独立的 `.html` 文件，包含：
- 内嵌 CSS（除 Google Fonts 外无外部样式表）
- CSS 自定义属性定义双主题（深色/浅色）
- 内联 SVG（无外部图片），SVG 文字使用 CSS class 适配主题
- 少量 JavaScript 用于主题切换和 localStorage 持久化
- 页眉右侧包含太阳/月亮图标切换按钮
- 文件可直接在任何现代浏览器中打开

## 常见架构类型参考

### Web 应用架构
前端框架 + 后端 API + 数据库 + 缓存 + 认证

### 微服务架构
API 网关 + 多个微服务 + 消息队列 + 服务注册发现 + 分布式数据库

### 云原生架构
CDN + 负载均衡 + 容器编排 + 云数据库 + 对象存储 + 监控

### Serverless 架构
API 网关 + 函数计算 + 云数据库 + 对象存储 + 消息队列

### 数据流架构
数据源 + 数据采集 + 流处理 + 数据仓库 + 可视化
