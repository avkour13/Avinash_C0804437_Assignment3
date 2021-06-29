import math
import logging


class Area:
    # now we will Create and configure logger
    logging.basicConfig(filename="file.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    # Let us Create an object
    logger = logging.getLogger()

    # Now we are going to Set the threshold of logger to DEBUG
    logger.setLevel(logging.WARNING)

    def area_circle(self, r):
        area = math.pi * (r * r)
        self.logger.info("The calculation of area of circle performed successfully.")
        return area

    def area_parallelogram(self, b, h):
        area = b * h
        self.logger.info("The calculation of area of parallelogram performed successfully.")
        return area

    def area_square(self, a):
        area = a * a
        self.logger.info("The calculation of area of square performed successfully.")
        return area

    def area_rectangle(self, w, h):
        try:
            assert h > 0
            area = 0.5 * w * h
            self.logger.info("The calculation of area of rectangle performed successfully.")
            return area
        except:
            self.logger.exception("Not a positive number.")

