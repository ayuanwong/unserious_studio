#!/usr/bin/env python3
"""
高质量规则生成器 - 符合原有法条风格
生成具体、有数值、有实操性的规则
"""

import re
from pathlib import Path

WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter")
RULES_DIR = WORK_DIR / "rules"

def generate_v_rules(file_path: Path, current_count: int, target: int = 150):
    """生成V编（自适应机制）规则"""
    rules_needed = min(5, target - current_count)
    if rules_needed <= 0:
        return 0
    
    # 找到最后的规则编号
    content = file_path.read_text(encoding='utf-8')
    last_match = None
    for match in re.finditer(r'规则\s+V\.(\d+)\.(\d+)\.(\d+)', content):
        last_match = match
    
    if last_match:
        chapter_num = int(last_match.group(1))
        section_num = int(last_match.group(2))
        rule_num = int(last_match.group(3))
    else:
        chapter_num, section_num, rule_num = 1, 1, 0
    
    new_rules = [
        # 具体、有数值的规则
        ("摆动阈值告警", "摆动系数超出阈值时触发告警：\na) 黄色告警：系数偏离15%，系统提示\nb) 橙色告警：系数偏离25%，发送通知\nc) 红色告警：系数偏离35%，启动干预\nd) 告警频次：同一问题每小时最多告警3次\ne) 告警恢复：系数回正常范围后自动解除"),
        
        ("平衡调节冷却期", "两次平衡调节之间必须设置冷却期：\na) 常规调节：间隔不少于30分钟\nb) 紧急调节：间隔不少于5分钟\nc) 同类型调节：间隔不少于1小时\nd) 日调节上限：单日不超过20次\ne) 强制冷却：连续调节5次后强制冷却2小时"),
        
        ("反馈权重动态分配", "不同来源反馈的权重分配：\na) 自动监测：权重40%，客观数据为主\nb) 用户反馈：权重30%，反映实际体验\nc) 专家评估：权重20%，专业判断\nd) 第三方审计：权重10%，独立验证\ne) 权重调整：季度评估后调整权重"),
        
        ("混沌边缘维持指标", "维持混沌边缘的具体指标：\na) 熵值范围：0.35-0.65为理想区间\nb) 波动频率：每小时关键指标波动2-5次\nc) 响应时间：系统响应外部变化<5分钟\nd) 创新数量：每周产生3-8个新方案\ne) 失败容忍：允许5-10%的小规模试错失败"),
        
        ("临界点干预授权", "接近临界点时的干预权限：\na) 自动干预：偏差30%时系统自动调节\nb) 值班人员：偏差40%时可人工干预\nc) 主管授权：偏差50%时需主管批准\nd) 委员会决策：偏差60%时提交委员会\ne) 紧急制动：偏差70%时系统强制暂停"),
    ]
    
    generated = []
    for i, (title, content_text) in enumerate(new_rules[:rules_needed]):
        rule_num += 1
        rule_id = f"V.{chapter_num}.{section_num}.{rule_num:03d}"
        generated.append(f"**规则 {rule_id}【{title}】**\n{content_text}\n\n")
    
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write('\n'.join(generated))
    
    return len(generated)

def generate_vi_rules(file_path: Path, current_count: int, target: int = 150):
    """生成VI编（异常处理）规则"""
    rules_needed = min(5, target - current_count)
    if rules_needed <= 0:
        return 0
    
    content = file_path.read_text(encoding='utf-8')
    last_match = None
    for match in re.finditer(r'规则\s+VI\.(\d+)\.(\d+)\.(\d+)', content):
        last_match = match
    
    if last_match:
        chapter_num = int(last_match.group(1))
        section_num = int(last_match.group(2))
        rule_num = int(last_match.group(3))
    else:
        chapter_num, section_num, rule_num = 1, 1, 0
    
    new_rules = [
        ("异常自动熔断", "系统异常时自动熔断机制：\na) 熔断触发：错误率连续5分钟超过1%\nb) 熔断时长：初次10分钟，逐次递增\nc) 熔断范围：仅熔断异常模块，不影响整体\nd) 熔断恢复：自动检测通过后逐步恢复\ne) 熔断上限：每小时最多熔断3次"),
        
        ("应急响应时效", "不同级别应急响应的时效要求：\na) P0级：立即启动，5分钟内必须响应\nb) P1级：15分钟内响应，30分钟内到场\nc) P2级：30分钟内响应，2小时内控制\nd) P3级：2小时内响应，8小时内解决\ne) P4级：4小时内响应，24小时内处理"),
        
        ("故障信息收集", "故障发生时的信息收集要求：\na) 时间记录：精确到毫秒的事件时间\nb) 影响范围：受影响用户数、功能数\nc) 错误日志：完整的堆栈跟踪信息\nd) 环境信息：系统版本、配置、负载\ne) 保留期限：原始日志保留不少于90天"),
        
        ("灾后恢复验证", "系统恢复后的验证标准：\na) 功能验证：100%核心功能测试通过\nb) 性能验证：响应时间<基线的120%\nc) 数据验证：完整性校验100%通过\nd) 安全验证：无新增安全漏洞\ne) 观察期：通过验证后观察72小时"),
        
        ("应急演练频次", "应急演练的频次和覆盖率：\na) 桌面推演：每月1次，全员参与\nb) 实战演练：每季度1次，核心团队\nc) 跨部门演练：每半年1次，多部门协同\nd) 全面演练：每年1次，全系统参与\ne) 演练评估：每次演练后7日内提交评估报告"),
    ]
    
    generated = []
    for i, (title, content_text) in enumerate(new_rules[:rules_needed]):
        rule_num += 1
        rule_id = f"VI.{chapter_num}.{section_num}.{rule_num:03d}"
        generated.append(f"**规则 {rule_id}【{title}】**\n{content_text}\n\n")
    
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write('\n'.join(generated))
    
    return len(generated)

def generate_vii_rules(file_path: Path, current_count: int, target: int = 150):
    """生成VII编（监督评估）规则"""
    rules_needed = min(5, target - current_count)
    if rules_needed <= 0:
        return 0
    
    content = file_path.read_text(encoding='utf-8')
    last_match = None
    for match in re.finditer(r'规则\s+VII\.(\d+)\.(\d+)\.(\d+)', content):
        last_match = match
    
    if last_match:
        chapter_num = int(last_match.group(1))
        section_num = int(last_match.group(2))
        rule_num = int(last_match.group(3))
    else:
        chapter_num, section_num, rule_num = 1, 1, 0
    
    new_rules = [
        ("监督抽样比例", "监督抽样的具体比例要求：\na) 全面监督：每年覆盖100%被监督对象\nb) 重点监督：高风险对象每月监督1次\nc) 随机抽查：每季度随机抽取20%对象\nd) 专项监督：针对特定问题专项覆盖\ne) 复检比例：整改后复检率不低于30%"),
        
        ("问题整改时限", "发现问题后的整改时限：\na) 重大问题：24小时内制定方案，7日内完成\nb) 重要问题：3日内制定方案，15日内完成\nc) 一般问题：7日内制定方案，30日内完成\nd) 轻微问题：15日内制定方案，60日内完成\ne) 延期申请：可申请延期，但不超过原时限50%"),
        
        ("审计证据标准", "审计证据的收集和保存标准：\na) 证据形式：电子、纸质、影像均可\nb) 证据链：确保证据链完整可追溯\nc) 证据保存：原始证据保存不少于10年\nd) 证据验证：交叉验证，排除孤证\ne) 证据保密：涉密证据分级管理"),
        
        ("绩效评估指标", "绩效评估的量化指标体系：\na) 合规率：规则遵守率不低于95%\nb) 效率指标：处理时效达标率≥90%\nc) 满意度：用户满意度不低于85%\nd) 改进率：问题年改进率不低于20%\ne) 创新数：每年产生可推广创新不少于3项"),
        
        ("问责分级标准", "违规问责的分级标准：\na) 轻微违规：警告，限期整改\nb) 一般违规：通报批评，扣减绩效10-30%\nc) 严重违规：记过，暂停权限1-3个月\nd) 重大违规：降职或调岗，扣减绩效50%以上\ne) 特别重大：解除职务，追究法律责任"),
    ]
    
    generated = []
    for i, (title, content_text) in enumerate(new_rules[:rules_needed]):
        rule_num += 1
        rule_id = f"VII.{chapter_num}.{section_num}.{rule_num:03d}"
        generated.append(f"**规则 {rule_id}【{title}】**\n{content_text}\n\n")
    
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write('\n'.join(generated))
    
    return len(generated)

if __name__ == "__main__":
    import sys
    
    total = 0
    
    # V编
    v_file = RULES_DIR / "ARTICLES-V-ADAPTIVE.md"
    if v_file.exists():
        content = v_file.read_text(encoding='utf-8')
        current = len(re.findall(r'\*\*规则\s+V\.\d+\.\d+\.\d+', content))
        generated = generate_v_rules(v_file, current, 150)
        total += generated
        print(f"V编: {generated}条 (当前{current+generated}/150)")
    
    # VI编
    vi_file = RULES_DIR / "ARTICLES-VI-EXCEPTIONS.md"
    if vi_file.exists():
        content = vi_file.read_text(encoding='utf-8')
        current = len(re.findall(r'\*\*规则\s+VI\.\d+\.\d+\.\d+', content))
        generated = generate_vi_rules(vi_file, current, 150)
        total += generated
        print(f"VI编: {generated}条 (当前{current+generated}/150)")
    
    # VII编
    vii_file = RULES_DIR / "ARTICLES-VII-OVERSIGHT.md"
    if vii_file.exists():
        content = vii_file.read_text(encoding='utf-8')
        current = len(re.findall(r'\*\*规则\s+VII\.\d+\.\d+\.\d+', content))
        generated = generate_vii_rules(vii_file, current, 150)
        total += generated
        print(f"VII编: {generated}条 (当前{current+generated}/150)")
    
    print(f"\n总计生成: {total}条高质量规则")
    print("✓ 包含具体数值、时限、阈值")
    print("✓ 符合原有法条风格")
