import sys
from typing import Optional

COMMAND = "plugins"

def _get_command_name(modules_name: str) -> Optional[str]:
    modules = sys.modules.get(modules_name)
    
    command = getattr(modules, "COMMAND", None)
    
    return command

def execute(_: list[str]) -> str:
    custom_modules = [mod for mod in sys.modules.keys() if mod.startswith("bot.plugins.")]
    if not custom_modules:
        return "No plugins found."
    
    commands = [command_name for command in custom_modules if (command_name := _get_command_name(command)) is not None]
    
    return "\n".join(commands) if commands else "No plugins found."
    
    