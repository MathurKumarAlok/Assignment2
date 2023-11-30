lenght_of_list = int(input("enter length of list: "))
input_list = []
for i in range(lenght_of_list):
    current_tup = input("Enter the tup valus space seprated")
    current_tup = current_tup.split()
    current_tup = tuple(map(int,current_tup))
    input_list.append(current_tup)
print(input_list)
input_list.sort(key = lambda r:r[1])
print(input_list)
