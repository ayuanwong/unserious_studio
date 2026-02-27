#!/usr/bin/env python3
"""
Remove all supplementary content from rules
"""

import re
from pathlib import Path

WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter")
RULES_DIR = WORK_DIR / "rules"
ANNOTATIONS_DIR = WORK_DIR / "annotations"
ANNOTATIONS_DIR.mkdir(exist_ok=True)

def clean_file(file_path: Path):
    """Clean a single rule file"""
    content = file_path.read_text(encoding='utf-8')
    
    # Find all rules and their supplementary content
    # Pattern: from **规则... to next **规则 or end
    rule_blocks = []
    pos = 0
    
    # Find all rule headers
    rule_headers = list(re.finditer(r'\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【[^】]+】\*\*', content))
    
    all_supplementary = []
    cleaned_blocks = []
    
    for i, header_match in enumerate(rule_headers):
        start = header_match.start()
        # Find end (next header or end of file)
        if i + 1 < len(rule_headers):
            end = rule_headers[i + 1].start()
        else:
            end = len(content)
        
        block = content[start:end]
        header = header_match.group(0)
        
        # Extract rule ID
        id_match = re.search(r'规则\s+([IVX]+\.\d+\.\d+\.\d+)', header)
        rule_id = id_match.group(1) if id_match else "Unknown"
        
        # Split block into core and supplementary
        # Find where supplementary starts (--- or **原则 etc)
        supp_start_patterns = [
            r'\n---\s*\n\s*\*\*原则',
            r'\n---\s*\n\s*\*\*示例',
            r'\n---\s*\n\s*\*\*边界',
            r'\n---\s*\n\s*\*\*情境',
            r'\n---\s*\n\s*\*\*Principle',
            r'\n---\s*\n\s*\*\*Example',
            r'\n---\s*\n\s*\*\*Boundary',
            r'\n---\s*\n\s*\*\*Context',
        ]
        
        supp_start = None
        for pattern in supp_start_patterns:
            match = re.search(pattern, block)
            if match:
                supp_start = match.start()
                break
        
        if supp_start:
            core_content = block[:supp_start]
            supp_content = block[supp_start:]
            
            # Save supplementary
            all_supplementary.append(f"## {rule_id}\n{supp_content}\n")
            cleaned_blocks.append(core_content)
        else:
            cleaned_blocks.append(block)
    
    # Rebuild file
    # Get header (before first rule)
    if rule_headers:
        header_end = rule_headers[0].start()
        file_header = content[:header_end]
    else:
        file_header = ""
    
    new_content = file_header + ''.join(cleaned_blocks)
    
    # Clean up
    new_content = re.sub(r'\n{4,}', '\n\n\n', new_content)
    new_content = re.sub(r'\n\n---\n\n---', '\n\n---', new_content)
    
    # Write back
    file_path.write_text(new_content, encoding='utf-8')
    
    # Save supplementary
    if all_supplementary:
        supp_file = ANNOTATIONS_DIR / f"{file_path.stem}-principles-examples.md"
        supp_content = f"# {file_path.stem} - Principles, Examples, Boundaries, Context\n\n"
        supp_content += ''.join(all_supplementary)
        supp_file.write_text(supp_content, encoding='utf-8')
    
    return len(all_supplementary)

# Clean all files
total_cleaned = 0
for file_path in sorted(RULES_DIR.glob("ARTICLES-*.md")):
    print(f"Processing {file_path.name}...")
    cleaned = clean_file(file_path)
    total_cleaned += cleaned
    print(f"  ✓ Removed {cleaned} supplementary sections")

print(f"\n✅ Total: {total_cleaned} supplementary sections removed")
print(f"📁 Saved to annotations/*-principles-examples.md")
