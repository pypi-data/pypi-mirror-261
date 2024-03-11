def libraries():
    print("""

import seaborn as sns
from sklearn.preprocessing import scale
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import scipy.stats as stats
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np
import pandas as pd
from  statsmodels.api import stats  as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.stats.multicomp as mc
from statsmodels.stats.proportion import proportions_ztest as prop
from scipy import stats
from statsmodels.multivariate.manova import MANOVA 
import cv2
""")


def anova():
    print(
        """
Notes: Check the null values and the datatypes of the columns

Step 1: Check the paramteres that we take ahead
    fit1=ols("X~Y",data=df).fit()
    two_anova=sm.stats.anova_lm(fit1,typ=1/2)
    two_anova=pd.DataFrame(two_anova)
    two_anova=two_anova[two_anova["PR(>F)"]<0.05]
    names=two_anova.index().tolist()

Step 2: Comparison
    pair=mc.MultiComparison(df[Basis],Values in names with +)
    test=pair.tukeyhsd().summary()
    test
    df=pd.DataFrame(test)
    df=df[1:]
    df=df[df[6]=="True"]

Step 3: T-Testing
    df1 = df[(df['Student']=='No')&(df['Cards']=='2')]
    df2 = df[(df['Student']=='No')&(df['Cards']=='2')]
    print(stats.ttest_ind(df1[Basis]],df2[Basis],equal_var=True,alternative='greater'))
        """  
    )

def  manova():
    print(
        """
Step 1: Checking the parameters to take ahead
    MANOVA.from_formula(f"Parameters(with '+')~AllColsToCheck",data=df).mv_test().summary()

Step 2: Filtering out
    cols= All the values <0.05
    for column in target values:
        print(f'Column : target Value')
        eq = ols(f'Target Value~Cols_with_*',data=df).fit()
        summarydf = sm.anova_lm(eq,typ=2)
        display(summarydf[summarydf['PR(>F)']<0.05].sort_values(by='PR(>F)')) 
        
Step 3: Getting the True Values
    a1=mc.MultiComparison(df["Value_In_Target_Variables"],df[Column Values in Addition]).tukeyhsd().summary()
    a1=pd.DataFrame(a1)
    a1=a1.tail(-1)
    a1[6]=a1[6].astype(str)
    a1=a1[a1[6]=="True"]
    a1

        """
    )
    
def LinearRegression():
    print(
    """
Step 1: Check the graphs to see which is most linear
    sns.pairplot(df)

Step 2: Get the Line
    sns.regplot(data=df1,x=,y=)
    
Step 3: Checking the Linearity of single variable
    def linearity_checker(df,parameter,order=7):
        eq = ols(f'Balance~{parameter}',data=df).fit()
        print(eq.summary())
        dfc = df.copy()
        for i in range(2,order):
            print(f'Order : {i}')
            dfc[f'{parameter}{i}'] = pow(dfc[f'{parameter}'], int(i))
            eq = ols(f'Balance~{parameter}{i}',data=dfc).fit()
            print(eq.summary())
            
Step 4: Filtering
    eq = ols('Balance~Sum_of_all_cols',data=df).fit()
    eq.summary()
    #Take the values less than 0.05

Step 5: Filtering
    eq = ols('Balance~Product_of_all_cols',data=df).fit()
    eq.summary()
    #Take the values less than 0.05
    
Step 6: Final Step
    eq = ols('Balance~Sum&Prod_of_all_cols',data=df).fit()
    eq.summary()
    #Take the values less than 0.05
    """
    )
    
    
def QualityAnalysis():
    print(
    """
successrate= #Calculated success rate
phat= # Needed number of success/population
population=
alpha=
sides="two-sided"/"larger"/"smaller"

# Manual (Use this preferably)
zvalL= stats.norm.ppf((alpha/2),0,1)
zvalR= stats.norm.ppf(1-(alpha/2),0,1)
zcal=(phat-successrate)/(np.sqrt((1-successrate)*successrate/population))
print(f"Calculated zval={zcal}")

# Trained Library
if (prop(count=(phat),nobs=population,value=successrate,alternative=sides)[1]<alpha):
    print("Rejected by pre trained library")
else:
    print("Accepted by pretrained library")
    """
    )