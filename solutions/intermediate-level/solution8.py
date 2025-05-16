def main():
    cmd = input("Enter command: ").split()
    if not cmd:
        print("No command entered.")
        return
    if cmd[0] == "add" and len(cmd) == 3:
        try:
            result = int(cmd[1]) + int(cmd[2])
            print(result)
        except ValueError:
            print("Invalid numbers.")
    elif cmd[0] == "sub" and len(cmd) == 3:
        try:
            result = int(cmd[1]) - int(cmd[2])
            print(result)
        except ValueError:
            print("Invalid numbers.")
    elif cmd[0] == "mul" and len(cmd) == 3:
        try:
            result = int(cmd[1]) * int(cmd[2])
            print(result)
        except ValueError:
            print("Invalid numbers.")
    elif cmd[0] == "div" and len(cmd) == 3:
        try:
            result = int(cmd[1]) // int(cmd[2])
            print(result)
        except ValueError:
            print("Invalid numbers.")
        except ZeroDivisionError:
            print("Division by zero.")
    else:
        print("Unknown command or wrong number of arguments.")

if __name__ == "__main__":
    main()
