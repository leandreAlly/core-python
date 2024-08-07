def main():
    # Write your code here!
    # Be careful, all your code must be indented like this comment !
    numbers = input("Enter the list of numbers: ")
    numbers = numbers.split(",")

    print("List of numbers: ", numbers)

    total_sum = 0
    for number in numbers:
        total_sum += int(number)
    print("Sum of numbers : ", total_sum)
   
    average = total_sum / len(numbers)
    print("Average of numbers : ", average)

    up_average_number = 0
    for number in numbers:
        if int(number) > average:
            up_average_number += 1
    print("Number of numbers greater than the average : ", up_average_number)

    even_numbers = 0
    i = 0
    while i < len(numbers):
        if int(numbers[i]) % 2 == 0:
            even_numbers += 1
        i += 1
    print("Number of even numbers :", even_numbers)

#NOTE: first I did everthing and i came to look for solution after and improve my code

# Do not modify the code below
if __name__ == "__main__":
    main()