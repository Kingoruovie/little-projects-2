import requests
import datetime

APP_ID = "b2783b24"
API_KEY = "8e6b5a5457d73b422b5dd8042b6521a3"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/bcdd9bd4849a93ee3ffa8d8df8c6acce/myWorkouts/sheet1"


nutrinox_params = {
    "query": input("Tell me the exercise done today: "),
    "gender": "male",
    "weight_kg": 60.5,
    "height_cm": 157.64,
    "age": 22
}

nutrinox_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

nutrinox_response = requests.post(url=exercise_endpoint, json=nutrinox_params, headers=nutrinox_headers)
nutrinox_output = nutrinox_response.json()

today = datetime.datetime.now()
formatted_time_date = today.strftime("%Y/%m/%d")
formatted_time = today.strftime("%H:%M:%S")

sheet_header = {
    "Content-Type": "application/json",
    "Authorization": "Basic b3J1b3ZpZTphYmNkMTIzNDU2"
}

for exercise in nutrinox_output["exercises"]:
    sheet_input = {
        "sheet1": {
            "date": formatted_time_date,
            "time": formatted_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(sheet_endpoint, json=sheet_input, headers=sheet_header, verify=True)
    print(response.text)