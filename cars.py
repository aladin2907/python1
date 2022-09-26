import json


class Toyota:
    def __init__(self):
        print('Creating new car')
        id_new = Abstractnyi.generate_new_id()
        self.car = {id_new: {"Color": input('What color ?'), "engine: ": input('Engine ?')}}

    def add_to_list(self):
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
        if Abstractnyi.generate_new_id()> id_car > 0:
            data = Abstractnyi.read_data(id_car)
            new_color = input('What is new color ?')
            Abstractnyi.write_data(data, id_car, new_color)

        else:
            print('Car with this id not found')

    def read_data(id):
        print('read_data', id)
        i = 1
        with open("DBpy/dbp.json", 'r') as myfile:
            for line in myfile:
                data1 = line
                print('liniya nomer', i, line)
                if i == id:
                    data = json.loads(line)
                    myfile.close()
                    print('Prochitali', data)
                    return data
                i += 1

    def write_data(data, id, new_color):
        data[str(id)]['Color'] = new_color
        print('new color', data)
        with open("DBpy/dbp.json", 'r+') as myfile:
            i = 1
            for line in myfile:
                if id == i:
                    print('menyaem')
                    myfile.write(json.dump(data))
                i += 1

