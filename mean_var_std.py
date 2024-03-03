import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the list into a 3 x 3 NumPy array
    matrix = np.array(lst).reshape(3, 3)

    # Calculate statistics
    result = {
        'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.flatten().mean()],
        'variance': [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.flatten().var()],
        'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.flatten().std()],
        'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.flatten().max()],
        'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.flatten().min()],
        'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.flatten().sum()]
    }

    return result

lst = list(imput("Enter the numbers": ))
