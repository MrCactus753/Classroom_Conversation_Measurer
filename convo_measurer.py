from datetime import datetime
import csv
while True:
    def csv_expander(list_of_lists):
        today = datetime.now()
        date = today.strftime('%d_%m_%y_%H_%M')
        filename = date +'.csv'
        with open(filename,'w',newline='') as protocol:
            filewriter = csv.writer(protocol, delimiter=',')
            filewriter.writerows(list_of_lists)
            protocol.close()

    def timer(starttime):
        start = starttime
        oldtime = starttime
        newtime = starttime
        entries = [['role', 'time spoken']]
        speaker_roles = {
        's':'student',
        't':'teacher',
        'ts':'teacher_and_students',
        'st': 'teacher_and_students',
        'ss':'students_and_students',
        'x':'nobody'}
        print('Please enter one of the following roles: '
              '\n\"s\": STUDENT; '
              '\n\"t\": TEACHER; '
              '\n\"st\": STUDENT & TEACHER; '
              '\n\"ss\": STUDENT & STUDENT'
              '\n\"x\": NO SPEAKER')
        while True:
            command = str(input('>>> '))
            try:
                '''if command == 'start':
                    start = datetime.now()
                    newtime = start
                    pass'''
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
        i = str(input('Hi, to start a new timing process, type \"start\". \nIf you want to quit recording after starting, simply enter \"q\".\n>>> '))
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