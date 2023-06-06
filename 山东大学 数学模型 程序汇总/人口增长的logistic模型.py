import numpy as np
from scipy.optimize import curve_fit
def logistic_model(t,r,K):
    return K/(1+(K/p0-1)*np.exp(-r*t))
N=int(input().strip())
populations=list(map(int,input().strip().split()))
T=int(input().strip())
years_to_predict=[int(input().strip())for _ in range(T)]
p0=populations[0]
t=np.arange(0,N)
initial_guess=[0.03,400]
params, _ = curve_fit(logistic_model,t,populations,p0=initial_guess,maxfev=10000)
r,K=params
predictions=[]
for year in years_to_predict:
    prediction=logistic_model(year,r,K)
    predictions.append(prediction)
for pred in predictions:
    print(f"{pred:.2f}")
