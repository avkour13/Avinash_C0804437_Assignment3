import logging


class Student:
    # Let us Create an object
    logger = logging.getLogger()

    # Now we are going to Set the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    def total_marks(self, subject1, subject2, subject3):
        try:
            assert subject1 > 0
            assert subject2 > 0
            assert subject3 > 0
            total = subject1+subject2+subject3
            self.logger.info("The total marks for the student calculated successfully.")
            return total
        except:
            self.logger.warning("The marks entered must be greater than zero.")

    def avg_marks(self, total_marks, num_students):
        try:
            average = total_marks/num_students
            self.logger.info("The average marks for the student calculated successfully.")
            return average
        except:
            self.logger.error("Number of students must be greater than zero.")