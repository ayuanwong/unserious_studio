#!/usr/bin/env python3
"""
Symbiosis Charter Rule Purification Agent
共生宪章规则纯化代理

Purpose: Ensure rules/ directory contains ONLY rules
Purpose: Move all supplementary content to annotations/
Purpose: Optimize rule expression for clarity and precision

Core Principles:
1. Rules document = ONLY rules (no principles, no cases, no boundaries)
2. Supplementary content → annotations/ directory
3. Deep thinking: analyze rule quality, logic, consistency
4. Iterative refinement of rule expression
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
ITERATION_DELAY = 120  # 2 minutes between iterations

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
        """Deep analysis of rule quality"""
        analysis = {
            'id': rule['id'],
            'title': rule['title'],
            'word_count': len(rule['content']),
            'issues': [],
            'suggestions': []
        }
        
        content = rule['content']
        
        # Check 1: Length appropriateness
        if len(content) < 50:
            analysis['issues'].append('Too short')
            analysis['suggestions'].append('Expand to clarify scope and requirements')
        elif len(content) > 500:
            analysis['issues'].append('Too long')
            analysis['suggestions'].append('Consider splitting into multiple rules')
        
        # Check 2: Clarity of requirements
        if not re.search(r'[必须|应当|禁止|允许]', content):
            analysis['issues'].append('No clear obligation')
            analysis['suggestions'].append('Add clear directive (must/should/shall)')
        
        # Check 3: Specificity
        vague_terms = ['适当', '合理', '必要', '相关']
        found_vague = [t for t in vague_terms if t in content]
        if found_vague:
            analysis['issues'].append(f'Vague terms: {found_vague}')
            analysis['suggestions'].append('Replace with quantifiable criteria')
        
        # Check 4: Structure
        if content.count('。') > 5:
            analysis['issues'].append('Too many sentences')
            analysis['suggestions'].append('Consider bullet points for clarity')
        
        # Check 5: Redundancy
        sentences = content.split('。')
        unique_sentences = set(s.strip() for s in sentences if len(s.strip()) > 10)
        if len(sentences) != len(unique_sentences):
            analysis['issues'].append('Potential redundancy')
        
        return analysis
    
    def purify_article(self, article_name: str) -> Dict:
        """Purify a single article file"""
        file_path = self.rules_dir / article_name
        if not file_path.exists():
            return {'status': 'error', 'message': f'File not found: {article_name}'}
        
        self.log(f"Purifying {article_name}...")
        
        # Extract pure rules and supplementary
        pure_rules, supp_doc = self.extract_pure_rules(file_path)
        
        if not pure_rules:
            return {'status': 'error', 'message': 'No rules found'}
        
        # Analyze each rule
        quality_reports = []
        for rule in pure_rules:
            report = self.analyze_rule_quality(rule)
            if report['issues']:
                quality_reports.append(report)
        
        # Rebuild rules document (only rules, no supplementary)
        original_content = file_path.read_text(encoding='utf-8')
        header_match = re.match(r'^(.*?)(?=\*\*规则\s+[IV]+\.\d+\.\d+\.\d+【|## |$)', original_content, re.MULTILINE | re.DOTALL)
        file_header = header_match.group(1) if header_match else ""
        
        new_content = file_header + '\n'
        for rule in pure_rules:
            new_content += f"{rule['header']}\n{rule['content']}\n\n"
        
        # Write purified rules
        file_path.write_text(new_content, encoding='utf-8')
        
        # Write supplementary to annotations
        if supp_doc:
            anno_path = self.annotations_dir / f"{article_name.replace('.md', '-annotations.md')}"
            anno_path.write_text(supp_doc, encoding='utf-8')
        
        return {
            'status': 'success',
            'rules_preserved': len(pure_rules),
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
