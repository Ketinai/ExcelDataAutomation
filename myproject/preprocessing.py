import numpy as np
from openpyxl.cell.cell import Cell


def get_values(data):
    if isinstance(data, Cell):
        return [data.value]
    return [x.value for x in data]


def prune_none(data):
    new_data = []

    for value in data:
        if value is not None:
            new_data += [value]

    return new_data


def prune_strings(data):
    new_data = []

    for value in data:
        if isinstance(value, (int, float)):  # not string or so...
            new_data += [value]

    return new_data


def flatten_data(data):
    return [item for sublist in data for item in sublist]


def get_data(sheet, index, prune_flag=False) -> np.ndarray:
    if index.find(":") != -1:  # index is range
        data = flatten_data(sheet[index])
    else:  # index is single cell, column or row
        data = sheet[index]

    data = get_values(data)

    if prune_flag is True:
        data = prune_none(data)
        data = prune_strings(data)

    return np.array(data)
