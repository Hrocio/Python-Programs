def element_of(itera, lst):
    '''A list can have only 1 item, or even 0 items.
    If the item is not in the list, then check the item.
    If item is in the list, then repeat the process.
    '''
    retrn = False
    # Iterate through the items in the list.
    for i in lst:
        # Comparing types to check if an element is a list.
        if type(i) == type([]):
            retrn = element_of(itera, i)

        else:
            if i == itera:
                retrn = True
                return retrn
    return retrn


def filter_by_depth(depth, lst):
    '''This Function takes two arguments that represent depth and a nested list.
    It removes all sub-lists that are more than depth deep.
    '''
    answer = []  # Initialize answer list.

    if depth == 0:  # Remove the list when depth = 0.
        return answer
    # Iterate through all the elements in the list.
    for i in lst:
        # Comparing types. I could have used if isinstance(type(i), ([]))
        if type(i) == type([]):
            # If this is deep enough, delete the list.
            repeat_var = filter_by_depth(depth - 1, i)
            if len(repeat_var) > 0:
                answer = answer + [repeat_var]
        # If it is not deep enough, repeat the process.
        else:
            answer = answer + [i]
    return answer


def main():
    '''The main function run the lists. The previous functions
    have recursive definitions. Note that in b, although 7 is not equal [7],
    the function nows that 7 is a list of 1.
    '''
    print("Run")  # Run this lists.
    a = element_of(5, [1, 2, 3, 4, 5, 6, 7])
    b = element_of(7, [1, 2, [3, 4, [5, 6]], [7]])
    c = element_of(77, [1, 2, [3, 4, [5, 6]], [7]])
    d = filter_by_depth(0, [1, 2, 3])
    e = filter_by_depth(1, [1, 2, 3])
    f = filter_by_depth(5, [1, 2, 3])
    g = filter_by_depth(2, [1, 2, [3, 4, [5, 6]], [7]])
    print("element_of(5, [1, 2, 3, 4, 5, 6, 7])", '\n', a)
    print("element_of(7, [1,2,[3,4,[5,6]],[7]])", '\n', b)
    print("element_of(77, [1, 2, [3, 4, [5, 6]], [7]])", '\n', c)
    print("filter_by_depth(0, [1, 2, 3])", '\n', d)
    print("filter_by_depth(1, [1, 2, 3])", '\n', e)
    print("filter_by_depth(5, [1, 2, 3])", '\n', f)
    print("filter_by_depth(2, [1, 2, [3, 4, [5, 6]], [7]])", '\n', g)

if __name__ == '__main__':  # Main.
        main()
