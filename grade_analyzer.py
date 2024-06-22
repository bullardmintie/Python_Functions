# Task 1 -- Code a function to calculate the average grade

grades = [80, 93, 68, 89, 90, 79]

def calculate_average_grade(grades):
    if not grades:
        return 0
    
    total_sum = sum(grades)
    average_grade = total_sum / len(grades)
    return average_grade

average = calculate_average_grade(grades)
print(f"Your average grade is: {average}")


# Task 2 -- Implement a function to find the highest and lowest grade

def find_highest_lowest_grades(grades):
    if not grades:
        return None, None
    
    highest_grade = grades[0]
    lowest_grade = grades[0]
    
    for grade in grades[1:]:
        if grade > highest_grade:
            highest_grade = grade
        elif grade < lowest_grade:
            lowest_grade = grade
    
    return highest_grade, lowest_grade

highest, lowest = find_highest_lowest_grades(grades)
print(f"Your highest grade is: {highest}")
print(f"Your lowest grade is: {lowest}")


# Task 3 -- Create a feature that categorizes grades into letter grades (A, B, C, etc.)

def categorize_grades(grades):
    letter_grades = []
    
    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')
    
    return letter_grades

letter_grades = categorize_grades(grades)
print("Your grades are as follows:", letter_grades)