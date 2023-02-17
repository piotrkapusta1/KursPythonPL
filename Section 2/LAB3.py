options = ['load data', 'export data', 'analyze & predict']
choice = 'x'



def DisplayOptions(options) -> str :
    print("1", options[0])
    print("2", options[1])
    print("3", options[2])
    x = input("Select option above or press enter to exit:")
    return x

while choice:
    choice = DisplayOptions(options)

    if choice:
        try:
            choice_num = int(choice) - 1
            if 0 <= choice_num < len(options):
                print(options[choice_num])
            else:
                print("Error wrong number")

        except:
            print("Input number")

    else:
        print("End of program")



