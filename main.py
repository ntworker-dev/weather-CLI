import requests
from rich.console import Console
from rich.panel import Panel
import json
from rich import box
import weather_types
from weather_types import weather_type_info

console = Console()

header = Panel(
    "Введи свой город:",
    title="[bold]Weather CLI[/bold]",
    border_style='blue',
    box=box.ROUNDED,
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
weather_data = weather_data['weather'][0]['main']

def display_weather(temperature, temperature_feel, humidity, wind_speed, weather):
    try:

        info = weather_type_info[weather]

        content = f"""
            {info["emoji"]} [bold blue]{info["description"]}[/bold blue]
        
            🌡️[yellow] Температура: [yellow][magenta]{temperature}°C[magenta]
            ℹ️[yellow] Ощущается: [yellow][magenta]{temperature_feel}°C[magenta]
            💧[yellow] Влажность: [yellow][magenta]{humidity}%[magenta]
            💨[yellow] Скорость ветра: [yellow][magenta]{wind_speed} м/c[magenta]
    """

        result = Panel(
            content,
            title=f"Погода в {city} прямо сейчас",
            border_style='cyan',
            box=box.ROUNDED,
        )

        console.print(result)
    except Exception as e:
        print(f'Произошла ошибка {e}')
    finally:
        console.print("[italic blue]Хорошего дня![/italic blue]")

display_weather(temperature_data, temperature_feel_data, humidity_data, wind_speed_data, weather_data)
