print('FOUND CHAR CODE')

char: str = input("Char: ")

code: int = 0

for i in range(1, 1114111):
    if chr(i) == char:
        code = i
        break

if code != 0:
    print(f"chr({code}) = {char}")
else:
    print("Not found")
