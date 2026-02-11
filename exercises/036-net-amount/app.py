# EJERCICIO 36 - net amount
# Your code here
def net_amount(amount):
    balance = 0
    money = amount.split()
    for i in range(0, len(money), 2):
        operation = money[i]
        value = int(money[i + 1])
        if operation == "D":
            balance += value
        elif operation == "W":
            balance -= value
    return balance
print(net_amount("D 300 D 300 W 200 D 100"))
