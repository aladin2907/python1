class Toyota:
    def __init__(self):
        id_new = Idgen.generate_new_id()
        self.car = {'Id': id_new, 'Color': input('What color ?'), 'engine: ': input('Engine ?')}


    def add_to_list(self):
        myfile1 = open("DBpy/dbp.json", 'a')
        myfile1.write(self.car + '\n')
        myfile1.close()

    def change_car(self, id):
        id

    # def drive(self):
    #     print(" We are drive this car")

    # def changecolor(self):
    #     self.color = input("Input color:")

    # def changeengine(self):
    #     self.engine = input('Input engine:')

    # def shift_gir(self):
    #     self.gear = 'automatic'

class Idgen:
    def generate_new_id(self):
        myfile1 = open("DBpy/dbp.json", 'r')
        myfile1.read('Id')
        myfile1.close()
        return id






