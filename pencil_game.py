pencil = "|"
num_of_pencils = int(input("How many pencils would you like to use:"))
user_name = str(input('Who will be the first (John, Jack):'))
pencil_list = num_of_pencils * pencil
print(pencil_list)

def swap_name(user_name):
    if user_name == "Jack":
        return "John"
    else:
        return "Jack"

while num_of_pencils > 0:
    print( user_name + "'s turn:" )
    user_name = swap_name(user_name)

    number_new = int(input())
    num_of_pencils = num_of_pencils - number_new

    if num_of_pencils > 0:
        print(num_of_pencils * "|")
       
    else:
        break







