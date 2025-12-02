# Python Learning Projects 🎓🐍

Welcome to my Python learning projects repository! This repo contains small scripts and programs I’ve written while learning Python. Some of them demonstrate my coding skills, and some are fun, playable programs like games.

---

## Guessing Game 🎲

A simple console-based number guessing game in Python.

### Description

The computer randomly selects a number, and the player tries to guess it. The game gives hints if the guess is too low or too high, and celebrates when the guess is correct.  

This project is a great way to practice Python basics:

- Loops and conditionals
- Input validation
- Random numbers
- Functions

### How to Play

1. Run the game:

```bash
python game.py
Enter a level (the maximum number to guess). Must be a positive integer.

Keep guessing the number. The game will respond with:

Too small! → your guess is lower than the number

Too large! → your guess is higher than the number

Just right! → you guessed the number correctly!

The game ends when you guess the number.

Example
Level: 50
Guess: 25
Too small!
Guess: 40
Too large!
Guess: 32
Just right!

Requirements

Python 3.x

No external libraries required (uses built-in random module)