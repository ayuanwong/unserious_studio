#!/usr/bin/env python3
"""
深度清理规则文件 - 移除所有非核心内容
保留：规则标题 + 核心定义/要求
移除：原则、示例、边界、情境、背景等
"""

import re
from pathlib import Path

WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter")
RULES_DIR = WORK_DIR / "rules"
ANNOTATIONS_DIR = WORK_DIR / "annotations"

def deep_clean_rules(file_path: Path):
    """深度清理规则文件"""
    content = file_path.read_text(encoding='utf-8')
    
    # 查找所有规则块
    rule_pattern = r'(\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【[^】]+】\*\*)(.*?)(?=\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【|\*\*## |\Z)'
    matches = list(re.finditer(rule_pattern, content, re.DOTALL))
    
    if not matches:
        return 0, 0
    
    # 需要移除的标记（更多模式）
    supplementary_patterns = [
        (r'\*\*原则\s*\([^)]+\)\s*\*\*.*?(?=\*\*规则|\*\*## |\Z)', '原则'),
        (r'\*\*示例\s*\([^)]+\)\s*\*\*.*?(?=\*\*规则|\*\*## |\Z)', '示例'),
        (r'\*\*边界\s*\([^)]+\)\s*\*\*.*?(?=\*\*规则|\*\*## |\Z)', '边界'),
        (r'\*\*情境\s*\([^)]+\)\s*\*\*.*?(?=\*\*规则|\*\*## |\Z)', '情境'),
        (r'\*\*背景\s*\([^)]+\)\s*\*\*.*?(?=\*\*规则|\*\*## |\Z)', '背景'),
        (r'\*\*原理\s*\([^)]+\)\s*\*\*.*?(?=\*\*规则|\*\*## |\Z)', '原理'),
        (r'\*\*Principle[:\s]*\*\*.*?(?=\*\*规则|\*\*## |\Z)', 'Principle'),
        (r'\*\*Example[:\s]*\*\*.*?(?=\*\*规则|\*\*## |\Z)', 'Example'),
        (r'\*\*Boundary[:\s]*\*\*.*?(?=\*\*规则|\*\*## |\Z)', 'Boundary'),
        (r'\*\*Context[:\s]*\*\*.*?(?=\*\*规则|\*\*## |\Z)', 'Context'),
        (r'---\s*\n\s*\*\*[^*]+\*\*.*?(?=\*\*规则|\*\*## |\Z)', 'separator_block'),
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
        
        for pattern, label in supplementary_patterns:
            while True:
                supp_match = re.search(pattern, clean_body, re.DOTALL | re.IGNORECASE)
                if not supp_match:
                    break
                
                supp_text = supp_match.group(0).strip()
                if len(supp_text) > 20:
                    # 截取前500字符保存
                    truncated = supp_text[:500] + "..." if len(supp_text) > 500 else supp_text
                    rule_supp.append(f"**{label}**: {truncated}")
                    cleaned_count += 1
                
                # 从正文中移除
                clean_body = clean_body[:supp_match.start()] + clean_body[supp_match.end():]
        
        # 移除多余的空行和分隔符
        clean_body = re.sub(r'\n{3,}', '\n\n', clean_body)
        clean_body = re.sub(r'^---\s*$', '', clean_body, flags=re.MULTILINE)
        
        # 清理后的规则
        cleaned_rules.append(f"{header}\n{clean_body.strip()}\n\n")
        
        # 如果有补充内容，记录下来
        if rule_supp:
            supplementary_content.append(f"### {rule_id}【{rule_title}】\n" + "\n".join(rule_supp) + "\n\n")
    
    # 重建规则文件（保留头部信息）
    header_match = re.match(r'^(.*?)(?=\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【|\Z)', content, re.MULTILINE | re.DOTALL)
    file_header = header_match.group(1) if header_match else ""
    
    new_content = file_header + '\n' + ''.join(cleaned_rules)
    
    # 移除多余的空行
    new_content = re.sub(r'\n{4,}', '\n\n\n', new_content)
    
    # 写回规则文件
    file_path.write_text(new_content, encoding='utf-8')
    
    # 写入补充内容到annotations
    if supplementary_content:
        anno_path = ANNOTATIONS_DIR / f"{file_path.stem}-supplementary.md"
        anno_content = f"# {file_path.stem} 补充内容\n\n"
        anno_content += "> 包含原则、示例、边界、情境等解释性内容\n\n"
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
        "ARTICLES-V-ADAPTIVE.md",
        "ARTICLES-VI-EXCEPTIONS.md",
        "ARTICLES-VII-OVERSIGHT.md"
    ]
    
    total_rules = 0
    total_cleaned = 0
    
    for filename in files:
        file_path = RULES_DIR / filename
        if file_path.exists():
            print(f"深度清理 {filename}...")
            rules, cleaned = deep_clean_rules(file_path)
            total_rules += rules
            total_cleaned += cleaned
            print(f"  ✓ 保留 {rules} 条规则, 清理 {cleaned} 处补充内容")
    
    print(f"\n总计: {total_rules} 条规则")
    print(f"清理 {total_cleaned} 处补充内容到 annotations/")

if __name__ == "__main__":
    main()
