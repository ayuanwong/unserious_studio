#!/usr/bin/env python3
"""
双语规则提取器 - 从完整文档中提取规则并添加英文翻译
"""

import re
import shutil
from pathlib import Path
from datetime import datetime

def extract_rules_with_translation(input_path, rules_output, annotations_output):
    """提取规则，保留双语内容"""
    content = input_path.read_text(encoding='utf-8')
    
    # 匹配规则块 - 支持 **规则...** 格式
    pattern = r'\*\*(规则\s+[IV]+\.\d+\.\d+\.\d+【.+?】)\*\*(.*?)(?=\*\*规则|\*\*## |\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    print(f"Found {len(matches)} rules in {input_path.name}")
    
    pure_rules = []
    annotations = []
    
    for header, body in matches:
        # 提取规则ID
        id_match = re.match(r'规则\s+([IV]+\.\d+\.\d+\.\d+)【(.+?)】', header)
        if not id_match:
            continue
        
        rule_id = id_match.group(1)
        title_cn = id_match.group(2)
        
        # 清理body，移除补充说明
        core_content = body
        supplementary = []
        
        # 查找补充说明
        markers = [
            ('**原理**', '原理'),
            ('**案例**', '案例'),
            ('**边界**', '边界'),
            ('**[English Version]**', '英文版')
        ]
        
        for marker, label in markers:
            if marker in core_content:
                idx = core_content.find(marker)
                if idx > 0:
                    supp = core_content[idx:]
                    # 截断到下一个主要标记
                    for next_m, _ in markers:
                        if next_m != marker:
                            next_idx = supp[len(marker):].find(next_m)
                            if next_idx > 0:
                                supp = supp[:len(marker) + next_idx]
                    supplementary.append((label, supp.strip()))
                    core_content = core_content[:idx]
        
        core_content = core_content.strip()
        
        # 添加到规则文件（保留中文）
        if core_content:
            pure_rules.append(f"**{header}**\n{core_content}\n\n")
        
        # 添加到注释文件
        if supplementary:
            annotations.append(f"### {rule_id}【{title_cn}】\n\n")
            for label, supp in supplementary:
                annotations.append(f"{supp}\n\n")
    
    # 保留文件头部
    header_match = re.match(r'^(.*?)(?=\*\*规则\s+[IV]+\.\d+\.\d+\.\d+【|## |$)', content, re.MULTILINE | re.DOTALL)
    file_header = header_match.group(1) if header_match else ""
    
    # 写入规则文件
    if pure_rules:
        rules_content = file_header + '\n' + ''.join(pure_rules)
        rules_output.write_text(rules_content, encoding='utf-8')
        print(f"  ✓ Extracted {len(pure_rules)} rules")
    
    # 写入注释文件
    if annotations:
        anno_content = f"# {input_path.stem} 补充说明\n\n"
        anno_content += f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        anno_content += ''.join(annotations)
        annotations_output.write_text(anno_content, encoding='utf-8')
        print(f"  ✓ Extracted {len(annotations)} annotation sections")

def main():
    rules_dir = Path('rules')
    anno_dir = Path('annotations')
    backup_dir = Path('meta/backup')
    
    anno_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("双语规则提取工具")
    print("=" * 60)
    
    for md_file in sorted(rules_dir.glob('ARTICLES-*.md')):
        # 检查是否是已恢复的文件（有备份且文件较大）
        backup_file = backup_dir / md_file.name
        if backup_file.exists() and backup_file.stat().st_size > md_file.stat().st_size:
            print(f"\n📄 {md_file.name}")
            print(f"   Current: {md_file.stat().st_size} bytes")
            print(f"   Backup: {backup_file.stat().st_size} bytes")
            
            # 从备份复制
            shutil.copy(backup_file, md_file)
            
            # 提取
            anno_file = anno_dir / f"{md_file.stem}-annotations.md"
            extract_rules_with_translation(md_file, md_file, anno_file)
    
    print("\n" + "=" * 60)
    print("✅ 完成!")
    print("=" * 60)

if __name__ == '__main__':
    main()
