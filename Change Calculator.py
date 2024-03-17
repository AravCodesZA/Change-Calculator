def calculateChange(totalChange):
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]

    for denomination in denominations:
        count = totalChange // denomination
        totalChange = totalChange % denomination
        print('R' + str(denomination) + 's: ' + str(count))


while True:
    amount = input("Enter the total change amount: ")
    if amount == "0":
        break
    else:
        calculateChange(int(amount))

    continuePrompt = input("Would you like to continue? (Y/N): ")
    if continuePrompt.lower() != 'y':
        break
