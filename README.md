# AI Personal Assistant Agent

## Overview
This project implements an adaptive Artificial Intelligence personal assistant using Python and the Google Gemini API. The assistant runs as a Command Line Interface (CLI) application and demonstrates modern software architecture principles, including SOLID principles and design patterns.

The assistant maintains conversation history, reasons about user requests, and autonomously decides when to use external tools through Gemini function calling.

## Features
- Natural language CLI interaction
- Session-based contextual memory
- Adaptive tool usage
- ReAct-style loop (Reason → Act → Observe)
- Modular and extensible architecture
- Robust error handling

## Implemented Components
- `Agent` - main orchestrator of the system
- `MemoryManager` - stores conversation history
- `ToolRegistry` - manages tool registration and execution
- `BaseTool` - abstract tool interface
- `tools/` - contains all tool implementations

## Tools
The assistant supports the following tools:
1. `calculator` - performs arithmetic calculations
2. `time` - returns the current local date and time
3. `translate_text` - prepares text for translation into a target language
4. `read_local_file` - reads the contents of a local text file

Custom tools:
- `translate_text`
- `read_local_file`

## Architecture and Design Principles

### SOLID Principles
- **Single Responsibility Principle (SRP):** Each module has one clear responsibility.
- **Open/Closed Principle (OCP):** New tools can be added without modifying the core agent logic.
- **Dependency Inversion Principle (DIP):** The agent depends on the abstract `BaseTool` interface rather than concrete tool implementations.

### Design Patterns
- **Strategy Pattern:** Each tool acts as a different strategy for handling a type of request.
- **Factory / Registry Pattern:** `ToolRegistry` dynamically stores and retrieves tool implementations.
- **ReAct Pattern:** The agent follows the loop: Reason → Act → Observe.

## Project Structure
```bash
ai-agent-assignment/
│
├── main.py
├── agent.py
├── memory_manager.py
├── tool_registry.py
├── requirements.txt
├── README.md
└── tools/
    ├── __init__.py
    ├── base_tool.py
    ├── calculator_tool.py
    ├── time_tool.py
    ├── translation_tool.py
    └── file_reader_tool.py

Author: Chanka Matara Arahchi