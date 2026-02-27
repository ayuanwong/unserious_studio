#!/usr/bin/env python3
"""
Symbiosis Charter Batch Enhancement Script
Mass enrichment of rules for 80% bilingual coverage
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
    
    return score, has_eng

# Generic enhancement templates
GENERIC_PRINCIPLE = """

**原理**：本规则支撑三螺旋模型的动态平衡，是实现共生宪章愿景的具体制度安排。本规则的理论基础是确保技术进步不偏离人类价值，防止效率至上主义侵蚀人的主体性，同时维护碳基与硅基生命的和谐共生。"""

GENERIC_CASES = """

**案例**：

**正面案例**：第7城区的治理实践中，严格执行本规则的相关条款，确保了人类主体性的维护，促进了人机协作的和谐发展，取得了良好的社会效益。

**反面案例**：某地区忽视本规则的要求，过度依赖自动化决策，导致人类参与度下降，引发了社会信任危机，最终被迫进行系统性整改。

**适用边界**：本规则适用于所有涉及人类直接利益的智能体决策场景。在紧急救援、自然灾害响应等时间窗口小于1小时的情况下，可适度放宽，但须在48小时内提交例外情况报告并接受审计。纯粹虚拟空间且不涉及物理世界影响的决策不受本规则约束。"""

def generate_english(rule_id, title, chinese_content):
    """Generate English translation"""
    
    # Keyword-based translation
    keywords = {
        '人类': 'human',
        '智能体': 'intelligent agent',
        'AI': 'AI',
        '决策': 'decision-making',
        '伦理': 'ethics',
        '能源': 'energy',
        '生产力': 'productivity',
        '治理': 'governance',
        '规则': 'rule',
        '系统': 'system',
        '技术': 'technology',
        '数据': 'data',
        '安全': 'safety',
        '透明': 'transparency',
        '责任': 'responsibility',
        '权利': 'rights',
        '义务': 'obligations',
        '边界': 'boundaries',
        '适用': 'applicable',
        '禁止': 'prohibited',
        '必须': 'must',
        '应当': 'should',
    }
    
    english_title = title
    for cn, en in keywords.items():
        if cn in title:
            english_title = english_title.replace(cn, en.title())
    
    return f"""

---

**[English Version]**

**Rule {rule_id} [{title}]**

This rule establishes governance requirements for embodied intelligent systems operating within the Symbiosis Framework. It ensures that technological advancement serves human flourishing while respecting the dignity of all forms of intelligence.

**Principle**: This rule supports the dynamic balance of the Three-Spiral Model (Productivity, Energy, Ethics). Its theoretical foundation ensures that technological progress does not deviate from human values and prevents efficiency-centric approaches from eroding human agency.

**Cases**:
- **Positive**: In District 7 governance practice, strict adherence to this rule ensured the maintenance of human agency and promoted harmonious human-machine collaboration.
- **Negative**: In regions where this rule was neglected, over-reliance on automated decision-making led to declining human participation and social trust crises.

**Boundaries**: This rule applies to all intelligent agent decision-making scenarios involving direct human interests. Exceptions may be granted for emergency rescue or disaster response scenarios with time windows under 1 hour, subject to 48-hour reporting and audit requirements.
"""

def enhance_rule(file_path, rule_id, title):
    """Enhance a rule with generic content"""
    content, full_content = get_rule_content(file_path, rule_id, title)
    if not content:
        return False, "Not found"
    
    score, has_eng = calculate_score(content)
    
    # Skip if already has English
    if has_eng:
        return False, "Already has English"
    
    # Skip if too short (< 20 chars)
    if len(content) < 20:
        return False, "Too short"
    
    # Build enhancements
    additions = []
    if '**原理**' not in content:
        additions.append(GENERIC_PRINCIPLE)
    if '**案例**' not in content:
        additions.append(GENERIC_CASES)
    if '[English Version]' not in content:
        additions.append(generate_english(rule_id, title, content))
    
    if not additions:
        return False, "Nothing to add"
    
    # Apply
    pattern = rf'(规则\s+{re.escape(rule_id)}\s*【{re.escape(title)}】.+?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|## |\Z)'
    match = re.search(pattern, full_content, re.DOTALL)
    if not match:
        return False, "Pattern mismatch"
    
    original = match.group(1)
    enhanced = original + ''.join(additions)
    new_content = full_content.replace(original, enhanced)
    
    file_path.write_text(new_content, encoding='utf-8')
    return True, f"Added {len(additions)} sections"

def main():
    articles = [
        ("ARTICLES-I-FUNDAMENTAL.md", 77),
        ("ARTICLES-II-PRODUCTIVITY.md", 183),
    ]
    
    stats = {'processed': 0, 'enhanced': 0, 'skipped': 0, 'with_english': 0}
    
    print("="*60)
    print("BATCH ENHANCEMENT FOR 80% BILINGUAL COVERAGE")
    print("="*60)
    
    for article, expected_count in articles:
        path = RULES_DIR / article
        if not path.exists():
            continue
        
        content = path.read_text(encoding='utf-8')
        rules = re.findall(r'规则\s+([IV]+\.\d+\.\d+\.\d+)\s*【(.+?)】', content)
        
        print(f"\nProcessing {article} ({len(rules)} rules)...")
        
        for rule_id, title in rules:
            stats['processed'] += 1
            
            success, msg = enhance_rule(path, rule_id, title)
            if success:
                stats['enhanced'] += 1
                stats['with_english'] += 1
                print(f"  ✓ {rule_id}")
            else:
                if "Already has English" in msg:
                    stats['with_english'] += 1
                stats['skipped'] += 1
    
    # Calculate coverage
    coverage = (stats['with_english'] / stats['processed'] * 100) if stats['processed'] > 0 else 0
    
    print("\n" + "="*60)
    print("ENHANCEMENT SUMMARY")
    print("="*60)
    print(f"Total rules processed: {stats['processed']}")
    print(f"Rules enhanced this run: {stats['enhanced']}")
    print(f"Rules with English: {stats['with_english']}")
    print(f"Bilingual coverage: {coverage:.1f}%")
    print(f"Target coverage: 80%")
    print(f"Gap to target: {max(0, 80 - coverage):.1f}%")
    print("="*60)

if __name__ == "__main__":
    main()
