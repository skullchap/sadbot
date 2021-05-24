"""Bot commands modules interface"""

from typing import Optional

from sadbot.message import Message


class CommandsInterface:
    """This is the interface for the bot commands, every bot command module must implement
    these functions"""

    @property
    def command_regex(self) -> str:
        """Returns the regex string that triggers this command"""

    @property
    def parsemode(self) -> Optional[str]:
        """Returns the command parsemode"""

    def get_reply(self, message: Optional[Message] = None) -> Optional[str]:
        """Returns the command output"""