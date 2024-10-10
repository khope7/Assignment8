#Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

#Copying Code from ExceptionalWeatherForecastTask3

#Writing Code for ExceptionalWeatherForecastTask4

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
#Writing conditional that prints only if user has made it to the end of the loop with a correct user Entry, printing thank you message regardless of whether an exception was caught or not
        ValueError = False
        break
    finally:
        if ValueError == False:
            print("Thank you user for using the application!")