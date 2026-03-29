from datetime import datetime
from tools.base_tool import BaseTool


class TimeTool(BaseTool):
    def execute(self):
        now = datetime.now()
        return now.strftime("Current local time: %Y-%m-%d %H:%M:%S")

    def get_declaration(self):
        return {
            "name": "time",
            "description": "Get the current local date and time",
            "parameters": {
                "type": "OBJECT",
                "properties": {}
            }
        }
