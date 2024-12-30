# Real-Time Strategy Game Engine

This repository contains a fully featured data-driven game engine built using Pygame. The engine supports scene management through a finite state machine (FSM) and is designed to load game data from external sources like JSON files. The current implementation includes a real-time strategy (RTS) game with unit management, resource gathering, and combat mechanics.

## Features

- Data-driven engine with support for loading game data from JSON files
- Scene management using a finite state machine (FSM)
- Real-time strategy game with unit management, resource gathering, and combat mechanics
- Pygame-based rendering and event handling

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pygame

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JorchRL/pyGameEngine.git
   cd pyGameEngine
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

To run the RTS game, execute the following command:
```bash
python main.py
```

## Directory Structure

```
pyGameEngine/
├── assets/                 # Game assets (images, sounds, etc.)
├── engine/                 # Core engine components
│   ├── __init__.py
│   ├── data_loader.py      # DataLoader class for loading game data from JSON files
│   ├── engine.py           # Main game engine
│   ├── events.py           # Event system
│   ├── scene.py            # Base class for scenes
│   └── scenefsm.py         # Finite state machine for scene management
├── game/                   # Game-specific components
│   ├── __init__.py
│   ├── constants.py        # Game constants
│   ├── resource.py         # Resource class for RTS game
│   └── unit.py             # Unit class for RTS game
├── scenes/                 # Game scenes
│   ├── __init__.py
│   ├── game_over_scene.py  # Game over scene
│   ├── gameplay_scene.py   # Gameplay scene for the snake game
│   ├── new_game_scene.py   # New game scene
│   └── rts_gameplay_scene.py # Gameplay scene for the RTS game
├── main.py                 # Entry point for the game
└── requirements.txt        # Required dependencies
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
