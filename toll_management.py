import mysql.connector as mys
mycon = mys.connect(host='localhost', user='root', password='root', database='tollex')
mycursor = mycon.cursor()

# opening message
print("-_-_-_-_-_-_-_WELCOME TO TOLLEX_-_-_-_-_-_-_-_-")
while(True):
    print("\n\n 1.SHOW RECORDS \n 2.NEW  \n 3.SORT \n 4.EDIT EXISTING TOLLS \n 5.DELETE  \n 6.EXIT\n\n")
    choice = int(input("Enter the corresponding number of the operation to be performed on the data:"))

    if (choice == 1):
        show = 'SELECT * FROM toll'
        mycursor.execute(show)
        row = mycursor.fetchall()
        print('''| name | id  | location | tollbooth | vehicleclass | choice | paymentmethod |''')
        for each in row:
            print("  ", each[0], "   ", each[1], "   ", each[2], "    ", each[3], "    ", each[4], "   ", each[5], "    ", each[6])

    elif (choice == 2):
        # ask user to enter name
        name = input("Enter username: ")

        # display message
        print("Hey there", name, "!......Make This Journey Yours")
        print("""             logging in 

              """)  
        print()

        import string
        import random

        # initializing size of string 
        N = 7

        # using random.choices()
        # generating random strings 
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))

        # print result
        print("ID generated  : " + str(res))
        id = str(res)

        # switch on location
        location = input("""Tollex requires location access |
        location is on(yes/no): """)

        # locations available
        if location.lower() == "yes":
            location = "YES"
            print("Location is switched on")
            tollbooth = input("""Select location---
                     BETL Toll Gate,Hosur Gate
                     Bangalore Elevated Tollway
                     Electronic city toll plaza
                     NICE mys Rd Toll Booth    
                     Elevated expressway       
                     NHAI Etw Toll Gate        
                     Ndtpl Toll Booth Office   
                     Bannerghatta Toll Booth   
                     ___________  """)
        else:
            print("Please turn on location")

        # selecting vehicle
        vehicle = input("""V E H I C L E  C L A S S                                               SINGLE  RETURNS  MONTHLY PASS
                   Two Wheeler	                                                        |20 |	|30 |	  |580 |
                   Car, Jeep, Van	                                                |50 |	|75 |	  |1455|
                   Light Commercial Vehices (LCV) , Mini bus	                        |70 |	|100|	  |2035|
                   Truck, Bus	                                                        |135|	|205|	  |4070|
                   Earth moving equipment, heavy construction machinery, MAV  	        |270|	|405|	  |8135|
                  (enter)____""")
        print()

        # cost options
        if vehicle == '':
            print("Field cannot be left blank")

        # checking if cost exists in options
        cost = [20, 30, 580, 50, 75, 1455, 70, 100, 2035, 135, 205, 4070, 270, 405, 8135]
        ticket = input("select option 'single','returns' or 'monthly pass': ")
        price = 0
        if vehicle == "two wheeler":
            if ticket == 'single':
                price += 20
            elif ticket == 'returns':
                price += 30
            else:
                price += 580
        elif vehicle in ["car", "jeep", "van"]:
            if ticket == 'single':
                price += 50
            elif ticket == 'returns':
                price += 75
            else:
                price += 1455
        elif vehicle in ["lcv", "mini bus"]:
            if ticket == 'single':
                price += 70
            elif ticket == 'returns':
                price += 100
            else:
                price += 2035
        elif vehicle in ["truck", "bus"]:
            if ticket == 'single':
                price += 135
            elif ticket == 'returns':
                price += 205
            else:
                price += 4070
        elif vehicle in ["earth moving equipment", "mav"]:
            if ticket == 'single':
                price += 270
            elif ticket == 'returns':
                price += 405
            else:
                price += 8135
        else:
            print("Enter valid vehicle entry.")

        print("Amount to be paid: Rupees", price)

        payment = input("payment method ----> online or Fastag: ")

        # selecting payment method
        if payment.lower() == "online":
            choice = input("Fastag is an efficient way to pay at tolls, are you sure you want to continue with online payment?(yes or no): ")

            if choice.lower() == "yes":
                print("You will be levied a 5% fine")
                print("Rupees", price + (0.05 * price), "has been debited from your account")
                print("BARRICADE IS OPEN")
            else:
                print("Rupees", price, "has been debited from your account")
                print("Use code '", name, ".Fastag' on shop.Fastag for credits or rewards")
                print("BARRICADE IS OPEN")

        elif payment.lower() == "fastag":
            print("Rupees", price, "has been debited from your account")
            print("Use code '", name, ".Fastag' on shop.Fastag for credits or rewards")
            print("BARRICADE IS OPEN")
        else:
            print("Please enter a valid response....")

        # Inserting the data without sno
        insert = "INSERT INTO toll (name, id, location, tollbooth, vehicleclass, choice, paymentmethod) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(name, id, location, tollbooth, vehicle, ticket, payment)
        mycursor.execute(insert)
        mycon.commit()
        print("Data saved")

    elif choice == 3:
        print("The table will be arranged in alphabetical order")
        sort = 'SELECT * FROM toll ORDER BY name'
        mycursor.execute(sort)
        record = mycursor.fetchall()
        for each in record:
            print(each[0], " ", each[1], " ", each[2], " ", each[3], " ", each[4], " ", each[5], " ", each[6])

    elif choice == 4:
        num = int(input("Enter the serial number to update: "))
        edit = int(input("Enter the section to be edited (1)name, (2)id, (3)location, (4)tollbooth, (5)vehicle, (6)ticket, (7)payment: "))

        if edit == 1:
            name = input("Enter updated name: ")
            edits = "UPDATE toll SET name = '{}' WHERE id = '{}'".format(name, num)
            mycursor.execute(edits)
            mycon.commit()
        elif edit == 2:
            id = input("Enter updated id: ")
            edits = "UPDATE toll SET id = '{}' WHERE id = '{}'".format(id, num)
            mycursor.execute(edits)
            mycon.commit()
        elif edit == 3:
            loc = input("Enter updated location: ")
            edits = "UPDATE toll SET location = '{}' WHERE id = '{}'".format(loc, num)
            mycursor.execute(edits)
            mycon.commit()
        elif edit == 4:
            booth = input("Enter updated booth: ")
            edits = "UPDATE toll SET tollbooth = '{}' WHERE id = '{}'".format(booth, num)
            mycursor.execute(edits)
            mycon.commit()
        elif edit == 5:
            vehicle = input("Enter updated vehicle: ")
            edits = "UPDATE toll SET vehicleclass = '{}' WHERE id = '{}'".format(vehicle, num)
            mycursor.execute(edits)
            mycon.commit()
        elif edit == 6:
            ticket = input("Enter updated ticket: ")
            edits = "UPDATE toll SET choice = '{}' WHERE id = '{}'".format(ticket, num)
            mycursor.execute(edits)
            mycon.commit()
        elif edit == 7:
            pay = input("Enter updated payment method: ")
            edits = "UPDATE toll SET paymentmethod = '{}' WHERE id = '{}'".format(pay, num)
            mycursor.execute(edits)
            mycon.commit()

        print("Data updated successfully")

    elif choice == 5:
        delete = input("Enter the ID of the row to be deleted: ")
        query = "DELETE FROM toll WHERE id = '{}'".format(delete)
        mycursor.execute(query)
        mycon.commit()
        print("Row successfully deleted")

    elif (choice == 6):
        break
