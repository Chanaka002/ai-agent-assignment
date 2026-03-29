# Tool registry system
class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, tool):
        self.tools[name] = tool

    def get_tool(self, name):
        return self.tools.get(name)

    def get_all_declarations(self):
        declarations = []
        for tool in self.tools.values():
            declarations.append(tool.get_declaration())
        return declarations

    def execute(self, name, **kwargs):
        tool = self.get_tool(name)
        if not tool:
            return f"Error: Tool '{name}' not found."

        try:
            return tool.execute(**kwargs)
        except TypeError as e:
            return f"Error: Invalid arguments for tool '{name}': {str(e)}"
        except Exception as e:
            return f"Error while executing tool '{name}': {str(e)}"
