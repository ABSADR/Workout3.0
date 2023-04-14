import time
import json

answers=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def programs():
    print('*---Programs MODE selected---*')
    print('*~~~~~Type the DAY~~~~*')
    while True:
        answer = input()
        if answer in answers[0]:
            time.sleep(0.2)
            print('****')
            time.sleep(0.3)
            print('***')
            time.sleep(0.3)
            print('*')
            return monday()
        if answer in answers[1]:
            time.sleep(0.2)
            print('****')
            time.sleep(0.3)
            print('***')
            time.sleep(0.3)
            print('*')
            return tuesday()
        if answer in answers[2]:
            time.sleep(0.2)
            print('****')
            time.sleep(0.3)
            print('***')
            time.sleep(0.3)
            print('*')
            return wednesday()
        if answer in answers[3]:
            time.sleep(0.2)
            print('****')
            time.sleep(0.3)
            print('***')
            time.sleep(0.3)
            print('*')
            return thursday()
        if answer in answers[4]:
            time.sleep(0.2)
            print('****')
            time.sleep(0.3)
            print('***')
            time.sleep(0.3)
            print('*')
            return friday()
        if answer in answers[5]:
            time.sleep(0.2)
            print('****')
            time.sleep(0.3)
            print('***')
            time.sleep(0.3)
            print('*')
            return saturday()
        if answer in answers[6]:
            time.sleep(0.2)
            print('****')
            time.sleep(0.3)
            print('***')
            time.sleep(0.3)
            print('*')
            return sunday()
        elif answer not in answers:
            print('Enter a DAY that we all know please ^^')

def monday():
    with open('../programs.json') as f:
        data = json.load(f)
        print('*-----------MONDAY   ARMS-------------*')
        print(json.dumps(data['Monday']['ARMS']['Biceps'],indent=2))
        print(json.dumps(data['Monday']['ARMS']['Triceps'],indent=2))
        print(json.dumps(data['Monday']['ARMS']['ABS/CARDIO'],indent=2))

def tuesday():
    with open('../programs.json') as f:
        data = json.load(f)
        print('*-----------TUESDAY  CHEST -------------*')
        print(json.dumps(data['Tuesday']['CHEST'],indent=2))
        print(json.dumps(data['Tuesday']['ABS/CARDIO'],indent=2))

def wednesday():
    with open('../programs.json') as f:
        data = json.load(f)
        print('*-----------WEDNESDAY BACK -------------*')
        print(json.dumps(data['Wednesday']['BACK'],indent=2))
        print(json.dumps(data['Tuesday']['ABS/CARDIO'],indent=2))


def thursday():
    with open('../programs.json') as f:
        data = json.load(f)
        print('*-----------THURSDAY SHOULDERS -------------*')
        print(json.dumps(data['Thursday']['SHOULDERS'],indent=2))
        print(json.dumps(data['Thursday']['ABS'],indent=2))


def friday():
    with open('../programs.json') as f:
        data = json.load(f)
        print('*-----------FRIDAY LEG-DAY -------------*')
        print(json.dumps(data['Friday']['LEG-DAY'],indent=2))
        print(json.dumps(data['Friday']['CARDIO'],indent=2))


def saturday():
    with open('../programs.json') as f:
        data = json.load(f)
        print('*-----------SATURDAY -------------*')
        print(json.dumps(data['Saturday'],indent=2))

def sunday():
    with open('../programs.json') as f:
        data = json.load(f)
        print('*-----------SUNDAY -------------*')
        print(json.dumps(data['Sunday'],indent=2))


programs()