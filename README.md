# Connect-N
An extended version of the Tic-Tac-Toe game. Connect N cells in a row to win the game. 

N can be configured in [config.py](config.py). So too can the size of the board.

# Usage
```
#!/bin/bash
> cd /path/to/project
> pip install -r requirements.txt
> python3 <game_type>.py
```
where game_type is one of: `human_vs_human_game`, `human_vs_simple_ai_game` or `human_vs_advanced_ai_game`

Then, follow the prompts provided by the game.

# Roadmap
- [x] Human vs human
- [x] Human vs simple AI (Monte Carlo Tree Search)
- [ ] Human vs reinforced AI (Monte Carlo Tree Search + Neural Network trained)

# Requirements
- Require python 3.9+
- For package requirements, see [requirements.txt](requirements.txt)