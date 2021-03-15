

octal = "755"
value_letters = [(4,"r"),(2,"w"),(1,"x")]
for num in [int(n) for n in str(octal)]:
    for value, letter in value_letters:
        print(num)
