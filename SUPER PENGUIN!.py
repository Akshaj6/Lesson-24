class Bird:
    def __init__(self):
        print("BIRD IS READY!")
    def whoisthis(self):
        print("BIRD!")
    def swim(self):
        print("SWIM FASTER")
class Penguin(Bird):
    def __init(self):
        super().__init__()
        print("PENGUIN IS READY!!")
    def whoisthis(self):
        print("PENGUIN!!")
    def run(self):
        print("RUN FASTER!")
peggy = Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()