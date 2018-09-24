import os
import csv
import pandas as pd


def fn_anotar():


    opcoes = {
        "1": ("Disbelieve", fn_set),
        "2": ("Neutral", fn_set),
        "3": ("Believe", fn_set),
        "0": ("Exit", my_quit_fn)
    }


    csv = abrirCSV()
    i=0
    while i< len(csv):
        os.system('cls' if os.name == 'nt' else 'clear')

        format(csv[i]['Rumour'], csv[i]['Submission'])

        ans = input("\n$: ")
        opcoes.get(ans,[None,invalid])[1](csv=csv, i=i, op=opcoes[ans])
        i += 1

def format(rumour, submission):
    print(rumour + '\n')
    print('Submission:\n' + submission)
    print('(1)Disbelieve  (2)Neutral  (3)Believe          (0)Exit')


def fn_set(**kwargs):
    csv = kwargs['csv']
    i = kwargs['i']
    op = kwargs['op']

    csv[i]['Label'] = op

def abrirCSV():    

    with open('Rumores discutidos no Reddit.csv', newline='') as csvfile:
        dicts = []

        df = pd.read_csv(csvfile)

        rumour = None

        for i in range(len(df.index)):

            if "Rumour: " in df["Submission"][i]:
                rumour = df["Submission"][i]
            else:
                d = {
                    "Rumour": rumour,
                    "Submission": df["Submission"][i],
                    "Label": df["Label"][i]
                }
                dicts.append(d)

        return dicts


def my_add_fn():
   print("SUM:%s"%sum(map(int,input("Enter 2 numbers seperated by a space").split())))

def my_quit_fn(**kwargs):
   raise SystemExit

def invalid():
   print("INVALID CHOICE!")





menu = {
    "1":("Anotar",fn_anotar),
    "0":("Quit",my_quit_fn)
}

while 1:
    
    for key in sorted(menu.keys()):
        print(key+":" + menu[key][0])

    ans = input("Make A Choice: ")
    menu.get(ans,[None,invalid])[1]()

    # os.system('cls' if os.name == 'nt' else 'clear')


