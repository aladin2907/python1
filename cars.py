import json


class Toyota:
    def __init__(self):
        print('Creating new car')
        id_new = Abstractnyi.generate_new_id()
        self.car = {id_new: {"Color": input('What color ?'), "engine: ": input('Engine ?')}}

    def add_car_to_list(self):
        print('Adding new car to file')
        myfile1 = open("DBpy/dbp.json", 'a')
        myfile1.write(json.dumps(self.car) + '\n')
        myfile1.close()


class Abstractnyi:

    def generate_new_id():
        myfile1 = open("DBpy/dbp.json", 'r')
        line_quantiti = 0
        for line in myfile1:
            line_quantiti += 1
        myfile1.close()
        return line_quantiti + 1

    def change_color():
        print('Chenging color')
        id_car = int(input('What ID do you want change ?'))
        if Abstractnyi.generate_new_id() > id_car > 0:
            data = Abstractnyi.read_data(id_car)
            new_color = input('What is new color ?')
            Abstractnyi.write_data(data, id_car, new_color)

        else:
            print('Car with this id not found')

    def read_data(id):
        print('read_data')
        with open("DBpy/dbp.json", 'r') as myfile:
            data = []
            i = 1
            for line in myfile:
                data.append(json.loads(line))
                i += 1
        print('Prochitali', len(data))
        return data

    def write_data(data, id, new_color):
        data[id - 1][str(id)]['Color'] = new_color
        with open("DBpy/dbp.json", 'r+') as myfile:
            j = 0
            for i in data:
                myfile.write(json.dumps(data[j]) + '\n')
                # myfile.write(json.dumps(data[i]))
                j += 1
