#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import click
import sys
import colorama
from typing import Tuple, Dict
from termcolor import colored
from random import randint


# Define the colors for each value
colors = {0: "blue", 1: "red", 2: "yellow"}

# Define a function to map each element to its corresponding color
def color_map(x):
    return click.style(str(x), fg=colors[x])


def Obtain_key(dict_val: Dict, value: int) -> str:

    return list(dict_val.keys())[list(dict_val.values()).index(value)]


def Toss_coin(value) -> Dict:
    """Function to know who will be the first to start

    Args:
        value (int): Choosen value 

    Returns:
        Dict: : dict allowing to know which player is associated to which position
    """

    rand_value = randint(0, 1)
    click.echo(f"The random value is : {rand_value}")
    if value == rand_value:
        dict_pos = {"human": "player_1", "bot": "player_2"}
        click.echo(
            click.style("Congratulation !!!! You are the first to start", fg="green")
        )
    else:
        dict_pos = {"human": "player_2", "bot": "player_1"}
        click.echo(click.style("You will start in second position", fg="green"))
    return dict_pos


def Victory_message(value: int, num_token: int, player: str):

    if num_token == 4:
        click.echo(f"The number of consecutive tokens is 4 the {player} wins")
        sys.exit(0)


class Connect4:
    def __init__(self, dim_array: int):
        """

        Args:
            dim_array (int): size of the array 
        """

        self.dim_array = dim_array
        self.DICT_VALUES = {"player_1": 1, "player_2": 2}
        self.array_connect = np.zeros((dim_array, dim_array))
        self.DICT_COLORS = {0: "blue", 1: "red", 2: "yellow"}

    def Display_connect4(self, array_connect: np.array) -> None:
        """ Print the connect4 state 

        Args:
            array_connect (np.array): 
        """
        colored_array = np.vectorize(color_map)(self.array_connect)
        for row in colored_array:
            click.echo(" ".join(row))
        # click.echo(self.array_connect)

    def Add_token(
        self, array_connect: np.array, ind_col: int, value: int
    ) -> Tuple[np.array, int, int, bool]:
        """This function is used to add the tokens in the choosen raw 

        Args:
            array_connect (np.array): 
            ind_col (int): column index
            value (int): Player's token it should be 1 for player 1 or 2 for player 2

        Returns:
            Tuple[np.array, int, int,bool]: return respectively the array with the added value,the column index and the line index
        """

        if ind_col < 0 or ind_col > len(self.array_connect) - 1:
            click.echo(
                f"The input value : {ind_col} that you have put is false it is out of bound"
            )
            return self.array_connect, ind_col, ind_col, False

        elif np.sum((self.array_connect[:, ind_col] == 0)) == 0:
            click.echo(
                f"The column {ind_col} is already full you must choose an other column"
            )
            return self.array_connect, ind_col, ind_col, False
        else:
            i = 0
            while self.array_connect[self.dim_array - 1 - i, ind_col] != 0:
                i += 1
            self.array_connect[self.dim_array - 1 - i, ind_col] = value
            return self.array_connect, self.dim_array - 1 - i, ind_col, True

    def Check_vertical(
        self,
        array_connect: np.array,
        ind_col: int,
        ind_line: int,
        value: int,
        DICT_VALUES: Dict,
    ) -> None:
        """ Check if there is 4 consecutives tokens of the same values vertically 

        Args:
            array_connect (np.array): array represnting the connect4
            ind_col (int): columns index 
            ind_line (int): line index 
            value (int): Value reprensting the token 1 for player_1 and 2 for player_2
            DICT_VALUES (Dict): Dict containing the value for player_1 and player_2
        """
        num_token = 0
        i = 0
        while i + ind_line < self.dim_array and i < 4:
            if self.array_connect[ind_line + i, ind_col] == value:
                i += 1
                num_token += 1
            else:
                break
        i = -1
        while ind_line + i >= 0 and i > -4:
            if self.array_connect[ind_line + i, ind_col] == value:
                i -= 1
                num_token += 1
            else:
                break

        player = Obtain_key(DICT_VALUES, value)
        Victory_message(value, num_token, player)
        # click.echo(
        #     f"The number of consecutives token for the value {value} vertically is {num_token}"
        # )

    def Check_horizontal(
        self,
        array_connect: np.array,
        ind_col: int,
        ind_line: int,
        value: int,
        DICT_VALUES: dict,
    ) -> None:

        """ Check if there is 4 consecutives tokens of the same values horizontaly
    
        Args:
            array_connect (np.array): array represnting the connect4
            ind_col (int): columns index 
            ind_line (int): line index 
            value (int): Value reprensting the token 1 for player_1 and 2 for player_2
            DICT_VALUES (Dict): Dict containing the value for player_1 and player_2
        """
        num_token = 0
        i = 0
        while i + ind_col < self.dim_array and i < 4:
            if self.array_connect[ind_line, ind_col + i] == value:
                i += 1
                num_token += 1
            else:
                break
        i = -1
        while ind_col + i >= 0 and i > -4:
            if self.array_connect[ind_line, ind_col + i] == value:
                i -= 1
                num_token += 1
            else:
                break

        # click.echo(
        #     f"The number of consecutives token for the value {value} horizontally is {num_token}"
        # )
        player = Obtain_key(DICT_VALUES, value)
        Victory_message(value, num_token, player)

    def Check_diagonal_pos(
        self,
        array_connect: np.array,
        ind_col: int,
        ind_line: int,
        value: int,
        DICT_VALUES: dict,
    ) -> None:

        """ Check if there is 4 consecutives tokens of the same values diagonaly
    
        Args:
            array_connect (np.array): array represnting the connect4
            ind_col (int): columns index 
            ind_line (int): line index 
            value (int): Value reprensting the token 1 for player_1 and 2 for player_2
            DICT_VALUES (Dict): Dict containing the value for player_1 and player_2
        """

        num_token = 0
        i = 0
        while i + ind_col < self.dim_array and i < 4 and i + ind_line < self.dim_array:
            if self.array_connect[ind_line + i, ind_col + i] == value:
                i += 1
                num_token += 1
            else:
                break
        i = -1
        while ind_line + i >= 0 and i > -4 and ind_col + i >= 0:
            if self.array_connect[ind_line + i, ind_col + i] == value:
                i -= 1
                num_token += 1
            else:
                break

        # click.echo(
        #     f"The number of consecutives token for the value {value} diagonaly is {num_token}"
        # )
        player = Obtain_key(DICT_VALUES, value)
        Victory_message(value, num_token, player)

    def Check_diagonal_neg(
        self,
        array_connect: np.array,
        ind_col: int,
        ind_line: int,
        value: int,
        DICT_VALUES: dict,
    ) -> None:

        """ Check if there is 4 consecutives tokens of the same values diagonaly
    
        Args:
            array_connect (np.array): array represnting the connect4
            ind_col (int): columns index 
            ind_line (int): line index 
            value (int): Value reprensting the token 1 for player_1 and 2 for player_2
            DICT_VALUES (Dict): Dict containing the value for player_1 and player_2
        """

        num_token = 0
        i = 0
        while i + ind_col < self.dim_array and i < 4 and ind_line - i >= 0:
            if self.array_connect[ind_line - i, ind_col + i] == value:
                i += 1
                num_token += 1
            else:
                break
        i = -1
        while ind_line - i < self.dim_array and i > -4 and ind_col + i >= 0:
            if self.array_connect[ind_line - i, ind_col + i] == value:
                i -= 1
                num_token += 1
            else:
                break

        # click.echo(
        #     f"The number of consecutives token for the value {value} diagonaly is {num_token}"
        # )
        player = Obtain_key(DICT_VALUES, value)
        Victory_message(value, num_token, player)
