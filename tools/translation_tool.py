from tools.base_tool import BaseTool


class TranslationTool(BaseTool):
    def execute(self, text, target_language):
        try:
            return f'Translate this text to {target_language}: "{text}"'
        except Exception as e:
            return f"Translation tool error: {str(e)}"

    def get_declaration(self):
        return {
            "name": "translate_text",
            "description": "Translate text into a target language",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "text": {
                        "type": "STRING",
                        "description": "Text to translate"
                    },
                    "target_language": {
                        "type": "STRING",
                        "description": "Target language, e.g. Sinhala, French, German"
                    }
                },
                "required": ["text", "target_language"]
            }
        }
