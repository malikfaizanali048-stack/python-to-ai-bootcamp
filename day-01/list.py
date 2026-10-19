# skills = ["Python", "PyTorch", "Machine Learning", "FastAPI"]

# # print(skills[2])

# skills[2] = "Pandas"
# print(skills[2])

# print(len(skills))

# print("Calculus" not in skills)

# skills.append("Computer Vision")
# print(skills)

# skills.extend(["Docker", "MLflow", "React"])
# print(skills)

# num = [10, 30, 20]
# sorted_num = sorted(num)
# print(sorted_num)

student = {
    "name": "Malik Faizan Ali",
    "age": 22,
    "focus": "Artificial Intelligence",
    "skills": skills
}

for key, value in student.items():
    print(key, ":", value)
    
print(student.get("age"))
print(student.keys())
print(student.values())
