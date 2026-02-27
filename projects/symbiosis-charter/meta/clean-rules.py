#!/usr/bin/env python3
"""
规则清理工具 - 分离补充内容到annotations/
"""

import re
from pathlib import Path

WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter")
RULES_DIR = WORK_DIR / "rules"
ANNOTATIONS_DIR = WORK_DIR / "annotations"

def clean_rule_file(file_path: Path):
    """清理规则文件，分离补充内容"""
    content = file_path.read_text(encoding='utf-8')
    
    # 查找所有规则块
    rule_pattern = r'(\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【[^】]+】\*\*)(.*?)(?=\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【|\*\*## |\Z)'
    matches = list(re.finditer(rule_pattern, content, re.DOTALL))
    
    if not matches:
        return 0, 0
    
    # 需要移除的标记
    supplementary_markers = [
        (r'\*\*【原理\s*\|?\s*Principle】\*\*', '原理'),
        (r'\*\*【案例\s*\|?\s*Examples?】\*\*', '案例'),
        (r'\*\*【背景\s*\|?\s*Context】\*\*', '背景'),
        (r'\*\*【边界\s*\|?\s*Boundaries?】\*\*', '边界'),
        (r'\*\*【历史\s*\|?\s*History】\*\*', '历史'),
        (r'\*\*原理\*\*', '原理'),
        (r'\*\*案例\*\*', '案例'),
        (r'\*\*背景\*\*', '背景'),
        (r'\*\*边界\*\*', '边界'),
    ]
    
    cleaned_rules = []
    supplementary_content = []
    cleaned_count = 0
    
    for match in matches:
        header = match.group(1)
        body = match.group(2)
        
        # 提取规则ID和标题
        id_match = re.search(r'规则\s+([IVX]+\.\d+\.\d+\.\d+)【(.+?)】', header)
        if not id_match:
            continue
        
        rule_id = id_match.group(1)
        rule_title = id_match.group(2)
        
        # 分离补充内容
        clean_body = body
        rule_supp = []
        
        for pattern, label in supplementary_markers:
            # 查找标记位置
            marker_match = re.search(pattern + r'.*?(?=\*\*规则|\*\*## |\Z)', clean_body, re.DOTALL)
            if marker_match:
                supp_text = marker_match.group(0).strip()
                if supp_text and len(supp_text) > 10:
                    rule_supp.append(f"**{label}**: {supp_text[:500]}...")
                    # 从正文中移除
                    clean_body = clean_body[:marker_match.start()] + clean_body[marker_match.end():]
                    cleaned_count += 1
        
        # 移除英文大段内容（保留规则本身的英文定义，移除额外解释）
        # 检测是否有大段英文（超过200字符且包含多个句子）
        english_pattern = r'([A-Z][^.]*(?:\.\s+[A-Z][^.]*){3,})'
        for eng_match in re.finditer(english_pattern, clean_body):
            if len(eng_match.group(1)) > 200:
                # 这是额外的英文解释，移除
                clean_body = clean_body[:eng_match.start()] + clean_body[eng_match.end():]
                cleaned_count += 1
        
        # 清理后的规则
        cleaned_rules.append(f"{header}\n{clean_body.strip()}\n\n")
        
        # 如果有补充内容，记录下来
        if rule_supp:
            supplementary_content.append(f"### {rule_id}【{rule_title}】\n" + "\n".join(rule_supp) + "\n\n")
    
    # 重建规则文件（保留头部信息）
    header_match = re.match(r'^(.*?)(?=\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【|\Z)', content, re.MULTILINE | re.DOTALL)
    file_header = header_match.group(1) if header_match else ""
    
    new_content = file_header + '\n' + ''.join(cleaned_rules)
    
    # 写回规则文件
    file_path.write_text(new_content, encoding='utf-8')
    
    # 写入补充内容到annotations
    if supplementary_content:
        anno_path = ANNOTATIONS_DIR / f"{file_path.stem}-annotations.md"
        anno_content = f"# {file_path.stem} 补充说明\n\n"
        anno_content += "> 从规则文件中分离的原理、案例、背景等内容\n\n"
        anno_content += ''.join(supplementary_content)
        anno_path.write_text(anno_content, encoding='utf-8')
    
    return len(cleaned_rules), cleaned_count

def main():
    ANNOTATIONS_DIR.mkdir(exist_ok=True)
    
    files = [
        "ARTICLES-I-FUNDAMENTAL.md",
        "ARTICLES-II-PRODUCTIVITY.md",
        "ARTICLES-III-ENERGY.md",
        "ARTICLES-IV-ETHICAL-AGENCY.md",
    ]
    
    total_rules = 0
    total_cleaned = 0
    
    for filename in files:
        file_path = RULES_DIR / filename
        if file_path.exists():
            print(f"清理 {filename}...")
            rules, cleaned = clean_rule_file(file_path)
            total_rules += rules
            total_cleaned += cleaned
            print(f"  ✓ 保留 {rules} 条规则, 清理 {cleaned} 处补充内容")
    
    print(f"\n总计: {total_rules} 条规则, 清理 {total_cleaned} 处补充内容")
    print(f"补充内容已保存到 annotations/ 目录")

if __name__ == "__main__":
    main()
