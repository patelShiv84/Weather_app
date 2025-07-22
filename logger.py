from datetime import datetime

def save_log(weather_data):
    with open("weather_logs.txt", "a") as log_file:
        log_file.write(f"\n--- Weather Data for ---\n")
        log_file.write(f"location    : {weather_data['location']}\n")
        log_file.write(f"Date & Time : {datetime.now()}\n")
        log_file.write(f"temperature : {weather_data['temperature']}°C\n")
        log_file.write(f"Weather Condition   : {weather_data['condition'].title()}\n")
        log_file.write(f"----------------------------------------------------------\n")
           
    print("Data Enter successfully")
        
        
        