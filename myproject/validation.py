# External libraries
import os.path
# My library
from myproject.operations import all_operations, PivotOperation, DoubleOperation, ConditionalOperation

def check_index(index, num):
    if index is None:
        raise ValueError(f"Please specify range, column or row for index{num}!")


def validate_args(args):
    """
    Validate arguments, raise error and exit program if something is wrong.
    """
    # Check if user file is existing
    if os.path.isfile(args.filename):
        print(f"Loading: {args.filename}")
    else:
        raise FileNotFoundError(f"Cannot find specified file: {args.filename}")

    # Check if operation is existing
    if args.operation in all_operations:
        print(f"Performing operation: {args.operation} {all_operations[args.operation]}")
    else:
        raise AttributeError(f"Unknown operation: `{args.operation}`, please check it!")

    # Checking indexes
    if isinstance(all_operations[args.operation](), PivotOperation):
        if args.pivot_names is None:
            raise AttributeError(f"pivot_names is missing!")
        if args.pivot_index is None:
            raise AttributeError(f"pivot_index is missing!")
    else:
        # Standard index
        check_index(args.index0, 0)
        # Index required by DoubleOperation
        if isinstance(all_operations[args.operation](), DoubleOperation):
            check_index(args.index1, 1)
        # Index required by ConditionalOperation
        if isinstance(all_operations[args.operation](), ConditionalOperation):
            if args.index_if is None or args.condition is None:
                raise AttributeError("Invalid arguments for 'if' operation")