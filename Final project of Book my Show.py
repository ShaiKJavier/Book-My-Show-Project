#!/usr/bin/env python
# coding: utf-8

# BOOK MY SHOW PROJECT

# In[ ]:


k = 10
Booked_seat = 0
prize_of_ticket = 0
Total_Income = 0
row = int(input('Enter number of row - \n')) #HERE WE ENTERING WHICH ROW WE NEED
Seats = int(input('Enter number of seats in a row - \n')) #HERE WE ENTERING WHICH SEAT WE NEED
Total_seat = row*Seats
To_See_Number_of_Rows_and_Seats = input("To see number of vaccant seats and rows?click:(yes/no):") #WE WANT TO KNOW WHICH SEAT IS VACCANT
for i in range(0,1):
    print("\nS shows the Vaccant Seats.\n" )
if To_See_Number_of_Rows_and_Seats.lower() == "yes":
    Booked_ticket_Person = [[None for j in range(Seats)] for i in range(row)] # FOR LOOP FOR ARRANGEING SEATS
    
class view: #CLASS TAKEN AS VIEW(FOR AN OBJECT)

    
    def view_making(): #FUNCTION USED FOR CLASS 
        seats_view = {}
        for i in range(row):   #NESTED FOR LOOP FOR ORDER AND VIEW OF THE SEATS
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j+1)] = 'S'  #INCRIMENT IS USED AS S
            seats_view[str(i)] = seats_in_row
        return seats_view

    
    def find_income_percentage():    #FUCTION IS USED FOR RETUNING PERCENTAGE
        income_percentage = (Booked_seat/Total_seat)*100
        return income_percentage

class_call = view
table_of_view = class_call.view_making()
    


while k != 0:   #LOOP IS USED FOR MUTLIPLE LOOPS OCCURED
    print('1 for Show the seats \n2 for Buy a Ticket \n3 for Statistics ', # USED TO SHOW FOUR OPTIONS TO THE USER
          '\n4 for Show booked Tickets User Info \n0 for Exit')
    k = int(input('Select Option - '))   #SELECTION OPTION BY INTERGER ONLY
    if k == 1:  #SLECTION OPTION IS EQUAL TO 1
        if Seats < 10: #AS K VALUE IS 10 DECLARED ABOVE IF USER ENTER ABOVE TEN IT GOES TO ELSE PART
            for seat in range(Seats):
                print(Seats, end='  ')
            print(Seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, Seats):
                print(seat, end=' ')
            print(Seats)
        if Seats < 10:
            for num in table_of_view.keys():
                print(int(num)+1, end='  ')
                for no in table_of_view[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_view.keys():
                if int(list(table_of_view.keys())[count_num]) < 9:
                    print(int(num)+1, end='  ')
                else:
                    print(int(num)+1, end=' ')
                count_key = 0
                for no in table_of_view[num].values():
                    if int(list(table_of_view[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant Seats = ', Total_seat - Booked_seat)
        print()

    elif k == 2:  #NESTED CONDITION IF USER SELECTED OPTION 2
        row_number = int(input('Enter Row Number - \n'))
        Column_number = int(input('Enter Column Number - \n'))
        if row_number in range(1, row+1) and Column_number in range(1, Seats+1):
            if table_of_view[str(row_number-1)][str(Column_number)] == 'S':
                if row*Seats <= 60:
                    prize_of_ticket = 10
                elif Row_number <= int(row/2):
                    prize_of_ticket = 10
                else:
                    prize_of_ticket = 8
                print('prize_of_ticket - ', '$', prize_of_ticket)
                conform = input('yes for booking and no for Stop booking - ')
                person_detail = {}
                if conform == 'yes':
                    person_detail['Name'] = input('Enter Name - ')
                    person_detail['Gender'] = input('Enter Gender - ')
                    person_detail['Age'] = input('Enter Age - ')
                    person_detail['Phone_No'] = input('Enter Phone number - ')
                    person_detail['Ticket_prize'] = prize_of_ticket
                    table_of_view[str(row_number-1)][str(Column_number)] = 'B'
                    Booked_seat += 1
                    Total_Income += prize_of_ticket
                else:
                    continue
                Booked_ticket_Person[row_number-1][Column_number-1] = person_detail
                print('Booked Successfully')
            else:
                print('This seat already booked by some one')
        else:
            print()
            print('*  Invalid Input  *')
        print()

    elif k == 3: #USER SELECT THE THIRD OPTION
        print('Number of purchased Ticket - ', Booked_seat)
        print('income percentage - ', class_call.find_income_percentage())
        print('Current  Income - ', '$', prize_of_ticket)
        print('Total Income - ', '$', Total_Income)
        print()

    elif k == 4: #USER SELECT THE FOURTH OPTION
        Enter_row = int(input('Enter Row number - \n'))
        Enter_column = int(input('Enter Column number - \n'))
        if Enter_row in range(1, row+1) and Enter_column in range(1, Seats+1):
            if table_of_view[str(Enter_row-1)][str(Enter_column)] == 'B':
                person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Phone number - ', person['Phone_No'])
                print('Ticket Prize - ', '$', person['Ticket_prize'])
            else:
                print()
                print('---*---  Vacant seat  ---*---')
        else:
            print()
            print('*  Invalid Input  *')
        print()

    else:
        print()
        print('*  Invalid Input  *')
        print()
    


# In[ ]:





# In[ ]:





# In[ ]:




