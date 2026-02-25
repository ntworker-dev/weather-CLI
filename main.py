import requests
from rich.console import Console
from rich.panel import Panel
from rich import box
from weather_types import weather_type_info
from requests.exceptions import ConnectionError, ConnectTimeout, HTTPError

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

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = {}

try:
    weather_data = requests.get(url).json()
except requests.exceptions.ConnectionError:
    print('Нет соединения!')
except requests.exceptions.ConnectTimeout:
    print("Вы отключены от сервера!")
except requests.exceptions.HTTPError:
    print("Сетевая ошибка!")

def display_weather(weather: dict[str, dict]) -> None:
    temperature = ""
    temperature_feel = ""
    humidity = ""
    wind_speed = ""

    try:

        temperature = round(weather['main']['temp'])
        temperature_feel = round(weather['main']['feels_like'])
        humidity = round(weather['main']['humidity'])
        wind_speed = round(weather['wind']['speed'])

        info = weather_type_info[weather['weather'][0]['main']]

    except KeyError:
        print(f'Ошибка данных')
    except Exception as e:
        print(f"Произошла ошибка {e}")

    info = weather_type_info[weather['weather'][0]['main']]

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
    console.print("[italic blue]Хорошего дня![/italic blue]")


display_weather(weather_data)
