import requests
from decouple import config
import datetime


nutritionix_appid = config("nutritionix_appid")
nutritionix_apiKey = config("nutritionix_apiKey")
sheety_token = config("sheety_token")

def get_exercise_details(user_input): 
    exercise_params = {
        "query": user_input,
        "gender":"male",
        "weight_kg":83.91,
        "height_cm":193.04,
        "age":33
    }

    headers = {
        "x-app-id": nutritionix_appid,
        "x-app-key": nutritionix_apiKey,
        "Content-Type": "application/json"
    }

    response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=exercise_params, headers=headers)
    response.raise_for_status()
    workout_data = response.json()
    exercises = workout_data["exercises"]
    return exercises

def create_row(exercise, duration, calories):
    today = datetime.date.today()
    formatted_date = today.strftime('%m/%d/%Y')
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    create_row_params = {
        "workout": {
        "date": formatted_date,
        "time": f"{hour}:{minute}:{second}",
        "exercise": exercise,
        "duration": duration,
        "calories": calories
        }
    }

    sheet_headers = {
        "Authorization": f"Bearer {sheety_token}"
    }

    response = requests.post(url="https://api.sheety.co/efbdef51c73a42ea2256a45219e84905/myWorkouts (pythonProject)/workouts", json=create_row_params, headers=sheet_headers)
    return response



user_input = input("Type in your exercise: ")
exercise_details = get_exercise_details(user_input)


for exercise in exercise_details:
    create_row(exercise['user_input'], exercise['duration_min'], exercise['duration_min'])
    





