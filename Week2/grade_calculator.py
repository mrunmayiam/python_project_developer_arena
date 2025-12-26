# function to get student name from user
def get_student_name():
    while True:   # do-while simulation
        name = input("Enter student name: ").strip()
        if name.isalpha():
            return name
        else:
            print("❌ Invalid name. Please use alphabets only.")


# function to get student marks from user
def get_marks():
    while True:   # do-while simulation
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks   # ✅ IMPORTANT
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid integer.")

# function to calculate student grades based on marks of student and provide an encouraging message
def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! 🙂"
    elif marks >= 60:
        return "D", "You passed. Needs improvement."
    else:
        return "F", "Failed. Better luck next time."


# function to display name, marks and message
def display_result(name, marks, grade, message):
    print("\n📊 RESULT FOR", name.upper() + ":")
    for line in [
        f"Marks: {marks}/100",
        f"Grade: {grade}",
        f"Message: {message}"
    ]:
        print(line)

# main function 
def main():
    name = get_student_name()
    marks = get_marks()             
    grade, message = calculate_grade(marks)
    display_result(name, marks, grade, message)


# Calling main function
main()

