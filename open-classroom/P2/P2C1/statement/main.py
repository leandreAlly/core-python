def main():
    # Write your code here!
    # Be careful, all your code must be indented like this comment !
    left_number = input("Enter the first number: ")
    right_number = input("Enter the second number: ")

    operation = input("Enter the operation: ")
    result = 0
    
    if not left_number.isnumeric() or not right_number.isnumeric():
        print("Error: both numbers must be integers")
    else:
        left_number = int(left_number)
        right_number = int(right_number)
    
    match operation:
        case "+":
            result = left_number + right_number
        case "-":
            result = left_number - right_number
        case "*":
            result = left_number * right_number
        case "/":
            if right_number == 0:
                print("Error: division by zero is not allowed.")
            else:
                result = left_number / right_number
        case other:
            print("Error: the operation symbol must be '+', '-', '*', or '/'.")
    print(result)
       

    

# Do not modify the code below
if __name__ == "__main__":
    main()