def collatz (num):
    input_check = num % 2
    if input_check == 0:
        num = int(num / 2)
        print (str(num))
        return num
    elif input_check == 1:
        num = int(num*3+1)
        print (str(num))
        return num

while True:
    try:
        user_input = int(input("Please put in a number: "))
        break
    except ValueError:
        print ("This is not a number. Please try again: ")
    
user_input = collatz (user_input)
while user_input != 1:
    user_input = collatz (user_input)
print ("You've reached '1'.")
