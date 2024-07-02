# main.py
# Добавь своё
print("1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius\n3.Exit")
choice = int(input("Enter your choice:"))
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = 5/9 * (fahrenheit - 32)
    print(f"{fahrenheit} Fahrenheit = {celsius} Celsius")
elif choice == 3:
    print("Exiting")
else:
    print("Invalid choice!")
