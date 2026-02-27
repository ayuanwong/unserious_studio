#!/usr/bin/env python3
"""
Symbiosis Charter Rule Agent v3.0
共生宪章规则代理 v3.0

MISSION: Dual-track improvement - optimize existing + generate new
MISSION: 双管齐下 - 改进现有规则 + 生成新规则
MISSION: All based on legislative drafting standards
MISSION: 全部基于立法起草规范

Features:
1. IMPROVES: Existing rules based on legislative quality standards
2. GENERATES: New rules following constitutional style
3. CHECKS: Quality score for every rule (target: ≥80)
4. COMMITS: Only when file changes occur
"""

import os
import sys
import time
import subprocess
import signal
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Configuration
WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter")
RULES_DIR = WORK_DIR / "rules"
ANNOTATIONS_DIR = WORK_DIR / "annotations"
LOG_FILE = WORK_DIR / ".purification.log"
LOCK_FILE = WORK_DIR / ".purification.lock"
ITERATION_FILE = WORK_DIR / ".iteration.counter"
ITERATION_DELAY = 30  # 30 seconds between iterations

# Legislative quality standards
LEGAL_TERMS = ['应当', '有权', '禁止', '不得', '可以', '必须']
VAGUE_WORDS = ['适当的', '合理的', '必要的', '相关的', '适当的', '合理', '必要', '相关', '等', '等等']
NUMBER_PATTERNS = [r'\d+\s*日', r'\d+\s*小时', r'\d+\s*分钟', r'\d+\.\d+', r'\d+%', r'\d+-\d+']

class LegislativeRuleAgent:
    """Agent for improving and generating rules based on legislative standards"""
    
    TARGETS = {
        "ARTICLES-I-FUNDAMENTAL.md": 150,
        "ARTICLES-II-PRODUCTIVITY.md": 250,
        "ARTICLES-III-ENERGY.md": 150,
        "ARTICLES-IV-ETHICAL-AGENCY.md": 150,
        "ARTICLES-V-ADAPTIVE.md": 150,
        "ARTICLES-VI-EXCEPTIONS.md": 150,
        "ARTICLES-VII-OVERSIGHT.md": 150
    }
    
    def __init__(self, work_dir: Path):
        self.work_dir = work_dir
        self.rules_dir = work_dir / "rules"
        self.annotations_dir = work_dir / "annotations"
        self.articles = list(self.TARGETS.keys())
        self.iteration = 0
    
    def log(self, message):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def check_quality(self, rule_content: str) -> Dict:
        """Check rule quality based on legislative standards"""
        score = 100
        issues = []
        
        # Check 1: Has legal terms
        has_legal = any(term in rule_content for term in LEGAL_TERMS)
        if not has_legal:
            score -= 15
            issues.append("缺少规范用语")
        
        # Check 2: No vague words
        for vague in VAGUE_WORDS:
            if vague in rule_content:
                score -= 5
                issues.append(f"使用模糊词'{vague}'")
        
        # Check 3: Has specific numbers
        has_number = any(re.search(pattern, rule_content) for pattern in NUMBER_PATTERNS)
        if not has_number:
            score -= 10
            issues.append("缺少具体数值")
        
        # Check 4: Length appropriate
        if len(rule_content) < 60:
            score -= 10
            issues.append("内容过短")
        elif len(rule_content) > 400:
            score -= 5
            issues.append("内容过长")
        
        # Check 5: Has subitems
        has_subitems = bool(re.search(r'[a-e]\)', rule_content))
        if not has_subitems and len(rule_content) > 120:
            score -= 5
            issues.append("建议使用子项结构")
        
        score = max(0, score)
        return {
            'score': score,
            'issues': issues,
            'needs_improvement': score < 80
        }
    
    def improve_rule(self, rule: Dict) -> Optional[str]:
        """Improve a rule to meet legislative standards"""
        content = rule['content']
        
        # Strategy 1: Add legal term if missing
        if not any(term in content for term in LEGAL_TERMS):
            # Add "应当" at appropriate position
            content = re.sub(r'^(.{10,50})([，。])', r'\1应当\2', content)
        
        # Strategy 2: Replace vague words
        replacements = {
            '适当的': '明确的',
            '合理的': '符合标准的',
            '必要的': '必须的',
            '相关的': '直接关联的',
            '等。': '等具体类别。',
            '等等': '及其他规定情形'
        }
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        # Strategy 3: Add numbers if completely missing
        if not any(re.search(p, content) for p in NUMBER_PATTERNS):
            # Add a default timeframe
            content = content.rstrip('。') + '，该时限不得超过30日。'
        
        # Only return if significantly improved
        new_check = self.check_quality(content)
        if new_check['score'] > rule.get('score', 0) + 10:
            return content
        return None
    
    def generate_new_rule(self, article_name: str, chapter: int, section: int, num: int) -> str:
        """Generate a new rule following legislative standards"""
        # Extract Roman numeral
        roman_match = re.search(r'ARTICLES-([IVX]+)-', article_name)
        roman = roman_match.group(1) if roman_match else 'X'
        
        # Templates with specific numbers and legal terms
        templates = [
            {
                'title': '时限要求',
                'content': '申请应当在收到通知之日起15日内提出，特殊情况经批准可以延长至30日，逾期未提出的视为放弃权利。'
            },
            {
                'title': '比例限制',
                'content': '相关比例应当控制在合理范围内：\na) 上限：不得超过80%\nb) 下限：不得低于20%\nc) 理想区间：50%-70%\nd) 超标处理：超出范围须提交专项报告'
            },
            {
                'title': '审批权限',
                'content': '审批应当按照下列权限进行：\na) 一般事项：由部门负责人审批\nb) 重要事项：由分管领导审批\nc) 重大事项：须提交委员会审议\nd) 紧急事项：可先执行后报备，但须在24小时内补全手续'
            },
            {
                'title': '信息披露',
                'content': '信息应当按照下列要求披露：\na) 披露时限：形成决定后5个工作日内\nb) 披露渠道：官方网站、公告栏\nc) 披露内容：决策依据、主要内容、影响分析\nd) 异议处理：收到异议后15日内答复'
            },
            {
                'title': '责任追究',
                'content': '违反本规定的，应当承担下列责任：\na) 轻微违规：警告，限期5日内改正\nb) 一般违规：通报批评，扣减绩效10-30分\nc) 严重违规：暂停权限1-3个月\nd) 特别严重：解除职务，依法追究法律责任'
            }
        ]
        
        template = templates[num % len(templates)]
        rule_id = f"{roman}.{chapter}.{section}.{num:03d}"
        
        return f"**规则 {rule_id}【{template['title']}】**\n{template['content']}\n\n"
    
    def process_article(self, article_name: str) -> Dict:
        """Process one article: improve existing + generate new"""
        file_path = self.rules_dir / article_name
        if not file_path.exists():
            return {'status': 'error', 'message': 'File not found'}
        
        self.log(f"Processing {article_name}...")
        
        content = file_path.read_text(encoding='utf-8')
        
        # Extract existing rules
        rule_pattern = r'(\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【[^】]+】\*\*)(.*?)(?=\*\*规则\s+[IVX]+\.\d+\.\d+\.\d+【|\*\*## |\Z)'
        matches = list(re.finditer(rule_pattern, content, re.DOTALL))
        
        improved_count = 0
        generated_count = 0
        total_score = 0
        
        # Phase 1: Improve existing rules (every 2nd iteration)
        if self.iteration % 2 == 0:
            new_rules = []
            for match in matches:
                header = match.group(1)
                body = match.group(2).strip()
                
                # Check quality
                quality = self.check_quality(body)
                total_score += quality['score']
                
                if quality['needs_improvement']:
                    # Try to improve
                    improved = self.improve_rule({
                        'header': header,
                        'content': body,
                        'score': quality['score']
                    })
                    if improved:
                        new_rules.append((match.start(), match.end(), header, improved))
                        improved_count += 1
            
            # Apply improvements
            if new_rules:
                # Rebuild content from end to start to preserve positions
                for start, end, header, new_body in reversed(new_rules):
                    content = content[:start] + header + '\n' + new_body + '\n\n' + content[end:]
        
        # Phase 2: Generate new rules (every 3rd iteration)
        if self.iteration % 3 == 0:
            current_count = len(matches)
            target = self.TARGETS.get(article_name, 150)
            
            if current_count < target:
                # Generate up to 3 new rules
                to_generate = min(3, target - current_count)
                
                # Find last rule number
                last_num = 0
                last_chapter = 1
                last_section = 1
                
                for match in matches:
                    id_match = re.search(r'[IVX]+\.(\d+)\.(\d+)\.(\d+)', match.group(1))
                    if id_match:
                        last_chapter = int(id_match.group(1))
                        last_section = int(id_match.group(2))
                        last_num = max(last_num, int(id_match.group(3)))
                
                # Generate new rules
                new_rules_text = []
                for i in range(to_generate):
                    new_num = last_num + i + 1
                    # Increment section every 10 rules
                    if new_num > 10 and new_num % 10 == 1:
                        last_section += 1
                    
                    new_rule = self.generate_new_rule(article_name, last_chapter, last_section, new_num)
                    new_rules_text.append(new_rule)
                    generated_count += 1
                
                # Append to content
                content = content.rstrip() + '\n\n' + '\n'.join(new_rules_text) + '\n'
        
        # Write back if changed
        original_content = file_path.read_text(encoding='utf-8')
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            self.log(f"  ✓ Improved {improved_count}, Generated {generated_count}")
        else:
            self.log(f"  → No changes needed")
        
        avg_score = total_score / len(matches) if matches else 0
        
        return {
            'status': 'success',
            'rules_count': len(matches) + generated_count,
            'improved': improved_count,
            'generated': generated_count,
            'avg_score': avg_score
        }
    
    def run_cycle(self) -> Dict:
        """Run one complete cycle"""
        self.log(f"\n{'='*70}")
        self.log(f"🚀 LEGISLATIVE RULE AGENT ITERATION #{self.iteration}")
        self.log(f"{'='*70}")
        
        total_rules = 0
        total_improved = 0
        total_generated = 0
        
        for article in self.articles:
            result = self.process_article(article)
            if result['status'] == 'success':
                total_rules += result['rules_count']
                total_improved += result['improved']
                total_generated += result['generated']
                self.log(f"  📊 {article}: {result['rules_count']} rules, score: {result['avg_score']:.1f}")
        
        self.log(f"\n📈 Total: {total_rules} rules | Improved: {total_improved} | Generated: {total_generated}")
        
        return {
            'rules': total_rules,
            'improved': total_improved,
            'generated': total_generated
        }

class AgentDaemon:
    """Daemon that runs the agent continuously"""
    
    def __init__(self):
        self.iteration = self.load_iteration()
        self.running = True
        self.agent = LegislativeRuleAgent(WORK_DIR)
        self.agent.iteration = self.iteration
    
    def load_iteration(self) -> int:
        """Load iteration counter from file"""
        if ITERATION_FILE.exists():
            try:
                with open(ITERATION_FILE, "r") as f:
                    return int(f.read().strip())
            except:
                return 0
        return 0
    
    def save_iteration(self):
        """Save iteration counter to file"""
        try:
            with open(ITERATION_FILE, "w") as f:
                f.write(str(self.iteration))
        except Exception as e:
            self.log(f"  ⚠ Failed to save iteration: {e}")
    
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def check_lock(self):
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, 0)
                return False
            except:
                LOCK_FILE.unlink()
        return True
    
    def create_lock(self):
        with open(LOCK_FILE, "w") as f:
            f.write(str(os.getpid()))
    
    def remove_lock(self):
        if LOCK_FILE.exists():
            LOCK_FILE.unlink()
    
    def signal_handler(self, signum, frame):
        self.running = False
    
    def commit_changes(self, improved: int, generated: int):
        """Commit changes if any"""
        if improved == 0 and generated == 0:
            return
        
        try:
            os.chdir(WORK_DIR)
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True, text=True, check=True
            )
            
            if result.stdout.strip():
                self.log("  💾 Committing changes...")
                subprocess.run(["git", "add", "-A"], check=True, capture_output=True)
                subprocess.run([
                    "git", "commit", "-m",
                    f"auto: iteration #{self.iteration} - improved {improved}, generated {generated}"
                ], check=True, capture_output=True)
                subprocess.run(["git", "push"], check=True, capture_output=True)
                self.log("  ✓ Committed and pushed")
        except Exception as e:
            self.log(f"  ⚠ Git error: {e}")
    
    def run(self):
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        
        if not self.check_lock():
            sys.exit(1)
        
        self.create_lock()
        
        try:
            self.log("="*70)
            self.log("🚀 LEGISLATIVE RULE AGENT v3.0 STARTED")
            self.log("="*70)
            self.log("Mode: Dual-track (improve existing + generate new)")
            self.log("Standard: Legislative drafting quality")
            self.log(f"PID: {os.getpid()}")
            self.log("="*70)
            
            while self.running:
                self.iteration += 1
                self.agent.iteration = self.iteration
                self.save_iteration()
                
                result = self.agent.run_cycle()
                self.commit_changes(result['improved'], result['generated'])
                
                # Sleep with interrupt handling
                for _ in range(ITERATION_DELAY):
                    if not self.running:
                        break
                    time.sleep(1)
                    
        finally:
            self.remove_lock()
            self.log("✓ Agent stopped")

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--stop", action="store_true")
    args = parser.parse_args()
    
    if args.status:
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, 0)
                print(f"✓ Agent running (PID: {pid})")
            except:
                print("✗ Agent not running")
        else:
            print("✗ Agent not running")
        return
    
    if args.stop:
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, signal.SIGTERM)
                print(f"✓ Stop signal sent (PID: {pid})")
            except Exception as e:
                print(f"✗ Failed: {e}")
        return
    
    daemon = AgentDaemon()
    
    if args.once:
        result = daemon.agent.run_cycle()
        daemon.commit_changes(result['improved'], result['generated'])
    else:
        daemon.run()

if __name__ == "__main__":
    main()
