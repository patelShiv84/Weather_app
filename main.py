from weather_api import get_weather_data
from logger import save_log


def main_menu():
    while True:
        print("\n==== Welcome to Weather App ====")
        print("1. Check Weather")
        print("2. Exit")



        choice = input("Enter your choice (1-2): ")
        
        if choice == '1': 
            while True:    
                try:    
                    city = input("Enter city Name: ")
                    if city:
                        data = get_weather_data(city)
                        weather_data = {
                            'location': data['location'],
                            'temperature' : data['temperature'],
                            'condition' :data['condition']
                        }
                        
                    print(weather_data)
                    save_log(weather_data)
                    break    
                except Exception as e:
                    print(f"Error: {type(e).__name__} - {e}: Please re-enter city name")
                    
            continue    
          


        elif choice == '2':
            print("Thank you for using weather app Goodbye!")
            break
        
        else:
            print("Invalid choice Please select from 1 or 2")
    


if __name__ == "__main__":
    main_menu()











# while True:
    
#     city = input("Enter City name: ")
#     if city:
#         weather_data = get_weather_data(city)
#         if weather_data:
#                 print(f"City Name: {weather_data['Location']}")
#                 print(f"Date & Time : {datetime.now()}")
#                 print(f"Temperature: {weather_data['temperature']}°C")
#                 print(f"Weather Condition: {weather_data['condition']}")
        

