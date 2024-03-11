import logging
from .._shell import Shell
from .._terminal import _print_command
from ..schema import reflect_system_promt
from ..models import get_reflection

_logger = logging.getLogger(__name__)

def reflect_command(args) -> None:
    _logger.debug("running reflect_command")
    user_query = ' '.join(args.reflect)
    with open('/tmp/user_query.txt', 'w') as f:
        f.write(user_query)
    shell = Shell.get()
    shell.execute_old("""history | tail -n 2 | head -n 1 | awk '{$1=""; print substr($0, 2)}' > /tmp/command.txt;source /tmp/command.txt > /tmp/command_result.txt; gaidme hidden""")
    _logger.debug("shell already run")

    # with open('/tmp/command.txt', 'r') as f:
    #     executed_command = f.read()

    # print(executed_command)
    # shell.execute(f"{executed_command} > /tmp/command_output.txt")
    # _logger.debug("Get previous command and saved to /tmp/command_output.txt")

    # with open('/tmp/command_output.txt') as f:
    #     command_result = f.read()

    # reflect_system_pr = reflect_system_promt(executed_command, command_result)

    # command = get_reflection(' '.join(args.ask), reflect_system_pr)
    # _print_command(command)


