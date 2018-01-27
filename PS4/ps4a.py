# Problem Set 4A
# Name: Min Joon So
# Collaborators:
# Time Spent: 10'

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    return_list = []
    if len(sequence) == 1:
        return [sequence]
    rec = get_permutations(sequence[1:])
    for x in rec:
        for y in range(len(x)+1):
            temp = x
            temp = temp[:y] + sequence[0] + temp[y:]
            return_list += [temp]
    return return_list
            

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    print(get_permutations('abc'))
    print(get_permutations('cat'))
    print(get_permutations('dog'))
