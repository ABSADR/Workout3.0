import time
import json
from workout import progs


day_list=[]
lista_ex=[]
workouts=''


class Hela():
    pass


def Days():
    print('Pick a day: ')
    print('------Monday<->Saturday---------: ')
    days=['monday','tuesday','wednesday','thursday','friday','saturday']


    while decizie==False:
        x = input().lower()
        if x in days:

            day_list.append(x)
            print(f'You selected {x.upper()}')
            return Introduction(), Options()


        elif x not in days:
            print('Enter a valid day <3 ')



def Introduction():
    print('''Here are your options :'
                          'Iti poti vizualiza lista de ex apasand L,'
                          'Poti adauga exercitii apasand A,'
                          'Poti sterge exercitiu apasand S,'
                          'Poti iesi din modul apasand X '
                          'You can choose a working program by pressing P' ''')
    print('---------------------------------------')
valid_answers = ['L', 'l', 'A', 'a', 'S', 's', 'X', 'x','P','p']

decizie=False


def Options():
    while decizie == False:
        print('-----------------------')
        answer=input('Pick one option! ')

        if answer in valid_answers:
            time.sleep(0.2)
            print('3')
            time.sleep(0.2)
            print('2')
            time.sleep(0.2)
            print('1')



        if answer=='L' or answer == 'l':
            with open('workouts.txt','r') as workouts:
                lista=workouts.read()
            print(f'Lista de exercitii este compusa din {lista}')



        elif answer=='A' or answer=='a':
            print('Adauga un exercitiu: ')
            print('~~~~~~~~~~~~HERE~~~~~~~~~~')
            exercitiu_adaugat=input()
            lista_ex.append(exercitiu_adaugat)
            with open('workouts.txt','a') as workout:
                workout.write(str(lista_ex))
            print(f'Cu exercitiul adaugat lista ta pentru {day_list} este compusa din {lista_ex}')



        elif answer=='P' or answer== 'p':
            print('-----------Programs----------')

            return progs()







        elif answer=='S' or answer=='s':
            with open('workouts.txt', 'r') as workouts:
                lista=workouts.read()
            print('Poti sterge un exercitiu acum!'
                  f'Introduce index-ul exercitiului pe care doresti sa il stergi din lista {lista}  ')
            print('~~~~~~~~~~~~~NOW~~~~~~~~~')
            delete=input()
            for _ in lista:
                new_list=lista.removeprefix(delete)

            print(f' {day_list} training is now : {new_list}')


        elif answer not in valid_answers :
            print('Enter a valid answer')


        elif answer == 'X' or 'x':
            time.sleep(1.5)
            print('-------------------')
            print('Exiting module')
            time.sleep(0.5)
            print('3')
            time.sleep(0.5)
            print('2')
            time.sleep(0.5)
            print('1')
            time.sleep(0.5)
            print('BYeeeeee ^.^')
            break


Days()

