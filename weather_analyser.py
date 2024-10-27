import csv

class WeatherData:
    def __init__(self, temperatures, file_path="weather_data.csv"):
        self.temperatures = temperatures
        self.file_path = file_path

    def average_temperature(self):
        return sum(self.temperatures) / len(self.temperatures)

    def highest_temperature(self):
        return max(self.temperatures)

    def lowest_temperature(self):
        return min(self.temperatures)

    def save_csv(self):
        with open(self.file_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Day", "Temperature"])
            for i, temp in enumerate(self.temperatures, start=1):
                writer.writerow([f"Day {i}", temp])

    def load_csv(self):
        temperatures = []
        try:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    temperatures.append(float(row[1]))
        except FileNotFoundError:
            print("No weather data found.")
            pass
        return WeatherData(temperatures)

weather = WeatherData([70, 75, 68, 72, 80, 65, 78])
print(f"Average Temp: {weather.average_temperature()}")
print(f"Highest Temp: {weather.highest_temperature()}")
print(f"Lowest Temp: {weather.lowest_temperature()}")
weather.save_csv()
loaded_weather = weather.load_csv()
print(f"Loaded Average Temp: {loaded_weather.average_temperature()}")
