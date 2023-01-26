#From hacker rank day of the programmer problem
def dayOfProgrammer(year):
    a = "12.09." + str(year)
    b = "13.09." + str(year)

    if year < 1918:
        if year % 4 == 0:
            return a
        else:
            return b
    elif year == 1918:
        return "26.09.1918"
    else:
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            return a
        else:
            return b
