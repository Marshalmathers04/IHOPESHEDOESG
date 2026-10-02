bill = float(input("Bill: "))
billTip = float(input("Tip: "))
while billTip<0 or billTip>100:
    billTip = float(input("Tip: "))
total = "{:.2f}".format(bill+(bill*(billTip/100)))
print("Your total is ",total)