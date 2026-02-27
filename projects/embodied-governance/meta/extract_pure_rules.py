#!/usr/bin/env python3
"""
规则提取器 - 从现有文档中提取纯规则内容
移除原理、案例、边界等补充说明
"""

import re
from pathlib import Path

def extract_pure_rules(input_file, output_file):
    """从文档中提取纯规则内容"""
    content = input_file.read_text(encoding='utf-8')
    
    # 匹配规则块：规则 ID + 标题 + 内容（直到下一个规则或章节标题）
    rule_pattern = r'(规则\s+[IV]+\.\d+\.\d+\.\d+\s*【.+?】)(.*?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|## |\Z)'
    
    matches = re.findall(rule_pattern, content, re.DOTALL)
    
    pure_rules = []
    for header, body in matches:
        # 只保留规则的核心定义，移除补充说明
        # 找到 "**原理**"、"**案例**"、"**边界**" 等标记之前的内容
        core_content = body
        
        # 移除补充部分
        for marker in ['**原理**', '**案例**', '**边界**', '**[English Version]**', '---']:
            if marker in core_content:
                core_content = core_content.split(marker)[0]
        
        # 清理空白
        core_content = core_content.strip()
        
        if core_content:  # 只保留有内容的规则
            pure_rules.append(f"{header}{core_content}\n\n")
    
    # 写回文件
    output_file.write_text(''.join(pure_rules), encoding='utf-8')
    return len(pure_rules)

def main():
    rules_dir = Path('rules')
    
    # 处理所有规则文件
    for md_file in sorted(rules_dir.glob('ARTICLES-*.md')):
        print(f"Processing {md_file.name}...")
        
        # 备份原文件
        backup_dir = Path('meta/backup')
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        import shutil
        shutil.copy(md_file, backup_dir / md_file.name)
        
        # 提取纯规则
        count = extract_pure_rules(md_file, md_file)
        print(f"  Extracted {count} pure rules")
    
    print("\n✓ Rule extraction complete!")
    print("  - Original files backed up to meta/backup/")
    print("  - Pure rules saved to rules/")
    print("\nNext: Move supplementary content to annotations/")

if __name__ == '__main__':
    main()
