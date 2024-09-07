def password(first_stone):
    second_stone = []
    for i in range(1,first_stone):
        for k in range(i+1,first_stone):
            if first_stone%(i+k) == 0:
                code = str(i) + str(k)
                second_stone.append(code)
    return second_stone

first_stone = int(input("Число из первой вставки :"))
while  first_stone < 3 or first_stone  > 20:
    first_stone = int(input("Посмотри ВНИМАТЕЛЬНО на число, которое выпало на первом камне :"))
sec_code=password(first_stone)
code_in_line=''
for i in sec_code:
    code_in_line+=str(i)
print("Нужный пароль"," - ", code_in_line)
