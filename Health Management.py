client_list = {1: "Harry", 2: "Karan", 3: "Hammad"}
log_list = {1: "Exercise", 2: "Diet"}


def getdata():
    import datetime
    return datetime.datetime.now()


try:
    print("Enter the client name: ")
    for x, y in client_list.items():
        print("Press", x, "for", y)

    client_name = int(input())

    print("Selected client is: ", client_name)
    print("Press 1 for Log")
    print("Press 2 for Retrieve data")
    print("Enter the mode: ")

    op = input()

    if op == '1':
        print("Enter the number: ")

        for x, y in log_list.items():
            print("Press", x, "for", y)
        data = int(input())
        print("Selected type is: ", data)
        f = open(client_list[client_name] + "_" + log_list[data] + ".txt", "a")

        k = 'y'
        while k != 'n':
            print("Enter", log_list[data])
            mydata = input()
            f.write("[" + str(getdata()) + "]:" + mydata + "\n")
            k = input("Do you want to add something more(y/n): ")
            continue

        f.close()

    elif op == '2':
        print("Enter which data ypu want to retrieve: ")

        for x, y in log_list.items():
            print("Press", x, "for", y)
        return_data = int(input())

        print(client_list[client_name] + "_" + log_list[return_data] + "\'s Report is: ")
        f = open(client_list[client_name] + "_" + log_list[return_data] + ".txt")
        contents = f.readlines()
        for x in contents:
            print(x, end="")

        f.close()

    else:
        print("Invalid Input")

# except Exception as ex:
#     print("Wrong Input")

finally:
    pass
