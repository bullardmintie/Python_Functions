# Task 1 -- Develop a function to log different fitness activities and their duration.
# For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and
# duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds
# to 20 minutes, and Biking corresponds to 15 minutes

exercise_activities = ("biking", "hoola-hoop", "dancing", "walking", "swimming")
duration = (20, 10, 50, 30, 40)

duration_activities = (exercise_activities, duration)


# Task 2 -- Write a simple function that estimates calories burned based on the activity
# and duration. For instance, Total calories burned = Duration (in minutes)*3.5

def calculate_calories(activity_durations, calorie_per_minute):
    return tuple(duration * calorie_per_minute for duration in activity_durations)

single_calorie = 3.5
total_calories_burned = calculate_calories(duration, single_calorie)

print(total_calories_burned)


# Task 3 -- Create a summary function that provides a report of all activities and total
# calories burned for the day

def summary_report(activities, durations, calorie_per_minute):
    total_calories = calculate_calories(durations, calorie_per_minute)
    report = "Activity Summary Report:\n"
    report += "-" * 30 + "\n"
    for activity, duration, calories in zip(activities, durations, total_calories):
        report += f"Activity: {activity}, Duration: {duration} minutes, Calories Burned: {calories:.1f}\n"
    report += "-" * 30 + "\n"
    report += f"Total Calories Burned: {sum(total_calories):.1f}\n"
    return report

print(summary_report(exercise_activities, duration, single_calorie))