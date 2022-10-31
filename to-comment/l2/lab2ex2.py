def encore():
    def celsius_en_fahrenheit(celsius):
    
        fahrenheit = (celsius * 9/5)+32
        return(fahrenheit)

    celsius_donnee = float(input("Quelle temperatere en Celsius voudrez vous convertir en Fahrenheit?"))
    fahrenheit_temperature = celsius_en_fahrenheit(celsius_donnee)

    print(celsius_donnee, "degree en celsius est", fahrenheit_temperature, "en degree fahrenheit.")
    encore()
encore()
