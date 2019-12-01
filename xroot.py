
number = float(input("Enter a number to root: "))
exp = int(input("Enter to which power you want to reduce it to: "))
# takes user input

oiList = ["st", "nd", "rd", "th"]
oi = ""
# works out ordinance indicator for answer
if exp > 3:
    oi = oiList[3]
else: oi = oiList[exp - 1]

oddExp = True
negNum = False

if number % 2 == 0:
    oddExp = False

if number <= 0:
    negNum = True

if oddExp and negNum is True:
    print("Even roots of negative numbers aren't real numbers")
    exit()
# checks to see if user asks for the impossible

number = abs(number)
check = 0
checkOut = 0
exped = 0
interval = 1
result = 1

expList = []


def exping():
    result = 1
    expList.clear()
    for i in range(0, exp):
        expList.append(check)

    for numbers in expList:
        result = result * numbers

    return result


computing = True


while computing:
    checking = exping()
    print(result)
    print(check)
    if checking <= number:
        checkOut = check
        check = check + interval

    if checking >= number:
        checkOut = check
        check = check - interval
        interval = interval / 10

    if checking == number or checkOut == check:
        if negNum == False:
            print("The", str(exp) + oi, "root of", str(number), "is:", str(check))
            finish = input("Press enter to finish")
            exit()

        else:
            print("The", str(exp) + oi, "root of -" + str(number), "is: -" + str(check))
            finish = input("Press enter to finish")
            exit()
