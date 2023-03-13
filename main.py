#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import click
from class_module import Connect4, Toss_coin, Obtain_key
from random import randint
import sys


def main() -> None:

    """Main function to make the 
    connect4 works

    """

    click.echo("Please choose the array dimension")
    bool_te = False
    while bool_te == False:
        try:
            size_array = int(input())
            bool_te = True
        except ValueError:
            bool_te = False
            click.echo(
                click.style("Error with the ValueError: it should be an int", fg="red")
            )
    click.echo(f"The array size is : {size_array}")
    click.echo("Please choose a value between 0 or 1 for the coin tossing")
    bool_te = False
    while bool_te == False:
        try:
            value_coin = int(input())
            bool_te = True
        except ValueError:
            bool_te = False
            click.echo(
                click.style("Error with the ValueError: it should be an int", fg="red")
            )

    while value_coin != 0 and value_coin != 1:
        click.echo(
            click.style(
                f"Warning : You type the input value {value_coin} which is not possible , you must choose between 0 or 1",
                fg="red",
            )
        )
        click.echo(click.style("Please type again", fg="red"))
        value_coin = int(input())
    click.echo(
        click.style(
            f"You choose this value : {value_coin} , let's toss the coin", fg="green"
        )
    )
    # Get a dictionary to know betwenn the humand (you) and the bot who is player 1 and who is player 2
    dict_pos = Toss_coin(value_coin)
    pos_human = dict_pos["human"]
    pos_bot = dict_pos["bot"]
    click.echo(click.style(f"human is {pos_human} and bot is {pos_bot}", fg="green"))
    # initialisation of the connect four
    Conn4 = Connect4(size_array)
    array_connect = Conn4.array_connect
    Conn4.Display_connect4(array_connect)
    player = "player_1"
    number_void_place = np.sum((array_connect == 0))
    DICT_VALUES = Conn4.DICT_VALUES
    # Start of the game
    while number_void_place != 0:
        value_token = DICT_VALUES[player]
        type_player = Obtain_key(dict_pos, player)
        click.echo("Choose where do you want to put the token")
        if type_player == "bot":
            val_col = randint(0, size_array - 1)
        elif type_player == "human":
            val_col = int(input())
        click.echo(f"{player} choose the column : {val_col}")
        array_connect, col, ligne, test_fill = Conn4.Add_token(
            array_connect, val_col, value_token
        )
        while test_fill == False:
            click.echo("Please Type again the column value")
            if type_player == "bot":
                val_col = randint(0, size_array - 1)
            elif type_player == "human":
                val_col = int(input())
            click.echo(f"You choose the column : {val_col}")
            array_connect, col, ligne, test_fill = Conn4.Add_token(
                array_connect, val_col, value_token
            )
        Conn4.Display_connect4(array_connect)
        # Check if there is 4 tokens alligned
        Conn4.Check_vertical(array_connect, ligne, col, value_token, DICT_VALUES)
        Conn4.Check_horizontal(array_connect, ligne, col, value_token, DICT_VALUES)
        Conn4.Check_diagonal_pos(array_connect, ligne, col, value_token, DICT_VALUES)
        Conn4.Check_diagonal_neg(array_connect, ligne, col, value_token, DICT_VALUES)
        # Change of player
        if player == "player_1":
            player = "player_2"
        elif player == "player_2":
            player = "player_1"
        number_void_place = np.sum((array_connect == 0))

    click.echo("There is no winner for this game, you should do it again !!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
