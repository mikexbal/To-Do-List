import sys

list = []

#Reads the file
try:
    file = open('to_do_list.txt', 'r')
    list = file.readlines()
    file.close()
except:
    pass

#Adds Item to List
if len(sys.argv) >= 3 and sys.argv[1].lower() == 'add':
    list.append(f"{(sys.argv[2])}\n")

#Removes Item from List
if len(sys.argv) >= 3 and sys.argv[1].lower() == 'remove':
    try:
        item_deleted = int(sys.argv[2])
        if item_deleted > 0:
            item_deleted -= 1
            del(list[item_deleted])
        else:
            print("Invalid number")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

#Views List
if len(list) == 0:
    print("Your To Do List is empty!")
else:
    print("\nHere's you To Do list:\n")
    print("______________________\n")
    for x in range(len(list)):
        print(f"{x+1}. {list[x]}", end="")


#Saves the List
file = open('to_do_list.txt', 'w')
list = file.writelines(list)
file.close()
