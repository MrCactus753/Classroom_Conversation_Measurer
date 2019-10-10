from datetime import datetime
import csv

def csv_expander(list_of_lists):
    today = datetime.now()
    date = today.strftime('%d_%m_%y_%H_%M')
    filename = date +'.csv'
    with open(filename,'w') as protocol:
        filewriter = csv.writer(protocol, delimiter=',')
        for i in list_of_lists:
            filewriter.writerow(i)
        protocol.close()
def timer():
    start = None
    oldtime = None
    newtime = None
    entries = [['role', 'time spoken']]
    commandlist = ['s','t','st','ss','n']
    while True:
        command = str(input('Please enter one of the following commands: \n\n\"start\": starts the script; \n\"q\": ends the script; \n\nPOSSIBLE SPEAKERS: \"s\": STUDENT; \"t\": TEACHER; \"st\": STUDENT & TEACHER; \"ss\": STUDENT & STUDENT\n>>> '))
        try:
            if command == 'start':
                start = datetime.now()
                newtime = start
                pass
            elif command == 'q':
                print('Thanks for using the program, please retrive your data in the working directory.')
                total_time = datetime.now() - start
                entries.append(['total time',total_time.total_seconds()])
                csv_expander(entries)
                break
            elif command in commandlist:
                oldtime = newtime
                newtime = datetime.now()
                difference = newtime - oldtime
                entries.append([command, difference.total_seconds()])
        except TypeError:
            print('PROGRAMM NOT YET STARTED!!!\n\n\n\n')
            continue
timer()
