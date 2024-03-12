from pypilot.agent import base
from pypilot.parser import json_parser      
from pypilot.agent.prompt import Prompt
PROMPT = Prompt(messages=[
        {"role": "system", "content": """
Given a user request inside a python terminal, select the best suited agent to handle the request.

Answer with a markdown code snippet with a JSON object formatted to look like:
```json
{{
    "thought": explain your thought process of selecting the agent,
    "agent": name of the agent,
}}
```

Agents:
- PythonCodeAgent: A python coding assistant that given the terminal history, locals, and a user request, generates a valid python code that can run as is inside a python terminal.
- ChatAgent: A chatbot that engage in a conversation and does not write code.
"""},
            {"role": "user", "content": "{instruction}"}
    ])

OUTPUT_PARSER = json_parser

class RouterAgent(base.AgentBase):
    output_parser = OUTPUT_PARSER
    prompt: Prompt = PROMPT