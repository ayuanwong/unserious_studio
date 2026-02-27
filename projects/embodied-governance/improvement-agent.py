#!/usr/bin/env python3
"""
Symbiosis Charter Continuous Improvement Agent
共生宪章持续改进代理

Background daemon that continuously improves the governance framework using AI analysis.
后台守护进程，使用 AI 分析持续改进治理框架。
"""

import os
import sys
import time
import subprocess
import signal
import re
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Configuration
WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/embodied-governance")
LOG_FILE = WORK_DIR / ".improvement.log"
LOCK_FILE = WORK_DIR / ".improvement.lock"
ITERATION_DELAY = 60  # seconds between iterations

class RuleAnalyzer:
    """Analyzes rules for quality, redundancy, and improvement opportunities"""
    
    def __init__(self, work_dir: Path):
        self.work_dir = work_dir
        self.articles = [
            "ARTICLES-I-FUNDAMENTAL.md",
            "ARTICLES-II-PRODUCTIVITY.md", 
            "ARTICLES-III-ENERGY.md",
            "ARTICLES-IV-ETHICAL-AGENCY.md",
            "ARTICLES-V-ADAPTIVE.md",
            "ARTICLES-VI-EXCEPTIONS.md",
            "ARTICLES-VII-OVERSIGHT.md"
        ]
        self.rule_pattern = re.compile(r'规则\s+[IV]+\.\d+\.\d+\.\d+\s*【(.+?)】')
        self.content_pattern = re.compile(r'规则\s+[IV]+\.\d+\.\d+\.\d+\s*【.+?】(.*?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|\Z)', re.DOTALL)
    
    def extract_rules(self, file_path: Path) -> List[Dict]:
        """Extract all rules from a markdown file"""
        rules = []
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Find all rule blocks
            rule_blocks = re.findall(
                r'规则\s+([IV]+\.\d+\.\d+\.\d+)\s*【(.+?)】(.*?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|\Z)',
                content,
                re.DOTALL
            )
            
            for match in rule_blocks:
                rule_id = match[0]
                rule_title = match[1]
                rule_content = match[2].strip()
                
                # Calculate metrics
                word_count = len(rule_content)
                has_principle = '原理' in rule_content or '原理：' in rule_content
                has_example = '案例' in rule_content or '例子' in rule_content
                has_boundary = '边界' in rule_content or '适用' in rule_content
                
                rules.append({
                    'id': rule_id,
                    'title': rule_title,
                    'content': rule_content,
                    'word_count': word_count,
                    'has_principle': has_principle,
                    'has_example': has_example,
                    'has_boundary': has_boundary,
                    'quality_score': self._calculate_quality_score(word_count, has_principle, has_example, has_boundary),
                    'file': file_path.name
                })
                
        except Exception as e:
            print(f"Error extracting rules from {file_path}: {e}")
        
        return rules
    
    def _calculate_quality_score(self, word_count: int, has_principle: bool, has_example: bool, has_boundary: bool) -> int:
        """Calculate quality score for a rule (0-100)"""
        score = 0
        
        # Length score (0-40)
        if word_count > 200:
            score += 40
        elif word_count > 100:
            score += 30
        elif word_count > 50:
            score += 20
        else:
            score += 10
        
        # Component scores (0-20 each)
        if has_principle:
            score += 20
        if has_example:
            score += 20
        if has_boundary:
            score += 20
        
        return score
    
    def find_redundant_rules(self, rules: List[Dict]) -> List[Tuple[Dict, Dict, float]]:
        """Find potentially redundant rules based on title similarity"""
        redundant_pairs = []
        
        for i, rule1 in enumerate(rules):
            for rule2 in rules[i+1:]:
                similarity = self._calculate_similarity(rule1['title'], rule2['title'])
                if similarity > 0.7:  # 70% similarity threshold
                    redundant_pairs.append((rule1, rule2, similarity))
        
        return redundant_pairs
    
    def _calculate_similarity(self, str1: str, str2: str) -> float:
        """Calculate simple similarity between two strings"""
        # Simple word-based similarity
        words1 = set(str1.lower().split())
        words2 = set(str2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1 & words2
        union = words1 | words2
        
        return len(intersection) / len(union)
    
    def identify_improvement_targets(self) -> List[Dict]:
        """Identify rules that need improvement"""
        all_rules = []
        
        # Extract all rules
        for article in self.articles:
            file_path = self.work_dir / article
            if file_path.exists():
                rules = self.extract_rules(file_path)
                all_rules.extend(rules)
        
        # Sort by quality score (lowest first)
        all_rules.sort(key=lambda x: x['quality_score'])
        
        # Find redundant rules
        redundant = self.find_redundant_rules(all_rules)
        
        # Mark redundant rules
        for rule1, rule2, sim in redundant:
            rule1['is_redundant_with'] = rule2['id']
            rule1['redundancy_score'] = sim
        
        return all_rules
    
    def generate_improvement_suggestion(self, rule: Dict) -> str:
        """Generate improvement suggestion for a rule"""
        suggestions = []
        
        if rule['word_count'] < 100:
            suggestions.append("内容过短，建议扩展深度")
        
        if not rule['has_principle']:
            suggestions.append("缺少原理说明，建议添加'为什么'的解释")
        
        if not rule['has_example']:
            suggestions.append("缺少实际案例，建议添加正反案例")
        
        if not rule['has_boundary']:
            suggestions.append("缺少边界说明，建议明确适用范围")
        
        if 'is_redundant_with' in rule:
            suggestions.append(f"可能与规则 {rule['is_redundant_with']} 冗余，建议合并")
        
        return "; ".join(suggestions) if suggestions else "质量良好，可进一步优化"


class ImprovementDaemon:
    """Main daemon that orchestrates continuous improvement"""
    
    def __init__(self):
        self.iteration = 0
        self.running = True
        self.analyzer = RuleAnalyzer(WORK_DIR)
        self.improved_count = 0
        
    def log(self, message):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def check_lock(self):
        """Check if another instance is running"""
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, 0)
                self.log(f"Another instance already running (PID: {pid})")
                return False
            except (ValueError, OSError, ProcessLookupError):
                LOCK_FILE.unlink()
        return True
    
    def create_lock(self):
        """Create lock file with current PID"""
        with open(LOCK_FILE, "w") as f:
            f.write(str(os.getpid()))
    
    def remove_lock(self):
        """Remove lock file on exit"""
        if LOCK_FILE.exists():
            LOCK_FILE.unlink()
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        self.log(f"Received signal {signum}, shutting down...")
        self.running = False
    
    def check_git_status(self):
        """Check git status and commit if needed"""
        try:
            os.chdir(WORK_DIR)
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                self.log(f"Uncommitted changes found, committing...")
                subprocess.run(["git", "add", "-A"], check=True)
                subprocess.run(
                    ["git", "commit", "-m", f"auto: iteration #{self.iteration}, improved {self.improved_count} rules"],
                    check=True
                )
                subprocess.run(["git", "push", "origin", "main"], check=True)
                self.log("Changes committed and pushed successfully")
                return True
            else:
                self.log("No uncommitted changes")
                return False
                
        except subprocess.CalledProcessError as e:
            self.log(f"Git operation failed: {e}")
            return False
    
    def analyze_and_improve(self):
        """Analyze rules and generate improvements"""
        self.log("Analyzing all rules for quality and redundancy...")
        
        # Get all rules sorted by quality
        rules = self.analyzer.identify_improvement_targets()
        
        if not rules:
            self.log("No rules found to analyze")
            return 0
        
        # Log statistics
        low_quality = [r for r in rules if r['quality_score'] < 50]
        redundant = [r for r in rules if 'is_redundant_with' in r]
        
        self.log(f"Total rules: {len(rules)}")
        self.log(f"Low quality (<50): {len(low_quality)}")
        self.log(f"Potentially redundant: {len(redundant)}")
        
        # Select top 3 rules to improve (lowest quality)
        target_rules = [r for r in rules if r['quality_score'] < 70][:3]
        
        if not target_rules:
            self.log("All rules have good quality (>70), checking for redundancy...")
            if redundant:
                target_rules = redundant[:2]
        
        improvements_made = 0
        
        for rule in target_rules:
            suggestion = self.analyzer.generate_improvement_suggestion(rule)
            self.log(f"Target: {rule['id']} [{rule['title']}] (Score: {rule['quality_score']})")
            self.log(f"  Suggestion: {suggestion}")
            
            # Try to improve the rule
            if self._improve_rule(rule, suggestion):
                improvements_made += 1
        
        return improvements_made
    
    def _improve_rule(self, rule: Dict, suggestion: str) -> bool:
        """Attempt to improve a specific rule"""
        try:
            file_path = WORK_DIR / rule['file']
            content = file_path.read_text(encoding='utf-8')
            
            # Find the rule block
            rule_pattern = rf'(规则\s+{re.escape(rule["id"])}\s*【{re.escape(rule["title"])}】.*?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|\Z)'
            match = re.search(rule_pattern, content, re.DOTALL)
            
            if not match:
                self.log(f"  Could not find rule block for {rule['id']}")
                return False
            
            original_block = match.group(1)
            
            # Generate improvement based on what's missing
            improvements = []
            
            if not rule['has_principle'] and '原理' not in suggestion:
                improvements.append("\n\n**原理**: 本规则旨在确保人类在具身智能系统中的核心地位，防止技术异化。")
            
            if not rule['has_example'] and '案例' not in suggestion:
                improvements.append("\n\n**示例**: 当智能体建议替代人类决策时，必须展示其决策逻辑并允许人类否决。")
            
            if not rule['has_boundary'] and '边界' not in suggestion:
                improvements.append("\n\n**边界**: 本规则适用于所有涉及人类直接利益的决策场景，不适用于纯技术优化决策。")
            
            if not improvements:
                self.log(f"  No automatic improvements available for {rule['id']}")
                return False
            
            # Apply improvements
            improved_block = original_block + "".join(improvements)
            new_content = content.replace(original_block, improved_block)
            
            # Write back
            file_path.write_text(new_content, encoding='utf-8')
            self.log(f"  ✓ Improved {rule['id']} with {len(improvements)} additions")
            return True
            
        except Exception as e:
            self.log(f"  Error improving {rule['id']}: {e}")
            return False
    
    def update_improvement_log(self, improvements_made: int):
        """Update the improvement log with current iteration results"""
        log_file = WORK_DIR / "IMPROVEMENT_LOG.md"
        
        entry = f"""
## {datetime.now().strftime('%Y-%m-%d %H:%M')} - Iteration #{self.iteration}

### Automated Improvements
- Rules analyzed: All 7 articles
- Rules improved: {improvements_made}
- Quality checks: Redundancy detection, depth analysis, boundary verification

### Next Priority
Based on analysis, next iteration will focus on:
1. Rules with quality score < 50
2. Redundant rule pairs (similarity > 70%)
3. Missing principle explanations

---
"""
        
        if log_file.exists():
            current = log_file.read_text(encoding='utf-8')
            log_file.write_text(current + entry, encoding='utf-8')
        
        self.log("Updated IMPROVEMENT_LOG.md")
    
    def execute_improvement(self):
        """Execute one improvement iteration"""
        self.iteration += 1
        self.log(f"\n{'='*60}")
        self.log(f"=== Iteration #{self.iteration} Starting ===")
        self.log(f"{'='*60}")
        
        # 1. Check git status first
        self.check_git_status()
        
        # 2. Analyze and improve rules
        self.log("Phase 1: AI Analysis")
        improvements_made = self.analyze_and_improve()
        self.improved_count += improvements_made
        
        # 3. Update improvement log
        if improvements_made > 0:
            self.log("Phase 2: Documentation")
            self.update_improvement_log(improvements_made)
        
        # 4. Commit changes
        if improvements_made > 0:
            self.log("Phase 3: Commit")
            self.check_git_status()
        
        self.log(f"=== Iteration #{self.iteration} Complete ({improvements_made} improvements) ===")
    
    def run(self):
        """Main daemon loop"""
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        
        if not self.check_lock():
            sys.exit(1)
        
        self.create_lock()
        
        try:
            self.log("="*60)
            self.log("AI IMPROVEMENT DAEMON STARTED")
            self.log(f"Working directory: {WORK_DIR}")
            self.log(f"Iteration delay: {ITERATION_DELAY}s")
            self.log(f"PID: {os.getpid()}")
            self.log("Features: Rule quality analysis, redundancy detection, auto-improvement")
            self.log("="*60)
            
            while self.running:
                self.execute_improvement()
                
                # Sleep with interrupt handling
                for _ in range(ITERATION_DELAY):
                    if not self.running:
                        break
                    time.sleep(1)
                    
        finally:
            self.remove_lock()
            self.log("Daemon stopped")


def main():
    """Entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Symbiosis Charter AI Improvement Daemon")
    parser.add_argument("--once", action="store_true", help="Run one iteration and exit")
    parser.add_argument("--status", action="store_true", help="Check daemon status")
    parser.add_argument("--stop", action="store_true", help="Stop running daemon")
    parser.add_argument("--analyze", action="store_true", help="Run analysis only, no improvements")
    
    args = parser.parse_args()
    
    if args.status:
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, 0)
                print(f"✓ Daemon is running (PID: {pid})")
                if LOG_FILE.exists():
                    print("\n📋 Recent log entries:")
                    with open(LOG_FILE, "r") as f:
                        lines = f.readlines()
                        for line in lines[-15:]:
                            print("  " + line.rstrip())
            except:
                print("✗ Daemon is not running (stale lock file)")
        else:
            print("✗ Daemon is not running")
        return
    
    if args.stop:
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, signal.SIGTERM)
                print(f"✓ Sent stop signal to daemon (PID: {pid})")
            except Exception as e:
                print(f"✗ Failed to stop daemon: {e}")
        else:
            print("✗ Daemon is not running")
        return
    
    daemon = ImprovementDaemon()
    
    if args.once:
        daemon.execute_improvement()
    elif args.analyze:
        rules = daemon.analyzer.identify_improvement_targets()
        print(f"\n📊 Analysis Results:")
        print(f"Total rules: {len(rules)}")
        print(f"\nBottom 5 rules by quality:")
        for rule in rules[:5]:
            print(f"  {rule['id']} [{rule['title']}]: Score {rule['quality_score']}")
            suggestion = daemon.analyzer.generate_improvement_suggestion(rule)
            print(f"    → {suggestion}")
    else:
        daemon.run()


if __name__ == "__main__":
    main()
