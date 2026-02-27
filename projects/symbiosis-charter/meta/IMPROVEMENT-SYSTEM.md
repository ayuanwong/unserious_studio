# Symbiosis Charter Improvement System
# 共生宪章持续改进系统

## Quick Start / 快速开始

### Option 1: Simple Background Mode (推荐)
最简单的方式 - 在后台持续运行

```bash
# 进入项目目录
cd /Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/embodied-governance

# 启动后台改进代理（每60秒检查一次）
python3 improvement-agent.py &

# 查看状态
python3 improvement-agent.py --status

# 停止
python3 improvement-agent.py --stop
```

### Option 2: macOS LaunchDaemon (系统级服务)
作为系统服务自动启动

```bash
# 加载服务
launchctl load ~/Library/LaunchAgents/com.symbiosis.charter.improvement.plist

# 启动服务
launchctl start com.symbiosis.charter.improvement

# 查看日志
tail -f .improvement.log

# 停止服务
launchctl stop com.symbiosis.charter.improvement
launchctl unload ~/Library/LaunchAgents/com.symbiosis.charter.improvement.plist
```

### Option 3: Bash Daemon
使用 bash 脚本

```bash
# 启动
./improvement-daemon.sh &

# 查看日志
tail -f .improvement.log

# 停止
kill $(cat .improvement.lock)
```

### Option 4: Single Iteration (测试)
只运行一次改进

```bash
python3 improvement-agent.py --once
```

---

## How It Works / 工作原理

### 持续改进循环 (Every 60 seconds)
```
1. 检查 git 状态
   └─ 如有未提交更改 → 自动提交并推送

2. 读取 IMPROVEMENT_PLAN.md
   └─ 确定当前改进阶段

3. 执行改进任务
   └─ 分析规则质量
   └─ 识别冗余/缺失
   └─ 生成改进建议
   └─ 实施改进

4. 记录到 IMPROVEMENT_LOG.md

5. 休眠 60 秒 → 重复
```

---

## Monitoring / 监控

### View Logs / 查看日志
```bash
# 实时日志
tail -f .improvement.log

# 完整日志
cat .improvement.log
```

### Check Status / 检查状态
```bash
python3 improvement-agent.py --status
```

Output:
```
Daemon is running (PID: 12345)

Recent log entries:
[2026-02-26 18:00:00] === Iteration #1 starting ===
[2026-02-26 18:00:01] No uncommitted changes
[2026-02-26 18:00:02] Reading improvement plan...
[2026-02-26 18:00:03] === Iteration #1 complete ===
```

---

## Configuration / 配置

Edit these variables in the script:

```python
# improvement-agent.py
ITERATION_DELAY = 60  # 迭代间隔（秒）
WORK_DIR = "/path/to/project"  # 工作目录
```

---

## Improvement Strategy / 改进策略

### Phase 1: Rule Consolidation (当前阶段)
- 删除冗余规则
- 合并相似规则
- 提升单条规则质量

### Phase 2: Worldview Framework
- 建立哲学基础
- 添加历史脉络
- 明确价值主张

### Phase 3: Rule Depth Enhancement
- 每条规则添加：目的、边界、原理、案例
- 建立规则间引用网络

### Phase 4: Narrative Optimization
- 增强故事性
- 添加可视化
- 制作摘要版本

---

## Files / 相关文件

- `IMPROVEMENT_PLAN.md` - 改进计划
- `IMPROVEMENT_LOG.md` - 改进日志
- `.improvement.log` - 运行时日志
- `improvement-agent.py` - Python 改进代理
- `improvement-daemon.sh` - Bash 守护进程
- `com.symbiosis.charter.improvement.plist` - macOS 服务配置

---

## Troubleshooting / 故障排除

### Daemon won't start
```bash
# Check if already running
python3 improvement-agent.py --status

# If stuck, remove lock file manually
rm .improvement.lock
```

### Git push fails
```bash
# Check git credentials
git remote -v
git status

# May need to configure git credentials helper
git config --global credential.helper osxkeychain
```

### Permission denied
```bash
# Make scripts executable
chmod +x improvement-agent.py
chmod +x improvement-daemon.sh
```

---

*"Continuous improvement is better than delayed perfection."*
*"持续改进胜过迟来的完美。"*
