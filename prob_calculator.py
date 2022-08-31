import copy, random

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for key, val in kwargs.items():
            for i in range(val): self.contents.append(key)
        self.og_contents = copy.copy(self.contents) # copy original contents for resetting hat 

    # removes n balls from hat without replacement; return string containing removed balls
    def draw(self, n):
        # commented code below did not work with test_module (but worked in my testing), I believe we need to use random.sample to have an exact match 
        #random.shuffle(self.contents)
        #removed_balls = self.contents[:n]
        #del self.contents[:n]
        if n>len(self.contents): n = len(self.contents)
        removed_balls = random.sample(self.contents, n)
        for ball in removed_balls: self.contents.remove(ball)
        return removed_balls

    def reset(self):
        self.contents = copy.copy(self.og_contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    correct = 0
    for i in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        check = True
        for key, val in expected_balls.items():
            if drawn_balls.count(key) < val:
                check = False
                break
        if check: correct += 1
        hat.reset()        
    return correct/num_experiments