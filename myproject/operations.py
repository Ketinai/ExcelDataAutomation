# External libraries
import numpy as np
import pandas as pd
# My library
from myproject.preprocessing import get_data

###
# Base classes definitions
###
class Operation:
    def __init__(self):
        pass

    def calculate(self):
        raise NotImplementedError("Implement calculate function!")

    def read_data(self):
        raise NotImplementedError("Implement read_data function!")


class SingleOperation(Operation):
    def read_data(self, sheet, index, prune_flag=True):
        self.data0 = get_data(sheet, index, prune_flag)


class ConditionalOperation(Operation):
    def check_condition(self):
        """Check condition, if invalid raise error."""
        raise NotImplementedError("Implement check_condition function!")

    def read_data(self, sheet, index0, index_if, prune_flag=True):
        self.data0 = get_data(sheet, index0, prune_flag)
        self.condition_data = get_data(sheet, index_if, False)


class DoubleOperation(Operation):
    def read_data(self, sheet, index0, index1, prune_flag=True):
        self.data0 = get_data(sheet, index0, prune_flag)
        self.data1 = get_data(sheet, index1, prune_flag)


###
# Custom operations
###
class SingleSum(SingleOperation):
    def calculate(self):
        return np.sum(self.data0)


class SingleProduct(SingleOperation):
    def calculate(self):
        return np.prod(self.data0)


class SingleMax(SingleOperation):
    def calculate(self):
        return np.max(self.data0)


class SingleMin(SingleOperation):
    def calculate(self):
        return np.min(self.data0)


class ConditionalSum(ConditionalOperation):
    def calculate(self):
        return np.sum(self.data0)

    def check_condition(self, condition):
        """Check if given data is matching the condition."""
        if np.all(self.condition_data != condition):
            raise RuntimeError("Condition != does not match!")
        # Exit without return, as this function raise error in case of fail.


class DoubleMul(DoubleOperation):
    def calculate(self):
        return np.multiply(self.data0, self.data1)


class PivotOperation(Operation):
    def calculate(self):
        return self.file.pivot_table(index=self.index, values=self.names)

    def read_data(self, filename, names, index):
        self.file = pd.read_excel(filename, engine='openpyxl')
        self.names = names
        self.index = index


###
# List of operations
###
all_operations = {
    "s_sum": SingleSum,
    "s_prod": SingleProduct,
    "s_max": SingleMax,
    "s_min": SingleMin,
    "if_sum": ConditionalSum,
    "d_mul": DoubleMul,
    "pivot": PivotOperation,
}