import random


def gen_list():
    generated_list = list()
    for x in range(0, 10):
        random_number = random.randint(-50, 50)
        generated_list.append(random_number)
    return generated_list


data = " "

f = open("my_file.txt", "wt+")
for x in range(0, 5):
    my_list = gen_list()
    data = data.join(map(str, my_list))
    f.write(data + "\n")
    data = " "
f.close()

f = open("my_file.txt", "rt+")
data = f.readlines()
result = list()
for line in data:
    numbers = line.split(" ")
    for number in numbers:
        num = int(number)
        if num == 0:
            num = 1
        elif num < 0:
            num = -num
        else:
            num //= 2
        result.append(num)
print("Сума = ", sum(result))
f.close()
