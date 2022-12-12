import time

class CPU:
    '''
    Elves communication system CPU emulator.
    '''
    instr_time = {"addx": 2, "noop": 1}

    def __init__(self, debug_enable: bool = False):
        self.clock_counter = 0
        self.program_counter = 0
        self.x_register = 1
        self.program = []  # [program_line_str1, program_line_str2, ...]
        self.running_instr = []  # [end_clock, instr_name, ...instr_args]
        self.debug = debug_enable
        self.devices = []

    def run(self):
        while self.program_counter <= len(self.program):
            self.clock_signal(0)
            if self.debug: time.sleep(0.01)
            self.clock_signal(1)
            if self.debug: time.sleep(0.01)

    def clock_signal(self, value):
        """
        Emulates a clock signal
        value: [0, 1] 
        
        Starting with 0, calling `clock_signal` with value alternating
        between 0 and 1 over and over will lead to the clock_counter increase
        """
        if not value:
            self.clock_counter += 1
        else:
            try:
                if self.running_instr[0] == self.clock_counter:
                    apply_intr = getattr(self, self.running_instr[1])
                    apply_intr(*self.running_instr[2:])

                    if self.debug:
                        print(
                            f"[{self.clock_counter}]\t{self.running_instr[1]} - completed"
                        )
                    self._next_instr()
            except IndexError:
                raise IndexError(
                    "CPU program is empty, please use `CPU.set_program` to provide a valid program to run."
                )

        registers_state = {
            'x': self.x_register
        }

        for device in self.devices:
            device.clock_signal(value, registers_state)

    def _next_instr(self):
        try:
            instr = self.program[self.program_counter].split(" ")
        except IndexError:
            raise EOFError("Program has finished")

        self.running_instr = [self.clock_counter + CPU.instr_time[instr[0]]] + instr
        self.program_counter += 1

    def set_program(self, program):
        self.program = program
        self._next_instr()

    def connect(self, device):
        self.devices.append(device)

    def addx(self, value):
        self.x_register += int(value)

    def noop(self):
        pass

class CRTDisplay:
    '''
    Elves communication system Cathode-Ray Tube emulator.
    '''

    def __init__(self, mode = 'sprite', debug_enable: bool = False):
        self.clock_counter = 0
        self.program = []  # [program_line_str1, program_line_str2, ...]
        self.running_instr = []  # [end_clock, instr_name, ...instr_args]
        self.debug = debug_enable
        self.devices = []
        self.mode = mode

    def clock_signal(self, value, cpu_register_state):
        """
        Emulates a clock signal
        value: [0, 1] 
        
        Starting with 0, calling `clock_signal` with value alternating
        between 0 and 1 over and over will lead to the clock_counter increase
        """
        if not value:
            if self.mode == 'sprite' and cpu_register_state['x'] - 1 <= (self.clock_counter) % 40 <= cpu_register_state['x'] + 1:
                print('#', end='')
            elif self.mode == 'dot' and self.clock_counter == cpu_register_state['x']:
                print('*', end='')
            else:
                print('.', end='')
            if (self.clock_counter + 1) % 40 == 0:
                print()

            self.clock_counter += 1
        else:
            pass