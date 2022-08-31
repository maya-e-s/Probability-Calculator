import copy, random

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for key, val in kwargs.items():
            for i in range(val): self.contents.append(key)

    # removes n balls from hat without replacement; return string containing removed balls
    def draw(self, n):
        #random.sample(population, k, *, counts=None)
        random.shuffle(self.contents)
        removed_balls = self.contents[:n]
        del self.contents[:n]
        return removed_balls

#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):


# test -----------------------------------------
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
print(hat1.contents)
#print(hat2.contents)
print(hat1.draw(5), hat1.contents)
