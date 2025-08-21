# Claude Code Statusline with ccusage Integration
## Photo
<img width="631" height="227" alt="image" src="https://github.com/user-attachments/assets/8f0391af-0702-4c0f-8a6e-26a684375b9e" />

[English](#english) | [中文](#中文)

## English

This project provides a custom Claude Code statusline that displays current model, usage cost, and remaining time information.

### Features

- Display current Claude model name (e.g., Sonnet 4)
- Show cumulative cost for current session
- Display estimated remaining usage time
- Automatically parse ccusage data to get latest active session info

### Prerequisites

1. **Python 3.6+** - Required to run the statusline script
2. **ccusage** - Claude usage statistics tool
   - Ensure `ccusage` command is available in PATH
   - Install and setup guide: https://ccusage.com/guide/live-monitoring
   - Verify by running `ccusage blocks --live -j`

### File Description

- `statusline-ccusage.py` - Main Python script that parses ccusage data
- `statusline-ccusage.bat` - Windows batch file that calls the Python script
- `statusline.bat` - Alternative batch file with same functionality

### Installation Steps

#### 1. Download Files

Save the following files to your Claude directory (typically `%USERPROFILE%\.claude\`):
- `statusline-ccusage.py`
- `statusline-ccusage.bat` or `statusline.bat`

#### 2. Verify Environment

Open command prompt and verify dependencies:

```cmd
# Verify Python
python --version

# Verify ccusage
ccusage blocks --live -j
```

#### 3. Test Run

```cmd
# Method 1: Run Python script directly
python %USERPROFILE%\.claude\statusline-ccusage.py

# Method 2: Run batch file
%USERPROFILE%\.claude\statusline-ccusage.bat

# Method 3: Use simplified batch file
%USERPROFILE%\.claude\statusline.bat
```

### Output Format

After successful execution, you'll see output in this format:

```
Model: Sonnet 4 | Cost: $1.98 | Remaining: 202m
```

- **Model**: Current Claude model name
- **Cost**: Cumulative cost for current session (USD)
- **Remaining**: Estimated remaining usage time (minutes)

### Integration with Claude Code

To integrate this statusline into Claude Code, set the statusline script path in Claude Code configuration:

```json
{
  "statusline": {
    "command": "%USERPROFILE%\\.claude\\statusline-ccusage.bat"
  }
}
```

### Troubleshooting

#### Issue 1: "ccusage command not found"

**Solutions**:
1. Confirm ccusage is properly installed
2. Check if ccusage is in system PATH
3. Try running `ccusage --version` directly in command line
4. Follow the setup guide: https://ccusage.com/guide/live-monitoring

#### Issue 2: Shows "Claude | No cost | No time"

**Possible causes**:
1. ccusage has no active session data
2. ccusage permission issues
3. JSON data format changes

**Troubleshooting steps**:
1. Run `ccusage blocks --live -j` to view raw data
2. Confirm if there's a block with `"isActive": true`
3. Check if `costUSD` and `projection` fields exist

#### Issue 3: Python script execution fails

**Check items**:
1. Is Python properly installed and in PATH?
2. Is the script file path correct?
3. Do you have sufficient permissions to execute the script?

### Customization

#### Modify Output Format

Edit the `main()` function in `statusline-ccusage.py`:

```python
def main():
    model_name, cost_info, time_info = get_ccusage_info()
    # Modify this line to customize output format
    print(f"Model: {model_name} | Cost: {cost_info} | Remaining: {time_info}")
```

#### Add More Information

Extract additional fields in the `get_ccusage_info()` function:
- `totalTokens` - Total token count
- `entries` - Number of entries
- `burnRate` - Consumption rate

### Technical Details

The script executes `ccusage blocks --live -j` to get JSON usage data, then parses active blocks (`isActive: true`) to extract relevant information.

---

## 中文

此项目提供了一个自定义的 Claude Code 状态栏，可以显示当前模型、使用花费和剩余时间信息。

### 功能特性

- 显示当前使用的 Claude 模型名称（如 Sonnet 4）
- 显示当前会话的累计花费
- 显示预估剩余使用时间
- 自动解析 ccusage 数据，获取最新活跃会话信息

### 前置要求

1. **Python 3.6+** - 用于运行状态栏脚本
2. **ccusage** - Claude 使用情况统计工具
   - 确保 `ccusage` 命令在 PATH 中可用
   - 安装和设置指南：https://ccusage.com/guide/live-monitoring
   - 可以通过运行 `ccusage blocks --live -j` 验证

### 文件说明

- `statusline-ccusage.py` - 主要的 Python 脚本，负责解析 ccusage 数据
- `statusline-ccusage.bat` - Windows 批处理文件，调用 Python 脚本
- `statusline.bat` - 另一个批处理文件，功能相同

### 安装步骤

#### 1. 下载文件

将以下文件保存到您的 Claude 目录（通常是 `%USERPROFILE%\.claude\`）：
- `statusline-ccusage.py`
- `statusline-ccusage.bat` 或 `statusline.bat`

#### 2. 验证环境

打开命令提示符，验证依赖项：

```cmd
# 验证 Python
python --version

# 验证 ccusage
ccusage blocks --live -j
```

#### 3. 测试运行

```cmd
# 方法1：直接运行 Python 脚本
python %USERPROFILE%\.claude\statusline-ccusage.py

# 方法2：运行批处理文件
%USERPROFILE%\.claude\statusline-ccusage.bat

# 方法3：使用简化版批处理文件
%USERPROFILE%\.claude\statusline.bat
```

### 输出格式

成功运行后，会看到如下格式的输出：

```
Model: Sonnet 4 | Cost: $1.98 | Remaining: 202m
```

- **Model**: 当前使用的 Claude 模型名称
- **Cost**: 当前会话的累计花费（美元）
- **Remaining**: 预估剩余使用时间（分钟）

### 集成到 Claude Code

要将此状态栏集成到 Claude Code 中，需要在 Claude Code 的配置中设置状态栏脚本路径：

```json
{
  "statusline": {
    "command": "%USERPROFILE%\\.claude\\statusline-ccusage.bat"
  }
}
```

### 故障排除

#### 问题1: "ccusage命令未找到"

**解决方案**:
1. 确认 ccusage 已正确安装
2. 检查 ccusage 是否在系统 PATH 中
3. 尝试在命令行中直接运行 `ccusage --version`
4. 参考安装指南：https://ccusage.com/guide/live-monitoring

#### 问题2: 显示 "Claude | No cost | No time"

**可能原因**:
1. ccusage 没有活跃的会话数据
2. ccusage 权限问题
3. JSON 数据格式变化

**解决步骤**:
1. 运行 `ccusage blocks --live -j` 查看原始数据
2. 确认是否有 `"isActive": true` 的块
3. 检查是否有 `costUSD` 和 `projection` 字段

#### 问题3: Python 脚本执行失败

**检查项**:
1. Python 是否正确安装并在 PATH 中
2. 脚本文件路径是否正确
3. 是否有足够的权限执行脚本

### 自定义修改

#### 修改输出格式

编辑 `statusline-ccusage.py` 文件中的 `main()` 函数：

```python
def main():
    model_name, cost_info, time_info = get_ccusage_info()
    # 修改这一行来自定义输出格式
    print(f"Model: {model_name} | Cost: {cost_info} | Remaining: {time_info}")
```

#### 添加更多信息

可以在 `get_ccusage_info()` 函数中提取更多字段：
- `totalTokens` - 总令牌数
- `entries` - 条目数量
- `burnRate` - 消耗速率

### 技术细节

脚本通过执行 `ccusage blocks --live -j` 命令获取 JSON 格式的使用数据，然后解析其中的活跃块（`isActive: true`）来提取相关信息。

---

**注意**: 此工具依赖于 ccusage 的输出格式，如果 ccusage 更新了数据格式，可能需要相应调整解析逻辑。

## License

This project is open source and free to use and modify.

## Contributing

Issues and Pull Requests are welcome to improve this tool.
