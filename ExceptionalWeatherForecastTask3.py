#Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

#Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

#Copying Code from ExceptionalWeatherForecastTask2

#Writing Code for ExceptionalWeatherForecastTask3

#Asking the user for input of a Fahrenheit degree and printing
print("Hello! Please enter a temperature in Fahrenheit:")

#Writing try block to catch potential errors during the conversion process with while loop for user re-entry on error
while True:
    try:
        user_degree = int(input())

#Writing function that converts Fahrenheit user entry to Celsius
        celsius_degree = (user_degree - 32) * 5/9
    except ValueError:
        print("Apologies, value must be a number, please try again")
#Writing else block that prints the converted temperature in a user-friendly format with break to end user re-entry loop
    else:
        print(f"{user_degree} degrees Fahrenheit is {celsius_degree:.2f} degrees Celsius.")
        break