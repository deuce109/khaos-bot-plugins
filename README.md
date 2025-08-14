# Khaos Bot Plugins

This repoository is meant to provide some basic plugins for my other project [Khaos Bot](https://github.com/deuce109/khaos-bot)

## Plugins In This Repo

### RNG

Provides some basic random number generation uses.

#### Usage 
`random numbers [--min <min>] [--max <max>] [--digits <digits>] [--amount <amount>]`

`random dice <NdM> [<NdM> ...]`

## Numbers
Generates random numbers based on the provided parameters.
`--min <min>` : Minimum value for the random number (default: 1)

`--max <max>` : Maximum value for the random number (default: 100)

`--digits <digits>` : Generates a random number with the specified number of digits (overrides --min and --max)

`--amount <amount>` : Number of random numbers to generate (default: 1)

Examples:

`random numbers --min 10 --max 50 --amount 5` outputs 5 random numbers between 10 and 50. i.e. 42, 17, 23, 18, 34

`random numbers --digits 3 --amount 2 outputs 2` random numbers with a maximum of 3 digits each. i.e 123, -456

## Dice
Rolls dice in `<N>d<M>` format, where N is the number of dice and M is the number of sides per die.

Example: `random dice 2d6 1d20`

### Server

#### Usage
`server` Returns the bots current external IP (found by calling `https://ifconfig.me/ip`)

### Source
#### Usage
`source` Returns the source code for the bot