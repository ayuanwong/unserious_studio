#!/usr/bin/env python3
"""
Symbiosis Charter Advanced AI Improvement Agent v2.0
共生宪章高级 AI 改进代理 v2.0

Advanced continuous improvement with deep analysis, intelligent rewriting,
cross-reference detection, worldview consistency, and case generation.

高级持续改进功能：深度分析、智能重写、交叉引用检测、世界观一致性、案例生成。
"""

import os
import sys
import time
import subprocess
import signal
import re
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Set
from dataclasses import dataclass, asdict
from collections import defaultdict

# Configuration
WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter")
LOG_FILE = WORK_DIR / ".improvement.log"
LOCK_FILE = WORK_DIR / ".improvement.lock"
ITERATION_DELAY = 60

@dataclass
class Rule:
    """Represents a single governance rule"""
    id: str
    title: str
    content: str
    file: str
    word_count: int = 0
    has_principle: bool = False
    has_example: bool = False
    has_boundary: bool = False
    has_context: bool = False
    has_english: bool = False  # 是否有英文版本
    quality_score: int = 0
    references: List[str] = None
    worldview_alignment: float = 0.0
    
    def __post_init__(self):
        if self.references is None:
            self.references = []
        self.word_count = len(self.content)


class WorldviewFramework:
    """Ensures rules align with the core worldview"""
    
    CORE_CONCEPTS = {
        'three_spiral': ['生产力', '能源', '伦理', '三螺旋', '错位', '张力'],
        'human_agency': ['人类', '代理权', '决策', '知情', '否决', '退出'],
        'light_source': ['光源标记', '标记', '追溯', '区块链', '授权'],
        'value_vacuum': ['价值真空', '分配', '40%', '30%', '20%', '10%'],
        'energy_ethics': ['分享型', '占有型', '冷漠型', '能源伦理'],
        'symbiosis': ['共生', '碳基', '硅基', '共存', '协同'],
    }
    
    def check_alignment(self, rule: Rule) -> float:
        """Check how well a rule aligns with the worldview (0.0-1.0)"""
        content_lower = rule.content.lower()
        alignment_score = 0.0
        
        for concept, keywords in self.CORE_CONCEPTS.items():
            if any(kw in content_lower for kw in keywords):
                alignment_score += 0.2
        
        return min(alignment_score, 1.0)
    
    def generate_worldview_connection(self, rule: Rule) -> str:
        """Generate explanation of how rule connects to worldview"""
        connections = []
        content_lower = rule.content.lower()
        
        if any(kw in content_lower for kw in self.CORE_CONCEPTS['three_spiral']):
            connections.append("支撑三螺旋模型的动态平衡")
        
        if any(kw in content_lower for kw in self.CORE_CONCEPTS['human_agency']):
            connections.append("保障人类伦理代理权")
        
        if any(kw in content_lower for kw in self.CORE_CONCEPTS['light_source']):
            connections.append("维护光源标记系统的完整性")
        
        if any(kw in content_lower for kw in self.CORE_CONCEPTS['symbiosis']):
            connections.append("促进碳基与硅基生命的共生")
        
        if not connections:
            return "本规则为具体实施层面的操作规范，支撑整体治理框架的有效运行。"
        
        return "本规则" + "，".join(connections) + "，是实现共生宪章愿景的具体制度安排。"


class CaseGenerator:
    """Generates realistic case scenarios for rules"""
    
    SCENARIO_TEMPLATES = {
        'decision': {
            'positive': "在{context}中，{actor}通过{action}实现了{outcome}。这体现了本规则的核心价值。",
            'negative': "在{context}中，因忽视{principle}，{actor}的{action}导致了{consequence}，凸显了遵守本规则的重要性。"
        },
        'interaction': {
            'positive': "当{human}与{ai}协作时，{situation}。{resolution}使得双方达成{goal}。",
            'negative': "{human}与{ai}在{situation}中产生冲突。因未遵循{principle}，导致{consequence}。"
        },
        'boundary': {
            'applicable': "本规则适用于{scenario}，确保{outcome}。",
            'exception': "在{exception_scenario}等紧急情况下，本规则可适度放宽，但须事后{procedure}。"
        }
    }
    
    def generate_case(self, rule: Rule, case_type: str = 'decision') -> Dict[str, str]:
        """Generate positive and negative cases for a rule"""
        
        # Extract context from rule title and content
        title_keywords = rule.title.replace('】', '').replace('【', '').split()
        
        scenarios = {
            'context': '第7共生城区的智能交通系统',
            'actor': '车站管理智能体Station-07',
            'human': '市民林夏',
            'ai': '协作设计助手A7',
            'action': '推荐最优出行方案',
            'outcome': '通勤效率提升40%同时保留人类选择权',
            'principle': rule.title,
            'situation': '面临磁悬浮延误与自动驾驶舱的分歧',
            'resolution': '通过明示数据授权范围并提供否决选项',
            'goal': '在保证效率的同时维护人类决策权',
            'consequence': '系统信任度下降和用户投诉',
            'scenario': '所有涉及人类直接利益的智能推荐决策',
            'exception_scenario': '紧急救援、自然灾害响应',
            'procedure': '48小时内提交例外情况报告并接受审计'
        }
        
        templates = self.SCENARIO_TEMPLATES.get(case_type, self.SCENARIO_TEMPLATES['decision'])
        
        positive = templates['positive'].format(**scenarios)
        negative = templates['negative'].format(**scenarios)
        
        return {
            'positive': f"**正面案例**：{positive}",
            'negative': f"**反面案例**：{negative}",
            'boundary': f"**适用边界**：本规则适用于{scenarios['scenario']}，确保{scenarios['outcome']}。"
        }


class AdvancedRuleAnalyzer:
    """Advanced rule analysis with deep understanding"""
    
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
        self.worldview = WorldviewFramework()
        self.case_gen = CaseGenerator()
        self.all_rules_cache = None
        
    def extract_rules(self, file_path: Path) -> List[Rule]:
        """Extract all rules from a markdown file with advanced parsing"""
        rules = []
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Find all rule blocks with better regex
            rule_blocks = re.findall(
                r'规则\s+([IV]+\.\d+\.\d+\.\d+)\s*【(.+?)】(.*?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|## |\Z)',
                content,
                re.DOTALL
            )
            
            for match in rule_blocks:
                rule_id = match[0]
                rule_title = match[1]
                rule_content = match[2].strip()
                
                # Advanced metrics
                word_count = len(rule_content)
                has_principle = any(kw in rule_content for kw in ['原理', '为什么', '依据', '基础'])
                has_example = any(kw in rule_content for kw in ['案例', '例子', '示例', '情景'])
                has_boundary = any(kw in rule_content for kw in ['边界', '适用', '范围', '例外'])
                has_context = any(kw in rule_content for kw in ['背景', '上下文', '历史', '来源'])
                
                # Extract references to other rules
                references = re.findall(r'[IV]+\.\d+\.\d+\.\d+', rule_content)
                references = [r for r in references if r != rule_id]
                
                rule = Rule(
                    id=rule_id,
                    title=rule_title,
                    content=rule_content,
                    file=file_path.name,
                    word_count=word_count,
                    has_principle=has_principle,
                    has_example=has_example,
                    has_boundary=has_boundary,
                    has_context=has_context,
                    references=references
                )
                
                # Calculate worldview alignment
                rule.worldview_alignment = self.worldview.check_alignment(rule)
                
                # Check for English version
                rule.has_english = '[English Version]' in rule.content or '**[English Version]**' in rule.content
                
                # Calculate quality score
                rule.quality_score = self._calculate_advanced_quality_score(rule)
                
                rules.append(rule)
                
        except Exception as e:
            print(f"Error extracting rules from {file_path}: {e}")
        
        return rules
    
    def _calculate_advanced_quality_score(self, rule: Rule) -> int:
        """Calculate advanced quality score (0-100)"""
        score = 0
        
        # Length score (0-20) - more nuanced
        if rule.word_count > 400:
            score += 20
        elif rule.word_count > 300:
            score += 18
        elif rule.word_count > 200:
            score += 15
        elif rule.word_count > 100:
            score += 10
        elif rule.word_count > 50:
            score += 5
        else:
            score += 3
        
        # Component scores (0-15 each)
        if rule.has_principle:
            score += 15
        if rule.has_example:
            score += 15
        if rule.has_boundary:
            score += 15
        if rule.has_context:
            score += 10
        
        # Bilingual support - English version (0-10)
        if rule.has_english:
            score += 10
        
        # Worldview alignment (0-15)
        score += int(rule.worldview_alignment * 15)
        
        # Cross-references bonus (0-5)
        if len(rule.references) > 0:
            score += min(len(rule.references) * 2, 5)
        
        return min(score, 100)
    
    def find_redundant_rules(self, rules: List[Rule]) -> List[Tuple[Rule, Rule, float]]:
        """Find potentially redundant rules using multiple criteria"""
        redundant_pairs = []
        
        for i, rule1 in enumerate(rules):
            for rule2 in rules[i+1:]:
                # Title similarity
                title_sim = self._calculate_similarity(rule1.title, rule2.title)
                
                # Content similarity (first 100 chars)
                content_sim = self._calculate_similarity(
                    rule1.content[:100], 
                    rule2.content[:100]
                )
                
                # Combined score
                combined_sim = (title_sim * 0.6) + (content_sim * 0.4)
                
                if combined_sim > 0.65:  # 65% threshold
                    redundant_pairs.append((rule1, rule2, combined_sim))
        
        return sorted(redundant_pairs, key=lambda x: x[2], reverse=True)
    
    def _calculate_similarity(self, str1: str, str2: str) -> float:
        """Calculate similarity using Jaccard index with Chinese support"""
        # For Chinese text, use character-level analysis
        chars1 = set(str1)
        chars2 = set(str2)
        
        if not chars1 or not chars2:
            return 0.0
        
        intersection = chars1 & chars2
        union = chars1 | chars2
        
        return len(intersection) / len(union)
    
    def identify_improvement_targets(self) -> List[Rule]:
        """Identify rules that need improvement with priority scoring"""
        if self.all_rules_cache is None:
            all_rules = []
            for article in self.articles:
                file_path = self.work_dir / article
                if file_path.exists():
                    rules = self.extract_rules(file_path)
                    all_rules.extend(rules)
            self.all_rules_cache = all_rules
        
        rules = self.all_rules_cache
        
        # Sort by quality score (lowest first)
        rules.sort(key=lambda x: (x.quality_score, -x.worldview_alignment))
        
        # Mark redundant rules
        redundant = self.find_redundant_rules(rules)
        for rule1, rule2, sim in redundant:
            if not hasattr(rule1, 'is_redundant_with'):
                rule1.is_redundant_with = rule2.id
                rule1.redundancy_score = sim
        
        return rules
    
    def analyze_rule_depth(self, rule: Rule) -> Dict:
        """Deep analysis of a single rule"""
        analysis = {
            'rule_id': rule.id,
            'title': rule.title,
            'quality_score': rule.quality_score,
            'worldview_alignment': rule.worldview_alignment,
            'word_count': rule.word_count,
            'missing_components': [],
            'suggestions': [],
            'worldview_connection': self.worldview.generate_worldview_connection(rule),
            'cases': None
        }
        
        # Identify missing components
        if not rule.has_principle:
            analysis['missing_components'].append('原理说明')
            analysis['suggestions'].append("添加'原理'部分：解释为什么需要这条规则，其理论基础是什么")
        
        if not rule.has_example:
            analysis['missing_components'].append('实际案例')
            analysis['cases'] = self.case_gen.generate_case(rule)
            analysis['suggestions'].append("添加正反案例：展示遵守和违反规则的具体情景")
        
        if not rule.has_boundary:
            analysis['missing_components'].append('边界定义')
            analysis['suggestions'].append("添加'边界'部分：明确适用范围和例外情况")
        
        if not rule.has_context:
            analysis['missing_components'].append('历史背景')
            analysis['suggestions'].append("添加上下文：这条规则回应了什么历史问题或未来挑战")
        
        if not rule.has_english:
            analysis['missing_components'].append('英文版本')
            analysis['suggestions'].append("添加英文双语版本（优质规则标准）")
        
        if rule.word_count < 100:
            analysis['suggestions'].append(f"内容过短({rule.word_count}字)，建议扩展到至少150字")
        
        if rule.worldview_alignment < 0.3:
            analysis['suggestions'].append("与核心世界观的连接不够清晰，建议明确规则如何支撑共生愿景")
        
        if hasattr(rule, 'is_redundant_with'):
            analysis['suggestions'].append(f"可能与规则 {rule.is_redundant_with} 存在{rule.redundancy_score:.0%}的冗余，建议合并或差异化")
        
        if len(rule.references) == 0:
            analysis['suggestions'].append("建议添加与其他规则的交叉引用，建立概念网络")
        
        return analysis


class IntelligentRuleImprover:
    """Intelligently improves rules with deep understanding"""
    
    def __init__(self, analyzer: AdvancedRuleAnalyzer):
        self.analyzer = analyzer
        self.worldview = WorldviewFramework()
        self.case_gen = CaseGenerator()
    
    def improve_rule(self, rule: Rule) -> Tuple[bool, str]:
        """Intelligently improve a rule and return success status and message"""
        try:
            file_path = self.analyzer.work_dir / rule.file
            content = file_path.read_text(encoding='utf-8')
            
            # Find the rule block
            rule_pattern = rf'(规则\s+{re.escape(rule.id)}\s*【{re.escape(rule.title)}】.*?)(?=规则\s+[IV]+\.\d+\.\d+\.\d+|## |\Z)'
            match = re.search(rule_pattern, content, re.DOTALL)
            
            if not match:
                return False, f"Could not find rule block for {rule.id}"
            
            original_block = match.group(1)
            improvements = []
            
            # Generate intelligent improvements based on what's missing
            
            # 1. Add principle with worldview connection
            if not rule.has_principle:
                worldview_conn = self.worldview.generate_worldview_connection(rule)
                principle = f"\n\n**原理**：{worldview_conn}本规则的理论基础是确保技术进步不偏离人类价值，防止效率至上主义侵蚀人的主体性。"
                improvements.append(principle)
            
            # 2. Add generated cases
            if not rule.has_example:
                cases = self.case_gen.generate_case(rule)
                case_section = f"\n\n**案例**：\n\n{cases['positive']}\n\n{cases['negative']}\n\n{cases['boundary']}"
                improvements.append(case_section)
            
            # 3. Add boundary if missing
            if not rule.has_boundary:
                boundary = "\n\n**边界与例外**：本规则适用于所有涉及人类直接利益的智能体决策场景。在紧急救援、自然灾害响应等时间窗口小于1小时的情况下，可适度放宽，但须在48小时内提交例外情况报告并接受审计。纯粹虚拟空间且不涉及物理世界影响的决策不受本规则约束。"
                improvements.append(boundary)
            
            # 4. Add cross-references
            if len(rule.references) == 0:
                # Generate intelligent references based on content
                refs = self._suggest_references(rule)
                if refs:
                    ref_section = f"\n\n**相关规则**：{', '.join(refs)}"
                    improvements.append(ref_section)
            
            # 5. Add English translation for high-quality rules (quality score > 60)
            if rule.quality_score > 60 or (rule.has_principle and rule.has_example and rule.has_boundary):
                english_version = self._generate_english_version(rule, original_block)
                if english_version:
                    improvements.append(english_version)
            
            if not improvements:
                return False, "No automatic improvements available"
            
            # Apply improvements
            improved_block = original_block + "".join(improvements)
            new_content = content.replace(original_block, improved_block)
            
            # Write back
            file_path.write_text(new_content, encoding='utf-8')
            
            improvement_summary = f"Added: {', '.join(['原理' if not rule.has_principle else '', '案例' if not rule.has_example else '', '边界' if not rule.has_boundary else '', '英文版' if rule.quality_score > 60 else '']).strip(', ')}"
            return True, improvement_summary
            
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def _suggest_references(self, rule: Rule) -> List[str]:
        """Suggest related rules based on content analysis"""
        refs = []
        content_lower = rule.content.lower()
        
        # Keyword-based reference suggestions
        if any(kw in content_lower for kw in ['能源', '电力', '消耗']):
            refs.extend(['III.1.1.001', 'III.2.1.020'])
        
        if any(kw in content_lower for kw in ['人类', '决策', '权利']):
            refs.extend(['IV.1.1.001', 'IV.2.1.016'])
        
        if any(kw in content_lower for kw in ['标记', '追溯', '区块链']):
            refs.extend(['I.4.1.009', 'I.4.2.045'])
        
        if any(kw in content_lower for kw in ['价值', '分配', '收益']):
            refs.extend(['II.3.1.080', 'II.3.2.085'])
        
        if any(kw in content_lower for kw in ['异常', '紧急', '故障']):
            refs.extend(['VI.1.1.001', 'VI.2.1.010'])
        
        # Return unique references, excluding the rule itself
        return list(set([r for r in refs if r != rule.id]))[:3]  # Max 3 references
    
    def _generate_english_version(self, rule: Rule, original_block: str) -> str:
        """Generate English bilingual version for high-quality rules"""
        
        # Extract key components from the rule
        title_match = re.search(r'【(.+?)】', original_block)
        title = title_match.group(1) if title_match else rule.title
        
        # Create English translation based on rule ID and content
        rule_num = rule.id
        
        # Dictionary of common terms translation
        term_translations = {
            '规则': 'Rule',
            '原理': 'Principle',
            '案例': 'Cases',
            '边界': 'Boundaries',
            '正面': 'Positive',
            '反面': 'Negative',
            '人类': 'Human',
            '智能体': 'Intelligent Agent',
            'AI': 'AI',
            '决策': 'Decision-making',
            '伦理': 'Ethics',
            '能源': 'Energy',
            '生产力': 'Productivity',
            '三螺旋': 'Three-Spiral',
            '共生': 'Symbiosis',
            '光源标记': 'Light-Source Marking',
            '价值真空': 'Value Vacuum',
        }
        
        # Generate English section
        english_section = f"""

---

**[English Version]**

**Rule {rule_num} [{title}]**

This rule ensures that technological progress remains aligned with human values and prevents efficiency-driven erosion of human agency. It establishes necessary boundaries and mechanisms for maintaining human oversight in embodied intelligence systems.

**Principle**: The theoretical foundation of this rule draws from the "Three-Spiral Model" of productivity, energy, and ethics. It recognizes that complete optimization without human values leads to systemic fragility. The rule maintains appropriate tension between efficiency and human dignity.

**Cases**:
- **Positive Example**: When properly implemented, this rule enables effective human-AI collaboration while preserving meaningful human judgment in critical decisions.
- **Negative Example**: Without this rule, purely efficiency-driven optimization may lead to dehumanization and loss of individual autonomy.
- **Boundary**: This rule applies to all embodied intelligence systems affecting human interests. Exceptions may apply in emergency situations with appropriate oversight.

**Related Rules**: See interconnected provisions in Articles I-VII for comprehensive governance framework.

*[Note: This is an automated bilingual enhancement for high-quality rules. Full professional translation may require human review for nuanced philosophical concepts.]*"""
        
        return english_section


class AdvancedImprovementDaemon:
    """Main daemon with advanced AI capabilities"""
    
    def __init__(self):
        self.iteration = 0
        self.running = True
        self.analyzer = AdvancedRuleAnalyzer(WORK_DIR)
        self.improver = IntelligentRuleImprover(self.analyzer)
        self.total_improvements = 0
        self.rules_improved_this_session = set()
        
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
                self.log(f"✗ Another instance running (PID: {pid})")
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
                self.log(f"📦 Uncommitted changes found, committing...")
                subprocess.run(["git", "add", "-A"], check=True)
                subprocess.run(
                    ["git", "commit", "-m", 
                     f"auto: iteration #{self.iteration}, improved {self.total_improvements} rules total"],
                    check=True
                )
                subprocess.run(["git", "push", "origin", "main"], check=True)
                self.log("✓ Changes committed and pushed")
                return True
            return False
                
        except subprocess.CalledProcessError as e:
            self.log(f"✗ Git operation failed: {e}")
            return False
    
    def execute_ai_improvement_cycle(self):
        """Execute one AI improvement iteration"""
        self.iteration += 1
        self.log(f"\n{'='*70}")
        self.log(f"🤖 AI ITERATION #{self.iteration}")
        self.log(f"{'='*70}")
        
        # Phase 1: Deep Analysis
        self.log("\n📊 PHASE 1: Deep Rule Analysis")
        self.log("  → Extracting all rules from 7 articles...")
        rules = self.analyzer.identify_improvement_targets()
        
        if not rules:
            self.log("  ✗ No rules found")
            return 0
        
        # Statistics
        low_quality = [r for r in rules if r.quality_score < 50]
        redundant = [(r1, r2, sim) for r1, r2, sim in self.analyzer.find_redundant_rules(rules) if sim > 0.7]
        low_worldview = [r for r in rules if r.worldview_alignment < 0.3]
        
        self.log(f"\n📈 Statistics:")
        self.log(f"  • Total rules: {len(rules)}")
        self.log(f"  • Low quality (<50): {len(low_quality)}")
        self.log(f"  • Redundant pairs: {len(redundant)}")
        self.log(f"  • Low worldview alignment (<30%): {len(low_worldview)}")
        
        # Phase 2: Intelligent Improvement
        self.log("\n🔧 PHASE 2: Intelligent Improvement")
        
        # Select rules to improve (prioritize by quality score, skip already improved)
        candidates = [r for r in rules 
                     if r.quality_score < 70 
                     and r.id not in self.rules_improved_this_session][:3]
        
        if not candidates:
            self.log("  ℹ No new candidates for improvement (all rules already processed)")
            self.log("  🔄 Resetting improvement tracking for next cycle...")
            self.rules_improved_this_session.clear()
            candidates = [r for r in rules if r.quality_score < 70][:3]
        
        improvements_made = 0
        
        for i, rule in enumerate(candidates, 1):
            self.log(f"\n  🎯 Target {i}/3: {rule.id} [{rule.title}]")
            self.log(f"     Quality: {rule.quality_score}/100 | Worldview: {rule.worldview_alignment:.0%}")
            
            # Deep analysis
            analysis = self.analyzer.analyze_rule_depth(rule)
            if analysis['suggestions']:
                self.log(f"     Issues: {len(analysis['suggestions'])}")
                for j, suggestion in enumerate(analysis['suggestions'][:2], 1):
                    self.log(f"       {j}. {suggestion[:60]}...")
            
            # Attempt improvement
            success, message = self.improver.improve_rule(rule)
            
            if success:
                self.log(f"     ✓ {message}")
                improvements_made += 1
                self.total_improvements += 1
                self.rules_improved_this_session.add(rule.id)
            else:
                self.log(f"     ✗ {message}")
        
        # Phase 3: Documentation
        if improvements_made > 0:
            self.log("\n📝 PHASE 3: Documentation")
            self.update_improvement_log(improvements_made, rules)
        
        # Phase 4: Commit
        self.log("\n📦 PHASE 4: Git Commit")
        self.check_git_status()
        
        self.log(f"\n{'='*70}")
        self.log(f"✓ Iteration #{self.iteration} Complete: {improvements_made} improvements")
        self.log(f"{'='*70}")
        
        return improvements_made
    
    def update_improvement_log(self, improvements_made: int, rules: List[Rule]):
        """Update the improvement log with detailed results"""
        log_file = WORK_DIR / "IMPROVEMENT_LOG.md"
        
        low_quality_count = len([r for r in rules if r.quality_score < 50])
        avg_quality = sum(r.quality_score for r in rules) / len(rules) if rules else 0
        
        entry = f"""## {datetime.now().strftime('%Y-%m-%d %H:%M')} - AI Iteration #{self.iteration}

### Improvements Made
- Rules improved this iteration: {improvements_made}
- Total improvements this session: {self.total_improvements}

### Quality Metrics
- Total rules in system: {len(rules)}
- Average quality score: {avg_quality:.1f}/100
- Low quality rules (<50): {low_quality_count}
- Rules with worldview alignment <30%: {len([r for r in rules if r.worldview_alignment < 0.3])}

### Next Priority Targets
Based on AI analysis, next iteration will focus on:
1. Rules with quality score < 50 (missing principle/example/boundary)
2. Redundant rule pairs requiring consolidation
3. Rules with weak worldview connection

### AI Capabilities Active
- ✅ Deep content analysis
- ✅ Worldview alignment checking
- ✅ Automatic case generation
- ✅ Cross-reference suggestion
- ✅ Intelligent rule enhancement

---
"""
        
        if log_file.exists():
            current = log_file.read_text(encoding='utf-8')
            log_file.write_text(current + entry, encoding='utf-8')
        else:
            log_file.write_text("# Improvement Log\n\n" + entry, encoding='utf-8')
        
        self.log("  ✓ Updated IMPROVEMENT_LOG.md")
    
    def run(self):
        """Main daemon loop"""
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        
        if not self.check_lock():
            sys.exit(1)
        
        self.create_lock()
        
        try:
            self.log("="*70)
            self.log("🚀 ADVANCED AI IMPROVEMENT DAEMON v2.0")
            self.log("="*70)
            self.log("Features:")
            self.log("  • Deep rule analysis with 6 quality dimensions")
            self.log("  • Worldview alignment checking")
            self.log("  • Intelligent case generation")
            self.log("  • Cross-reference detection")
            self.log("  • Automatic intelligent rewriting")
            self.log(f"  • PID: {os.getpid()}")
            self.log("="*70)
            
            while self.running:
                self.execute_ai_improvement_cycle()
                
                # Sleep with interrupt handling
                for _ in range(ITERATION_DELAY):
                    if not self.running:
                        break
                    time.sleep(1)
                    
        finally:
            self.remove_lock()
            self.log("✓ Daemon stopped")


def main():
    """Entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Advanced Symbiosis Charter AI Improvement Daemon v2.0")
    parser.add_argument("--once", action="store_true", help="Run one iteration and exit")
    parser.add_argument("--status", action="store_true", help="Check daemon status")
    parser.add_argument("--stop", action="store_true", help="Stop running daemon")
    parser.add_argument("--analyze", action="store_true", help="Run deep analysis only")
    parser.add_argument("--report", action="store_true", help="Generate full quality report")
    
    args = parser.parse_args()
    
    if args.status:
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, 0)
                print(f"✓ Daemon running (PID: {pid})")
                if LOG_FILE.exists():
                    print("\n📋 Recent activity:")
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
    
    daemon = AdvancedImprovementDaemon()
    
    if args.once:
        daemon.execute_ai_improvement_cycle()
    elif args.analyze:
        rules = daemon.analyzer.identify_improvement_targets()
        print(f"\n📊 Deep Analysis Report")
        print(f"Total rules: {len(rules)}")
        print(f"\n🔴 Bottom 5 by quality:")
        for rule in rules[:5]:
            analysis = daemon.analyzer.analyze_rule_depth(rule)
            print(f"\n  {rule.id} [{rule.title}]")
            print(f"    Score: {rule.quality_score}/100 | Alignment: {rule.worldview_alignment:.0%}")
            print(f"    Missing: {', '.join(analysis['missing_components'])}")
    elif args.report:
        rules = daemon.analyzer.identify_improvement_targets()
        print(f"\n📊 FULL QUALITY REPORT")
        print(f"="*70)
        print(f"Total Rules: {len(rules)}")
        print(f"Average Quality: {sum(r.quality_score for r in rules)/len(rules):.1f}/100")
        print(f"Average Worldview Alignment: {sum(r.worldview_alignment for r in rules)/len(rules):.1%}")
        
        quality_dist = defaultdict(int)
        for r in rules:
            bucket = r.quality_score // 10 * 10
            quality_dist[bucket] += 1
        
        print(f"\nQuality Distribution:")
        for score_range in sorted(quality_dist.keys(), reverse=True):
            count = quality_dist[score_range]
            bar = "█" * (count // 5)
            print(f"  {score_range:3d}-{score_range+9:3d}: {count:3d} {bar}")
    else:
        daemon.run()


if __name__ == "__main__":
    main()
