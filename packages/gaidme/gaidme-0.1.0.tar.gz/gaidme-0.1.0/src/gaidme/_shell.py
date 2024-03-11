import os
import sys
import shutil
import signal
import pexpect
import logging
from typing import Any
from pathlib import Path
from shellingham import detect_shell, ShellDetectionFailure

_logger = logging.getLogger(__name__)


class Shell:
    _shell = None

    def __init__(self, name: str, path: str) -> None:
        self._name = name
        self._path = path

    @property
    def name(self) -> str:
        return self._name

    @property
    def path(self) -> str:
        return self._path

    @classmethod
    def get(cls):
        if cls._shell is not None:
            return cls._shell

        try:
            name, path = detect_shell(os.getpid())
        except (RuntimeError, ShellDetectionFailure):
            shell = None

            if os.name == "posix":
                shell = os.environ.get("SHELL")
            elif os.name == "nt":
                shell = os.environ.get("COMSPEC")

            if not shell:
                raise RuntimeError("Unable to detect the current shell")
            _logger.debug(f"Shell: {shell}")
            name, path = Path(shell).stem, shell

        cls._shell = cls(name, path)
        return cls._shell

    def get_last_command(self) -> None:
        # c = pexpect.spawn('/bin/zsh', ['-c', command])
        # if self._name == "zsh":
        #     command = '/bin/zsh -c "echo $(fc -ln -1)"'
        # else:
        #     command = "ls -la"
        # terminal = shutil.get_terminal_size()
        # c = pexpect.spawn('/bin/zsh -c "history"', dimensions=(terminal.lines, terminal.columns))
        
        # c.expect(pexpect.EOF)
        # print(c.before)
        # c.close()
        print(pexpect.run("history"))

    def execute_old(self, command: str) -> int:
        if self._name != "bash":  # TODO: mozna to jakos poprawić pewnie
            _logger.debug(f"SHELL: {self._name}")

        terminal = shutil.get_terminal_size()
        c = pexpect.spawnu(
            self._path, dimensions=(terminal.lines, terminal.columns))

        if self._name == "zsh":
            c.setecho(False)

        c.sendline(command)

        def resize(sig: Any, data: Any) -> None:
            terminal = shutil.get_terminal_size()
            c.setwinsize(terminal.lines, terminal.columns)

        signal.signal(signal.SIGWINCH, resize)

        c.interact(escape_character=None)
        c.close()

        # Usunięto sys.exit(c.exitstatus) i zamiast tego zwracamy status wyjścia
        return c.exitstatus
