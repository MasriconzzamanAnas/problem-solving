height, weight = map(float,input().split())
bmi= weight / (height ** 2)
print(f"BMI: {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25.0:
    print("Normal weight")
elif bmi >= 25.0 and bmi < 30.0:
    print("Overweight")
else:
    print("Obese")