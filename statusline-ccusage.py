#!/usr/bin/env python3
import json
import subprocess
import sys

def get_ccusage_info():
    """获取ccusage信息并返回模型名称、花费、剩余时间"""
    try:
        # 执行ccusage命令
        result = subprocess.run('ccusage blocks --live -j', 
                              capture_output=True, text=True, check=True, shell=True)
        
        data = json.loads(result.stdout)
        blocks = data.get('blocks', [])
        
        # 找到活跃的块
        for block in blocks:
            if block.get('isActive', False):
                # 提取模型名称
                models = block.get('models', [])
                model_name = "Claude"
                if models:
                    if 'claude-sonnet-4' in models[0]:
                        model_name = "Sonnet 4"
                    else:
                        model_name = models[0].split('-')[-1] if '-' in models[0] else models[0]
                
                # 提取花费
                cost = block.get('costUSD', 0)
                cost_info = f"${cost:.2f}" if cost > 0 else "No cost"
                
                # 提取剩余时间
                projection = block.get('projection', {})
                remaining_minutes = projection.get('remainingMinutes', 0)
                time_info = f"{remaining_minutes}m" if remaining_minutes > 0 else "No time"
                
                return model_name, cost_info, time_info
        
        return "Claude", "No cost", "No time"
        
    except (subprocess.CalledProcessError, json.JSONDecodeError, FileNotFoundError):
        return "Claude", "No cost", "No time"

def main():
    model_name, cost_info, time_info = get_ccusage_info()
    print(f"Model: {model_name} | Cost: {cost_info} | Remaining: {time_info}")

if __name__ == "__main__":
    main()