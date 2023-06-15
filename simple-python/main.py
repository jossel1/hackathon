def extract_weather_description(weather_data):
    weather_descriptions = []
    for weather in weather_data["weather"]:
        description = weather["description"]
        score = calculate_weather_score(description)
        if score >= 5:
            weather_descriptions.append(description)
    return weather_descriptions


def calculate_weather_score(description):
    weather_scores = {
        "clear sky": 10,
        "few clouds": 8,
        "scattered clouds": 6,
        "broken clouds": 4,
        "overcast clouds": 2,
        "light rain": 5,
        "moderate rain": 3,
        "heavy rain": 1,
    }

    score = weather_scores.get(description, 0)
    return score

SECRET_TOKEN = "xkdknfcskd-1213-xcsbfcnscb-123"


def connect():
    print(SECRET_TOKEN)
