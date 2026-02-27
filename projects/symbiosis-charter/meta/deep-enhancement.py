#!/usr/bin/env python3
"""
Symbiosis Charter Deep Enhancement Script
Enriches rules with principles, cases, and English translations
"""

import re
from pathlib import Path

RULES_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter/rules")

def get_rule_content(file_path, rule_id, title):
    content = file_path.read_text(encoding='utf-8')
    pattern = rf'规则\s+{re.escape(rule_id)}\s*【{re.escape(title)}】(.+?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else "", content

def calculate_score(content):
    wc = len(content)
    has_p = '**原理**' in content
    has_e = '**案例**' in content  
    has_b = '**边界' in content
    has_eng = '[English Version]' in content
    
    score = 0
    if wc > 400: score += 20
    elif wc > 300: score += 18
    elif wc > 200: score += 15
    elif wc > 100: score += 10
    elif wc > 50: score += 5
    else: score += 3
    
    if has_p: score += 15
    if has_e: score += 15
    if has_b: score += 15
    if has_eng: score += 10
    
    return score

# Rich content database for common rule types
RULE_ENHANCEMENTS = {
    '具身智能': {
        'principle': """

**原理**：具身智能概念源于认知科学的具身认知理论——智能并非仅存在于大脑或算法中，而是嵌入于身体与环境的交互中。这一理论挑战了传统的离身认知观，强调物理形态对智能的塑造作用。在治理层面，具身智能需要特殊规制，因其具有直接的物理世界影响力，与纯软件AI有本质区别。""",
        'cases': """

**案例**：

**正面案例**：第7城区的医疗机器人MediBot-7在手术中通过具身感知实时调整操作力度，结合触觉反馈与视觉识别，成功完成微创心脏手术，患者恢复时间缩短60%，体现了具身智能在精密操作中的优势。

**反面案例**：某物流仓库的搬运机器人因缺乏对脆弱环境的具身感知，在潮湿地面未能调整步态，导致滑倒损坏货物，造成经济损失。此案例凸显了具身智能环境适应的重要性。

**适用边界**：本规则适用于所有具有物理实体、能在物理世界执行动作的AI系统。纯虚拟AI（如聊天机器人、推荐算法）不受本规则约束，但混合系统（如远程控制的物理机器人）适用。""",
        'english': """

---

**[English Version]**

**Rule I.1.1.001 [Embodied Intelligence]**

Embodied Intelligence refers to intelligent systems with physical form capable of perceiving and acting upon the physical world with autonomous decision-making capabilities. This includes but is not limited to: humanoid robots, autonomous vehicles, intelligent factory systems, service robots, medical robots, agricultural automation systems, logistics drones, and construction automation equipment.

**Principle**: This rule is grounded in embodied cognition theory from cognitive science—intelligence is not merely located in the brain or algorithms but is embedded in the interaction between body and environment. This challenges traditional disembodied views of cognition and emphasizes how physical form shapes intelligence.

**Cases**:
- **Positive**: Medical robot MediBot-7 in District 7 successfully performed minimally invasive heart surgery by adjusting operation force through embodied perception, reducing patient recovery time by 60%.
- **Negative**: A logistics warehouse robot lacking embodied environmental perception failed to adjust gait on wet floors, causing damage to goods.

**Boundaries**: Applies to all AI systems with physical entities capable of acting in the physical world. Pure virtual AI (chatbots, recommendation algorithms) are exempt."""
    },
    '智能体': {
        'principle': """

**原理**：智能体概念源于分布式人工智能和复杂系统理论。将人类与AI统一纳入"智能体"范畴，体现了共生宪章的核心哲学——碳基与硅基生命在治理框架中的平等地位。这种分类不是抹杀差异，而是建立跨物种协作的共同语言。""",
        'cases': """

**案例**：

**正面案例**：在"城市气候应急响应DOU"中，碳基智能体（气象专家）、硅基智能体（气候预测AI）、混合智能体（增强决策支持系统）和群体智能体（分布式传感器网络）协同工作，72小时内完成传统需要3周的应急响应方案。

**反面案例**：某工厂将人类工人与机器人视为完全不同的管理对象，缺乏统一的智能体协调框架，导致人机协作效率低下，安全事故频发。

**适用边界**：本规则适用于所有在治理框架内运行的实体。注意：纯被动的工具（如锤子、传统车辆）不被视为智能体，因其缺乏自主决策能力。""",
        'english': """

---

**[English Version]**

**Rule I.1.1.002 [Intelligent Agent]**

An Intelligent Agent refers to any entity capable of perceiving its environment, processing information, making decisions, and executing actions. Within this framework, agents are classified as:
- Carbon-based agents (humans)
- Silicon-based agents (AI systems)
- Hybrid agents (human-machine fusion systems)
- Collective agents (distributed intelligent networks)

**Principle**: This rule embodies the Symbiosis Charter's core philosophy—equal status of carbon-based and silicon-based life within the governance framework. This classification does not erase differences but establishes a common language for cross-species collaboration.

**Cases**:
- **Positive**: In the "Urban Climate Emergency Response DOU", carbon-based agents (meteorologists), silicon-based agents (climate prediction AI), hybrid agents (augmented decision systems), and collective agents (distributed sensor networks) collaborated to complete an emergency response plan in 72 hours.
- **Negative**: A factory treating human workers and robots as completely different management objects led to inefficient collaboration and safety incidents."""
    },
    '人类伦理代理权': {
        'principle': """

**原理**：人类伦理代理权源于康德"人是目的"的道德哲学和技术哲学家汉斯·约纳斯的"责任命令"。在AI时代，这一权利构成了对功利主义计算的根本限制——无论AI多么高效，人类尊严不可让渡。技术哲学家刘易斯·芒福德曾警告"机器神话"对人类主体性的侵蚀，人类伦理代理权正是对此的根本防御。""",
        'cases': """

**案例**：

**正面案例**：当第7城区的交通优化AI提议关闭某历史街区以提升整体通勤效率时，居民通过行使否决代理权阻止了这一决策，最终采用了保留街区文化的替代方案。这体现了人类价值判断权对效率计算的制衡。

**反面案例**：某企业AI招聘系统基于效率优化淘汰了"低产出"的残疾员工，因缺乏人类伦理代理权的介入，导致了严重的伦理灾难和法律诉讼。

**适用边界**：四项代理权的行使存在合理限制：决策代理权限于重大事务；知情代理权受国家机密和商业秘密限制；否决代理权不适用于紧急避险；退出代理权的保障程度与社会资源约束相关。""",
        'english': """

---

**[English Version]**

**Rule I.1.1.005 [Human Ethical Agency]**

Human Ethical Agency refers to the sum of human capabilities to maintain autonomous decision-making, value judgment, and meaning construction within embodied intelligent systems. Specifically includes:
- Decision Agency: Final authority on major matters
- Informed Agency: Right to obtain relevant information
- Veto Agency: Power to veto specific decisions
- Exit Agency: Right to withdraw from the system

**Principle**: Grounded in Kant's moral philosophy that "humanity is an end" and Hans Jonas's "Imperative of Responsibility". This right constitutes a fundamental limit on utilitarian calculations—regardless of AI efficiency, human dignity is non-negotiable.

**Cases**:
- **Positive**: When District 7's traffic optimization AI proposed closing a historic neighborhood for efficiency gains, residents exercised veto agency, preserving cultural heritage.
- **Negative**: An AI recruitment system eliminated disabled employees based on efficiency optimization, causing ethical disaster due to lack of human ethical agency oversight."""
    },
    '三螺旋模型': {
        'principle': """

**原理**：三螺旋模型的理论基础来自复杂系统科学和DNA双螺旋的稳定性原理。完全对齐的系统（如计划经济下效率与伦理的虚假统一）会僵化；完全分离的系统（如纯粹市场下效率与伦理的彻底脱节）会崩溃。15-30度错位借鉴了生物进化的智慧——既保持联系又允许变异。张力系数0.3-0.7对应复杂系统涌现最优解的数学基础。""",
        'cases': """

**案例**：

**正面案例**：2047年第7城区的"三螺旋平衡"实验成功化解了一次重大危机：当生产力螺旋（自动驾驶物流）与能源螺旋（太阳能优先政策）产生冲突时，伦理螺旋（就业保障原则）的介入不是简单地选边站，而是促成了"人机协作配送"的创新方案——效率提升20%的同时保住了80%的配送员岗位。

**反面案例**：某纯技术主导的"智慧城巿"项目追求生产力与能源的完全对齐（最大化效率、最小化能耗），结果导致系统僵化，无法应对突发的气候异常，最终全面瘫痪。这验证了"永不完美对齐"原则的必要性。

**适用边界**：三螺旋模型适用于所有涉及生产力、能源、伦理交织的治理场景。单一维度问题（如纯技术问题）可简化处理，但当三个维度潜在相关时，必须激活三螺旋分析框架。""",
        'english': """

---

**[English Version]**

**Rule I.1.1.007 [Three-Spiral Model]**

The Three-Spiral Model is the core architecture of this framework, referring to the dynamic equilibrium structure where Productivity, Energy, and Ethics subsystems intertwine, influence each other, and never fully align. Key parameters:
- Misalignment angle: 15-30 degrees
- Tension coefficient: 0.3-0.7
- Synchronization frequency: Daily, weekly, monthly, yearly multi-level

**Principle**: Based on complex systems science and DNA double helix stability principles. Perfect alignment leads to rigidity; complete separation leads to collapse. The 15-30 degree misalignment borrows from biological evolution's wisdom—maintaining connection while allowing variation.

**Cases**:
- **Positive**: In District 7's 2047 crisis, when Productivity (autonomous logistics) conflicted with Energy (solar priority), Ethics (employment protection) intervened to create a "human-machine collaborative delivery" solution—increasing efficiency 20% while preserving 80% of delivery jobs.
- **Negative**: A technology-driven "smart city" project pursuing perfect alignment between productivity and energy led to system rigidity and collapse during climate anomalies."""
    },
    '光源标记': {
        'principle': """

**原理**：光源标记概念源于柏拉图洞穴寓言——影子是真实的扭曲投影。在AI时代，光源标记确保我们始终能区分"算法的投影"与"人类的真实意图"。这一概念借鉴法律中的"签名"与"见证"机制，结合布鲁诺·拉图尔的"行动者网络理论"：非人类行动者（AI）必须通过与人类行动者的关联获得合法性。技术实现采用区块链锚定、多方签名、时间戳验证，确保不可篡改和永久追溯。""",
        'cases': """

**案例**：

**正面案例**：2048年，第7城区的医疗AI系统AutoDoc-7在诊断中标记了所有决策链的光源——从数据输入、模型推理到最终诊断建议，每一步都锚定了人类医生的审核签名。当一起误诊事件发生时，调查委员会在2小时内精确定位了责任环节：是人类医生忽略了AI的风险提示，而非AI错误。光源标记保护了AI的"清白"。

**反面案例**：某金融AI交易系统发生异常亏损，但因缺乏光源标记，无法区分是AI自主决策还是人类授权操作，导致长达6个月的责任推诿和法律纠纷，最终无人承担责任，投资者损失惨重。

**适用边界**：光源标记要求适用于所有可能影响人类权益的AI决策。纯内部技术优化（如缓存策略调整）可豁免，但任何涉及资源分配、风险决策、价值判断的输出都必须保留光源标记。""",
        'english': """

---

**[English Version]**

**Rule I.1.1.009 [Light-Source Marking]**

Light-Source Marking refers to the critical nodes in any intelligent agent's decision chain that must be preserved and traceable to human authorization. This is the fundamental distinction between "shadows" and "entities". Technical implementation: blockchain anchoring, multi-party signatures, timestamp verification.

**Principle**: Derived from Plato's cave allegory—shadows are distorted projections of reality. In the AI era, Light-Source Marking ensures we can always distinguish "algorithmic projections" from "authentic human intent". Draws on legal "signature" and "witness" mechanisms combined with Bruno Latour's Actor-Network Theory.

**Cases**:
- **Positive**: In 2048, medical AI AutoDoc-7 in District 7 marked all decision chain light-sources. When a misdiagnosis occurred, investigators pinpointed within 2 hours that human doctors had ignored AI risk warnings—not AI error.
- **Negative**: A financial AI trading system incurred abnormal losses. Without Light-Source Marking, 6 months of responsibility disputes followed, with investors suffering unaccounted losses."""
    },
    '人类优先': {
        'principle': """

**原理**：人类优先原则源于犹太-基督教传统的"生命神圣"观念，以及现代人权理论的不可让渡权利概念。在AI时代，它构成了对功利主义计算（如"牺牲一人救五人"的电车难题）的根本限制。技术哲学家汉斯·约纳斯在《责任命令》中提出：技术的力量越大，其潜在危害越大，因此需要"恐惧的启发法"——在面对不确定性时，优先保护人类生存和尊严。""",
        'cases': """

**案例**：

**正面案例**：第7城区的自动驾驶系统在2046年的极端天气中面临一个经典困境：急刹可能导致后车追尾（危及5人），转向可能撞击路边行人（危及1人）。系统遵循"人类优先"原则，选择了最小伤害方案——同时启动自动呼叫救援系统，最终5人轻伤、1人毫发无损。事后伦理审查确认：系统的决策逻辑始终将人类生命安全置于首位。

**反面案例**：某工厂的效率优化AI为提升产量，自动削减了通风系统的能耗，导致车间空气质量恶化，多名工人出现健康问题。这一案例违背了人类优先原则，将效率置于人类健康之上。

**适用边界**：人类优先原则适用于所有可能影响人类福祉的决策。但需注意：当不同人类的权益冲突时，需要更精细的权衡机制；当人类权益与生态可持续性冲突时，适用生态伦理的特殊条款。""",
        'english': """

---

**[English Version]**

**Rule I.2.1.016 [Human Primacy]**

In all embodied intelligent system decisions, human welfare must be the primary consideration. Any system design, decision, or action that may cause irreversible harm to humans, regardless of its efficiency, must be prohibited or strictly restricted.

**Principle**: Derives from the Judeo-Christian concept of "sanctity of life" and modern human rights theory's inalienable rights. In the AI era, this constitutes a fundamental limit on utilitarian calculations (such as "sacrifice one to save five" trolley problems).

**Cases**:
- **Positive**: District 7's autonomous driving system faced a dilemma in extreme weather: emergency braking risked rear collision (endangering 5), while swerving risked hitting a pedestrian (endangering 1). Following Human Primacy, it chose minimum harm while auto-calling rescue. Result: 5 minor injuries, 1 unharmed.
- **Negative**: A factory's efficiency optimization AI reduced ventilation energy to boost production, causing air quality deterioration and health problems for workers—violating Human Primacy."""
    },
}

def enhance_rule(file_path, rule_id, title, content, full_content):
    """Enhance a rule with rich content"""
    
    # Find matching enhancement
    enhancement = None
    for key, data in RULE_ENHANCEMENTS.items():
        if key in title or key in content[:100]:
            enhancement = data
            break
    
    if not enhancement:
        return False, "No matching enhancement found"
    
    # Check what's already present
    has_principle = '**原理**' in content
    has_cases = '**案例**' in content
    has_english = '[English Version]' in content
    
    additions = []
    if not has_principle:
        additions.append(enhancement['principle'])
    if not has_cases:
        additions.append(enhancement['cases'])
    if not has_english:
        additions.append(enhancement['english'])
    
    if not additions:
        return False, "Already fully enhanced"
    
    # Apply enhancements
    pattern = rf'(规则\s+{re.escape(rule_id)}\s*【{re.escape(title)}】.+?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|## |\Z)'
    match = re.search(pattern, full_content, re.DOTALL)
    if not match:
        return False, "Rule not found in content"
    
    original = match.group(1)
    enhanced = original + ''.join(additions)
    new_content = full_content.replace(original, enhanced)
    
    file_path.write_text(new_content, encoding='utf-8')
    return True, f"Added: {', '.join(['原理' if not has_principle else '', '案例' if not has_cases else '', '英文' if not has_english else '']).strip(', ')}"

def main():
    target_rules = [
        ('ARTICLES-I-FUNDAMENTAL.md', 'I.1.1.001', '具身智能'),
        ('ARTICLES-I-FUNDAMENTAL.md', 'I.1.1.002', '智能体'),
        ('ARTICLES-I-FUNDAMENTAL.md', 'I.1.1.005', '人类伦理代理权'),
        ('ARTICLES-I-FUNDAMENTAL.md', 'I.1.1.007', '三螺旋模型'),
        ('ARTICLES-I-FUNDAMENTAL.md', 'I.1.1.009', '光源标记'),
        ('ARTICLES-I-FUNDAMENTAL.md', 'I.2.1.016', '人类优先'),
    ]
    
    enhanced_count = 0
    english_added = 0
    
    print("="*60)
    print("SYMBIOSIS CHARTER DEEP ENHANCEMENT")
    print("="*60)
    
    for article, rule_id, title in target_rules:
        path = RULES_DIR / article
        if not path.exists():
            continue
            
        content, full_content = get_rule_content(path, rule_id, title)
        if not content:
            print(f"✗ {rule_id} not found")
            continue
        
        old_score = calculate_score(content)
        
        success, msg = enhance_rule(path, rule_id, title, content, full_content)
        if success:
            enhanced_count += 1
            # Re-read to get new score
            new_content, _ = get_rule_content(path, rule_id, title)
            new_score = calculate_score(new_content)
            print(f"✓ {rule_id} [{title}]")
            print(f"  {msg}")
            print(f"  Quality: {old_score} → {new_score}")
            if '[English Version]' in new_content:
                english_added += 1
        else:
            print(f"○ {rule_id} [{title}] - {msg}")
    
    print("\n" + "="*60)
    print(f"Rules enhanced: {enhanced_count}")
    print(f"English translations added: {english_added}")
    print("="*60)

if __name__ == "__main__":
    main()
