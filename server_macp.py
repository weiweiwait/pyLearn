#server_demo.py
from mcp.server.fastmcp import FastMCP
# 创建一个MCP服务器
mcp = FastMCP("演示")
# 添加一个工具
@mcp.tool()
def calculate(expression: str) -> float:
    """计算四则运算表达式
    参数:
        expression: 数学表达式字符串，如 "1 + 2 * 3"
    返回:
        计算结果
    """
    # 移除空格并验证表达式
    expr = expression.replace(" ", "")
    
    # 验证表达式只包含数字和运算符
    allowed_chars = set("0123456789+-*/(). ")
    if not all(char in allowed_chars for char in expr):
        raise ValueError("表达式包含非法字符")
    
    # 使用安全的eval计算（在生产环境中建议使用更安全的解析器）
    try:
        result = eval(expr)
        return float(result)
    except Exception as e:
        raise ValueError(f"计算错误: {str(e)}")

if __name__ == "__main__":
    mcp.run(transport='stdio')
