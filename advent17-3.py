pzlin = 325489

class bot:
    def __init__(self):
        self.move_hist = {}

        self.curr_x = 0
        self.curr_y = 0
        self.curr_dir = 0

    def fwrd(self):
        if self.curr_dir == 0:
            self.curr_x += 1
        elif self.curr_dir == 1:
            self.curr_y -= 1
        elif self.curr_dir == 2:
            self.curr_x -= 1
        elif self.curr_dir == 3:
            self.curr_y += 1
        else:
            raise Exception
    
    def set_value_at_curr_pos(self, value):
        self.move_hist[(self.curr_x,self.curr_y)] = value

    def get_value_at_pos(self, x, y):
        if (x, y) in self.move_hist:
            return self.move_hist[(x, y)]
        else:
            return 0
    
    def get_sum_of_surrounding_values_at_curr_pos(self):
        return sum([
            self.get_value_at_pos(self.curr_x+1,self.curr_y),
            self.get_value_at_pos(self.curr_x+1,self.curr_y-1),
            self.get_value_at_pos(self.curr_x,self.curr_y-1),
            self.get_value_at_pos(self.curr_x-1,self.curr_y-1),
            self.get_value_at_pos(self.curr_x-1,self.curr_y),
            self.get_value_at_pos(self.curr_x-1,self.curr_y+1),
            self.get_value_at_pos(self.curr_x,self.curr_y+1),
            self.get_value_at_pos(self.curr_x+1,self.curr_y+1)
        ])

    def turn_left(self):
        self.curr_dir += 1
        if self.curr_dir > 3:
            self.curr_dir -= 4

b = bot()
b.set_value_at_curr_pos(1)
# total_steps = 0

dist_until_turns = sorted(list(range(100000)) * 2)
for dist in dist_until_turns:
    for step in range(dist):
        b.fwrd()
        # total_steps += 1

        surrounding_sum = b.get_sum_of_surrounding_values_at_curr_pos()
        b.set_value_at_curr_pos(surrounding_sum)
        if surrounding_sum > pzlin:
            print(surrounding_sum)
            raise Exception

        # if total_steps+1 == pzlin:
        #     break


    # if total_steps+1 == pzlin:
        # print(abs(b.curr_x)+abs(b.curr_y))
        # break

    b.turn_left()