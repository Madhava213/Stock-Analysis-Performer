#%%
from nsepy import get_history
import datetime 
import dateutil.relativedelta
#Stock history
now = datetime.datetime.now().date()
month_before = now + dateutil.relativedelta.relativedelta(months=-1)

while True:
    user_input = input("Enter something:")
    if user_input == "q":
        break
    stock = get_history(symbol=user_input,
                        start=datetime.date(month_before.year,month_before.month,month_before.day), 
                        end=datetime.date(now.today().year,now.today().month,now.today().day))
    print(stock)
    HI_values = []
    LO_values = []
    CL_values = []
    P_val = []
    P_plus_val = []
    P_min_val = []
    R_one_val = []
    R_two_val = []
    S_one_val = []
    S_two_val = []
    percent_val = []
    for i in range(0,len(stock)):
        HI = round(stock['High'][i] - stock['Open'][i],3)
        LO = round(stock['Open'][i] - stock['Low'][i],3)
        CL = round(stock['Close'][i] - stock['Open'][i],3)
        P = round((stock['High'][i] + stock['Low'][i] + stock['Close'][i])/3,3)
        P_plus = round(P + (P-((stock['High'][i] + stock['Low'][i] )/2)),3)
        P_min = round(P - (P-((stock['High'][i] + stock['Low'][i] )/2)),3)
        R_one = round((P*2) - stock['Low'][i],3)
        S_one = round((P*2) - stock['High'][i],3)
        R_two = round(P + (stock['High'][i] - stock['Low'][i] ),3)
        S_two = round(P - (stock['High'][i] - stock['Low'][i] ),3)
        percent = round(((stock['Prev Close'][i] - stock['Close'][i] )/stock["Prev Close"][i]) * 100,3)
        HI_values.append(HI)
        LO_values.append(LO)
        CL_values.append(CL)
        P_val.append(P)
        P_plus_val.append(P_plus)
        P_min_val.append(P_min)
        R_one_val.append(R_one)
        R_two_val.append(R_two)
        S_one_val.append(S_one)
        S_two_val.append(S_two)
        percent_val.append(percent)
    stock['HI'] = HI_values
    stock['LO'] = LO_values
    stock['CL'] = CL_values
    stock['PER'] = percent_val
    stock['P'] = P_val
    stock['P+'] = P_plus_val
    stock['P-'] = P_min_val
    stock['R1'] = R_one_val
    stock['R2'] = R_two_val
    stock['S1'] = S_one_val
    stock['S2'] = S_two_val
    stock.to_csv(str(user_input) + ".csv")

# %%
