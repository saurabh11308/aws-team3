total = 0
count = 0
while True:
    num = raw_input("Enter the number")
    if num == "done":
        break
    total += float(num)
    count += 1
avg = total/count
print("The average of the numbers is ",avg)
