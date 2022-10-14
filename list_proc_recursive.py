def iterative_find_elem(l: list, a: int) -> int:
    for i in l:
        if i == a: 
            return f"{a} is in the list"
    return f"{a} is not in the list"

def recursive_find_elem(l:list, a: int) -> int:
    if len(l) == 0:
        return f"{a} is not in the list"
    cur_elem = l[0]
    if cur_elem == a:
        return f"{a} is in the list"
    else:
        return recursive_find_elem(l[1:], a)

if __name__ == '__main__':
    l = [1,2,3,4,5]
    print(iterative_find_elem(l,3))
    print(iterative_find_elem(l,6))
    print(recursive_find_elem(l,3))
    print(recursive_find_elem(l,6))