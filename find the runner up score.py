def runnerup(arr):
    array = list(arr)
    max_value = max(array)
    
    while max_value == max(array):
        array.remove(max(array))
    
    print(max(array))
    
    
 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runnerup(arr)