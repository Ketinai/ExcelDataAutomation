# External packages
import argparse
import numpy as np
import pandas as pd
from openpyxl import load_workbook

# My library
import myproject as m


def main(args):
    m.validation.validate_args(args)

    # Get user_operation and initialize it
    user_operation = m.operations.all_operations[args.operation]()

    # Read data and check conditions
    if isinstance(user_operation, m.operations.PivotOperation):
        user_operation.read_data(args.filename, args.pivot_names, args.pivot_index)
    else:
        # Load file
        wb = load_workbook(filename=args.filename)
        # Get sheet, will throw error if sheet is not existing
        sheet = wb[args.sheet]

        if isinstance(user_operation, m.operations.SingleOperation):
            user_operation.read_data(sheet, args.index0)
        elif isinstance(user_operation, m.operations.DoubleOperation):
            user_operation.read_data(sheet, args.index0, args.index1)
        elif isinstance(user_operation, m.operations.ConditionalOperation):
            user_operation.read_data(sheet, args.index0, args.index_if)
            user_operation.check_condition(args.condition)
        else:
            raise AttributeError("Unknown operation type!")

    # Perform operation
    result = user_operation.calculate()

    # Save results
    if args.save is True:
        if isinstance(user_operation, m.operations.PivotOperation):
            result.to_excel("./report_pivot.xlsx", sheet_name='Report', startrow=1)
            print("Created new file with pivot table!")
        else:
            df = pd.read_excel(args.filename)
            df.insert(
                len(df.columns) if args.save_index is None else args.save_index,
                "Results" if args.save_name is None else args.save_name,
                result,
            )
            print(f"Updated file f{args.filename} with column:\n {df.head()}")
            df.to_excel(args.filename, args.sheet)

    print(f"Result: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--filename", type=str, help="Name of the file.")
    parser.add_argument("--sheet", type=str, help="Name of the sheet.")
    parser.add_argument(
        "--operation",
        type=str,
        choices=m.operations.all_operations.keys(),
        help="Operation that will be done on range, column or row. Types of operations:\n\n"
             "'s_xxx'  are single operations, require: 'index0'\n"
             "'if_xxx' are conditional operations, require: 'index0', 'index_if', 'condition'\n"
             "'d_xxx'  are double operations, require: 'index0', 'index1'\n"
             "'pivot'  makes pivot column, require: pivot_names, pivot_index\n\n",
    )
    parser.add_argument(
        "--index0",
        type=str,
        help="First range/column/row from the spreadsheet.",
    )
    parser.add_argument(
        "--index1",
        type=str,
        help="Second range/column/row from the spreadsheet."
    )
    parser.add_argument("--index_if", type=str, help="Conditional range/column/row from the spreadsheet.")
    parser.add_argument("--condition", type=str, help="Condition value to check against.")
    parser.add_argument(
        "--pivot_names",
        nargs='+',
        type=str,
        help="Create a pivot table. Names of columns from the spreadsheet.",
    )
    parser.add_argument(
        "--pivot_index",
        nargs='+',
        type=str,
        help="Create a pivot table. Name of a column from the spreadsheet.",
    )
    parser.add_argument(
        "--save",
        type=bool,
        choices=[True, False],
        help="Saving results inside a file."
    )
    parser.add_argument(
        "--save_index",
        nargs='?',
        type=int,
        help="Column where results will be stored. Default: next to the last column of the file"
    )
    parser.add_argument(
        "--save_name",
        nargs='?',
        type=str,
        help="Column name where results will be stored. Default: 'Results'"
    )
    # parser.add_argument('--mode', nargs='+', type=int)

    args = parser.parse_args()

    main(args)
