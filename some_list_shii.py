import getpass
def login_details():
    username = "hewlett_packard"
    password = str("hp2000")
    
    username1 = input("Input your username: ")
    password1 = getpass.getpass("Password: ")

    if username1 == username and password1 == password:
        print("\nWelcome", username1)
        print("Here is your saved data below: \n")
        
        tup=((1, "Jason","Miller", 42, 0.4),(2, "Mullin", "Jacob", 52, 0.6), (3, "Tina", "Bridget", 36, 0.31),(4, "Jake", "Miller", 42, 0.42),(5, "Amy", "Kroos", 19, 0.73))
        print("Serial_No First_Name Last_Name     Age         Score")
        length = len("Serial_No First_Name Last_Name     Age         Score")
        print (length*"-")
        
        for tuple in tup:
            Serial_No, First_Name, Last_Name, Age, Score = tuple
            Score = int(Score*100)
            print("%-10s %-10s %-12s %-12s %-10s" % (Serial_No, First_Name, Last_Name, Age, Score))        
    else:
        print("Access Denied!")
login_details()
