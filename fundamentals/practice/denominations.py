
denominations = [1, 15, 25]
coins = [5, 2, 2]

def returnChange(change, denominations):
    denominations.reverse()
    coins.reverse()

    result = {}
    current = change
    for pos in range(len(denominations)):
        while denominations[pos] <= current and coins[pos] > 0:
            current -= denominations[pos]
            coins[pos] -= 1

            if denominations[pos] not in result:
                result[denominations[pos]] = 0
            result[denominations[pos]] += 1
    if current != 0:
        print("not possible")
    return result

ans = returnChange(30, denominations)
print(f"result is = {ans}")

