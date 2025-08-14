import random
import re
from typing import Optional

COMMAND = "random"

help_text = """
# Usage: 
random numbers [--min <min>] [--max <max>] [--digits <digits>] [--amount <amount>]
random dice <NdM> [<NdM> ...]

## Numbers
Generates random numbers based on the provided parameters.
--min <min> : Minimum value for the random number (default: 1)
--max <max> : Maximum value for the random number (default: 100)
--digits <digits> : Generates a random number with the specified number of digits (overrides --min and --max)
--amount <amount> : Number of random numbers to generate (default: 1)

Examples:
`random numbers --min 10 --max 50 --amount 5` outputs 5 random numbers between 10 and 50. i.e. 42, 17, 23, 18, 34
`random numbers --digits 3 --amount 2 outputs 2` random numbers with a maximum of 3 digits each. i.e 123, -456

## Dice
Rolls dice in NdM format, where N is the number of dice and M is the number of sides per die.
Example: random dice 2d6 1d20
"""

random_arg_re = re.compile(r"--(min|max|digits|amount) (-?\d+)")
dice_arg_re = re.compile(r"(\d+)[dD](\d+)")

def _generate_random_numbers(command_string: str) -> str:
    parsed_args = {match.group(1): int(match.group(2)) 
            for match in random_arg_re.finditer(command_string)}
    return _random_numbers(parsed_args['min'], parsed_args['max'], parsed_args.get('digits'), parsed_args.get('amount', 1))

def _random_numbers(min_value: int = 1, max_value: int = 100, digits: Optional[int] = None, amount: int = 1) -> str:
    if digits is not None:
        min_value = -int("9" * digits)
        max_value = int("9" * digits)
    
    return ",".join([str(random.randint(min_value, max_value)) for _ in range(amount)])

def _parse_dice_arguments(arg: list[str]) -> dict[int, int]:
    return {int(match.group(2)): int(match.group(1)) for match in dice_arg_re.finditer(" ".join(arg))}

def _dice_rolls(dice: list[str]) -> str:
    output = "## Results:\n"
    running_total = 0
    for roll_group, (side_count, roll_count) in enumerate(_parse_dice_arguments(dice).items(), 1):
        outcomes = [random.randint(1, side_count) for _ in range(0, roll_count)]
        
        total = sum(outcomes)
        running_total += total
        output += f"### Roll group {roll_group}:\n" 
        for roll_number, outcome in enumerate(outcomes, 1):
            output += f"d{side_count} #{roll_number}: {outcome if side_count > 2 else ("H" if outcome == 1 else "2") }\n"
        output += f"d{side_count} Total: {total}\n\n"
        
    output += f"### Overall total: {running_total}"
    
    return output

def execute(args: list[str]) -> str:
    if not args:
        return help_text
    
    match args[0]:
        case "numbers":
            return _generate_random_numbers(" ".join(args[1:]))
            
        case "dice":
            return _dice_rolls(args[1:])

    return help_text
    
    