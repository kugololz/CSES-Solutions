string = input()
result = []
current_substring = string[0]
maximo = 0

for char in string[1:]:
    if char == current_substring[-1]:
        current_substring += char
    else:
        result.append(current_substring)
        current_substring = char

result.append(current_substring)  

for dato in result:
    dato = [*dato]
    if maximo < len(dato):
        maximo = len(dato)

print(maximo)