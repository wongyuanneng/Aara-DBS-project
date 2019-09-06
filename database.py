import pandas as pd
import numpy as np
import joblib
import json
import datetime
from datetime import datetime
from datetime import date
import calendar
from sklearn import metrics
from pmdarima import auto_arima
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['text.color'] = 'Green'


def recreateData():
    data = {}
    data['james999'] = {
        "Name": "James",
	"UserID": "james999",
	"Balance": "120000",
	"Goal": "Car",
        "Marital status": "Single",
        "Number of dependencies": 0,
        "Transaction data file": "filename.csv",
        "Savings_arima": "",
        "Savings_arima_month": "",
        "Clothing & Footwear_arima": "",
        "Clothing & Footwear_arima_month": "",
        "Communication_arima": "",
        "Communication_arima_month": "",
        "Education_arima": "",
        "Education_arima_month": "",
        "Food_arima": "",
        "Food_arima_month": "",
        "Food Servicing Services_arima": "",
        "Food Servicing Services_arima_month": "",
        "Food Excl Food Servicing Services_arima": "",
        "Food Excl Food Servicing Services_arima_month": "",
        "Health Care_arima": "",
        "Health Care_arima_month": "",
        "Household Durables And Services_arima": "",
        "Household Durables And Services_arima_month": "",
        "Housing & Utilities_arima": "",
        "Housing & Utilities_arima_month": "",
        "Miscellaneous Goods & Services_arima": "",
        "Miscellaneous Goods & Services_arima_month": "",
        "Housing & Utilities_arima": "",
        "Housing & Utilities_arima_month": "",
        "Recreation & Culture_arima": "",
        "Recreation & Culture_arima_month": "",
        "Salary_arima": "",
        "Salary_arima_month": "",
        "Transferrables (All except housing, household, healthcare, communication, education)_arima": "",
        "Transferrables (All except housing, household, healthcare, communication, education)_arima_month": "",
        "Transport_arima": "",
        "Transport_arima_month": "",
        "SafeSavings_arima": "",
        "SafeSavings_arima_month": ""
    }
    data['sam1234'] = {
        "Name": "Sam",
	"UserID": "sam1234",
	"Balance": "64000",
	"Goal": "Car",
        "Marital status": "Married",
        "Number of dependencies": 0,
        "Transaction data file": "transactionData.csv",
        "Savings_arima": "",
        "Savings_arima_month": "",
        "Clothing & Footwear_arima": "",
        "Clothing & Footwear_arima_month": "",
        "Communication_arima": "",
        "Communication_arima_month": "",
        "Education_arima": "",
        "Education_arima_month": "",
        "Food_arima": "",
        "Food_arima_month": "",
        "Food Servicing Services_arima": "",
        "Food Servicing Services_arima_month": "",
        "Food Excl Food Servicing Services_arima": "",
        "Food Excl Food Servicing Services_arima_month": "",
        "Health Care_arima": "",
        "Health Care_arima_month": "",
        "Household Durables And Services_arima": "",
        "Household Durables And Services_arima_month": "",
        "Housing & Utilities_arima": "",
        "Housing & Utilities_arima_month": "",
        "Miscellaneous Goods & Services_arima": "",
        "Miscellaneous Goods & Services_arima_month": "",
        "Housing & Utilities_arima": "",
        "Housing & Utilities_arima_month": "",
        "Recreation & Culture_arima": "",
        "Recreation & Culture_arima_month": "",
        "Salary_arima": "",
        "Salary_arima_month": "",
        "Transferrables (All except housing, household, healthcare, communication, education)_arima": "",
        "Transferrables (All except housing, household, healthcare, communication, education)_arima_month": "",
        "Transport_arima": "",
        "Transport_arima_month": "",
        "SafeSavings_arima": "",
        "SafeSavings_arima_month": ""
    }

    with open('userdb.txt', 'w') as outfile:
        json.dump(data, outfile)

    goaldata = {}
    goaldata['Car'] = {
        "DataFile1": "coeData.csv",
	"DataFile2": "carPrices.csv",
	"DataFile3": "",
	"Arima file": "carArimaModel.pkl",
        "Arima month": ""
    }
    goaldata['House'] = {
        "DataFile1": "housePrices.csv",
	"DataFile2": "",
	"DataFile3": "",
	"Arima file": "houseArimaModel.pkl",
        "Arima month": ""
    }

    with open('goaldb.txt', 'w') as outfile:
        json.dump(goaldata, outfile)

def register():
    print("Let's be friends! But first, would you like to introduce yourself? :)\n")
    userid = input('Userid: \n')
    name = input('Name: \n')
    #balance = get from bank system
    balance = input('balance: \n')
    goal = input('Input 1 goal you would like to achieve in 5 years: \n')
    marital = input('Input marital status: \n')
    dependencies = input('Input number of dependencies: \n')
    UserDB[userid] = {
        "Name": name,
	"UserID": userid,
	"Balance": balance,
	"Goal": goal,
        "Marital status": marital,
        "Number of dependencies": dependencies,
        "Transaction data file": userid+"_transactionData.csv",
        "Savings_arima": "",
        "Savings_arima_month": "",
        "Clothing & Footwear_arima": "",
        "Clothing & Footwear_arima_month": "",
        "Communication_arima": "",
        "Communication_arima_month": "",
        "Education_arima": "",
        "Education_arima_month": "",
        "Food_arima": "",
        "Food_arima_month": "",
        "Food Servicing Services_arima": "",
        "Food Servicing Services_arima_month": "",
        "Food Excl Food Servicing Services_arima": "",
        "Food Excl Food Servicing Services_arima_month": "",
        "Health Care_arima": "",
        "Health Care_arima_month": "",
        "Household Durables And Services_arima": "",
        "Household Durables And Services_arima_month": "",
        "Housing & Utilities_arima": "",
        "Housing & Utilities_arima_month": "",
        "Miscellaneous Goods & Services_arima": "",
        "Miscellaneous Goods & Services_arima_month": "",
        "Housing & Utilities_arima": "",
        "Housing & Utilities_arima_month": "",
        "Recreation & Culture_arima": "",
        "Recreation & Culture_arima_month": "",
        "Salary_arima": "",
        "Salary_arima_month": "",
        "Transferrables (All except housing, household, healthcare, communication, education)_arima": "",
        "Transferrables (All except housing, household, healthcare, communication, education)_arima_month": "",
        "Transport_arima": "",
        "Transport_arima_month": "",
        "SafeSavings_arima": "",
        "SafeSavings_arima_month": ""
    }
    
    with open('userdb.txt', 'w') as outfile:
            json.dump(UserDB, outfile)

def testScore(train_test, model):
    y_pred = model.predict(n_periods=len(train_test))

    print('R2 Score')
    acc = metrics.r2_score(train_test.values, y_pred)
    print(acc)
    print('RMSE score')
    print(np.sqrt(metrics.mean_squared_error(train_test.values,y_pred)))



def arimaAnalysis(df, settings, fname):
    model = auto_arima(df, trace=True, start_p=settings[0], start_q=settings[1], start_P=settings[2], start_Q=settings[3],
                  max_p=40, max_q=40, max_d=40, max_P=40, max_Q=40, seasonal=settings[4], m=12, stationary=settings[5],
                  stepwise=True, suppress_warnings=True,
                  error_action='ignore',approximation = False)
    model_fit = model.fit(y=df)
    joblib.dump(model_fit,fname)
    return model_fit

def dataPrep(dataFile, category):
    #Prep transaction Data
    transData = pd.read_csv(dataFile, sep=',')
    transData['Month'] = pd.to_datetime(transData['Month'], format = '%d/%m/%Y')
    transCat = transData['Category'].unique() #list of all categories in transData
    numCat = len(transCat)

    #loading and conveting time series data by setting index as time
    transData.index = transData.Month
    transData = transData.drop('Month', axis =1)
    #transData.head()
    if (category == 'all'):
        return transData['Amount']
    return transData[transData['Category']==category]['Amount']

def categoricalAnalysis(UserDB, userid, category, n):
    fname = userid+'_'+category+'.pkl'
    catData = pd.DataFrame(dataPrep(UserDB[userid]['Transaction data file'], category))
    newest_arima = (UserDB[userid][category+"_arima_month"]==datetime.today().month)
    
    #visualizing timeseries data
    #plt.figure()
    #plt.plot(savingsData)
    #plt.xlabel('Time')
    #plt.ylabel('Amount')
    #plt.plot()
    
    #test for model accuracy
    #savingsModel = arimaAnalysis(savingsData[:-8])
    #fc = savingsModel.predict(n_periods=8)
    #print("Model accuracy:")
    #print(np.mean(np.abs(fc - savingsData.values[-8:])/np.abs(savingsData.values[-8:])))
    
    if not(newest_arima):
        #model and save
        catModel = arimaAnalysis(catData, [1,1,1,1, False, False], fname)
        #update UserDB on renewal of arima model
        UserDB[userid][category+"_arima"] = fname
        UserDB[userid][category+"_arima_month"]=datetime.today().month
        with open('userdb.txt', 'w') as outfile:
            json.dump(UserDB, outfile)
    else:
        #load previous model
        catModel = joblib.load(fname)
    #predict future
    return factorPredict(catData, catModel, n) #returns dataframe for graph output

def savingsAnalysis(UserDB, userid, n):
    fname = userid+'_Savings.pkl'
    #dataprep to get transData
    transData = dataPrep(UserDB[userid]["Transaction data file"], 'all')
    #obtain savings data
    savingsData = pd.DataFrame(transData.groupby(['Month']).sum())
    newest_arima = (UserDB[userid]["Savings_arima_month"]==datetime.today().month)
    
    #print(savingsData)
    
    #visualizing timeseries data
    #plt.figure()
    #plt.plot(savingsData)
    #plt.xlabel('Time')
    #plt.ylabel('Amount')
    #plt.plot()
    
    #test for model accuracy
    #savingsModel = arimaAnalysis(savingsData[:-8])
    #fc = savingsModel.predict(n_periods=8)
    #print("Model accuracy:")
    #print(np.mean(np.abs(fc - savingsData.values[-8:])/np.abs(savingsData.values[-8:])))

    if not(newest_arima):
        #model and save
        savingsModel = arimaAnalysis(savingsData, [1,1,1,1, False, False], fname)
        #update UserDB on renewal of arima model
        UserDB[userid]["Savings_arima"] = fname
        UserDB[userid]["Savings_arima_month"]=datetime.today().month
        with open('userdb.txt', 'w') as outfile:
            json.dump(UserDB, outfile)
    else:
        #load previous model
        savingsModel = joblib.load(fname)

    #predict future
    return factorPredict(savingsData, savingsModel, n) #returns savingsForecast dataframe for graph output

        
def factorPredict(factorData, factorModel, n):
    #predict future n years
    factor_forecast = factorModel.predict(n_periods=(n*12))
    indexList = pd.date_range(start=factorData.index[len(factorData)-1], periods=(n*12), freq='M')
    factor_forecast = pd.DataFrame(factor_forecast,index = indexList,columns=['Amount'])
    
    return pd.concat([factorData,factor_forecast]); #return dataframe for graph output

def goalPlanner(goal, savingsForecast, goalDB):    
    if (goal=='Car'):
        #COE price
        coeData = pd.read_csv("coeData.csv", sep=',')
        coeData['month'] = pd.to_datetime(coeData['month'], format = '%Y-%m')
        #consider most common category A vehicles.
        coeData = coeData[coeData['vehicle_class']=='Category A']
        coeData = pd.DataFrame(coeData.groupby(['month']).sum())
        coeData = coeData.drop(['bidding_no', 'quota', 'bids_success', 'bids_received'], axis=1)

        if (goalDB['Car']["Arima month"]!=datetime.today().month):
            #arima analysis
            coeArima = arimaAnalysis(coeData, [7,0,2,0,False,True], "carArimaModel.pkl")
            #update goalDB on renewal of arima model
            goalDB['Car']['Arima file'] = "carArimaModel.pkl"
            goalDB['Car']['Arima month'] = datetime.today().month
            with open('goaldb.txt', 'w') as outfile:
                json.dump(goalDB, outfile)
        else: #if not just load prev model
            coeArima = joblib.load(goalDB['Car']['Arima file'])
        
        #predict future n years
        n=5
        coe_forecast = coeArima.predict(n_periods=(n*12))
        indexList = pd.date_range(start=coeData.index[len(coeData)-1], periods=n*12, freq='M')
        coe_forecast = pd.DataFrame(coe_forecast,index = indexList,columns=['premium'])
        #print(coe_forecast)

        #coe price after 5 years
        fcstcoe_price = coe_forecast['premium'][len(coe_forecast)-1]
        #print(fcstcoe_price)

        #CAR price
        carData = pd.read_csv('carPrices.csv', sep=',')
        est_car_price = carData['MSRP'].mean()
        #print(est_car_price)

        est_total_Price = fcstcoe_price+est_car_price
        return est_total_Price

# Import LocalOutlierFactor from sklearn.neighbors
from sklearn.neighbors import LocalOutlierFactor

def checkfactorRaise(df, change_in_val):
    if (abs(df['Amount'][len(df)-2]-df['Amount'][len(df)-1])>change_in_val):
        return True;
    return False;
        
        
def payByInstalment(savingsForecast, est_total_Price, numOfYears):
    #assume 20-year instalment
    monthlyPrice = est_total_Price/(numOfYears*12)
    #print(monthlyPrice)

    savingsForecast["Amount"]-=monthlyPrice

    aft_5_yrs = date(date.today().year+5,date.today().month-1,calendar.monthrange(date.today().year,date.today().month-1)[1])
    aft_numOfYears_yrs = date(date.today().year+5+numOfYears,date.today().month-1,calendar.monthrange(date.today().year,date.today().month-1)[1])
    
    #print(savingsForecast)
    return savingsForecast[aft_5_yrs:aft_numOfYears_yrs];
    

if __name__ == '__main__':
    #dataPrep('transactionData.csv')
    carGoalPlanner()
