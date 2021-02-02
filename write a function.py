def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
                return leap
            return leap
        leap = True
        return leap
    # Write your logic here
    return leap

if __name__ == "__main":
    year = input()
    is_leap(year)