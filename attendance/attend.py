class Attend:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def print(self):
        print("이름 : " + str(self.name) + " 출석률 : " + str(self.rate));