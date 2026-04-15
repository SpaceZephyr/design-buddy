# A 类：技术架构类模板

涵盖：架构图、云基础设施图、微服务图、网络拓扑图、部署图、C4 图、威胁建模图。

**通用语义色**：cyan=前端，emerald=后端/服务，violet=数据库/存储，amber=云服务/队列，rose=安全/鉴权，slate=外部依赖。

---

## 1 架构图 (Architecture)

### 布局结构

分层横向排列：前端层 → 服务层 → 数据层 → 外部服务层。每层一个圆角矩形容器，内部用 Flexbox 横排模块卡片。

### 必填字段

- 系统名称
- 至少 2 个层级
- 每层的模块/组件
- 层与层之间的连接关系

### 引导问题

- 系统分几层？（前端/后端/数据/第三方）
- 每层有哪些模块？
- 模块间通信方式？HTTP / MQ / 直接调用？

### HTML 布局方式

纵向 Flexbox 排列每层。层内模块横向 Flexbox。层间用 SVG 箭头或 CSS 伪元素画竖线。

---

## 2 云基础设施图 (Cloud Infra)

### 布局结构

外层 VPC/Region 大框 → 内嵌 AZ/子网框 → 最内层放资源图标卡（EC2/Lambda/RDS/S3）。右侧或底部单独列外部服务（CDN、第三方 API）。

### 必填字段

- 云厂商（AWS/GCP/Azure）
- Region / 可用区划分
- 核心资源清单及所在子网
- 入口（LB、API Gateway）和出口（NAT、Internet Gateway）

### 引导问题

- 部署在哪个云？
- 有几个 Region / AZ？
- 主要资源是什么？（Lambda、EC2、RDS、S3 等）
- 流量入口走哪里？

### HTML 布局方式

嵌套 div 表示 VPC → 子网 → 资源。资源卡带厂商 logo 色边框（AWS=amber，GCP=cyan，Azure=blue）。用虚线框标示安全边界。

---

## 3 微服务图 (Microservices)

### 布局结构

顶部：API Gateway / BFF；中部：服务网格（多个服务卡横向或网格排列）；底部：消息总线（Kafka/RabbitMQ）+ 数据存储。服务间用箭头表示同步调用，虚线表示异步消息。

### 必填字段

- 至少 3 个微服务
- 服务负责的业务域
- 服务间调用关系（同步/异步）
- 共享基础设施（消息队列、服务注册中心、配置中心）

### 引导问题

- 有哪些微服务？各自负责什么？
- 哪些是同步 HTTP/gRPC 调用？哪些是异步事件？
- 用了什么消息中间件？

### HTML 布局方式

Grid 三层布局（网关 / 服务群 / 基础设施）。服务卡片用 emerald 边框，事件总线用 amber 横条贯穿底部。

---

## 4 网络拓扑图 (Network Topology)

### 布局结构

左→右表示南北向流量：Internet → WAF/CDN → LB → Public Subnet → Private Subnet → Data Subnet。每层用不同底色。安全组用虚线框标注。

### 必填字段

- 公网入口（域名、WAF、LB）
- 子网划分（Public / Private / DB）
- 关键主机/实例
- 安全组 / ACL 规则要点

### 引导问题

- 用户流量怎么进来？过了哪些网关？
- 子网怎么划？
- 哪些端口对哪些源开放？

### HTML 布局方式

横向 Grid 6–7 列，每列一个网络区域。服务器用小圆角卡片堆叠在列内。安全组用带标签的虚线矩形覆盖多列。

---

## 5 部署图 (Deployment / K8s)

### 布局结构

Cluster 大框 → Namespace 子框 → Deployment/Pod 卡片（带副本数标注）→ Service/Ingress 连接线。底部放 ConfigMap / Secret / PVC。

### 必填字段

- Cluster 名称
- Namespace 划分
- Deployment / Pod 及副本数
- Service 暴露方式（ClusterIP / NodePort / Ingress）

### 引导问题

- 几个 Namespace？各自部署什么？
- 每个 Deployment 有几个副本？
- 对外怎么暴露？Ingress 路由规则？

### HTML 布局方式

双层嵌套 div（Cluster > Namespace）。Pod 用小方块 Grid 排列，副本数用角标。Ingress 用顶部横条带路径箭头指向对应 Service。

---

## 6 C4 模型图 (C4 Diagram)

### 布局结构

按 C4 四层分别绘制一张，常用前两层：

- **L1 Context**：系统（中央方块）+ 人物（人形图标）+ 外部系统（灰色方块），用带标签的箭头连接。
- **L2 Container**：系统内部的容器（Web App / API / DB / Mobile）用色块区分，连线标注协议。
- L3 Component / L4 Code：按需选用。

### 必填字段

- 系统名称
- 用户角色（至少 1 个）
- 相邻外部系统（至少 1 个）
- L2：容器列表及技术栈（React / Spring / PostgreSQL）

### 引导问题

- 这个系统叫什么？给谁用？
- 它依赖哪些外部系统？
- （L2）内部拆成哪几个容器？各自用什么技术？

### HTML 布局方式

L1：中央主系统大卡 + 四周人物/外部系统小卡，SVG 连线带中文标签。L2：Grid 网格，容器卡片带"[技术栈]"标签行。**必须附图例**说明人物/系统/容器的形状语义。

---

## 7 威胁建模图 (Threat Model, STRIDE)

### 布局结构

左侧画系统数据流图（用户 → Web → API → DB），中间用红色菱形标注 Trust Boundary。右侧是 STRIDE 威胁清单表格。

### 必填字段

- 数据流路径（至少 3 个节点）
- 至少 1 条 Trust Boundary
- 每个威胁类型（S/T/R/I/D/E）的具体风险描述
- 对应缓解措施

### 引导问题

- 数据从哪到哪流？
- 信任边界在哪（从外网到内网？跨服务？）
- 每个阶段最担心什么攻击？

### HTML 布局方式

左 60%：数据流节点 + 箭头 + 红虚线 Trust Boundary。右 40%：6 行 STRIDE 表格（威胁名 / 场景 / 缓解）。**必须附图例**：节点形状、边界样式、威胁标号。
