import requests
import json
import os.path
url = "https://saral.navgurukul.org/api/courses"
def saral_data(link):
    url_data = requests.get(url)
    response = url_data.json()
    return response
saral_data(url)
all_course = saral_data(url)
def displayCourse(all_course):
    i =0
    while i<len(all_course['availableCourses']):
        saral_course = all_course['availableCourses'][i]['name']
        saral_list = all_course['availableCourses'][i]['id']
        print((i+1), saral_course,saral_list)
        i+=1
    return saral_list
displayCourse(all_course)
course_list = all_course['availableCourses']
def exercises(user_id):
    exercise_url = url+"/"+str(user_id)+"/exercises"
    exercise_data = requests.get(exercise_url)
    exercise_response = exercise_data.json()
    return (exercise_response)
user_exercises = int(input("enter your id: "))
exercises_name = exercises(user_exercises)
print (exercises_name)
def data():
    exercise_url = url+"/"+str(user_id)+"/exercises"
    exercise_data = requests.get(exercise_url)
    exercise_response = exercise_data.json()
    return (exercise_response)
user_exercises = int(input("enter your id: "))
exercises_name = exercises(user_exercises)
solditems = requests.get("https://saral.navgurukul.org/api/courses/"+str(user_exercises)+"/exercises") # (your url)
data = solditems.json()
file = input("Enter file name: ")
with open(file, 'w+') as f:
    # ifCaching=True
    # i =0
    # while i<len(all_course['availableCourses']):
    json.dump(data, f)    
if os.path.isfile('k.json'):
    print ("File exist")
else:
    print ("File not exist")

