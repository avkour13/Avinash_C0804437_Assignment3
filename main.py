import timeit
import UnitTest_Area
import Student

if __name__ == '__main__':
    start_time = timeit.default_timer()
    UnitTest_Area.UnitTest_Area().run_test()

    # Average marks for the class
    total_marks = int(input("Enter total marks for the students: "))
    num_students = int(input("Enter total number of students: "))
    average = Student.Student().avg_marks(total_marks, num_students)
    print("The average marks for the class is ", average)

    # Total marks for a student
    subject1 = int(input("Enter marks for Subject 1: "))
    subject2 = int(input("Enter marks for Subject 2: "))
    subject3 = int(input("Enter marks for Subject 3: "))
    total = Student.Student().total_marks(subject1, subject2, subject3)
    print("Total marks for the student is ", total)

    end_time = timeit.default_timer()
    print(end_time - start_time)

