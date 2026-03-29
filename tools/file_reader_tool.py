from pathlib import Path
from tools.base_tool import BaseTool


class FileReaderTool(BaseTool):
    def execute(self, file_path):
        try:
            path = Path(file_path).expanduser()

            if not path.exists():
                return f"Error: File not found -> {file_path}"

            if not path.is_file():
                return f"Error: Path is not a file -> {file_path}"

            content = path.read_text(encoding="utf-8")
            if len(content) > 3000:
                content = content[:3000] + "\n...[truncated]"

            return f"File content from {file_path}:\n{content}"
        except Exception as e:
            return f"File reader error: {str(e)}"

    def get_declaration(self):
        return {
            "name": "read_local_file",
            "description": "Read a local text file",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "file_path": {
                        "type": "STRING",
                        "description": "Path to a local file, for example ./sample.txt"
                    }
                },
                "required": ["file_path"]
            }
        }
