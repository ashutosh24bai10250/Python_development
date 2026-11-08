num = int(input("Enter the Number "))

if num < 0 :
    print("Negative ")

elif num == 0 :
    print("Zero")

else :
    print("Positive")

age = int(input("Enter your age "))
if age < 18 :
    print("You are not eligible to vote .")
else :
    print("You are  eligible to vote .")


grades = int(input("Enter your marks "))


if grades >= 90:
    print("Grade A")

elif grades >= 80:
    print("Grade B")

elif grades >= 70:
    print("Grade C")

elif grades >= 60:
    print("Grade D")

else:
    print("Grade F")