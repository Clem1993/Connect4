#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import numpy as np
import sys
from pathlib import Path

# To execute directly from test
sys.path.append("../")

from class_module import Connect4


def test_add_token() -> None:
    """Test that the Add_token is working adding the tokens
    """
    size_array = 9
    value_token = 1
    choose_col = 0
    compare_array = np.zeros((size_array, size_array))
    compare_array[size_array - 1, 0] = 1
    Con4 = Connect4(size_array)
    array_ori = Con4.array_connect

    array_ori, _, _, _ = Con4.Add_token(array_ori, choose_col, value_token)
    assert (array_ori == compare_array).all()
