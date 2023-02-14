from datetime import datetime
import csv

""" This part handles everything related to outputting the data. DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING!"""
def csv_expander(list_of_lists): 
    today = datetime.now()
    klasse = str(input('In which classroom was this hospitation? \n>>>'))
    date = today.strftime('%d_%m_%y')
    filename = date + '_'+ klasse+'.csv'
    with open(filename,'w',newline='') as protocol:
        filewriter = csv.writer(protocol, delimiter=',')
        filewriter.writerows(list_of_lists)
        protocol.close()


def timer(starttime):
    start = starttime
    oldtime = starttime
    newtime = starttime
    entries = [['role', 'time spoken']]
    speaker_roles={ # If you want to change the parameters, simply modify the list in the way shown.
    's':'student',
    'd':'teacher',
    'a':'nobody'}
    print('Please enter one of the following roles: ' # If you change the parameters, you can modify this list to have it also show up in the menu.
          '\n\"s\": STUDENT'
          '\n\"d\": TEACHER'
          '\n\"a\": NO SPEAKER')

    while True:
        command = str(input('>>> '))
        try:
            if command == 'q':
                print('Thanks for using the program, please retrive your data in the working directory.')
                total_time = datetime.now() - start
                entries.append(['total time',total_time.total_seconds()])
                csv_expander(entries)
                break
            elif command in speaker_roles.keys():
                oldtime = newtime
                newtime = datetime.now()
                difference = newtime - oldtime
                entries.append([speaker_roles[command], difference.total_seconds()])
                print('The last speaker was a {} that spoke for {} seconds.'.format(speaker_roles[command],entries[::-1][0][1]))
        except TypeError:
            print('PROGRAMM NOT YET STARTED!!!\n\n\n\n')
            continue


def start():
    print('Classroom Conversation Measurer by MrCactus753')
    i = str(input('To start a new timing process, type \"start\". \nIf you want to quit recording after starting, simply enter \"q\".\n>>> '))
    if i == 'start':
        first_time = datetime.now()
        timer(first_time)
    elif i == 'q':
        print('Goodbye!')
        exit()
    else:
        print('UNKNOWN INPUT')
        start()


start()

