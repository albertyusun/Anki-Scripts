def compareDate(yearA, monthA, dayA, yearB, monthB, dayB):
    if yearA > yearB:
        return 1
    elif yearA == yearB:
        if monthA > monthB:
            return 1
        elif monthA == monthB:
            if dayA > dayB:
                return 1
            elif dayA == dayB:
                return 0
    return -1

if __name__ == '__main__':
    print(compareDate(2019, 1, 1, 2010, 11, 1))
