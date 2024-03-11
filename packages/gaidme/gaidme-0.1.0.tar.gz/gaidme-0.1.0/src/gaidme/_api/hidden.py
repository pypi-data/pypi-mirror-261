import logging
from .._terminal import _print_command
from ..utils import _get_hidden_args
from ..models import get_reflection
from ..schema import reflect_system_promt
from .._terminal import _print_command
_logger = logging.getLogger(__name__)

def hidden_command(args):
    user_query, command_result, command = _get_hidden_args()
    system_prompt = reflect_system_promt(command, command_result)
    result = get_reflection(user_query, system_prompt)
    _print_command(result)
    