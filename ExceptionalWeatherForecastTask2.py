#Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

#Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

#Copying Code from ExceptionalWeatherForecastTask1

#Writing Code for ExceptionalWeatherForecastTask2

#Asking the user for input of a Fahrenheit degree and printing
print("Hello! Please enter a temperature in Fahrenheit:")

#Writing try block to catch potential errors during the conversion process
while True:
    try:
        user_degree = int(input())
        break
    except ValueError:
        print("Apologies, value must be a number, please try again")

#Writing function that converts Fahrenheit user entry to Celsius
celsius_degree = (user_degree - 32) * 5/9

print(f"Thank you, your Fahrenheit degree is {user_degree}.")