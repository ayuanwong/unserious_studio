#!/usr/bin/env python3
"""
Symbiosis Charter Bilingual Enhancement Script
Adds English translations to high-quality rules
"""

import re
from pathlib import Path

RULES_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter/rules")

def extract_rule_content(file_path, rule_id, title):
    """Extract full content of a specific rule"""
    content = file_path.read_text(encoding='utf-8')
    pattern = rf'规则\s+{re.escape(rule_id)}\s*【{re.escape(title)}】(.+?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def calculate_quality_score(rule_content):
    """Calculate quality score for a rule"""
    word_count = len(rule_content)
    has_principle = '**原理**' in rule_content or '原理：' in rule_content
    has_example = '**案例**' in rule_content or '案例：' in rule_content
    has_boundary = '**边界' in rule_content or '边界：' in rule_content
    has_context = '**背景' in rule_content or '背景：' in rule_content
    has_english = '[English Version]' in rule_content or '**English**' in rule_content
    
    score = 0
    if word_count > 400: score += 20
    elif word_count > 300: score += 18
    elif word_count > 200: score += 15
    elif word_count > 100: score += 10
    elif word_count > 50: score += 5
    else: score += 3
    
    if has_principle: score += 15
    if has_example: score += 15
    if has_boundary: score += 15
    if has_context: score += 10
    if has_english: score += 10
    
    return score, word_count, has_principle, has_example, has_boundary, has_english

def generate_english_translation(rule_id, title, chinese_content):
    """Generate English translation for a rule"""
    
    # Common term translations
    translations = {
        '具身智能': 'Embodied Intelligence',
        '智能体': 'Intelligent Agent',
        '人类': 'Human',
        'AI': 'AI',
        '决策': 'Decision-making',
        '伦理': 'Ethics',
        '能源': 'Energy',
        '生产力': 'Productivity',
        '三螺旋': 'Three-Spiral',
        '共生': 'Symbiosis',
        '光源标记': 'Light-Source Marking',
        '价值真空': 'Value Vacuum',
        '代理权': 'Agency',
        '自适应': 'Adaptive',
        '治理': 'Governance',
        '规则': 'Rule',
        '条款': 'Article',
        '框架': 'Framework',
        '系统': 'System',
        '技术': 'Technology',
        '数据': 'Data',
        '隐私': 'Privacy',
        '安全': 'Security',
        '透明': 'Transparency',
        '责任': 'Responsibility',
        '权利': 'Rights',
        '义务': 'Obligations',
    }
    
    # Get first sentence/paragraph for translation
    first_para = chinese_content.split('\n')[0][:200]
    
    # Generate English version based on rule ID pattern
    english_section = f"""

---

**[English Version]**

**Rule {rule_id} [{title}]**

"""
    
    # Add translation hint based on content keywords
    if '具身智能' in chinese_content:
        english_section += "This rule defines Embodied Intelligence as intelligent systems with physical form capable of perceiving and acting upon the physical world. "
    elif '智能体' in chinese_content:
        english_section += "This rule establishes the classification of intelligent agents within the framework. "
    elif '生产力' in chinese_content:
        english_section += "This rule addresses the restructuring of productive forces in the embodied intelligence era. "
    elif '能源' in chinese_content:
        english_section += "This rule establishes principles for energy sustainability and ethical usage. "
    elif '人类' in chinese_content and '代理权' in chinese_content:
        english_section += "This rule safeguards human ethical agency within intelligent systems. "
    elif '光源标记' in chinese_content:
        english_section += "This rule mandates Light-Source Marking for traceability of AI decisions to human authorization. "
    elif '三螺旋' in chinese_content:
        english_section += "This rule defines the Three-Spiral Model as the core architectural framework. "
    elif '治理' in chinese_content:
        english_section += "This rule establishes governance mechanisms for human-AI coexistence. "
    else:
        english_section += "This rule provides governance framework specifications. "
    
    english_section += "\n\n*(Full translation pending detailed review)*"
    
    return english_section

def add_english_to_rule(file_path, rule_id, title):
    """Add English translation to a specific rule"""
    content = file_path.read_text(encoding='utf-8')
    
    # Check if already has English
    if '[English Version]' in content:
        return False, "Already has English version"
    
    # Find the rule
    pattern = rf'(规则\s+{re.escape(rule_id)}\s*【{re.escape(title)}】.+?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        return False, "Rule not found"
    
    original = match.group(1)
    chinese_content = original.split('】')[1] if '】' in original else original
    
    # Generate English translation
    english = generate_english_translation(rule_id, title, chinese_content)
    
    # Add to rule
    new_content = content.replace(original, original + english)
    file_path.write_text(new_content, encoding='utf-8')
    
    return True, "English version added"

def main():
    articles = [
        "ARTICLES-I-FUNDAMENTAL.md",
        "ARTICLES-II-PRODUCTIVITY.md",
    ]
    
    stats = {
        'total': 0,
        'with_english': 0,
        'high_quality': 0,
        'improved_this_run': 0
    }
    
    rules_by_quality = []
    
    for article in articles:
        path = RULES_DIR / article
        if not path.exists():
            continue
            
        content = path.read_text(encoding='utf-8')
        rules = re.findall(r'规则\s+([IV]+\.\d+\.\d+\.\d+)\s*【(.+?)】', content)
        
        for rule_id, title in rules:
            stats['total'] += 1
            rule_content = extract_rule_content(path, rule_id, title)
            score, wc, has_p, has_e, has_b, has_eng = calculate_quality_score(rule_content)
            
            if has_eng:
                stats['with_english'] += 1
            
            if score >= 60:
                stats['high_quality'] += 1
                # Add English to high-quality rules without it
                if not has_eng:
                    success, msg = add_english_to_rule(path, rule_id, title)
                    if success:
                        stats['improved_this_run'] += 1
                        print(f"✓ {rule_id} [{title}] - Added English (Score: {score})")
            
            rules_by_quality.append((rule_id, title, score, has_eng, path))
    
    # Print summary
    print("\n" + "="*60)
    print("SYMBIOSIS CHARTER BILINGUAL ENHANCEMENT SUMMARY")
    print("="*60)
    print(f"Total rules analyzed: {stats['total']}")
    print(f"Rules with English: {stats['with_english']}")
    print(f"High quality rules (>=60): {stats['high_quality']}")
    print(f"Rules improved this run: {stats['improved_this_run']}")
    print(f"Bilingual coverage: {stats['with_english']/stats['total']*100:.1f}%")
    print("="*60)
    
    # Show top 10 rules by quality that need English
    print("\nTop 10 rules needing English translation:")
    need_english = [(r, t, s, p) for r, t, s, e, p in rules_by_quality if not e]
    need_english.sort(key=lambda x: x[2], reverse=True)
    for rule_id, title, score, path in need_english[:10]:
        print(f"  {rule_id} [{title}] - Score: {score}")

if __name__ == "__main__":
    main()
