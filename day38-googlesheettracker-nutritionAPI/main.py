import requests
from datetime import datetime

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("What type of exercises did you do? ")

SHEETY_ENDPOINT = "https://api.sheety.co/<username>/workoutTracking/workouts"


GENDER = "female"
WEIGHT_KG = 42
HEIGHT_CM = 165
AGE = 21

APP_ID = "APP_ID"
API_KEY = "API_KEY"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

response = requests.post(url=EXERCISE_ENDPOINT, json=user_params, headers=headers)
result = response.json()
print(result)

exercise = result["exercises"][0]
print(exercise)


today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": "Bearer thisissecret"
}

for exercise in result["exercises"]:
    workout_config = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_post_response = requests.post(url=SHEETY_ENDPOINT, json=workout_config, headers=bearer_headers)
    print(sheety_post_response.text)

