# Temperature Check Program

# Input temperature in Celsius
temp = float(input("Enter temperature in Celsius: "))

# Conditions
if temp < 20:
    print("It's Cold ")
elif 20 <= temp <= 30:
    print("It's Normal ")
else:
    print("It's Hot ")
        temp_fahrenheit = (temp_celsius * 9/5) + 32

    print(f"\nTemperature in Celsius: {temp_celsius}°C")
print(f"Temperature in Fahrenheit: {temp_fahrenheit}°F")
print("Condition:", condition)
