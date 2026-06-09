n = input("enter a digit: ")

if n.isdigit():
    ans = int(n) + int(n + n) + int(n + n + n)
    print(ans)
else:
    print("please enter a valid digit")
