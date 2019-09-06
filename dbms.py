import database
#import threading
import json
import pandas as pd
import datetime
from datetime import datetime
from datetime import date
import calendar
import joblib
import os
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['text.color'] = 'Green'

def loadUser(UserDB, userid):
    savingsForecast = database.savingsAnalysis(UserDB, userid, 25)
    print("Your current goal is: %s"%(UserDB[userid]['Goal']))
    #can use nice photos to depict the goals instead of using words --> idea but won't do in prototype
    return savingsForecast;

def deleteArima(UserDB, userid, keys):
    UserDB[userid][keys[0]] = ""
    UserDB[userid][keys[1]]= 0
    os.remove(UserDB[userid][keys[0]])

def loadTransaction(UserDB, userid):
    #look at datasets for EACH factor to identify anomalies to identify significant events like marriage etc.
    #get the dataset
    category = ['Clothing & Footwear', 'Communication', 'Education', 'Food', 'Food Excl Food Servicing Services', 'Food Servicing Services', 'Health Care', 'Household Durables And Services', 'Housing & Utilities', 'Miscellaneous Goods & Services', 'Recreation & Culture', 'Salary', 'Transferrables (All except housing, household, healthcare, communication, education)', 'Transport']

    for i in range(0,15):
        catData = pd.DataFrame(dataPrep(UserDB[userid]['Transaction data file'], category[i]))
        
    print("test")

def reviewTransaction(UserDB, userid):
    #output 13 graphs one for each cat
    #forecast for the next 1 year
    choice = '100'
    clothesRaise=commRaise=eduRaise=foodRaise=foodexclsvcRaise=foodsvcRaise=healthcareRaise=hospitalRaise=recRaise=payRaise=transferrableRaise=False

    while (choice!='0'):
        print("Select the category you wish to review:")
        choice = input("0.Exit\n1.Clothing & Footwear\n2.Communication\n3.Education\n4.Food\n5.Food Excl Food Servicing Services\n6.Food Servicing Services\n\
7.Health Care\n8.Household Durables And Services\n9.Housing & Utilities\n10.Miscellaneous Goods & Services\n11.Recreation & Culture\n12.Salary\n\
13.Transferrables (All except housing, household, healthcare, communication, education)\n14.Transport\n")
        #change_in_val for database.checkfactorRaise() must be changed according to the bank's criteria and definitions.
        if (choice == '1'):
            df = database.categoricalAnalysis(UserDB, userid, "Clothing & Footwear", 1)
            title = "Clothing & Footwear"
            clothesRaise = database.checkfactorRaise(df[:date.today()],80)
        elif (choice == '2'):
            df = database.categoricalAnalysis(UserDB, userid, "Communication", 1)
            title = "Communication"
            commRaise = database.checkfactorRaise(df[:date.today()],80)
        elif (choice == '3'):
            df = database.categoricalAnalysis(UserDB, userid, "Education", 1)
            title = "Education"
            eduRaise = database.checkfactorRaise(df[:date.today()],200)
        elif (choice == '4'):
            df = database.categoricalAnalysis(UserDB, userid, "Food", 1)
            title = "Food"
            foodRaise = database.checkfactorRaise(df[:date.today()],100)
        elif (choice == '5'):
            df = database.categoricalAnalysis(UserDB, userid, "Food Excl Food Servicing Services", 1)
            title = "Food Excl Food Servicing Services"
            foodexclsvcRaise = database.checkfactorRaise(df[:date.today()],50)
        elif (choice == '6'):
            df = database.categoricalAnalysis(UserDB, userid, "Food Servicing Services", 1)
            title = "Food Servicing Services"
            foodsvcRaise = database.checkfactorRaise(df[:date.today()],500)
        elif (choice == '7'):
            df = database.categoricalAnalysis(UserDB, userid, "Health Care", 1)
            title = "Health Care"
            healthcareRaise = database.checkfactorRaise(df[:date.today()],100)
            hospitalRaise = database.checkfactorRaise(df[:date.today()],750)
        elif (choice == '8'):
            df = database.categoricalAnalysis(UserDB, userid, "Household Durables And Services", 1)
            title = "Household Durables And Services"
        elif (choice == '9'):
            df = database.categoricalAnalysis(UserDB, userid, "Housing & Utilities", 1)
            title = "Housing & Utilities"
        elif (choice == '10'):
            df = database.categoricalAnalysis(UserDB, userid, "Miscellaneous Goods & Services", 1)
            title = "Miscellaneous Goods & Services"
        elif (choice == '11'):
            df = database.categoricalAnalysis(UserDB, userid, "Recreation & Culture", 1)
            title = "Recreation & Culture"
            recRaise = database.checkfactorRaise(df[:date.today()],1500)
        elif (choice == '12'):
            df = database.categoricalAnalysis(UserDB, userid, "Salary", 1)
            title = "Salary"
            payRaise = database.checkfactorRaise(df[:date.today()],500)
                
        elif (choice == '13'):
            df = database.categoricalAnalysis(UserDB, userid, "Transferrables (All except housing, household, healthcare, communication, education)", 1)
            title = "Transferrables"
            transferrableRaise = database.checkfactorRaise(df[:date.today()],300)
        elif (choice == '14'):
            df = database.categoricalAnalysis(UserDB, userid, "Transport", 1)
            title = "Transport"
        elif (choice == '0'):
            if (payRaise):
                print("Congrats on your recent pay raise and/or promotion! :)")

            if (foodsvcRaise):
                print("Seems like you had an event recently...")
                if (clothesRaise and recRaise and transferrableRaise and (UserDB[userid]['Marital status']=='Single')): #marriage event
                    print("Let me guess... did you just get married?? Congratulations!!!")
                    a = input("1. Oh, thank you! :)\n2. No, what are you talking about?\n")
                    if (a=='1'):
                        UserDB[userid]['Marital status'] = 'Married'
                        UserDB[userid]['Number of dependencies'] +=1
                        with open('userdb.txt', 'w') as outfile:
                            json.dump(UserDB, outfile)
                elif (clothesRaise and transferrableRaise and healthcareRaise): #baby first month
                    print("Let me guess... it must be for celebrating your baby being 1 month old!\n")
            if (hospitalRaise): #detect hospitalisation
                if (clothesRaise and foodRaise and (UserDB[userid]['Marital status']=='Married')):
                    print("Congratulations on your baby! :)")
                    a = input("1. Oh, thank you! :)\n2. No, what are you talking about?\n")
                    if (a=='1'):
                        UserDB[userid]['Number of dependencies'] +=1
                        with open('userdb.txt', 'w') as outfile:
                            json.dump(UserDB, outfile)
            else:
                print("Oh no! Seems like someone got hospitalised! Are you and your family OK? :(")

            if (recRaise):
                print("Seems like you went for a holiday! How was it? Hope you had a fun and relaxing time! :)")
                    
            print("Hope you have learnt something from this review session! :)")
        else:
            print('You have entered an invalid selection.')

        if (int(choice) in range(1,15)):
            plt.figure()
            if (choice=='12' or choice=='13'):
                line, =plt.plot(df, label=title)
            else:
                line, =plt.plot(-df, label=title)
            plt.legend(handles=[line])
            plt.xlabel('Time')
            plt.ylabel('Amount per month')
            plt.plot()
            plt.show()
    

def editGoals(UserDB, userid):
    print("Edit goals")
    print("Your current goal is: %s"%(UserDB[userid]['Goal']))
    
    newGoal = input("What is your new goal?")
    UserDB[userid]['Goal']=newGoal
    
    print("Your new goal is: %s"%(UserDB[userid]['Goal']))    
    confirmation = input("Confirm? Y/N")
    if (confirmation[0]=='y' or confirmation[0]=='Y'):
        with open('userdb.txt', 'w') as outfile:
            json.dump(UserDB, outfile)
    return;

def futurePlanner(UserDB, userid, savingsForecast):
    #get goals
    with open('goaldb.txt') as json_file:
        goalDB = json.load(json_file)
    goal = UserDB[userid]["Goal"]
    if ("Car" in goal) or ("car" in goal):
        est_total_Price = database.goalPlanner("Car", savingsForecast, goalDB)
        
        savingsForecast1 = pd.DataFrame(savingsForecast[(date(date.today().year,date.today().month-1,calendar.monthrange(date.today().year,date.today().month-1)[1])):])
        future_df10 = database.payByInstalment(savingsForecast1.copy(), est_total_Price, 10)
        future_df20 = database.payByInstalment(savingsForecast1.copy(), est_total_Price, 20)
        
        plt.figure()
        line_up, =plt.plot(savingsForecast1, label="Original Predicted Savings")
        line_mid, =plt.plot(future_df10, label="10 Year Instalment")
        line_down, =plt.plot(future_df20, label="20 Year Instalment")
        plt.legend(handles=[line_up, line_mid, line_down])
        plt.xlabel('Time')
        plt.ylabel('Savings per month')
        plt.plot()
        plt.show()

        #recommend plans
        planData = pd.read_csv('savingPlans.csv', sep=',')
        balance = int(UserDB[userid]['Balance'])
        #goal to be reached in 5 years --> own a car 5 years from today so instalment payments only start from 5 years later
        #criteria for recommending plans: 1) Balance in bank acc must be more than Minimum sum required 2) Plan should be <=5 years so that can save more within the 5 years before buying the car.
        available_plans = planData[(planData['Minimum sum']<balance) & (planData['Number of Years']<=5)]
        print("If you would like to buy a car in 5 years, here are some short-term savings plans from DBS you might want to consider :)")
        print(available_plans)

        print("You should ensure you have financial stability while you pay your monthly instalments over the next 5-10 years.")
        
        print("The plans recommended below are the most suitable for you")
        recommended_plans = planData[(planData['Minimum sum']==0) & (planData['Interest Rate Per Annum']==planData['Interest Rate Per Annum'].max())]
        print(recommended_plans)
    
    
    
    

if __name__=="__main__":
    print("Hello, I'm Aara. Nice to meet you :)")
    database.recreateData();
    userid = input('Please enter your Userid: ')
    print("Remember NOT to give anybody your password. Even the admin, which is myself, will not ask you for your password.")
    #need userid to identify the user. Userid should be automatically identified by the system, not through user input. User is required to be already logged in online before accessing this service. As such, passwords are not required (but can be implemented).
    
    with open('userdb.txt') as json_file:
        UserDB = json.load(json_file)

    while not(userid in UserDB.keys()):
        choice = input("Invalid account! Looks like you have not registered for this service yet. Are you a new user? (Y/N)")
        if (choice=='y' or choice=='Y'):
            userid = database.register(UserDB) #***Pls use john5678 as new userid
            #getData(userid, userid+'_transactionData') --> to be implemented as a function that gets data directly from transaction db and output into userid_transactionData.csv file.
        else:
            userid = input("Please reenter userid:")
    
    print("Welcome ", UserDB[userid]['Name'],"!")
    savingsForecast = loadUser(UserDB, userid)
    
    # do some stuff
    print("How may I help you today?")
    initial_savings_graph = 0
    #aara output
    
    
    #download_thread = threading.Thread(target=database.dataPrep())
    #download_thread.start()
    # continue doing stuff
    a=1000
    while (a!='4'):
        a = input("1. Review monthly transaction data\n2. Edit financial goals\n3. Plan my future\n4. Goodbye Aara!\n")
        
        if (initial_savings_graph==0 and a!='4') :
            print("Firsly, here is a depiction of your savings to date! :)")
            plt.figure()
            plt.plot(savingsForecast[:date.today()])
            plt.xlabel('Time')
            plt.ylabel('Savings')
            plt.plot()
            plt.show()
            initial_savings_graph+=1
        if (a=='1'):
            reviewTransaction(UserDB, userid)
        elif (a=='2'):
            editGoals(UserDB, userid)
        elif (a=='3'):
            futurePlanner(UserDB, userid, savingsForecast)
        elif (a=='4'):
            print('See you again soon! Goodbye! :)')
        else:
            print("This is not a valid selection!")
    
