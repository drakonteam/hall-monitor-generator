#-------------------------------------------------------------------------------
# Name:        Hall Monitor Randomizer
# Purpose:      Randomly Generate Hall Monitor Sheets
#
# Author:      Christopher Liu
#
# Created:     03/10/2013
# Copyright:   (c) Christopher Liu 2013
# Licence:     http://www.binpress.com/license/view/l/4d3513a0b024a5cd1353e42f51c737dc
#-------------------------------------------------------------------------------

import random, time
from random import randrange

#Print Copyright And Stuff
print "(c) 2013 Christopher Liu\n"
print "Welcome to the Hall Monitor Randomizer"
time.sleep(5)

#Print Hall Monitors And Week of month days
f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
f.write("Hall Monitors\r\n")
f.write("Week of month days\r\n")
f.close()

#Ask for which days to start
dayoftheweek = raw_input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat day of the week do you want to start from? \n1 = Monday\n2 = Tuesday\n3 = Wednesday\n4 = Thursday\n5 = Friday\n(Enter a number between 1-5, if you don't the program won't work)\n")
dayoftheweek = int(dayoftheweek)
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5

#Opening Text Files For Each Grade And Putting Them Into A list Format.
grade8 = open('C:\\Hall Monitor Files\\8c.txt', 'r')
grade8names = grade8.readlines()

grade7 = open('C:\\Hall Monitor Files\\7c.txt', 'r')
grade7names = grade7.readlines()

grade6 = open('C:\\Hall Monitor Files\\6c.txt', 'r')
grade6names = grade6.readlines()

grade5 = open('C:\\Hall Monitor Files\\5c.txt', 'r')
grade5names = grade5.readlines()

#Now I Will Randomly Shuffle The List.
grade8rand = randrange(1, 100)
while grade8rand > 0:
    random.shuffle(grade8names)
    grade8rand = grade8rand - 1

grade7rand = randrange(1, 100)
while grade7rand > 0:
    random.shuffle(grade7names)
    grade7rand = grade8rand - 1

grade6rand = randrange(1, 100)
while grade6rand > 0:
    random.shuffle(grade6names)
    grade6rand = grade6rand - 1

grade5rand = randrange(1, 100)
while grade5rand > 0:
    random.shuffle(grade5names)
    grade5rand = grade5rand - 1

#Now I Will Get Students From Every Grade For The First 9 Days(REASON FOR 9: THERE ARE ONLY 9 STUDENTS IN GRADE 7)
x = 9
while x > 0:
    x =  x - 1
    students = []
#Get Students For Each Day From Every Grade
    grade8student = list.pop(grade8names)
    grade8student = grade8student.replace("\n", "")
    students.append(grade8student)

    grade7student = list.pop(grade7names)
    grade7student = grade7student.replace("\n", "")
    students.append(grade7student)

    grade6student = list.pop(grade6names)
    grade6student = grade6student.replace("\n", "")
    students.append(grade6student)

#I Will Then Randomize The list Of Students So Then One Grade Won't Always Be At The Same Location
    studentsrand = randrange(1, 100)
    while studentsrand > 0:
        random.shuffle(students)
        studentsrand = studentsrand - 1

#I Will Insert The Data Into A Text File
    if dayoftheweek == Monday:
        f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
        f.write("Monday:\r\n")
        f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
        f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
        f.close()
        dayoftheweek = dayoftheweek + 1
    else:
        if dayoftheweek == Tuesday:
            f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
            f.write("Tuesday:\r\n")
            f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
            f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
            f.close()
            dayoftheweek = dayoftheweek + 1
        else:
            if dayoftheweek == Wednesday:
                f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
                f.write("Wednesday:\r\n")
                f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
                f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
                f.close()
                dayoftheweek = dayoftheweek + 1
            else:
                if dayoftheweek == Thursday:
                    f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
                    f.write("Thursday:\r\n")
                    f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
                    f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
                    f.close()
                    dayoftheweek = dayoftheweek + 1
                else:
                    if dayoftheweek == Friday:
                        f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
                        f.write("Friday:\r\n")
                        f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
                        f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
                        f.close()
                        dayoftheweek = 1





#Doing The Abnormal Days With 2x8th 1x6th
students = []
z = 2
while z > 0:
    grade8student = list.pop(grade8names)
    grade8student = grade8student.replace("\n", "")
    students.append(grade8student)
    z = z -1

grade6student = list.pop(grade6names)
grade6student = grade6student.replace("\n", "")
students.append(grade6student)

studentsrand = randrange(1, 100)
while studentsrand > 0:
    random.shuffle(students)
    studentsrand = studentsrand - 1

if dayoftheweek == Monday:
    f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
    f.write("Monday:\r\n")
    f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
    f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
    f.close()
    dayoftheweek = dayoftheweek + 1
else:
    if dayoftheweek == Tuesday:
        f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
        f.write("Tuesday:\r\n")
        f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
        f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
        f.close()
        dayoftheweek = dayoftheweek + 1
    else:
        if dayoftheweek == Wednesday:
            f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
            f.write("Wednesday:\r\n")
            f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
            f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
            f.close()
            dayoftheweek = dayoftheweek + 1
        else:
            if dayoftheweek == Thursday:
                f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
                f.write("Thursday:\r\n")
                f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
                f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
                f.close()
                dayoftheweek = dayoftheweek + 1
            else:
                if dayoftheweek == Friday:
                    f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
                    f.write("Friday:\r\n")
                    f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
                    f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
                    f.close()
                    dayoftheweek = 1

#Doing The Abnormal Days With 2x8th 1x5th
students = []
z = 2
while z > 0:
    grade8student = list.pop(grade8names)
    grade8student = grade8student.replace("\n", "")
    students.append(grade8student)
    z = z -1

studentsrand = randrange(1, 100)
while studentsrand > 0:
    random.shuffle(students)
    studentsrand = studentsrand - 1

grade5student = list.pop(grade5names)
grade5student = grade5student.replace("\n", "")
students.append(grade5student)

if dayoftheweek == Monday:
    f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
    f.write("Monday:\r\n")
    f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
    f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
    f.close()
    dayoftheweek = dayoftheweek + 1
else:
    if dayoftheweek == Tuesday:
        f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
        f.write("Tuesday:\r\n")
        f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
        f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
        f.close()
        dayoftheweek = dayoftheweek + 1
    else:
        if dayoftheweek == Wednesday:
            f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
            f.write("Wednesday:\r\n")
            f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
            f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
            f.close()
            dayoftheweek = dayoftheweek + 1
        else:
            if dayoftheweek == Thursday:
                f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
                f.write("Thursday:\r\n")
                f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
                f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
                f.close()
                dayoftheweek = dayoftheweek + 1
            else:
                if dayoftheweek == Friday:
                    f = open('C:\\Hall Monitor Files\\Output.txt', 'a')
                    f.write("Friday:\r\n")
                    f.write("Downstairs: " + list.pop(students) + "/" + list.pop(students) + "\r\n")
                    f.write("Upstairs: " + list.pop(students) + "\r\n" + "\r\n")
                    f.close()
                    dayoftheweek = 1

print "Finished Creating Hall Monitor List"
print "All you do is put it on Word and make it the right fonts."
print "The list is at 'C:\Hall Monitor Files\Output.txt' if you followed my instructions"
print "(c) 2013 Christopher Liu"
time.sleep(5)