class WesternDigitalRuleChecker(object):

    def __init__(self):
        self.estimated_value = 0
        self.standard_deviation = 0

    def __init__(self, estimated_value, standard_deviation):
        self.estimated_value = estimated_value
        self.standard_deviation = standard_deviation

    def check_rule_1(self, datapoints):
        # TODO Vervollstaendige die Methode und gebe true zurueck, 
        # wenn die Regel erfuellt wird und false, 
        # wenn gegen die Regel verstossen wird. 
        # Das "pass" kann geloescht werden, sobald du deinen Code schreibst.
        """Any single data point falls outside the 3σ limit from the centerline"""





        pass

    def check_rule_2(self, datapoints):
        """Two out of three consecutive points fall beyond the
        2σ limit (in zone A or beyond), on the same side of the centerline"""
        if (len(datapoints) >= 3):
            number_of_points_outside_2_deviations = 0
            for item in datapoints[len(datapoints) - 3:len(datapoints)]:
                if (self.estimated_value + 2 * self.standard_deviation < item):
                    number_of_points_outside_2_deviations += 1
                if (self.estimated_value - 2 * self.standard_deviation > item):
                    number_of_points_outside_2_deviations -= 1
            if number_of_points_outside_2_deviations >= 2 or number_of_points_outside_2_deviations <= -2:
                print("Rule 2 failed")
                return False
        return True

    def check_rule_3(self, datapoints):
        """Four out of five consecutive points fall beyond the
        1σ limit (in zone B or beyond), on the same side of the centerline"""
        if (len(datapoints) >= 5):
            number_of_points_outside_1_deviation = 0
            for item in datapoints[len(datapoints) - 5:len(datapoints)]:
                if (self.estimated_value + self.standard_deviation < item):
                    number_of_points_outside_1_deviation += 1
                if (self.estimated_value - self.standard_deviation > item):
                    number_of_points_outside_1_deviation -= 1
            if (number_of_points_outside_1_deviation >= 4 or number_of_points_outside_1_deviation <= -4):
                print("Rule 3 failed")
                return False
        return True

    def check_rule_4(self, datapoints):
        """Nine consecutive points fall on the same side of the centerline (in zone C or beyond)"""
        if (len(datapoints) >= 9):
            relevant_points = datapoints[len(datapoints) - 9:len(datapoints)]
            for index, item in enumerate(relevant_points):
                if (index > 0):
                    if relevant_points[index - 1] > self.estimated_value:
                        if item < self.estimated_value:
                            return True
                    if relevant_points[index - 1] < self.estimated_value:
                        if item > self.estimated_value:
                            return True
                    if item == self.estimated_value:
                        return True
                elif index == 0:
                    if item == self.estimated_value:
                        return True
            print("Rule 4 failed")
            return False
        return True