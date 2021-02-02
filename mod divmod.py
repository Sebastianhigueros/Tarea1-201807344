# Enter your code here. Read input from STDIN. Print output to STDOUT
def division(a,b):
    print(a//b)
    print(a%b)
    print(divmod(a,b))
    
    
if __name__ == '__main__':
        a = int(input())
        b = int(input())
        division(a,b)