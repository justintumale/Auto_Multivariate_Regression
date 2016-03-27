import pandas as pd
import statsmodels.api as sm


df = pd.read_excel('TRAININGFILE_HackGSU_MidnightMadness.xlsx')

X = df[['GDP Per Capita (USD)', 'Youth unemployment rate (%)', 'Energy Production (Quadrillion Btu)', 'High-technology exports (current US$)']]
y = df[['Electric power consumption (kWh per capita)']]

#create a model that uses ordinary least squares and fits it
x1 = sm.add_constant(X)
est = sm.OLS(y, x1).fit()
print(est.summary())

'''
#method that calculates the prediction using the coefficients obtained from the results of the model
def formulate(gdp, youth_unemployment_rate, energy_prod, hi_tech_exports):
    const = 13720
    c_gdp = 0.0549
    c_yur = -54.5982
    c_ep = 194.7173
    c_ht = -.00000009256

    return const + c_gdp*gdp+ c_yur*youth_unemployment_rate + c_ep*energy_prod + c_ht*hi_tech_exports

def Main():
    print(formulate(25980.22038, 10.60000038, 11.16134, 71648946915))

if __name__ == '__main__':
    Main()
'''



