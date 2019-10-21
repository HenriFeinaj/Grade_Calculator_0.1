#================================================================================================================
#                                  BASIC_STUDENT_GRADE_CALCULATOR V2
#================================================================================================================

#================================================================================================================
# FUNCTION THAT GETS INPUT INFO FROM THE USER. IT TAKES THE COURSE_CHOICES AND THEN APPENDS THEM TO A DICTIONARY.
#================================================================================================================

def get_users():
    students = []
    all_students = {}
    print("Welcome to Henry's Student_Grade Calculator!")
    print("________________AVAILABLE COURSES__________________")
    print("________________1.MATHEMATICS______________________")
    print("________________2.COMPUTING________________________")
    print("________________3.PSYCHOLOGY_______________________")
    print("________________4.ENGLISH__________________________")
    print(" ")
    
    available_choices = ["mathematics", "computing", "psychology", "english"]
    
    total = 0
    while True:
        if total == 10:   #TOTAL STANDS FOR NUMBER OF STUDENTS.
            break

        student_name = input("Please enter your name: ").lower()
        if student_name in students:
            print(f"{student_name} is already taken")
            continue

        course_choice_1 = input("Enter the name of your first course: ").lower()
        if course_choice_1 not in available_choices:
            print(f"{course_choice_1} isn't a valid course")
            continue

        course_choice_2 = input("Enter the name of your second course: ").lower()
        if course_choice_2 not in available_choices:
            print(f"{course_choice_2} isn't a valid course")
            continue

        if course_choice_1 == course_choice_2:
            print("You can't have the same course twice!")
            continue

        students.append(student_name)

        all_students[student_name] = {course_choice_1: {}, course_choice_2: {}}

        total += 1

    return all_students

#================================================================================================================
# FUNCTION THAT ADD GRADES TO EACH STUDENT'S DICTIONARY.'
#================================================================================================================
def add_grades():
    exam_info = get_users()  # GET THE STUDENTS AND THEIR COURSE CHOICES.
    for student in exam_info:  # GET THE SPECIFIC STUDENT.
        for course in exam_info[student]:  # GET THE COURSE OF EACH STUDENT.
            exam_info[student][course]["project"] = return_grade(
                student, course, "project"
            )  # ASSIGN THE 'project' GRADE TO RETURNED VALUE.
            exam_info[student][course]["exam"] = return_grade(
                student, course, "exam"
            )  # ASSIGN THE 'exam' GRADE TO RETURNED VALUE.
            exam_info[student][course]["class"] = return_grade(
                student, course, "class"
            )  # ASSIGN THE 'class' GRADE TO RETURNED VALUE.
            exam_info[student][course]["average"] = get_average_of_course(
                exam_info, student, course
            )
            exam_info[student][course]["letter"] = get_letter(
                exam_info[student][course]["average"] #ASSIGNMENT OF LETTER (OR SUCCESS MESSAGE).
            )
#================================================================================================================
# PRINT OF AVERAGE GRADES AND THE MESSAGE INDICATING SUCCSS OR FAILURE PER COURSE.
#================================================================================================================
    for student, lessons in exam_info.items():
        for lesson, info in lessons.items():
            print(" ")
            print(f"{student}'s {lesson} average is {info['average']} % and the letter is {info['letter']}.")            
        all_avgs = [info["average"] for info in lessons.values()]
        
        print(" ")
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print(" ")
        print(f"{student}'s total average is {sum(all_avgs) / len(all_avgs)} % \n")
        
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    course_bounds = {}
    
#================================================================================================================
# APPEND OF ALL AVERAGES INTO A DICTIONARY.
#================================================================================================================
    for student_info in exam_info.values():
        for course, course_info in student_info.items():
            if course not in course_bounds:
                course_bounds[course] = []
            course_bounds[course].append(course_info["average"])
    averages = {}
    
#================================================================================================================
# MOST DIFFICULT COURSE AMONGST STUDENTS.
#================================================================================================================
    for course_name, bounds in course_bounds.items():
        averages[course_name] = sum(bounds) / len(bounds)
        
    print(" ")
    print(f"Most difficult course is: {min(averages, key=averages.get)}")
    hardest_category = {"project": [], "exam": [], "class": []}
    
#================================================================================================================
# HARDEST CATEGORY TO GET AN EASY GRADE.
#================================================================================================================
    for student_info in exam_info.values():
        for course_info in student_info.values():
            hardest_category["project"].append(course_info["project"])
            hardest_category["exam"].append(course_info["exam"])
            hardest_category["class"].append(course_info["class"])

    hardest_category_averages = {}

    for category, bounds in hardest_category.items():
        hardest_category_averages[category] = sum(bounds) / len(bounds)

    print(f"Easiest category is: {max(hardest_category_averages, key = hardest_category_averages.get)}")
    print(" ")

#================================================================================================================
#FUNCTION THAT RETURNS GRADE.
#================================================================================================================
def return_grade(student, course, grade_type):
    grade = float(input(f"Enter {student}'s {grade_type} grade for {course}: "))
    return grade

#================================================================================================================
# FUNCTION THAT CALCULATES THE AVERAGES.
#================================================================================================================
def get_average_of_course(exam_info, student, course):
    average_project_grade = exam_info[student][course]["project"] * 0.25
    average_exam_grade = exam_info[student][course]["exam"] * 0.5
    average_class_grade = exam_info[student][course]["class"] * 0.25

    total_average = average_project_grade + average_exam_grade + average_class_grade
    return total_average

#================================================================================================================
# FUNCTION THAT DETECTES THE LETTER/MESSAGE USING THE AVERAGE GRADE.
#================================================================================================================
def get_letter(average):
    grade_range = {
        "A": [70, 100],
        "B": [60, 69],
        "C": [50, 59],
        "D": [40, 49],
        "F": [0, 39],
    }

    for letter, bounds in grade_range.items():
        if int(average) in range(bounds[0], bounds[1]):
            return letter
    raise ValueError("There was a problem in the inputs of the grades. Probably you entered a value(grade) greater than 100 !")

add_grades()
