import json

one = {"first_name": "Arin",
       "last_name": "Hanson",
       "gender": "male",
       "student_number": 1,
       "grade": 10,
       "email": "arin.hanson22@gmail.com",
       "marks": [45, 65, 74, 34, 76, 87],
       "comments": "xd"}

two = {"first_name": "Dan",
       "last_name": "Avidan",
       "gender": "male",
       "student_number": 2,
       "grade": 11,
       "email": "dan.avidan21@gmail.com",
       "marks": [76, 87, 67, 87, 67],
       "comments": "21"}

three = {"first_name": "Suzie",
         "last_name": "Anson",
         "gender": "female",
         "student_number": 3,
         "grade": 12,
         "email": "suzie.anson20@gmail.com",
         "marks": [76, 85, 46, 96, 56],
         "comments": "owo"}

four = {"first_name": "Ross",
        "last_name": "Rubber",
        "gender": "male",
        "student_number": 4,
        "grade": 9,
        "email": "ross.rubber23@gmail.com",
        "marks": [97, 67, 87, 98, 94],
        "comments": "terrible"} 

listing = [one, two, three, four]

with open("studentlist.json", "w") as f:
    json.dump(listing, f)

