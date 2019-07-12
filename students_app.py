__author__ = 'lulu'


from statistics import mean as  m
admins = {'python','password123@'}

studentDict = {'Emma':[12,45,34],
                   'Alex':[67,87,90],
                    'Sam':[89,90,67] }

def enterGrade():
    nameToenter = input('studentname:  ')
    gradeToenter = input('Grade:  ')

    if nameToenter in studentDict:
        print('Adding Grade.....')
        studentDict[nameToenter].append(float(gradeToenter))
    else :print('Student does not exist')
    print('studentDict')

    def removeStudent():
        nameToremove = input('What student do you want to remove ?:  ')
        if nameToremove in studentDict:
            print('removing student....')
            del studentDict[nameToremove]
            print('StudentDict')



        def studentAVG():
            for eachStudent in studentDict:
                gradelist = studentDict[eachStudent]
                avgGrade = m(gradelist)
                print (eachStudent,'has an average of  : avgGrade')


        def main():
            print ("""Welcome to Grade Central
                   [1] - Enter Grades
                   [2] - Remove Student
                   [3]- Student Average Grade
                   [4]- Exit
                    """)
            action = input('What would you like to do today ?(Enter a number)  ')
            if action =='1':
                enterGrade()
            elif action=='2':
                removeStudent()
            elif action=='3':
                studentAVG()
            elif action=='4':
                exit()
            else:
                print ('No valid choice was given try Again')

                login = input('Username')
                password = input('password')

                if login in admins:
                    if admins[login] == password:
                        print('Welcome', login)

                        while true :
                            main()
                    else:
                        print('Invalid password, will denote in 5 seconds')
                else:
                    print('Invalid Username,calling the FBI to report this')

