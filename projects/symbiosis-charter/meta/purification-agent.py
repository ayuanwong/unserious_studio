#!/usr/bin/env python3
"""
Symbiosis Charter Rule Purification Agent
共生宪章规则纯化代理

MISSION: Keep rules/ directory clean - ONLY rules, no explanations

What This Agent Does:
1. REMOVES from rules/: Principles, cases, boundaries, explanations
2. MOVES to annotations/: All supplementary content
3. ANALYZES: Rule clarity, precision, logic, consistency
4. OPTIMIZES: Rule expression through deep thinking

What This Agent Does NOT Do:
- Does NOT add "principles" to rules
- Does NOT add "cases" to rules  
- Does NOT add "boundaries" to rules
- Does NOT add explanatory text to rules

Core Philosophy:
- Rules should be standalone, clear, actionable
- Explanations belong in annotations/
- Quality through precision, not verbosity
"""

import os
import sys
import time
import subprocess
import signal
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple

# Configuration
WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter")
RULES_DIR = WORK_DIR / "rules"
ANNOTATIONS_DIR = WORK_DIR / "annotations"
LOG_FILE = WORK_DIR / ".purification.log"
LOCK_FILE = WORK_DIR / ".purification.lock"
ITERATION_DELAY = 30  # 30 seconds between iterations

class RulePurifier:
    """Purifies rules: keeps only rule content, moves supplementary to annotations"""
    
    def __init__(self, work_dir: Path):
        self.work_dir = work_dir
        self.rules_dir = work_dir / "rules"
        self.annotations_dir = work_dir / "annotations"
        self.articles = [
            "ARTICLES-I-FUNDAMENTAL.md",
            "ARTICLES-II-PRODUCTIVITY.md",
            "ARTICLES-III-ENERGY.md",
            "ARTICLES-IV-ETHICAL-AGENCY.md",
            "ARTICLES-V-ADAPTIVE.md",
            "ARTICLES-VI-EXCEPTIONS.md",
            "ARTICLES-VII-OVERSIGHT.md"
        ]
    
    def log(self, message):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def extract_pure_rules(self, file_path: Path) -> Tuple[List[Dict], str]:
        """
        Extract pure rules from document
        Returns: (list of rules, supplementary content)
        """
        content = file_path.read_text(encoding='utf-8')
        
        # Match rule blocks: **规则 X.X.X.X【Title】** + content
        rule_pattern = r'(\*\*规则\s+[IV]+\.\d+\.\d+\.\d+【.+?】\*\*)(.*?)(?=\*\*规则|\*\*## |\Z)'
        matches = re.findall(rule_pattern, content, re.DOTALL)
        
        pure_rules = []
        supplementary_sections = []
        
        for header, body in matches:
            # Extract rule ID and title
            id_match = re.match(r'\*\*规则\s+([IV]+\.\d+\.\d+\.\d+)【(.+?)】\*\*', header)
            if not id_match:
                continue
            
            rule_id = id_match.group(1)
            rule_title = id_match.group(2)
            
            # Separate core rule from supplementary
            core_content = body
            supp_content = []
            
            # Markers that indicate supplementary content
            supplementary_markers = [
                '**原理**',
                '**案例**',
                '**示例**',
                '**边界**',
                '**边界与例外**',
                '**[English Version]**',
                '**英文版**',
                '**History**',
                '**背景**'
            ]
            
            for marker in supplementary_markers:
                if marker in core_content:
                    idx = core_content.find(marker)
                    if idx > 0:
                        # Extract supplementary
                        supp = core_content[idx:]
                        # Find where next section starts
                        next_idx = len(supp)
                        for next_marker in supplementary_markers:
                            if next_marker != marker:
                                pos = supp[len(marker):].find(next_marker)
                                if pos > 0:
                                    next_idx = min(next_idx, len(marker) + pos)
                        
                        supp_content.append(supp[:next_idx].strip())
                        # Remove from core
                        core_content = core_content[:idx]
            
            # Clean core content
            core_content = core_content.strip()
            
            if core_content:
                pure_rules.append({
                    'id': rule_id,
                    'title': rule_title,
                    'header': header,
                    'content': core_content
                })
            
            if supp_content:
                supplementary_sections.append({
                    'id': rule_id,
                    'title': rule_title,
                    'content': '\n\n'.join(supp_content)
                })
        
        # Build supplementary document
        supp_doc = ""
        if supplementary_sections:
            supp_doc = f"# {file_path.stem} 补充说明\n\n"
            supp_doc += f"> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
            supp_doc += "本文档包含规则的解释性内容：原理、案例、边界等。\n\n"
            supp_doc += "---\n\n"
            
            for sec in supplementary_sections:
                supp_doc += f"### {sec['id']}【{sec['title']}】\n\n"
                supp_doc += sec['content'] + "\n\n---\n\n"
        
        return pure_rules, supp_doc
    
    def analyze_rule_quality(self, rule: Dict) -> Dict:
        """Deep analysis of rule quality - returns score and improvement flag"""
        analysis = {
            'id': rule['id'],
            'title': rule['title'],
            'word_count': len(rule['content']),
            'score': 100,
            'needs_improvement': False,
            'issues': [],
            'improved_version': None
        }
        
        content = rule['content']
        original_content = content
        
        # Check 1: Length appropriateness (-10 to -20 points)
        if len(content) < 30:
            analysis['score'] -= 20
            analysis['issues'].append('Too short - lacks clarity')
            analysis['needs_improvement'] = True
        elif len(content) > 400:
            analysis['score'] -= 15
            analysis['issues'].append('Too long - needs conciseness')
            analysis['needs_improvement'] = True
        
        # Check 2: Clarity of requirements (-15 points)
        if not re.search(r'[必须|应当|禁止|不得|允许]', content):
            analysis['score'] -= 15
            analysis['issues'].append('No clear directive (必须/应当/禁止)')
            analysis['needs_improvement'] = True
        
        # Check 3: Specificity (-10 per vague term)
        vague_terms = ['适当', '合理', '必要', '相关', '等', '等等']
        found_vague = [t for t in vague_terms if t in content]
        if found_vague:
            analysis['score'] -= min(10 * len(found_vague), 30)
            analysis['issues'].append(f'Vague terms: {found_vague}')
            analysis['needs_improvement'] = True
        
        # Check 4: Structure (-5 points)
        if content.count('。') > 6:
            analysis['score'] -= 5
            analysis['issues'].append('Overly complex structure')
        
        # Check 5: Repetition (-10 points)
        sentences = [s.strip() for s in content.split('。') if len(s.strip()) > 5]
        if len(sentences) != len(set(sentences)):
            analysis['score'] -= 10
            analysis['issues'].append('Redundant content')
            analysis['needs_improvement'] = True
        
        # Check 6: Completeness
        if '包括' in content and '：' not in content and ':' not in content:
            analysis['score'] -= 5
            analysis['issues'].append('Incomplete enumeration')
        
        analysis['score'] = max(0, analysis['score'])
        
        # Generate improved version if needed
        if analysis['needs_improvement'] and analysis['score'] < 70:
            analysis['improved_version'] = self.generate_improved_rule(rule, analysis)
        
        return analysis
    
    def generate_improved_rule(self, rule: Dict, analysis: Dict) -> str:
        """Generate improved rule expression based on quality analysis"""
        original = rule['content']
        issues = analysis['issues']
        title = rule['title']
        
        # Core improvement logic based on issues
        improved = original
        
        # Fix 1: Add directive if missing
        if 'No clear directive' in str(issues):
            if '禁止' not in improved and '不得' not in improved:
                improved = re.sub(r'^(.{10,30})([，。])', r'\1必须\2', improved)
        
        # Fix 2: Remove vague terms and add specificity
        vague_replacements = {
            '适当的': '明确量化的',
            '合理的': '符合标准的',
            '必要的': '关键性的',
            '相关的': '直接关联的',
            '等。': '等具体类别。',
            '等等': '及其他明确规定的情形'
        }
        
        for vague, specific in vague_replacements.items():
            improved = improved.replace(vague, specific)
        
        # Fix 3: Improve structure with bullet points for lists
        if '：' in improved or ':' in improved:
            parts = re.split(r'([：:])', improved, 1)
            if len(parts) >= 3:
                intro = parts[0] + parts[1]
                items = parts[2]
                # Convert comma-separated to bullet points if long
                if len(items) > 60 and '、' in items:
                    items = items.replace('、', '\n- ')
                    improved = intro + '\n- ' + items
        
        # Fix 4: Remove redundancy
        sentences = [s.strip() for s in improved.split('。') if s.strip()]
        unique_sentences = []
        for s in sentences:
            if s not in unique_sentences:
                unique_sentences.append(s)
        improved = '。'.join(unique_sentences) + '。'
        
        # Ensure proper ending
        if not improved.endswith('。') and not improved.endswith('：'):
            improved += '。'
        
        return improved.strip()
    
    def purify_article(self, article_name: str) -> Dict:
        """Purify and improve a single article file"""
        file_path = self.rules_dir / article_name
        if not file_path.exists():
            return {'status': 'error', 'message': f'File not found: {article_name}'}
        
        self.log(f"Purifying {article_name}...")
        
        # Extract pure rules and supplementary
        pure_rules, supp_doc = self.extract_pure_rules(file_path)
        
        if not pure_rules:
            return {'status': 'error', 'message': 'No rules found'}
        
        # Analyze and improve each rule
        quality_reports = []
        improved_count = 0
        
        for i, rule in enumerate(pure_rules):
            report = self.analyze_rule_quality(rule)
            
            # If rule needs improvement and we have improved version, apply it
            if report['needs_improvement'] and report['improved_version']:
                old_content = rule['content']
                new_content = report['improved_version']
                
                # Only apply if significantly different
                if new_content != old_content and len(new_content) > 20:
                    pure_rules[i]['content'] = new_content
                    improved_count += 1
                    self.log(f"  → Improved {rule['id']}: {report['score']}pts → better expression")
            
            if report['issues']:
                quality_reports.append(report)
        
        # Rebuild rules document with improvements
        original_content = file_path.read_text(encoding='utf-8')
        header_match = re.match(r'^(.*?)(?=\*\*规则\s+[IV]+\.\d+\.\d+\.\d+【|## |$)', original_content, re.MULTILINE | re.DOTALL)
        file_header = header_match.group(1) if header_match else ""
        
        new_content = file_header + '\n'
        for rule in pure_rules:
            new_content += f"{rule['header']}\n{rule['content']}\n\n"
        
        # Write improved rules
        file_path.write_text(new_content, encoding='utf-8')
        
        # Write supplementary to annotations
        if supp_doc:
            anno_path = self.annotations_dir / f"{article_name.replace('.md', '-annotations.md')}"
            anno_path.write_text(supp_doc, encoding='utf-8')
        
        return {
            'status': 'success',
            'rules_preserved': len(pure_rules),
            'rules_improved': improved_count,
            'supplementary_moved': len(supp_doc) > 0,
            'quality_issues': len(quality_reports),
            'details': quality_reports
        }
    
    def run_purification_cycle(self):
        """Run one purification cycle"""
        self.log("\n" + "="*70)
        self.log("🧹 RULE PURIFICATION CYCLE")
        self.log("="*70)
        
        total_rules = 0
        total_supp = 0
        total_issues = 0
        
        for article in self.articles:
            result = self.purify_article(article)
            
            if result['status'] == 'success':
                total_rules += result['rules_preserved']
                if result['supplementary_moved']:
                    total_supp += 1
                total_issues += result['quality_issues']
                
                self.log(f"  ✓ {article}: {result['rules_preserved']} rules, " +
                        f"{result['quality_issues']} quality issues")
            else:
                self.log(f"  ✗ {article}: {result['message']}")
        
        self.log(f"\nSummary: {total_rules} rules purified, " +
                f"{total_supp} supplementary docs created, " +
                f"{total_issues} quality issues identified")
        
        return total_rules, total_issues

class PurificationDaemon:
    """Daemon that continuously purifies and optimizes rules"""
    
    def __init__(self):
        self.iteration = 0
        self.running = True
        self.purifier = RulePurifier(WORK_DIR)
    
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
                self.log(f"Another instance running (PID: {pid})")
                return False
            except (ValueError, OSError, ProcessLookupError):
                LOCK_FILE.unlink()
        return True
    
    def create_lock(self):
        with open(LOCK_FILE, "w") as f:
            f.write(str(os.getpid()))
    
    def remove_lock(self):
        if LOCK_FILE.exists():
            LOCK_FILE.unlink()
    
    def signal_handler(self, signum, frame):
        self.log(f"Received signal {signum}, stopping...")
        self.running = False
    
    def execute_purification(self):
        """Execute one purification cycle"""
        self.iteration += 1
        self.log(f"\n{'='*70}")
        self.log(f"🧹 PURIFICATION ITERATION #{self.iteration}")
        self.log(f"{'='*70}")
        
        # Run purification
        rules_count, issues_count = self.purifier.run_purification_cycle()
        
        # Commit changes
        self.commit_changes()
        
        self.log(f"{'='*70}")
        self.log(f"✓ Iteration #{self.iteration} complete")
        self.log(f"{'='*70}")
    
    def commit_changes(self):
        """Commit changes to git"""
        try:
            os.chdir(WORK_DIR)
            
            # Check if there are changes
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                self.log("Committing changes...")
                subprocess.run(["git", "add", "-A"], check=True)
                subprocess.run([
                    "git", "commit", "-m",
                    f"auto: rule purification iteration #{self.iteration}"
                ], check=True)
                subprocess.run(["git", "push", "origin", "main"], check=True)
                self.log("✓ Changes committed and pushed")
        except subprocess.CalledProcessError as e:
            self.log(f"Git operation failed: {e}")
    
    def run(self):
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        
        if not self.check_lock():
            sys.exit(1)
        
        self.create_lock()
        
        try:
            self.log("="*70)
            self.log("🧹 RULE PURIFICATION DAEMON STARTED")
            self.log("="*70)
            self.log("Mission: Keep rules/ clean, move supplementary to annotations/")
            self.log("Focus: Rule expression quality, clarity, precision")
            self.log(f"PID: {os.getpid()}")
            self.log("="*70)
            
            while self.running:
                self.execute_purification()
                
                # Sleep with interrupt handling
                for _ in range(ITERATION_DELAY):
                    if not self.running:
                        break
                    time.sleep(1)
                    
        finally:
            self.remove_lock()
            self.log("✓ Daemon stopped")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Symbiosis Charter Rule Purification")
    parser.add_argument("--once", action="store_true", help="Run one iteration and exit")
    parser.add_argument("--status", action="store_true", help="Check daemon status")
    parser.add_argument("--stop", action="store_true", help="Stop running daemon")
    
    args = parser.parse_args()
    
    if args.status:
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, 0)
                print(f"✓ Daemon running (PID: {pid})")
                if LOG_FILE.exists():
                    print("\nRecent activity:")
                    with open(LOG_FILE, "r") as f:
                        lines = f.readlines()
                        for line in lines[-10:]:
                            print("  " + line.rstrip())
            except:
                print("✗ Daemon not running")
        else:
            print("✗ Daemon not running")
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
        else:
            print("✗ Daemon not running")
        return
    
    daemon = PurificationDaemon()
    
    if args.once:
        daemon.execute_purification()
    else:
        daemon.run()

if __name__ == "__main__":
    main()
