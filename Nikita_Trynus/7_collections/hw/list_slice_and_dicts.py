import random


prog_list = []

for i in range(10):
    prog_list.append(random.randint(1, 101))

if __name__ == '__main__':
    print(prog_list[:3])
    print(prog_list[len(prog_list)//2-1:(len(prog_list)//2)+2])
    print(prog_list[::-1])
    print(prog_list[-1:-4:-1])

    names = ['Andrew', 'John', 'Semen']
    fav_number = {i : len(i) for i in names}
    # print(fav_number)

    for i,j in fav_number.items():
        print(f'{i} and {j}')

