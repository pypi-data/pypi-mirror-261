def libraries():
    print("""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.stats.multicomp as mc
from scipy import stats
from statsmodels.multivariate.manova import MANOVA 
import cv2
import seaborn as sns
import matplotlib.pyplot as plt
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
    MANOVA.from_formula(f"A+B~AllColsToCheck",data=df).mv_test().summary()

Step 2: Other than intercept, Take all those that have Pval<0.05 and continue with Anova
    pair=mc.MultiComparison(df[Basis1]+df[basis2],Values in names with +)   
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
    