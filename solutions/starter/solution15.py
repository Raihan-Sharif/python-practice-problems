
student_1 = [40, 35, 70, 90, 56]

student_2 = [57, 35, 80, 98, 46]
student_3 = [57, 40, 80, 98, 46]

def calculate_average(marks):
    # Check if any subject's mark is less than 40
    if any(mark < 40 for mark in marks):
        return "FAILED"
    
    # Calculate the average marks
    average_marks = sum(marks) / len(marks)
    
    return average_marks

# Example of usage
average_student_1 = calculate_average(student_1)
average_student_2 = calculate_average(student_2)
average_student_3 = calculate_average(student_3)
print(f"The average marks of student 1 is: {average_student_1}")    
print(f"The average marks of student 2 is: {average_student_2}")
print(f"The average marks of student 3 is: {average_student_3}")