#!/usr/bin/env python3
import re
from pathlib import Path

RULES_DIR = Path("rules")
ANNOTATIONS_DIR = Path("annotations")
ANNOTATIONS_DIR.mkdir(exist_ok=True)

for file in RULES_DIR.glob("ARTICLES-*.md"):
    content = file.read_text(encoding='utf-8')
    original_len = len(content)
    
    # Remove supplementary sections
    # Match: newline + **原则/示例/边界/情境 (Label):** + content until next section
    patterns = [
        r'\n\n---\n\n\*\*原则\s*\([^)]+\):\*\*.*?\n(?=\*\*规则|\Z)',
        r'\n\n---\n\n\*\*示例\s*\([^)]+\):\*\*.*?\n(?=\*\*规则|\Z)',
        r'\n\n---\n\n\*\*边界\s*\([^)]+\):\*\*.*?\n(?=\*\*规则|\Z)',
        r'\n\n---\n\n\*\*情境\s*\([^)]+\):\*\*.*?\n(?=\*\*规则|\Z)',
        r'\n\n\*\*原则\s*\([^)]+\):\*\*.*?\n(?=\*\*规则|\Z)',
        r'\n\n\*\*示例\s*\([^)]+\):\*\*.*?\n(?=\*\*规则|\Z)',
        r'\n\n\*\*边界\s*\([^)]+\):\*\*.*?\n(?=\*\*规则|\Z)',
        r'\n\n\*\*情境\s*\([^)]+\):\*\*.*?\n(?=\*\*规则|\Z)',
    ]
    
    cleaned = content
    for pattern in patterns:
        cleaned = re.sub(pattern, '\n\n', cleaned, flags=re.DOTALL)
    
    # Clean up
    cleaned = re.sub(r'\n{4,}', '\n\n\n', cleaned)
    
    if len(cleaned) < original_len:
        file.write_text(cleaned, encoding='utf-8')
        print(f"✓ {file.name}: removed {original_len - len(cleaned)} chars ({(original_len-len(cleaned))/original_len*100:.1f}%)")
    else:
        print(f"- {file.name}: no changes ({len(cleaned)} chars)")

print("\n✅ Cleaning complete!")
