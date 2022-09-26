from cars import Toyota
from cars import Abstractnyi
while True:

    flag = int(input('What do you want ? 1 - create new car 2 - change car '))
    if flag == 1:
        newcar = Toyota()
        newcar.add_to_list()

    elif flag == 2:
        Abstractnyi.change_color()
    else:
        print('Attention !')

    # test commit