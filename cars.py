class Toyota:
    def __init__(self):
        print('created obj')
        self.color = input('What color ?')
        self.engine = engine
        self.gear = 'automatik'


    def drive(self):
        print(" We are drive this car")

    def changecolor(self):
        self.color = input("Input color:")

    def changeengine(self):
        self.engine = input('Input engine:')

    def shift_gir(self):
        self.gear = 'automatic'

    def printPrintData(self):
        print("Color  of this car: ", self.color)
        print('Engine of this car: ', self.engine)

    def add_car(self):
        myfile1 = open("DBpy/dbp.json", 'a')
        myfile1.write('Color:')
        myfile1.write(self.color)
        myfile1.write(' engine:')
        myfile1.write(self.engine)
        myfile1.write(' gear:')
        myfile1.write(self.gear)
        myfile1.write('\n')
        myfile1.close()


