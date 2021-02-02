# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def degree(ab,bc):
    radian = math.atan2(ab,bc)
    degree = round(math.degrees(radian))
    print(str(degree)+"°")

if __name__ == '__main__':
    ab = float(input())
    bc = float(input())
    degree(ab,bc)