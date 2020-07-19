def print_formatted(number):
    for i in range(1,int(number+1)):
        binn = bin(i)
        n = int(len(binn[2:]))
        octn = oct(i)
        hexn = hex(i)
        print(i,octn[1:],hexn[2:].upper(),binn[2:])
        # format the output later

n = int(raw_input())
print_formatted(n)
