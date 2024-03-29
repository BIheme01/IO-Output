# 1. Create Welcome Message
LINE = "-"*100

print(f"\nWelcome to the student registration portal\n{LINE}")


# 2. Ask the user how many students are registering.
while True:

    total_students = input("How many students would you like to register? ")

    if total_students.isnumeric():    # Check that user has entered a number 
            total_students = int(total_students)
            print(f"\nYou are planning to register {total_students} students.")
            break
    else: 
        print("""\nError! You have entered an invalid character.
Please enter an integer.\n""")
        print (LINE)        


# 3. Create a for loop that runs for the total students being registered.
for i, j in enumerate(range(total_students),1):
        while True:
            student_id = input(f"\nPlease enter the student ID number of Student {i}: ")
            # Only allow Student ID to be printed if it's a 5-digit number
            if len(student_id) == 5 and student_id.isnumeric():
                    with open ("io-output/reg_form.txt", "a+") as file:  #use append
                            file.write(f"{i}. Student ID:{student_id}\n")
                            file.write(LINE +"\n")
                            break                
            else:
                print("Error! The Student ID number must be 5 digits long\n")

print("\n")
print(LINE)
print("\n")


# 4. Create and center the goodbye message
last_message = f"""Thank you for completing the student registration process.\n
                        Have a nice day!"""
goodbye_message = last_message.center(110)
print(goodbye_message)
print("\n")
print(LINE)