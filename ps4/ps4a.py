# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

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

    if len(sequence) == 1:
        return sequence
    else:
        # get sequence without the first letter 
        shorten = ''
        for letter in sequence[1:]:
            shorten += letter
            
        new_list = []
        for i in get_permutations(shorten):
            new_list.append(sequence[0]+i)
            new_list.append(i+sequence[0])
            if len(i)>1:
                for j in range(len(i)-1):
                    new_list.append(i[:(j+1)]+sequence[0]+i[(j+1):])
        return new_list
    
        
            
if __name__ == '__main__':
#    #EXAMPLE 1
    # example_input = 'abc'
    # print('Input:', example_input)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input))
    
#    #EXAMPLE 2
    # example_input = 'hvl'
    # print('Input:', example_input)
    # print('Expected Output:', ['hvl', 'hlv', 'vhl', 'vlh', 'lhv', 'lvh'])
    # print('Actual Output:', get_permutations(example_input))

# #    #EXAMPLE 3
    example_input = 'obw'
    print('Input:', example_input)
    print('Expected Output:', ['obw', 'bow', 'bwo', 'owb', 'wob', 'wbo'])
    print('Actual Output:', get_permutations(example_input))
  
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)



