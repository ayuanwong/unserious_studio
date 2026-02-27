#!/bin/bash
# Symbiosis Charter Continuous Improvement Daemon
# 共生宪章持续改进守护进程

# 配置
WORK_DIR="/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/embodied-governance"
LOG_FILE="$WORK_DIR/.improvement.log"
LOCK_FILE="$WORK_DIR/.improvement.lock"
ITERATION_DELAY=60  # 每次迭代间隔60秒（1分钟）

# 防止重复运行
if [ -f "$LOCK_FILE" ]; then
    PID=$(cat "$LOCK_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        echo "[$(date)] Improvement daemon already running (PID: $PID)" >> "$LOG_FILE"
        exit 1
    fi
fi

# 保存当前PID
echo $$ > "$LOCK_FILE"

# 清理函数
cleanup() {
    rm -f "$LOCK_FILE"
    echo "[$(date)] Daemon stopped" >> "$LOG_FILE"
    exit 0
}

trap cleanup SIGINT SIGTERM

echo "[$(date)] Improvement daemon started" >> "$LOG_FILE"
echo "Working directory: $WORK_DIR" >> "$LOG_FILE"
echo "Iteration delay: ${ITERATION_DELAY}s" >> "$LOG_FILE"
echo "----------------------------------------" >> "$LOG_FILE"

# 主循环
iteration=0
while true; do
    iteration=$((iteration + 1))
    echo "[$(date)] Iteration #$iteration starting..." >> "$LOG_FILE"
    
    cd "$WORK_DIR"
    
    # 1. 检查改进计划
    if [ -f "IMPROVEMENT_PLAN.md" ]; then
        echo "[$(date)] Reading improvement plan..." >> "$LOG_FILE"
    fi
    
    # 2. 检查 git 状态
    git_status=$(git status --porcelain 2>/dev/null)
    if [ -n "$git_status" ]; then
        echo "[$(date)] Uncommitted changes found, committing..." >> "$LOG_FILE"
        git add -A
        git commit -m "auto: continuous improvement iteration #$iteration" >> "$LOG_FILE" 2>&1
        git push origin main >> "$LOG_FILE" 2>&1
    fi
    
    # 3. 检查改进日志，确定下一步
    if [ -f "IMPROVEMENT_LOG.md" ]; then
        last_entry=$(tail -50 IMPROVEMENT_LOG.md | grep -E "^## " | tail -1)
        echo "[$(date)] Last improvement: $last_entry" >> "$LOG_FILE"
    fi
    
    # 4. 执行具体改进任务（待实现）
    # 这里可以调用具体的改进脚本
    
    echo "[$(date)] Iteration #$iteration complete. Sleeping ${ITERATION_DELAY}s..." >> "$LOG_FILE"
    echo "" >> "$LOG_FILE"
    
    # 休眠
    sleep $ITERATION_DELAY
done
