class cpu_cycles:
    def __init__(self):
        self.cycle = 0
        self.x = 1  # AKA spirte position
        self.history = dict()  # For debugging
        self.crt_rows = [["." for x in range(40)] for y in range(6)]
        self.sprite_pos = [self.x - 1, self.x, self.x + 1]

    def increase_cycle(self, job):
        # All jobs must increase the cycle
        self.cycle += 1
        self.history[self.cycle] = [self.x, self.cycle * self.x]
        self.draw_pixel()  # all cycles draw a pixel
        if job != "noop":  # if a add_x task then we have another cycle to do
            self.cycle += 1
            self.draw_pixel()  # all cycles draw a pixel
            self.history[self.cycle] = [self.x, self.cycle * self.x]
            self.add_x(int(job[job.find(" ") + 1 : len(job)]))
            self.update_sprite_position()

    def add_x(self, addx):
        self.x += addx

    def update_sprite_position(self):
        self.sprite_pos = [self.x - 1, self.x, self.x + 1]

    def draw_pixel(self):
        row = int((self.cycle - 1) / 40)
        col = (self.cycle - 1) % 40
        if col in self.sprite_pos:
            self.crt_rows[row][col] = "#"

    def draw_board(self):
        line = ""
        for row in range(6):
            for col in range(40):
                line = line + str(self.crt_rows[row][col])
            print(line)
            line = ""


cpu = cpu_cycles()

with open("input.txt") as infile:
    for line in infile:
        cpu.increase_cycle(line.strip())

## Output ##
print(cpu.history[20])
print(cpu.history[60])
print(cpu.history[100])
print(cpu.history[140])
print(cpu.history[180])
print(cpu.history[220])


print(
    cpu.history[20][1]
    + cpu.history[60][1]
    + cpu.history[100][1]
    + cpu.history[140][1]
    + cpu.history[180][1]
    + cpu.history[220][1]
)  # Part one answer

# Part two answer
cpu.draw_board()
