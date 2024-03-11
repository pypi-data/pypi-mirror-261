from openai.types import Completion
from typing import List
import os
import json
from ._errors import GaidmeError

class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def _parse_command_from_response(response: Completion) -> str:
    arguments = json.loads(
        response.choices[0].message.tool_calls[0].function.arguments)
    return arguments['command']


def load_env() -> None:
    chat_model = os.getenv("OPENAI_API_MODEL")

    if not chat_model:
        os.environ["OPENAI_API_MODEL"] = "gpt-4-turbo-preview"
    else:
        if chat_model[4:5] == '3':
            raise GaidmeError("Only GPT-4 and higher can be used")

    if not os.getenv("OPENAI_API_KEY"):
        if not os.getenv("AZURE_OPENAI_API_KEY"):
            raise GaidmeError("Missing OpenAi API Key")
        if not os.getenv("AZURE_OPENAI_ENDPOINT"):
            raise GaidmeError("Missing Azure OpenAI Endpint")

def _check_files_exist(paths: list) -> bool:
    for file_path in paths:
        if os.path.exists(file_path):
            if os.path.getsize(file_path) > 0:
                return True
            else:
                print(f"File {file_path} istnieje, ale jest pusty.")
                return False
        else:
            print(f"Plik {file_path} nie istnieje.")
            return False
        
def _get_hidden_args() -> List:
    paths = ["/tmp/user_query.txt", "/tmp/command_result.txt", "/tmp/command.txt"]
    _check_files_exist(paths)
    commands = []
    for path in paths:
        with open(path, 'r') as f:
            commands.append(f.read())
    return commands
