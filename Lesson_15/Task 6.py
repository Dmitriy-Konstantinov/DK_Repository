# Напишіть рекурсивну функцію, яка підраховує глибину вкладеності списків

def depth(lst):
    if isinstance(lst, list):
        if not lst:
            return 0
        else:
            depths = [depth(item) for item in lst]
            return max(depths) + 1
    else:
        return 0


print(depth([1, [2, [3, [4, [5]]]]]))
