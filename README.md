# Python Mini Projects Collection

This repository contains a collection of Python-based mini projects, showcasing a variety of applications and games built using Python's `tkinter` for GUI and `pygame` for game development. The project includes a main menu to select and run different modules, such as a Snake Game, Banking System, Dot Matrix Printer, Number Game, Rock Paper Scissors, and Train Ticket Booking system.

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
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project is a collection of interactive Python applications accessible through a `tkinter`-based main menu. Each module demonstrates different aspects of Python programming, including GUI development, database integration, game logic, and animations. The applications are designed to be user-friendly and modular, allowing easy additions or modifications.

## Features
- **Main Menu**: A `tkinter` GUI to select and launch different modules.
- **Snake Game**: A classic snake game built with `pygame`, featuring score tracking and pause functionality.
- **Banking System**: A simple banking application with MySQL integration for account management (create, delete, deposit, withdraw, and display accounts).
- **Dot Matrix Printer**: A text-based animation tool that renders letters in a dot-matrix style using `pyfiglet`.
- **Number Game**: A competitive number-adding game where players aim to reach a score of 100 without exceeding it.
- **Rock Paper Scissors**: A GUI-based game with animated outcomes and user vs. computer gameplay.
- **Train Ticket Booking**: A train ticket reservation system with station, train, and coach selection, including pricing.

## Prerequisites
To run this project, you need the following installed:
- Python 3.6 or higher
- Required Python libraries:
  - `tkinter` (usually included with Python)
  - `pygame`
  - `pyfiglet`
  - `mysql-connector-python`
- MySQL Server (for the Banking System module)
- A MySQL database named `banking_system` with a table `accounts` (see [Banking System](#banking-system) for setup instructions)

Install the required Python libraries using:
```bash
pip install -r requirements.txt

Installation:-

git clone https://github.com/your-username/python-mini-projects.git
cd python-mini-projects
pip install -r requirements.txt


Set up the MySQL database for the Banking System:
Create a database named banking_system.
Create the accounts table using the following SQL:

CREATE TABLE accounts (
    account_number BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    balance DECIM
AL(10, 2) NOT NULL
);


- Update the `db_config` in `banking_system.py` with your MySQL credentials:
```python
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'banking_system'
}



Usage :-
Run the main program:

python main.py

The main menu will appear, allowing you to select one of the following options:

Snake Game
Train Ticket Booking
Banking System
Dot Matrix Printer
Number Game
Rock Paper Scissors

Click a button to launch the corresponding module. Each module runs independently and returns to the main menu upon completion (where applicable).


Modules :-

Snake Game
A classic snake game implemented using pygame. The snake moves to collect food, increasing its length and score. Features include:

Pause functionality (click the pause icon in the top-right corner).
Game over screen with a "Start Again" option.
Increasing speed as the score grows.
File: snake_game.py

Banking System
A simple banking application with MySQL integration for managing accounts. Features include:

Create a new account with a unique account number and initial balance.
Delete an existing account.
Deposit and withdraw money.
Display all accounts in a table format.
File: banking_system.py

Note: Requires a MySQL server and database setup as described in Installation.

Dot Matrix Printer
A fun application that renders a single letter in a dot-matrix style using pyfiglet. Features include:

Input a single letter to display its ASCII art representation.
Slow animation effect for rendering each line.
Option to quit by entering 'q' or 'quit'.
File: dot_matrix_printer.py

Number Game
A competitive game where the player and computer take turns adding numbers (1-10) to a total score, aiming to reach 100 without exceeding it. Features include:

Input validation for numbers between 1 and 10.
Computer strategy to counter the player's moves.
Reset functionality to start a new game.
File: game.py

Rock Paper Scissors
A classic game implemented with a tkinter GUI, featuring:

Animated "Rock, Paper, Scissors, Shoot!" sequence.
Visual display of user and computer choices using ASCII art.
Win/loss/draw results with color-coded feedback.
File: rock_paper_scissors.py

Train Ticket Booking
A train ticket reservation system with a tkinter GUI, allowing users to:

Select departure and arrival stations.
Choose a train and coach type (e.g., First Class, Sleeper, AC).
View train timings and calculate total ticket prices based on the number of tickets.
Confirm bookings with a summary of the total price.
File: train.py
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author :- Vishrut Chawda

GitHub :- https://github.com/vishrutchawda/Python-Mini-Projects-Collection

LinkeIn :- www.linkedin.com/in/vishrut-chawda-899898342
