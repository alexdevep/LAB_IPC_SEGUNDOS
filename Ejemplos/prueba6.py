# Write a function that, when passed a list and a target sum, returns, efficiently with respect to time used, two distinct zero-based indices of any two of the numbers, whose sum is equal to the target sum. If there are no two numbers, the function should return None.

# For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the following pairs of indices:

# 0 and 3 (or 3 and 0) as 3 + 7 = 10
# 1 and 5 (or 5 and 1) as 1 + 9 = 10
# 2 and 4 (or 4 and 2) as 5 + 5 = 10

def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    taken = {}
    for i, num in enumerate(numbers):
        diff = target_sum - num
        if diff in taken:
            #print(taken)
            return i, taken[diff]
        taken[num] = i
    return None
       
if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))


# Implement a group_by_owners function that:

# Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.
# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

def group_by_owners(files):
    
    result = {}
    for file, owner in files.items():
        result[owner] = result.get(owner, []) + [file]
    return result

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))