import copy
import random
# Consider using the modules imported above.
# print(dir(random))
class Hat:
    def __init__(self, **colour):
        self.contents = []
        for k,v in colour.items():
            for i in range(v):
                self.contents.append(k)

        # print(self.contents)

    def draw(self, draw_number):
        balls_drawn = []
        if draw_number > len(self.contents):
            return self.contents
        else:
            # contents_copy = copy.deepcopy(self.contents)
            for i in range(draw_number):
                index = random.randint(0,len(self.contents)-1)
                # print(index)
                balls_drawn.append(self.contents[index])
                self.contents.pop(index)

        return balls_drawn




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        count_balls = {}
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        # print("Ball Drawn: ", balls_drawn)
        # print("Expected Balls: ", expected_balls)
        for i in balls_drawn:
            count_balls[i] =count_balls.get(i,0) + 1

        success = False

        for k,v in expected_balls.items():
            if (v != 0):
                if k not in count_balls:
                    success = False
                    break
                elif count_balls[k] >= v:
                    success = True
                else:
                    success = False
                    break
        if success:
            M = M + 1

    return M/num_experiments
