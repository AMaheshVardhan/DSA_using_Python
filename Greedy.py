stock = [5, 10, 20, 50]
userinput = int(input()) #85 = 50+20+10+5
while userinput != 0:
    if userinput >= max(stock):
        print(max(stock), end=" ")
        userinput = userinput - max(stock)
    else:
        stock = stock[:stock.index(max(stock))]  
