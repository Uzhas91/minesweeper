# tests/test_minesweeper.py

import random

import pytest

import src.minesweeper.minesweeper as minesweeper


def test_module_exists():
    assert minesweeper


def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    assert len(game.mines) == 2


def test_reveal():
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    game.reveal(2, 2)
    assert game.revealed == {(2, 2)}
