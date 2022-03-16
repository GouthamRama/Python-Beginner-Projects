# Weighted Exam Score Average

# Completed Exams
number_of_exams = int(input("Number of exams: "))

# Exam Credits
total_credits = int(input("How many credits do these exams cover: "))

# Begin with average of 0 and then add up percentages from each exam
average = 0
for exam in range(number_of_exams):
    score = int(input("Exam score: "))
    exam_credits = int(input("How many credits does this exam cover: "))
    average = average + score * exam_credits/total_credits
print("Your average is", average)
