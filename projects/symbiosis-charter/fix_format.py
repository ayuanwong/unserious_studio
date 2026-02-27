import re
from pathlib import Path

rules_dir = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter/rules")

for file in ["ARTICLES-II-PRODUCTIVITY.md", "ARTICLES-IV-ETHICAL-AGENCY.md", 
             "ARTICLES-V-ADAPTIVE.md", "ARTICLES-VI-EXCEPTIONS.md", "ARTICLES-VII-OVERSIGHT.md"]:
    path = rules_dir / file
    if not path.exists():
        print(f"File not found: {file}")
        continue
    
    content = path.read_text(encoding='utf-8')
    
    # 查找规则行并添加 ** 标记
    # 匹配 "规则 X.x.x.x【标题】" 格式的行
    pattern = r'^(规则\s+[IVX]+\.\d+\.\d+\.\d+【[^】]+】)$'
    
    def add_bold(match):
        return f"**{match.group(1)}**"
    
    new_content = re.sub(pattern, add_bold, content, flags=re.MULTILINE)
    
    # 统计修改数量
    old_count = len(re.findall(pattern, content, re.MULTILINE))
    new_count = len(re.findall(r'\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【[^】]+】\*\*', new_content))
    
    path.write_text(new_content, encoding='utf-8')
    print(f"{file}: 修复 {old_count} 条规则格式 -> 现在有 {new_count} 条")

print("\n修复完成！")
