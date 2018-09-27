import os
import csv
import pandas as pd



def fn_anotar():    
    opcoes = {
        "1": ("Disbelieve", fn_set),
        "2": ("Neutral", fn_set),
        "3": ("Believe", fn_set),
        "E": ("Just Exit", my_quit_fn),
        "S": ("Save and Exit", fn_save_exit),
        "P": ("Previous Submission", fn_previous),
        "N": ("Next Submission", fn_next)
    }

    resp=None

    global _csv
    _csv = abrirCSV()
    
    i=0
    while i< len(_csv):
        clear()

        if "Title" not in _csv[i]:

            format(_csv[i]['Rumour'], _csv[i]['Submission'])

            ans = input("\n$: ")

            resp = opcoes.get(ans.upper(),[None,invalido])[1](csv=_csv, i=i, opcoes=opcoes, ans=ans)
            i += resp

            if i < 0:
                return

        else:
            i += 1

def fn_save_exit(**kwargs):
    # pd.DataFrame(csv).T.reset_index().to_csv('myfile.csv', header=False, index=False)
    filename = input("Give a name to your file: ")


    with open(str(filename)+".csv", mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in _csv:
            if "Title" not in row:
                employee_writer.writerow([row['Submission'], row['Label']])
            else:
                employee_writer.writerow(row['Rumour'])

    print(input("File created! You are good to go! Thank You =]"))

    return -2000

def format(rumour, submission):
    print(rumour + '\n')
    print('Submission:\n' + submission)
    print('\n(1)Disbelieve  (2)Neutral  (3)Believe\n\n(P)Previous Submission  (N)Next Submission\n(E)Just Exit  (S)Save and Exit')

def fn_previous(**kwargs):
    return -1

def fn_next(**kwargs):
    return 1

def fn_set(**kwargs):
    # csv = kwargs['csv']
    i = kwargs['i']
    opcoes = kwargs['opcoes']
    ans = kwargs['ans']

    _csv[i]['Label'] = opcoes[ans][0]

    return 1

def abrirCSV():  
    clear()

    filename = input("Give the name of your .csv file (it is case SeNsiTIvE!).\nJust the name, without the extension.\n$: ")  

    try:
        with open(str(filename)+".csv", newline='') as csvfile:
            dicts = []

            df = pd.read_csv(csvfile)

            rumour = None

            for i in range(len(df.index)):

                if "Rumour: " in df["Submission"][i]:
                    rumour = df["Submission"][i]
                    dicts.append({"Rumour": rumour, "Title": "True"})

                else:
                    d = {
                        "Rumour": rumour,
                        "Submission": df["Submission"][i],
                        "Label": df["Label"][i]
                    }
                    dicts.append(d)

            return dicts
    except Exception as e:
        print("File not supported!")
        print(e)

def my_add_fn():
   print("SUM:%s"%sum(map(int,input("Enter 2 numbers seperated by a space").split())))

def my_quit_fn(**kwargs):
    ans = input("Are you sure you want to exit? (Y) \"Yes, and leave\" or (N) \"No and go back\"\n$: ")
    if(ans.upper()=="Y"):
        raise SystemExit

def invalido(**kwargs):
   print(input("INVALID CHOICE!\n Press Enter to try again..."))
   return 0

def invalid():
   print(input("INVALID CHOICE!\n Press Enter to try again..."))
   

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



menu = {
    "S":("Start!",fn_anotar),
    "E":("Exit",my_quit_fn)
}

while 1:
    clear()
    print("Welcome to the Annotation facilitator tool")

    print("To start, make sure you have a file .csv in your folder\nNeither he file extension .xlsx or other works, just .csv!")

    print("The system will automatically iterate over the many rows of your file and then you can choose the type of the field\n")

    for key in sorted(menu.keys()):
        print(key+":" + menu[key][0])

    ans = input("\nChoose an option.\n$: ")
    menu.get(ans.upper(),[None,invalid])[1]()

