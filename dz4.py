my_list = [12, 100, 112, 0, 32, 111]
for now in my_list:
    if now > 100:
        print(now)

#################################

my_list = [12, 100, 112, 0, 32, 111]
my_result = []
for now in my_list:
    if now > 100:
        my_result.append(now)
print(my_result)

#################################

my_list = [12]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

#################################

my_string = '0123456789'
answer = []
for i in my_string:
    for j in my_string:
        answer.append(int(i + j))
print(answer)
