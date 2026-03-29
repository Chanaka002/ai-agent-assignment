import os
import google.generativeai as genai

from memory_manager import MemoryManager
from tool_registry import ToolRegistry
from tools.calculator_tool import CalculatorTool
from tools.time_tool import TimeTool
from tools.translation_tool import TranslationTool
from tools.file_reader_tool import FileReaderTool


class Agent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

        self.memory = MemoryManager()
        self.registry = ToolRegistry()

        self.registry.register("calculator", CalculatorTool())
        self.registry.register("time", TimeTool())
        self.registry.register("translate_text", TranslationTool())
        self.registry.register("read_local_file", FileReaderTool())

    def build_prompt(self, user_input):
        return f"""
You are a CLI personal assistant.

Rules:
- Answer naturally and helpfully.
- Use tools when needed.
- If the user asks for time, calculations, translation, or file reading, choose the correct tool.
- Maintain memory of the current session.
- If no tool is needed, answer directly.

Conversation history:
{self.memory.get_history_as_text()}

Current user message:
{user_input}
"""

    def handle_user_input(self, user_input):
        self.memory.add_user_message(user_input)

        try:
            response = self.model.generate_content(
                self.build_prompt(user_input),
                tools=self.registry.get_all_declarations()
            )

            part = response.candidates[0].content.parts[0]

            if hasattr(part, "function_call") and part.function_call:
                function_name = part.function_call.name
                function_args = dict(part.function_call.args)

                tool_result = self.registry.execute(function_name, **function_args)

                final_response = self.model.generate_content(
                    f"""
The user asked: {user_input}

The tool '{function_name}' returned:
{tool_result}

Now provide the final user-friendly response.
"""
                )

                answer = final_response.text.strip()
                self.memory.add_assistant_message(answer)
                return answer

            answer = response.text.strip()
            self.memory.add_assistant_message(answer)
            return answer

        except Exception as e:
            error_message = f"Agent error: {str(e)}"
            self.memory.add_assistant_message(error_message)
            return error_message
