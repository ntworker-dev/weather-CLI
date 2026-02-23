import requests
from rich.console import Console
from rich.panel import Panel
import json

console = Console()

header = Panel(
    "Введи свой город:",
    title="Weather CLI",
    border_style='blue',
)

console.print(header)

console.print("[bold green]> [/bold green]", end="")
city = input()


url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

temperature_data = round(weather_data['main']['temp'])
temperature_feel_data = round(weather_data['main']['feels_like'])
humidity_data = round(weather_data['main']['humidity'])
wind_speed_data = round(weather_data['wind']['speed'])

def display_weather(temperature, temperature_feel, humidity, wind_speed):

    content = f"""
    [bold yellow]🌡️ Температура: {temperature}°C[/bold yellow]
    [bold yellow]ℹ️ Ощущается: {temperature_feel}°C[/bold yellow]
    [bold yellow]💧 Влажность: {humidity}%[/bold yellow]
    [bold yellow]💨 Скорость ветра: {wind_speed} м/c[/bold yellow]
"""

    result = Panel(
        content,
        title=f"Погода в {city} прямо сейчас",
        border_style='cyan',
    )

    console.print(result)

display_weather(temperature_data, temperature_feel_data, humidity_data, wind_speed_data)

