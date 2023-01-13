def main():
    with open('CaesarCipher/input.txt') as f:
        N = int(f.read())
        result = get_decreasing(N)
        print(result)

def get_decreasing(N:int):
    """Returns the number of integers which have decreasing digits"""
    count = 0
    for i in range(N+1):
        if check_is_decreasing(i):
            count += 1
    
    return count

def check_is_decreasing(n:int):
    "Check if a no. have decreasing digits or not."
    arr = list(map(lambda x: int(x), list(str(n))))
    is_satisfied = True

    for i, ele in enumerate(arr):
        if i == len(arr) - 1:
            break

        if ele < arr[i+1]:
            is_satisfied = False
            break
    
    return is_satisfied

if __name__ == '__main__':
    main()
