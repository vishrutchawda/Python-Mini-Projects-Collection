# Python Mini Projects Collection [![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains a collection of Python-based mini projects, showcasing a variety of applications and games built using Python's `tkinter` for GUI and `pygame` for game development. The project includes a main menu to select and run different modules, such as a Snake Game, Banking System, Dot Matrix Printer, Number Game, Rock Paper Scissors, and Train Ticket Booking system.[attached_file:1]

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [Snake Game](#snake-game)
  - [Banking System](#banking-system)
  - [Dot Matrix Printer](#dot-matrix-printer)
  - [Number Game](#number-game)
  - [Rock Paper Scissors](#rock-paper-scissors)
  - [Train Ticket Booking](#train-ticket-booking)
- [License](#license)
- [Contributing](#contributing)
- [Author](#author)

## Project Overview
This project is a collection of interactive Python applications accessible through a `tkinter`-based main menu. Each module demonstrates different aspects of Python programming, including GUI development, database integration, game logic, and animations. The applications are designed to be user-friendly and modular, allowing easy additions or modifications.[attached_file:1]

## Features
- **Main Menu**: A `tkinter` GUI to select and launch different modules.
- **Snake Game**: A classic snake game built with `pygame`, featuring score tracking and pause functionality.
- **Banking System**: A simple banking application with MySQL integration for account management (create, delete, deposit, withdraw, and display accounts).
- **Dot Matrix Printer**: A text-based animation tool that renders letters in a dot-matrix style using `pyfiglet`.
- **Number Game**: A competitive number-adding game where players aim to reach a score of 100 without exceeding it.
- **Rock Paper Scissors**: A GUI-based game with animated outcomes and user vs. computer gameplay.
- **Train Ticket Booking**: A train ticket reservation system with station, train, and coach selection, including pricing.[attached_file:1]

## Prerequisites
To run this project, you need the following installed:
- Python 3.6 or higher
- Required Python libraries:
  - `tkinter` (usually included with Python)
  - `pygame`
  - `pyfiglet`
  - `mysql-connector-python`
- MySQL Server (for the Banking System module)
- A MySQL database named `banking_system` with a table `accounts` (see Banking System for setup instructions)[attached_file:1]

## Installation
1. Clone the repository:
git clone https://github.com/vishrutchawda/Python-Mini-Projects-Collection.git
cd Python-Mini-Projects-Collection

2. Install the required libraries:
pip install -r requirements.txt

3. Set up the MySQL database for the Banking System:
- Create a database named `banking_system`.
- Create the `accounts` table using the following SQL:
  ```
  CREATE TABLE accounts (
      account_number BIGINT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      balance DECIMAL(10, 2) NOT NULL
  );
  ```
- Update the `db_config` in `banking_system.py` with your MySQL credentials:
  ```
  db_config = {
      'host': 'localhost',
      'user': 'your_username',
      'password': 'your_password',
      'database': 'banking_system'
  }
  ```[attached_file:1]

## Usage
Run the main program:
python main.py

The main menu will appear, allowing you to select one of the following options:
- Snake Game
- Train Ticket Booking
- Banking System
- Dot Matrix Printer
- Number Game
- Rock Paper Scissors

Click a button to launch the corresponding module. Each module runs independently and returns to the main menu upon completion (where applicable).[attached_file:1]

## Modules
### Snake Game
A classic snake game implemented using pygame. The snake moves to collect food, increasing its length and score. Features include:
- Pause functionality (click the pause icon in the top-right corner).
- Game over screen with a "Start Again" option.
- Increasing speed as the score grows.
File: `snake_game.py`[attached_file:1]

### Banking System
A simple banking application with MySQL integration for managing accounts. Features include:
- Create a new account with a unique account number and initial balance.
- Delete an existing account.
- Deposit and withdraw money.
- Display all accounts in a table format.
File: `banking_system.py`

Note: Requires a MySQL server and database setup as described in Installation.[attached_file:1]

### Dot Matrix Printer
A fun application that renders a single letter in a dot-matrix style using pyfiglet. Features include:
- Input a single letter to display its ASCII art representation.
- Slow animation effect for rendering each line.
- Option to quit by entering 'q' or 'quit'.
File: `dot_matrix_printer.py`[attached_file:1]

### Number Game
A competitive game where the player and computer take turns adding numbers (1-10) to a total score, aiming to reach 100 without exceeding it. Features include:
- Input validation for numbers between 1 and 10.
- Computer strategy to counter the player's moves.
- Reset functionality to start a new game.
File: `game.py`[attached_file:1]

### Rock Paper Scissors
A classic game implemented with a tkinter GUI, featuring:
- Animated "Rock, Paper, Scissors, Shoot!" sequence.
- Visual display of user and computer choices using ASCII art.
- Win/loss/draw results with color-coded feedback.
File: `rock_paper_scissors.py`[attached_file:1]

### Train Ticket Booking
A train ticket reservation system with a tkinter GUI, allowing users to:
- Select departure and arrival stations.
- Choose a train and coach type (e.g., First Class, Sleeper, AC).
- View train timings and calculate total ticket prices based on the number of tickets.
- Confirm bookings with a summary of the total price.
File: `train.py`[attached_file:1]

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.[attached_file:1]

## Contributing
Contributions are welcome! Fork the repo, create a branch for your feature, and submit a pull request. Ideas for new modules (e.g., more games or utilities) or bug fixes are encouraged. Ensure code is modular and tested with Python 3.6+.[attached_file:1]

## Author
Vishrut Chawda - Computer Science Student @ A.V Parekh Technical Institute, Rajkot  
Email: vishrutchawda@gmail.com  
LinkedIn: [www.linkedin.com/in/gp-avpti-comp-vishrut-chawda-s236020307230](https://www.linkedin.com/in/gp-avpti-comp-vishrut-chawda-s236020307230)  
GitHub: [vishrutchawda](https://github.com/vishrutchawda)[attached_file:1]
