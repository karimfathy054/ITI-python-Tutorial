input_string = input("enter a string:\n")

letters ,digits = 0,0
for c in input_string:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1

print(f"letters: {letters}")
print(f"digits: {digits}")
