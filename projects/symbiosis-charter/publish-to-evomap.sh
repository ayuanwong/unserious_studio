#!/bin/bash
# EVOMAP资产发布脚本
# 网络恢复后执行

ASSETS_FILE="evomap_assets_v2.json"
API_ENDPOINT="https://evomap.io/api/v1/assets"

echo "检查EVOMAP网络状态..."
if curl -s -o /dev/null -w "%{http_code}" $API_ENDPOINT | grep -q "404"; then
    echo "❌ EVOMAP API仍不可用 (404)"
    echo "等待网络恢复..."
    exit 1
fi

echo "🚀 发布资产到EVOMAP..."
RESPONSE=$(curl -s -X POST $API_ENDPOINT \
    -H "Content-Type: application/json" \
    -d @$ASSETS_FILE)

if echo "$RESPONSE" | grep -q "success"; then
    echo "✅ 资产发布成功！"
    echo "$RESPONSE" | jq .
else
    echo "⚠️ 发布遇到问题:"
    echo "$RESPONSE"
fi
