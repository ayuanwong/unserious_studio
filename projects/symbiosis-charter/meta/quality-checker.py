#!/usr/bin/env python3
"""
立法质量检查器 - 基于宪法/法条起草规范
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter")
RULES_DIR = WORK_DIR / "rules"

class LegislativeQualityChecker:
    """检查规则是否符合立法起草规范"""
    
    # 规范用语检查
    LEGAL_TERMS = {
        'good': ['应当', '有权', '禁止', '不得', '可以', '必须'],
        'bad': ['应该', '需要', '适当', '合理', '必要', '相关', '等', '等等']
    }
    
    # 数字模式
    NUMBER_PATTERNS = [
        r'\d+\s*日',      # X日
        r'\d+\s*小时',   # X小时
        r'\d+\s*分钟',   # X分钟
        r'\d+\.\d+',     # 小数
        r'\d+%',          # 百分比
        r'\d+-\d+',       # 范围
    ]
    
    def __init__(self):
        self.issues = []
        self.score = 100
    
    def check_rule(self, rule_text: str) -> Dict:
        """检查单条规则质量"""
        self.issues = []
        self.score = 100
        
        # 检查1: 是否有模糊词
        for bad_word in self.LEGAL_TERMS['bad']:
            if bad_word in rule_text:
                self.issues.append(f"使用模糊词'{bad_word}'，建议替换为具体数值或标准")
                self.score -= 5
        
        # 检查2: 是否有规范用语
        has_legal_term = any(term in rule_text for term in self.LEGAL_TERMS['good'])
        if not has_legal_term:
            self.issues.append("缺少规范用语(应当/有权/禁止/不得/可以)")
            self.score -= 10
        
        # 检查3: 是否有具体数字
        has_number = any(re.search(pattern, rule_text) for pattern in self.NUMBER_PATTERNS)
        if not has_number:
            self.issues.append("缺少具体数值，建议添加量化标准")
            self.score -= 8
        
        # 检查4: 是否过短（缺乏具体内容）
        if len(rule_text) < 80:
            self.issues.append("规则内容过短，建议补充具体措施")
            self.score -= 10
        
        # 检查5: 是否过长（可能包含多个事项）
        if len(rule_text) > 500:
            self.issues.append("规则内容过长，建议拆分为多条规则")
            self.score -= 5
        
        # 检查6: 是否有子项结构（a/b/c/d）
        has_subitems = bool(re.search(r'[a-e]\)', rule_text))
        if not has_subitems and len(rule_text) > 150:
            self.issues.append("复杂规则建议使用子项结构(a/b/c/d)分条列出")
            self.score -= 3
        
        # 检查7: 是否重复用词
        sentences = re.split(r'[。；]', rule_text)
        for i, s1 in enumerate(sentences):
            for s2 in sentences[i+1:]:
                if s1.strip() and s1.strip() == s2.strip():
                    self.issues.append("存在重复句子")
                    self.score -= 5
                    break
        
        # 检查8: 中英文格式
        if '**Rule' in rule_text or '**规则' in rule_text:
            # 检查是否有英文翻译
            if not re.search(r'[a-zA-Z]{10,}', rule_text):
                self.issues.append("标注为双语规则但缺少英文内容")
                self.score -= 5
        
        self.score = max(0, self.score)
        
        return {
            'score': self.score,
            'issues': self.issues,
            'is_good': self.score >= 80,
            'is_excellent': self.score >= 90
        }
    
    def check_file(self, file_path: Path) -> Tuple[int, int, List[Dict]]:
        """检查整个文件"""
        content = file_path.read_text(encoding='utf-8')
        
        # 提取所有规则
        rule_pattern = r'\*\*规则\s+([IVX]+\.\d+\.\d+\.\d+【[^】]+】)\*\*(.*?)(?=\*\*规则|\*\*## |\Z)'
        matches = list(re.finditer(rule_pattern, content, re.DOTALL))
        
        results = []
        good_count = 0
        
        for match in matches:
            rule_id = match.group(1)
            rule_content = match.group(2).strip()
            
            check_result = self.check_rule(rule_content)
            check_result['rule_id'] = rule_id
            results.append(check_result)
            
            if check_result['is_good']:
                good_count += 1
        
        return len(matches), good_count, results
    
    def generate_report(self, file_path: Path) -> str:
        """生成质量报告"""
        total, good, results = self.check_file(file_path)
        
        report = f"# 立法质量检查报告: {file_path.name}\n\n"
        report += f"总规则数: {total}\n"
        report += f"优质规则(≥80分): {good} ({good/total*100:.1f}%)\n"
        report += f"需改进规则: {total-good}\n\n"
        
        # 按分数排序
        results.sort(key=lambda x: x['score'])
        
        report += "## 低质量规则 (需优先改进)\n\n"
        for r in results[:10]:
            if r['score'] < 80:
                report += f"### {r['rule_id']} - 得分: {r['score']}\n"
                for issue in r['issues']:
                    report += f"- {issue}\n"
                report += "\n"
        
        report += "## 优秀规则示例\n\n"
        excellent = [r for r in results if r['is_excellent']]
        for r in excellent[:5]:
            report += f"- {r['rule_id']} (得分: {r['score']})\n"
        
        return report

def main():
    checker = LegislativeQualityChecker()
    
    files = list(RULES_DIR.glob("ARTICLES-*.md"))
    
    total_rules = 0
    total_good = 0
    
    for file_path in files:
        print(f"\n检查 {file_path.name}...")
        total, good, results = checker.check_file(file_path)
        total_rules += total
        total_good += good
        
        # 生成报告
        report = checker.generate_report(file_path)
        report_path = WORK_DIR / "meta" / f"quality-report-{file_path.stem}.md"
        report_path.write_text(report, encoding='utf-8')
        
        print(f"  规则数: {total}, 优质: {good} ({good/total*100:.1f}%)")
        print(f"  报告: {report_path}")
    
    print(f"\n{'='*50}")
    print(f"总计: {total_rules} 条规则")
    print(f"优质: {total_good} 条 ({total_good/total_rules*100:.1f}%)")
    print(f"需改进: {total_rules-total_good} 条")

if __name__ == "__main__":
    main()
