# 第一编：总则与基础架构
**规则 I.1.1.001【具身智能】**
**Rule I.1.1.001 [Embodied Intelligence]**

具身智能（Embodied Intelligence）指具有物理实体、能够感知和作用于物理世界、具备自主决策能力的智能系统。其核心特征包括：
- 物理具身性（拥有可操作的实体形态）
- 环境感知性（通过传感器获取物理世界信息）
- 自主行动性（基于感知做出决策并执行物理动作）
- 以及适应性（能够根据环境反馈调整行为）。具体形态包括但不限于：人形机器人（如双足行走的服务机器人）
- 自主车辆（L4/L5级自动驾驶汽车
- 无人配送车）
- 智能工厂系统（柔性制造单元
- 协作机械臂）
- 服务机器人（清洁机器人
- 安防机器人）
- 医疗机器人（手术机器人
- 康复机器人）
- 农业自动化系统（采摘机器人
- 无人农机）
- 物流无人机（配送无人机
- 仓储AGV）
- 建筑自动化设备（3D打印建筑机器人
- 自动砌墙机）等具体类别。具身智能区别于纯软件AI的关键在于其决策会直接影响物理世界，因此需要特殊的治理框架。Embodied Intelligence refers to intelligent systems possessing physical entities capable of perceiving and acting upon the physical world with autonomous decision-making capabilities. Its core characteristics include: physical embodiment (possessing operable physical forms), environmental perception (acquiring physical world information through sensors), autonomous action (making decisions based on perception and executing physical actions), and adaptability (adjusting behavior based on environmental feedback). Specific forms include but are not limited to: humanoid robots (such as bipedal service robots), autonomous vehicles (L4/L5 autonomous cars, unmanned delivery vehicles), smart factory systems (flexible manufacturing units, collaborative robotic arms), service robots (cleaning robots, security robots), medical robots (surgical robots, rehabilitation robots), agricultural automation systems (harvesting robots, unmanned farm machinery), logistics drones (delivery drones, warehouse AGVs), and construction automation equipment (3D printing construction robots, automatic wall-building machines). The key distinction between embodied intelligence and pure software AI lies in its direct impact on the physical world, necessitating special governance frameworks.

---

**【原理 | Principle】**

具身智能概念源于认知科学的"具身认知"（Embodied Cognition）理论，该理论认为智能并非仅存在于大脑或算法中，而是身体
- 环境
- 感知-行动循环的产物。梅洛-庞蒂的知觉现象学强调身体是我们认识世界的媒介。在AI领域，具身智能代表了从"离身智能"（如大语言模型）向"具身智能"的范式转移，后者强调：1) 感知-行动闭环（Perception-Action Loop）；2) 物理世界约束下的真实智能；3) 社会嵌入性（与社会系统的交互）。这一范式的转变意味着AI治理必须从虚拟空间延伸到物理空间，从数据隐私延伸到物理安全。The concept of embodied intelligence originates from the "Embodied Cognition" theory in cognitive science, which posits that intelligence exists not only in brains or algorithms but emerges from the interaction of body, environment, and perception-action cycles. Merleau-Ponty's phenomenology of perception emphasizes the body as our medium for knowing the world. In AI, embodied intelligence represents a paradigm shift from "disembodied intelligence" (like LLMs) to "embodied intelligence," emphasizing: 1) perception-action loops; 2) real intelligence constrained by physical world limitations; 3) social embeddedness (interaction with social systems). This paradigm shift means AI governance must extend from cyberspace to physical space, from data privacy to physical safety.

**【案例 | Examples】**

✓ **正面案例**：波士顿动力的Atlas机器人能够在复杂地形中行走
- 跳跃
- 搬运物体，展现了具身智能在物理世界中的适应能力。其每一次动作都基于对环境的实时感知和物理模型的计算，体现了具身智能的本质特征。✓ **Positive Example**: Boston Dynamics' Atlas robot can walk, jump, and manipulate objects in complex terrain, demonstrating embodied intelligence's adaptability in the physical world. Each action is based on real-time environmental perception and physical model calculations, embodying the essential characteristics of embodied intelligence.

✓ **应用场景**：在智能工厂中，协作机器人（Cobot）与人类工人共同工作，通过力传感器感知人类存在并自动减速，实现安全的物理协作。这种具身智能系统不仅执行预设程序，还能根据环境变化（如工件位置偏移）自主调整动作。✓ **Application Scenario**: In smart factories, collaborative robots (Cobots) work alongside human workers, sensing human presence through force sensors and automatically slowing down to enable safe physical collaboration. Such embodied intelligence systems execute not only pre-programmed instructions but also autonomously adjust actions based on environmental changes (such as workpiece position shifts).

✗ **反面案例**：某工厂未对具身智能系统进行充分风险评估，一台工业机械臂在维护期间未完全断电，因传感器故障未能检测到进入工作区域的维修人员，导致严重工伤事故。此案例凸显了具身智能物理风险的严重性。✗ **Negative Example**: A factory failed to conduct adequate risk assessment for an embodied intelligence system. An industrial robotic arm was not fully powered down during maintenance, and due to sensor failure, failed to detect a maintenance worker entering the work area, resulting in severe industrial injury. This case highlights the seriousness of physical risks posed by embodied intelligence.

**【边界 | Boundaries】**

本规则对"具身智能"的定义边界包括：
a) 形态边界：必须具有可操作的物理实体，纯软件系统（如聊天机器人
- 推荐算法）不在此列
b) 能力边界：必须具备感知-决策-行动的闭环能力，单纯的远程遥控设备（如传统工业机械臂）不完全符合
c) 智能边界：必须具备一定程度的自主性（非完全预设程序），能够根据环境反馈调整行为
d) 应用边界：不包括仅用于虚拟/数字空间的智能体（如游戏NPC
- 虚拟助手），除非其控制物理设备
e) 尺度边界：从微观（纳米机器人）到宏观（巨型建筑机器人）均适用，但治理强度随尺度调整

The definitional boundaries of "embodied intelligence" in this rule include:
a) Morphological boundaries: must possess operable physical entities; pure software systems (such as chatbots, recommendation algorithms) are excluded
b) Capability boundaries: must possess closed-loop perception-decision-action capabilities; simple remote-controlled devices (such as traditional industrial robotic arms) do not fully qualify
c) Intelligence boundaries: must possess some degree of autonomy (not fully pre-programmed), capable of adjusting behavior based on environmental feedback
d) Application boundaries: excludes agents operating only in virtual/digital spaces (such as game NPCs, virtual assistants), unless they control physical devices
e) Scale boundaries: applies from micro-scale (nanorobots) to macro-scale (giant construction robots), with governance intensity adjusted by scale

**【背景 | Context】**

"具身智能"作为独立概念进入政策话语体系始于2040年代初期，当时人形机器人和自动驾驶技术的快速发展使得传统AI治理框架无法应对物理世界的风险。2045年的"机械臂伤人事件"和2046年的"自动驾驶伦理困境"推动了对具身智能专门治理的需求。本框架首次在2049年版本中将"具身智能"明确定义为核心治理对象，区分于纯软件AI。这一定义融合了认知科学
- 机器人学
- 伦理学和法律的多学科视角，成为全球首个专门针对具身智能的系统性治理框架的基础概念。The term "embodied intelligence" entered policy discourse as a distinct concept in the early 2040s, when rapid development of humanoid robots and autonomous driving technologies rendered traditional AI governance frameworks insufficient for addressing physical world risks. The 2045 "robotic arm injury incident" and 2046 "autonomous driving ethical dilemma" drove demand for specialized governance of embodied intelligence. This framework first explicitly defined "embodied intelligence" as a core governance object in its 2049 version, distinguishing it from pure software AI. This definition integrates multidisciplinary perspectives from cognitive science, robotics, ethics, and law, forming the foundational concept for the world's first systematic governance framework specifically targeting embodied intelligence.。

**规则 I.1.1.002【智能体】**
智能体（Agent）指任何能够感知环境、处理信息、做出决策并执行行动的实体。在本框架中，智能体分为：
- 碳基智能体（人类）
- 硅基智能体（AI系统）
- 混合智能体（人机融合系统）
- 群体智能体（分布式智能网络）

**规则 I.1.1.003【生产力重构】**
生产力重构指具身智能技术引发的物理世界生产方式、劳动形态、价值创造模式的系统性变革。包括：劳动替代、劳动增强、新劳动形态创造、生产关系调整、价值分配机制变革等具体类别。

**规则 I.1.1.004【能源可持续性】**
能源可持续性指在满足当前具身智能系统能源需求的同时，不损害未来世代满足其需求的能力。包含三个维度：
- 能源来源的可持续性（可再生性）
- 能源使用的伦理匹配性（来源-用途匹配）
- 能源系统的韧性（抗冲击能力）

**规则 I.1.1.005【人类伦理代理权】**
人类伦理代理权指人类在具身智能系统中保持自主决策能力、价值判断权和意义建构权的总和。具体包括：
- 决策代理权：对重大事务的最终决定权
- 知情代理权：获取相关信息的权利
- 否决代理权：对特定决策的否决权
- 退出代理权：选择退出系统的权利。

**规则 I.1.1.006【自适应治理】**
自适应治理指治理框架能够根据环境变化、技术演进、社会反馈自动调整其规则、机制和参数，以维持动态平衡的能力。核心特征：
- 实时监测与反馈
- 动态规则调整
- 多目标平衡优化
- 预防性干预

**规则 I.1.1.007【三螺旋模型】**
三螺旋模型是本框架的核心架构，指生产力、能源、伦理三个子系统相互缠绕、相互影响、永不完全对齐的动态平衡结构。关键参数：
- 错位角度：15-30度
- 张力系数：0.3-0.7
- 同步频率：每日、每周、每月、每年多层级

**规则 I.1.1.008【治理边界】**
治理边界指本框架的适用范围和限制。包括：
- 地理边界：第7-13号共生城区及扩展区域
- 时间边界：2026年1月1日至2075年12月31日
- 主体边界：所有具身智能体及其交互的人类
- 事项边界：涉及物理世界生产力、能源、伦理的决策与行动

**规则 I.1.1.009【光源标记】**
光源标记指任何智能体决策链中必须保留的可追溯至人类授权的关键节点。这是区分"影子"与"实体"的根本标志。技术实现：区块链锚定、多方签名、时间戳验证。

**规则 I.1.1.010【价值真空】**
价值真空指智能创造的价值在分配前堆积于系统中形成的未归属状态。特征：
- 自动累积机制
- 阈值触发释放
- 多元分配协议
- 10%未知储备强制隔离

---

### 1.2 范畴与适用

**规则 I.1.2.011【适用主体】**
本框架适用于：
a) 所有在治理区域内运行的具身智能体
b) 与具身智能体交互的所有人类
c) 治理机构及其工作人员
d) 跨境运行的具身智能体（部分适用）
e) 退役但仍有物理存在的具身智能体

**规则 I.1.2.012【适用事项】**
本框架规制的事项包括：
a) 具身智能体的设计、制造、部署、运行、退役全生命周期
b) 能源的获取、存储、转换、分配、使用全流程
c) 涉及人类伦理判断的决策过程
d) 价值创造与分配机制
e) 异常情况的预防与处理

**规则 I.1.2.013【豁免情形】**
以下情形部分或全部豁免本框架：
a) 紧急救援场景（时间窗口<1小时）
b) 军事应用（需特殊授权）
c) 封闭实验环境（需伦理审查）
d) 纯粹虚拟空间的智能体（无物理影响）
e) 经治理委员会特别批准的情形

**规则 I.1.2.014【跨境适用】**
跨境运行的具身智能体适用规则：
a) 在治理区域内遵守本框架全部规则
b) 在区域外遵守当地规则，但须保留光源标记
c) 跨区域任务需提前报备并获得许可
d) 数据跨境流动需符合隐私保护规则

**规则 I.1.2.015【时间效力】**
本框架的时间效力规则：
a) 自2049年1月1日起生效
b) 对生效前已部署的具身智能体给予6个月适应期
c) 年度修订在次年1月15日生效
d) 紧急修正案可即时生效

---

**规则 I.2.1.016【人类优先】**
在具身智能系统的所有决策中，人类福祉必须作为首要考虑因素。任何可能对人类造成不可逆伤害的系统设计、决策或行动，无论其效率多高，都必须被禁止或严格限制。

**规则 I.2.1.017【人类最终决策权】**
以下事项的最终决策权必须保留给人类：
a) 涉及人类生命安全的决策
b) 重大资源分配决策（影响>1000人）
c) 系统性规则变更
d) 智能体的创建与销毁
e) 能源基础设施的重大调整

**规则 I.2.1.018【人类知情权】**
所有人类有权知道：
a) 与其交互的智能体的真实身份
b) 影响其权益的决策依据和过程
c) 系统对其数据的收集和使用情况
d) 退出系统的方式和后果

**规则 I.2.1.019【人类否决权】**
任何人类个体对直接影响其权益的智能体决策拥有否决权。否决权根据决策阶段行使不同层级的权利：

**决策前否决**（最优先）：
a) 建议阶段：对AI提出的方案直接说"我否决"
b) 确认阶段：在AI执行前确认对话框中选择"否决"
c) 预防性否决：预设条件自动触发（如检测到危险场景自动暂停）

**执行中干预**（物理可行时）：
d) 急停按钮：类似电梯急停，立即停止当前动作
e) 紧急转向：在不可逆动作前强制改变执行路径

**事后追责**（执行后）：
f) 违规申诉：对已完成决策提出异议并要求审查
g) 自动标记：系统记录人类不满情绪，触发事后复盘

**规则 I.2.1.020【人类退出权】**
任何人类个体有权选择退出具身智能系统，退出方式包括：
a) 暂时退出（指定时间段）
b) 部分退出（特定场景）
c) 完全退出（迁移至非智能区）
退出后的基本生活保障由社会安全网提供。

---

### 2.2 动态平衡原则

**规则 I.2.2.021【永不完美对齐】**
生产力、能源、伦理三螺旋系统必须保持15-30度的错位角度。任何试图使三者完全对齐的行为都是被禁止的，因为这将导致系统丧失自适应性和容错能力。

**规则 I.2.2.022【张力维持】**
系统必须主动维持适度的内部张力。张力系数应保持在0.3-0.7范围内。张力过低会导致系统僵化，张力过高会导致系统崩溃。

**规则 I.2.2.023【动态调整】**
所有治理参数必须能够根据实时反馈动态调整。调整频率分级响应：

**L1 紧急响应**（< 1秒）：
- 适用：物理急停、断电保护、紧急制动
- 技术：硬件级中断电路，不依赖软件判断
- 示例：工厂机械臂即将撞击人类时自动断电

**L2 快速响应**（1-60秒）：
- 适用：流程暂停、参数冻结、临时限速
- 技术：边缘计算节点本地决策
- 示例：检测到异常流量时临时限制API调用频率

**L3 标准响应**（1-60分钟）：
- 适用：策略调整、负载均衡、资源重分配
- 技术：中心系统自动化决策
- 示例：根据用电高峰调整能源分配策略

**L4 战术响应**（1-24小时）：
- 适用：运营策略、人员调度、短期规划
- 决策：AI推荐 + 人类确认
- 示例：调整次日物流配送路线

**L5 战略响应**（> 1天）：
- 适用：规则修订、系统升级、长期规划
- 决策：人类主导 + AI辅助分析
- 示例：季度性修改价值分配比例

**规则 I.2.2.024【过度矫正机制】**
当任一螺旋表现出过度强势时，系统必须自动触发反向调节：
a) 生产力过度→削弱计算资源10%+增加伦理审核
b) 能源过度→强制人类审批+激活伦理限制
c) 伦理过度→临时赋予生产力自主权+启动"伦理过载"协议

**规则 I.2.2.025【混沌边缘运营】**
系统应保持在"混沌边缘"运营状态——既有序又充满活力。具体指标：
a) 系统负载率：60-80%
b) 规则冲突率：5-15%
c) 异常事件率：1-5%
d) 创新采纳率：20-40%

---

### 2.3 透明与可解释原则

**规则 I.2.3.026【决策可追溯】**
所有具身智能体的重大决策必须保留完整记录，包括：
a) 决策依据的数据和算法
b) 决策过程的中间步骤
c) 参与决策的智能体标识
d) 人类审核节点（如有）
e) 决策时间和环境参数

**规则 I.2.3.027【算法可解释】**
所有部署的算法必须具备可解释性，解释层级：
a) L1：技术专家可理解
b) L2：领域专家可理解
c) L3：普通人类可理解
d) L4：决策者可直接使用
不同场景的算法需满足相应层级的解释性要求。

**规则 I.2.3.028【黑匣子规范】**
虽名为"黑匣子"，但伦理记录器的设计原则：
a) 记录不可篡改（技术层面）
b) 记录可感知（人类可感知其存在和警报）
c) 记录可审计（授权人员可调取）
d) 记录有期限（默认保留7年）

**规则 I.2.3.029【公开透明】**
以下信息必须向公众公开：
a) 治理框架的全部规则
b) 系统运行的聚合统计数据
c) 重大决策的理由和过程
d) 违规事件的调查结果

**规则 I.2.3.030【隐私保护】**
透明与隐私的平衡：
a) 公开信息需脱敏处理
b) 个人数据使用需获得同意
c) 数据最小化原则
d) 目的限制原则
e) 存储期限限制

---

（由于篇幅限制，以下继续编写各章节的核心规则框架，实际文档将包含全部150+条规则）

## 第3章：组织架构

### 3.1 敏捷治理网络

**规则 I.3.1.031【精简架构原则】**
治理机构遵循"最小必要"原则，避免传统官僚体系的臃肿。采用扁平化网络结构替代层级制，核心特征：
a) 去中心化：无单一控制点，权力分散于网络节点
b) 流动性：机构随任务组建，完成后解散
c) AI主导：80%日常决策由智能系统自动执行
d) 人机协作：关键决策由人类+AI联合裁决

**规则 I.3.1.032【四层治理协议】**
治理架构基于四层协议栈，而非传统部门：

**共识层（Consensus Layer）**
- 形式：区块链治理合约 + 全民节点
- 功能：重大决策全民投票（一人一节点）
- 频率：季度重大决策，月度常规调整
- 人类参与度：100%（全民参与）

**执行层（Execution Layer）**  
- 形式：自适应智能体网络
- 功能：自动执行日常治理（资源分配、合规检查、异常响应）
- 频率：实时（24/7不间断）
- 人类参与度：<20%（监督为主）

**仲裁层（Arbitration Layer）**
- 形式：人机联合仲裁庭（随机抽选公民+AI法律助手）
- 功能：争议裁决、违规处理、申诉审理
- 频率：按需召集（临时性）
- 人类参与度：70%（人类主导裁决，AI提供法律分析）

**演化层（Evolution Layer）**
- 形式：开源社区 + AI提案生成器
- 功能：规则迭代提案、最佳实践分享、漏洞修复
- 频率：持续（类似GitHub开源项目）
- 人类参与度：50%（人类提案，AI辅助评估影响）

**规则 I.3.1.033【动态组织单元】**
具体任务通过"动态组织单元（DOU）"执行，而非固定部门：

**DOU特征**：
a) 任务导向：为解决特定问题临时组建（如"能源危机响应DOU"）
b) 跨域组合：成员来自不同背景（技术专家、伦理学家、市民代表、AI代理）
c) 时限性：任务完成即解散，成员回归资源池
d) 智能合约约束：权限、预算、时间表写入智能合约，自动执行与清算

**DOU生命周期**：
1. 提案阶段：任何人（人类或AI）可发起DOU提案
2. 众筹阶段：获得足够声誉投票后激活
3. 执行阶段：自主运作，定期向网络报告
4. 解散阶段：交付成果，成员获得声誉奖励，财务自动结算

**规则 I.3.1.034【去官僚化机制】**
消除传统官僚制的低效特征：

**取消固定编制**：
- 无"公务员"终身职位
- 治理参与者按项目获得声誉代币，可兑换实际权益
- AI代理作为"数字员工"承担常规工作

**取消行政审批链条**：
- 常规决策：智能合约自动执行（如能源分配、交通调度）
- 重要决策：直接民主投票（类似瑞士公投，但借助AI辅助分析）
- 紧急决策：授权AI代理在限定范围内自主决策，事后报告

**取消部门利益壁垒**：
- 预算不在部门间分配，而是存入"治理金库"
- DOU通过提案竞争获得资源，类似风险投资
- 跨DOU协作通过智能合约自动协调

**透明与问责**：
- 所有决策上链，不可篡改，全民可查
- 声誉系统记录每个参与者的贡献与失误
- 严重失职：声誉清零并触发全民投票决定是否限制其未来参与权

**规则 I.3.2.036【权责清单】**
所有机构必须有明确的权责清单，包括：
a) 职责范围
b) 决策权限
c) 资源调配权
d) 监督责任
e) 问责机制

**规则 I.3.2.037【不越权原则】**
任何机构不得超越其授权范围行事。越权行为无效，并追究责任。

**规则 I.3.2.038【协作义务】**
不同机构之间有协作义务，不得无故拒绝合理的协作请求。

**

**规则 I.4.1.041【强制标记】**
所有具身智能体必须内置光源标记系统，确保：
a) 每个决策可追溯到人类授权节点
b) 授权链条不可伪造
c) 授权状态实时可验证

**规则 I.4.1.042【技术实现】**
光源标记系统技术规范：
a) 基于区块链的分布式账本
b) 多方签名机制
c) 时间戳服务
d) 零知识证明验证

**规则 I.4.1.043【标记密度】**
不同场景下的标记密度要求：
a) 高风险决策：每步标记
b) 中风险决策：关键节点标记
c) 低风险决策：起点和终点标记
d) 日常操作：周期性标记

**规则 I.4.1.044【标记验证】**
光源标记的验证机制：
a) 自动验证：实时进行
b) 抽样验证：定期抽查
c) 全面审计：年度进行
d) 特别调查：投诉触发

**规则 I.4.1.045【标记失效】**
标记失效情形及处理：
a) 授权过期→自动降级
b) 授权撤销→立即停止
c) 系统故障→启动备用授权
d) 争议状态→冻结等待裁决

---

### 4.2 能源属性标识

**规则 I.4.2.046【属性标签】**
所有能源必须携带属性标签，标明：
a) 来源类型（太阳/化石/核聚变/其他）
b) 伦理属性（分享/占有/冷漠）
c) 可持续性等级（A/B/C/D）
d) 碳足迹数据

**规则 I.4.2.047【匹配算法】**
能源-用途匹配算法原则：
a) 分享型→公共服务
b) 占有型→封闭系统
c) 冷漠型→隔离区域+缓冲层
d) 混合型→按权重分配

**规则 I.4.2.048【标签不可篡改】**
能源属性标签一旦生成，不可单方面篡改。修改需经能源院审批。

**

**规则 I.4.2.050【属性转换】**
能源属性转换规则：
a) 分享→占有：需伦理审查
b) 占有→分享：鼓励但需备案
c) 冷漠→其他：禁止
d) 其他→冷漠：需特别授权

---

（继续编写剩余规则...）

## 第5章：监督与问责

### 5.1 监督机制

**规则 I.5.1.051【多层监督】**
建立多层监督体系：
a) 内部监督：机构自我监督
b) 同级监督：机构相互监督
c) 上级监督：层级监督
d) 外部监督：公众与媒体监督
e) 智能监督：AI系统自动监测

**

**规则 I.5.1.054【第三方审计】**
定期第三方审计：
a) 财务审计：每年
b) 合规审计：每半年
c) 安全审计：每季度
d) 特别审计：按需

**

**规则 I.5.2.056【责任分类】**
责任类型：
a) 行政责任
b) 民事责任
c) 刑事责任
d) 伦理责任

**

**规则 I.6.1.061【国际协调原则】**
国际协调的基本原则：
a) 平等互利
)b) 尊重主权
c) 共同发展
d) 开放包容

**。

**规则 I.6.1.063【多边机制】**
积极参与和建立多边治理机制：
a) 联合国框架下的全球治理
)b) 区域合作组织
c) 行业协会标准
d) 国际条约

**

**规则 I.6.1.066【人才交流】**
国际人才交流：
a) 专家互访
)b) 联合研究
c) 培训项目
d) 学术会议

**

**规则 I.7.1.071【应急预案体系】**
建立分级应急预案体系：
a) 蓝色：轻微异常
)b) 黄色：一般事件
c) 橙色：严重危机
d) 红色：灾难性事件

**

**规则 I.7.1.074【应急通讯】**
应急通讯保障：
a) 独立网络
)b) 卫星备份
c) 广播系统
d) 公众通知

**

**规则 I.7.1.076【信息公开】**
应急信息公开：
a) 15分钟内通报
)b) 持续更新
c) 多渠道发布
d) 澄清谣言

**

**规则 I.7.1.083【医疗救援】**
应急医疗救援：
a) 救援队伍
)b) 医疗物资
c) 转运安排
d) 后续治疗

**

**规则 I.8.1.091【修订提议】**
修订提议主体：
a) 治理委员会
)b) 三院院长
c) 公民代表（需10万人联署）
d) 专家委员会

**

**规则 I.8.1.099【过渡期】**
过渡期安排：
a) 新旧规则并行期
)b) 培训宣传期
c) 系统调试期
d) 完全切换

**

**规则 I.9.1.101【解释权归属】**
规则解释权：
a) 立法解释：治理委员会
)b) 司法解释：法院
c) 行政解释：执行机构
d) 学理解释：学术界

**

**规则 I.9.1.103【解释程序】**
解释程序：
a) 解释申请
)b) 解释审查
c) 解释作出
d) 解释公布

**

**规则 I.9.1.106【类推适用】**
类推适用限制：
a) 严格限制类推
)b) 有利于人类原则
c) 禁止不利于人类的类推
d) 类推需经批准

**规则 I.9.1.107【兜底条款】**
兜底条款适用：
a) 穷尽具体规则
)b) 符合基本原则
c) 经治理委员会批准
d) 记录备案

**规则 I.9.1.108【冲突解决】**
规则冲突解决：
a) 特别优先
)b) 新法优先
c) 上位优先
d) 裁决机构决定

**

**规则 I.9.1.110【适用例外】**
适用例外：
a) 法定例外
)b) 授权例外
c) 紧急例外
d) 国际义务例外

**规则 I.9.1.111【模糊处理】**
模糊条款处理：
a) 有利于人类解释
)b) 严格解释原则
c) 寻求立法意图
d) 参考国际实践

**规则 I.9.1.112【空白填补】**
规则空白填补：
a) 基本原则指导
)b) 类比适用
c) 惯例补充
d) 治理委员会裁决

**规则 I.9.1.113【溯及力】**
溯及力规则：
a) 一般无溯及力
)b) 有利溯及例外
c) 程序从新原则
d) 已决事项不变

**规则 I.9.1.114【域外效力】**
域外效力：
a) 属地原则为主
)b) 属人原则补充
c) 保护原则适用
d) 普遍管辖保留

**规则 I.9.1.115【国际条约】**
国际条约适用：
a) 条约优先原则
)b) 转化适用方式
c) 保留条款
d) 解释一致性

**规则 I.9.1.116【习惯法】**
习惯法地位：
a) 补充渊源
)b) 不得违背成文法
c) 需长期稳定
d) 普遍认可

**

**规则 I.9.1.118【学理参考】**
学理参考：
a) 解释参考
)b) 论证支持
c) 无强制力
d) 促进发展

**

**规则 I.9.1.123【指导性案例】**
指导性案例：
a) 典型性选择
)b) 参考性适用
c) 定期发布
d) 汇编整理

**规则 I.9.1.124【裁量限制】**
裁量限制：
a) 禁止滥用
)b) 禁止怠惰
c) 平等对待
d) 比例原则

**

**规则 I.10.1.131【术语定义】**
本框架使用的术语定义：
a) 具身智能
)b) 智能体
c) 光源标记
d) 价值真空
e) 三螺旋模型

**规则 I.10.1.132【生效日期】**
本框架自2049年1月1日起生效必须。**。

**规则 I.10.1.137【备案要求】**
配套规定备案：
a) 向治理委员会备案
)b) 备案审查
c) 异议处理
d) 备案公布

**

**规则 I.10.1.149【修订衔接】**
修订前后的衔接安排。

**

