#!/usr/bin/env python3
"""
文档分离器 - 将规则与补充说明分离
"""

import re
import shutil
from pathlib import Path
from datetime import datetime

def split_rule_document(input_path, rules_output, annotations_output):
    """分离规则文档"""
    content = input_path.read_text(encoding='utf-8')
    
    # 匹配规则：规则 I.1.1.001【标题】
    rule_pattern = r'^(规则\s+[IV]+\.\d+\.\d+\.\d+【.+?】)(.*?)(?=^规则\s+[IV]+\.\d+\.\d+\.\d+【|^## |\Z)'
    
    matches = re.findall(rule_pattern, content, re.MULTILINE | re.DOTALL)
    
    pure_rules = []
    annotations = []
    
    for header, body in matches:
        # 提取规则ID和标题
        id_match = re.match(r'规则\s+([IV]+\.\d+\.\d+\.\d+)【(.+?)】', header)
        if not id_match:
            continue
        rule_id = id_match.group(1)
        title = id_match.group(2)
        
        # 分离核心内容和补充说明
        core_content = body
        supplementary = []
        
        # 查找补充说明标记
        markers = [
            ('**原理**', '原理'),
            ('**案例**', '案例'),
            ('**边界**', '边界'),
            ('**边界与例外**', '边界与例外'),
            ('**[English Version]**', '英文版'),
            ('---\n\n**', '分隔')
        ]
        
        for marker, label in markers:
            if marker in core_content:
                idx = core_content.find(marker)
                if idx > 0:
                    # 保存补充内容
                    supp = core_content[idx:]
                    # 截断到下一个规则或主要标记
                    for next_m, _ in markers:
                        if next_m != marker:
                            next_idx = supp[len(marker):].find(next_m)
                            if next_idx > 0:
                                supp = supp[:len(marker) + next_idx]
                    
                    supplementary.append((label, supp.strip()))
                    # 截断核心内容
                    core_content = core_content[:idx]
        
        # 清理
        core_content = core_content.strip()
        
        # 添加到纯规则
        if core_content:
            pure_rules.append(f"**{header}**\n{core_content}\n\n")
        
        # 添加到注释
        if supplementary:
            annotations.append(f"### {rule_id}【{title}】\n\n")
            for label, supp in supplementary:
                annotations.append(f"{supp}\n\n")
    
    # 保留文件头部
    header_match = re.match(r'^(.*?)(?=^规则\s+[IV]+\.\d+\.\d+\.\d+【|^## |$)', content, re.MULTILINE | re.DOTALL)
    file_header = header_match.group(1) if header_match else ""
    
    # 写入规则文件
    if pure_rules:
        rules_content = file_header + '\n' + ''.join(pure_rules)
        rules_output.write_text(rules_content, encoding='utf-8')
    
    # 写入注释文件
    if annotations:
        anno_content = f"# {input_path.stem} 补充说明\n\n"
        anno_content += f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        anno_content += ''.join(annotations)
        annotations_output.write_text(anno_content, encoding='utf-8')
    
    return len(pure_rules), len(annotations)

def main():
    rules_dir = Path('rules')
    anno_dir = Path('annotations')
    backup_dir = Path('meta/backup')
    
    anno_dir.mkdir(exist_ok=True)
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("文档分离工具")
    print("=" * 60)
    
    total_rules = 0
    total_anno = 0
    
    for md_file in sorted(rules_dir.glob('ARTICLES-*.md')):
        print(f"\n📄 {md_file.name}")
        
        # 备份
        shutil.copy(md_file, backup_dir / md_file.name)
        
        # 分离
        anno_file = anno_dir / f"{md_file.stem}-annotations.md"
        n_rules, n_anno = split_rule_document(md_file, md_file, anno_file)
        
        total_rules += n_rules
        total_anno += n_anno
        
        status = "✓" if n_rules > 0 else "⚠"
        print(f"   {status} 规则: {n_rules}, 注释: {n_anno}")
    
    print("\n" + "=" * 60)
    print(f"✅ 完成! 共 {total_rules} 条规则, {total_anno} 段注释")
    print("=" * 60)

if __name__ == '__main__':
    main()
