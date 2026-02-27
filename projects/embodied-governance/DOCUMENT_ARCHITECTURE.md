# 文档架构规范 (Document Architecture)

## 目录结构

```
embodied-governance/
├── README.md                 # 项目介绍（对外展示）
├── index.html               # 交互式网页
│
├── rules/                   # 📜 规则文档（核心，对外展示）
│   ├── 00-PREAMBLE.md
│   ├── ARTICLES-I-FUNDAMENTAL.md
│   ├── ARTICLES-II-PRODUCTIVITY.md
│   ├── ARTICLES-III-ENERGY.md
│   ├── ARTICLES-IV-ETHICAL-AGENCY.md
│   ├── ARTICLES-V-ADAPTIVE.md
│   ├── ARTICLES-VI-EXCEPTIONS.md
│   └── ARTICLES-VII-OVERSIGHT.md
│
├── annotations/             # 📚 解释和注释（内部参考）
│   ├── principles/          # 原理说明
│   ├── cases/               # 案例分析
│   ├── boundaries/          # 边界说明
│   └── context/             # 历史背景
│
├── logs/                    # 📝 运行日志（内部）
│   ├── improvement.log
│   └── commits/
│
└── meta/                    # ⚙️ 元数据和配置（内部）
    ├── roadmap/
    ├── issues/
    └── plans/
```

## 规则文档格式 (rules/)

**只包含规则本身**，格式如下：

```markdown
**规则 I.1.1.001【具身智能】**
具身智能（Embodied Intelligence）指具有物理实体、能够感知和作用于物理世界、具备自主决策能力的智能系统。包括但不限于：人形机器人、自主车辆、智能工厂系统、服务机器人、医疗机器人、农业自动化系统、物流无人机、建筑自动化设备等。

**规则 I.1.1.002【智能体】**
智能体（Agent）指任何能够感知环境、处理信息、做出决策并执行行动的实体。在本框架中，智能体分为：
- 碳基智能体（人类）
- 硅基智能体（AI系统）
- 混合智能体（人机融合系统）
- 群体智能体（分布式智能网络）
```

**禁止在规则文档中包含**：
- ❌ "原理" 段落
- ❌ "案例" 段落  
- ❌ "边界" 段落
- ❌ 运行日志
- ❌ 改进记录

这些内容应该放在 `annotations/` 目录下的对应文件中。

## 解释文档格式 (annotations/)

### principles/I.1.1.001.md
```markdown
# 规则 I.1.1.001【具身智能】原理

**理论依据**：
具身认知理论（Embodied Cognition）认为认知过程不仅发生在大脑中，还涉及身体与环境的交互...

**哲学基础**：
梅洛-庞蒂的知觉现象学...
```

### cases/I.1.1.001.md
```markdown
# 规则 I.1.1.001【具身智能】案例

**正面案例**：
...

**反面案例**：
...

**边界案例**：
...
```

## 日志文档 (logs/)

所有自动化运行的日志放在这里，不影响主文档的阅读。

## 元数据 (meta/)

- 技术路线图
- 改进计划
- 问题记录
- 配置文件

## 对外展示 vs 内部使用

| 目录 | 用途 | 访问权限 |
|------|------|---------|
| `rules/` | 对外展示的核心规则 | 公开 |
| `annotations/` | 内部参考和深度解释 | 内部 |
| `logs/` | 运行记录 | 内部 |
| `meta/` | 项目管理和配置 | 内部 |

---

**原则**：简洁、清晰、分离关注点。规则文件只包含规则，解释和日志放在别处。
