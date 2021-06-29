import timeit
import UnitTest_Area
import Student

if __name__ == '__main__':
    start_time = timeit.default_timer()
    UnitTest_Area.UnitTest_Area().run_test()
    total_marks = int(input("Enter total marks for the students: "))
    num_students = int(input("Enter total number of students: "))
    average = Student.Student().avg_marks(total_marks, num_students)
    print("The average marks for the class is ", average)
    end_time = timeit.default_timer()
    print(end_time - start_time)

