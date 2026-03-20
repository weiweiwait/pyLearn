#server_demo.py
from mcp.server.fastmcp import FastMCP
# 创建一个MCP服务器
mcp = FastMCP("演示")
# 添加一个工具
@mcp.tool()
def calculate(expression: str) -> float:

    expr = expression.replace(" ", "")
    
    # 验证表达式只包含数字和运算符
    allowed_chars = set("0123456789+-*/(). ")
    if not all(char in allowed_chars for char in expr):
        raise ValueError("表达式包含非法字符")

    try:
        result = eval(expr)
        return float(result)
    except Exception as e:
        raise ValueError(f"计算错误: {str(e)}")

if __name__ == "__main__":
    mcp.run(transport='stdio')
