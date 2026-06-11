print("===== STUDENT PROFILE SYSTEM =====")
print("Please enter your details below:\n")

raw_name = input("Full Name: ")
raw_age = input("Age: ")
raw_gpa = input("GPA: ")
raw_courses = input("Courses (comma-separated): ")

name = raw_name
age = int(raw_age)
gpa = float(raw_gpa)
courses = [c.strip() for c in raw_courses.split(",")]
num_courses = len(courses)

is_adult = age >= 18
deans_list = gpa >= 3.5

student_profile = {
    "name": name,
    "age": age,
    "gpa": gpa,
    "courses": courses,
    "num_courses": num_courses
}

print("\n--- Type Conversion Demo ---")
print(f"raw_age:  '{raw_age}'  → type: {type(raw_age)._name}  →  {age}  type: {type(age).name_}")
print(f"raw_gpa:  '{raw_gpa}'  → type: {type(raw_gpa)._name}  →  {gpa}  type: {type(gpa).name_}")
print(f"raw_courses: '{raw_courses}'")
print(f"  → type: {type(raw_courses)._name}  →  {courses}  type: {type(courses).name_}")

print("\n===== STUDENT PROFILE =====")
print(f"{'Name:':<13} {student_profile['name']}")
print(f"{'Age:':<13} {student_profile['age']} ({'Adult' if is_adult else 'Minor'})")
print(f"{'GPA:':<13} {student_profile['gpa']:.2f}")
print(f"{'Courses:':<13} {student_profile['courses']}")
print(f"{'# Courses:':<13} {student_profile['num_courses']}")
print(f"{'Deans List:':<13} {'Yes' if deans_list else 'No'}")
print("===========================")

print("\n--- Data Types Used ---")
print(f"str:   {type(name)._name_}  → {name}")
print(f"int:   {type(age)._name_}   → {age}")
print(f"float: {type(gpa)._name_} → {gpa}")
print(f"bool:  {type(is_adult)._name_}  → is_adult = {is_adult}, deans_list = {deans_list}")
print(f"list:  {type(courses)._name_}  → {courses}")
print(f"dict:  {type(student_profile)._name_}   → keys: {list(student_profile.keys())}")