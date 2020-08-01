import random
random.seed(None)

class Generate_Field():

    

    def __init__(self):
        self.x_len = 30
        self.y_len = 24
        self.field = [[-1 for y in range(self.y_len)] for x in range(self.x_len)]
        self.mines = 180
    # X address major, field[x][y]
    

    def first_input(self, input_loc):
        self.field[input_loc[0]][input_loc[1]] = 0
        if(self.check_valid(input_loc[0]-1,input_loc[1]-1)):
            self.field[input_loc[0]-1][input_loc[1]-1] = 0
        if(self.check_valid(input_loc[0]-1,input_loc[1])):
            self.field[input_loc[0]-1][input_loc[1]] = 0
        if(self.check_valid(input_loc[0]-1,input_loc[1]+1)):
            self.field[input_loc[0]-1][input_loc[1]+1] = 0
        if(self.check_valid(input_loc[0],input_loc[1]-1)):
            self.field[input_loc[0]][input_loc[1]-1] = 0
        if(self.check_valid(input_loc[0],input_loc[1]+1)):
            self.field[input_loc[0]][input_loc[1]+1] = 0
        if(self.check_valid(input_loc[0]+1,input_loc[1]-1)):
            self.field[input_loc[0]+1][input_loc[1]-1] = 0
        if(self.check_valid(input_loc[0]+1,input_loc[1])):
            self.field[input_loc[0]+1][input_loc[1]] = 0
        if(self.check_valid(input_loc[0]+1,input_loc[1]+1)):
            self.field[input_loc[0]+1][input_loc[1]+1] = 0

    def build_field(self):
        x_vals = [None for i in range(self.x_len)]
        y_vals = [None for i in range(self.y_len)]
        for i in range(self.x_len):
            x_vals[i] = i
        for i in range(self.y_len):
            y_vals[i] = i
        random.shuffle(x_vals)
        random.shuffle(y_vals)
        while(self.mines > 0):
            for y in y_vals:
                for x in x_vals:
                    if(random.randrange(self.x_len)==1 and self.field[x][y]==-1 and self.mines > 0):
                        self.field[x][y] = 9
                        self.mines -= 1
        for y in y_vals:
            for x in x_vals:
                if(self.field[x][y]==-1 or self.field[x][y]==0):
                    self.field[x][y] = 0
                    input_loc = [x,y]
                    if(self.check_value(input_loc[0]-1,input_loc[1]-1)==9):
                        self.field[x][y] += 1
                    if(self.check_value(input_loc[0]-1,input_loc[1])==9):
                        self.field[x][y] += 1
                    if(self.check_value(input_loc[0]-1,input_loc[1]+1)==9):
                        self.field[x][y] += 1
                    if(self.check_value(input_loc[0],input_loc[1]-1)==9):
                        self.field[x][y] += 1
                    if(self.check_value(input_loc[0],input_loc[1]+1)==9):
                        self.field[x][y] += 1
                    if(self.check_value(input_loc[0]+1,input_loc[1]-1)==9):
                        self.field[x][y] += 1
                    if(self.check_value(input_loc[0]+1,input_loc[1])==9):
                        self.field[x][y] += 1
                    if(self.check_value(input_loc[0]+1,input_loc[1]+1)==9):
                        self.field[x][y] += 1

    def print_field(self):
        outf = open("board.txt", 'w')
        for y in range(self.y_len):
            output = ""
            for x in range(len(self.field)):
                if(self.field[x][y]==9):
                    output += "X"
                elif(self.field[x][y]==0):
                    output += " "
                else:
                    output += str(self.field[x][y])
                output += "  "
                
                #outf.write(self.field[x][y])

            outf.write(output)
            outf.write("\n")
        outf.close()
    def check_valid(self, x_val, y_val):
        return bool (x_val >= 0 and y_val >= 0 and y_val < self.y_len and x_val < self.x_len)
    def check_value(self, x_val, y_val):
        if(self.check_valid(x_val, y_val)):
            return self.field[x_val][y_val]
        return 0


ms_field = Generate_Field()
ms_field.first_input([5,4])
ms_field.build_field()
ms_field.print_field()