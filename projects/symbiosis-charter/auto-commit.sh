#!/bin/bash
# 定期提交脚本 - 每小时提交一次AI改进

cd /Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/symbiosis-charter

# 检查是否有改进
IMPROVED=$(tail -50 .purification.log | grep -c "rules improved")

if [ "$IMPROVED" -gt 0 ]; then
    echo "$(date): 发现$IMPROVED次改进，提交到GitHub..."
    cd /Users/pcofmarcus/.openclaw/workspace/unserious_studio
    git add -A
    git commit -m "auto: AI rule improvement - $(date +%H:%M)"
    git push
    echo "✓ 已提交"
else
    echo "$(date): 本次无改进，跳过提交"
fi
