from tools.base_tool import BaseTool


class CalculatorTool(BaseTool):
    def execute(self, expression):
        try:
            allowed_chars = "0123456789+-*/(). "
            if not all(ch in allowed_chars for ch in expression):
                return "Error: Invalid characters in expression."

            result = eval(expression, {"__builtins__": {}}, {})
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except Exception as e:
            return f"Calculator error: {str(e)}"

    def get_declaration(self):
        return {
            "name": "calculator",
            "description": "Perform arithmetic calculations",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "expression": {
                        "type": "STRING",
                        "description": "Arithmetic expression like 25*8 or 10+5"
                    }
                },
                "required": ["expression"]
            }
        }
