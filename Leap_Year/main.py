def leap_year(date):
    if date%400 == 0 or date%4 == 0:
        return "Leap Year!"
    return 'Not a Leap Year...'

if __name__ == "__main__":
    print(leap_year(2024))