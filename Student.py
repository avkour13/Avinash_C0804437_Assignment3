import unittest

import logging


class Student(unittest.TestCase):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def total_marks(self, subject1, subject2, subject3):
        try:
            assert subject1 > 0
            assert subject2 > 0
            assert subject3 > 0
            self.assertGreater(subject1, subject2, "Subject 2 has higher marks")
            self.assertLess(subject2, subject3, "Subject 2 has less marks.")
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
