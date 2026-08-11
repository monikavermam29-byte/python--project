HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    file.seek(0)
    lines = file.readlines()
    if len(lines) == 0:
        print("No history file found!")
    else:
        for line in reversed(lines):
            print(line.strip())
        file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('history file has been cleared.')

def save_to_history(equation,result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + '\n')
    file.close()

def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print('Invalid input. use format: number operation number (e.g 8+8)' )
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2

    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator. USE ONLY + - * /.")
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)
def  save_to_history(user_input,result):
     file = open(HISTORY_FILE, 'a')
     file.write(user_input + "=" + str(result) + '\n')
     file.close()



def main():
        print('---SIMPLE CALCULATOR (type history, clear or exit) ')
        while True:
            user_input = input("Enter calculator (+ - * /)or command(history or exit): ")
            if user_input == "exit":
                print("GOOD BYY")
                break
            elif user_input == "history":
                show_history()
            elif user_input == "clear":
                clear_history()
            else:
                calculate(user_input)

main()