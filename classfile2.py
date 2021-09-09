class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is - ", self.cpu, "And Laptop is", self.ram)

com1 = computer("I5", "HP Laptop")
com2 = computer("M1", "Applelaptop")

com1.config()
com2.config()
