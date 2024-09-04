def determine_weather(temperature, humidity):
    if temperature >= 30:
        if humidity >= 90:
            return "Hot and Humid"
        else:
            return "Hot"
    else:
        if humidity >= 90:
            return "Cool and Humid"
        else:
            return "Cool"

temperature = float(input("Enter the temperature (in Celsius): "))
humidity = float(input("Enter the humidity (in percentage): "))

weather = determine_weather(temperature, humidity)
print(f"The weather is: {weather}")
