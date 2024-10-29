systolic = int(input('Please enter your systolic: '))
diastolic = int(input('Please enter your diastolic: '))
if systolic <= 120 and diastolic <= 80:
    stage = "Normal"
elif 120 < systolic <= 129 and diastolic <= 80:
    stage = "Elevated"
elif 130 < systolic <= 139 or 80 < diastolic <= 89:
    stage = "High blood pressure (hypertension) stage 1"
elif 140 < systolic <= 180 or 90 < diastolic <= 120:
    stage = "High blood pressure (hypertension) stage 2"
elif systolic > 180 or diastolic > 120:
    stage = "Hypertensive crisis(seek emergency care)"
else:
    stage = "Invalid input entered"
print(f'Your blood pressure stage is {stage}.')

