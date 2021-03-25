# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:45:57 2021

@author: cac61
"""

from scipy import stats

class HTSims:
    """simulations for testing one sample"""
    
    def __init__(self):
        """initializes the class"""
        self.pvalues = []
        self.result = []
        
    def update(self, n_sims):
        """simulate the data and perform t-test"""
        
        for i in range(n_sims):
            dat = stats.norm.rvs(loc=10, scale=5, size=30)
            result = stats.ttest_1samp(dat,10)
            self.pvalues.append(result.pvalue)
            
    def print_pvalues(self):
        """print the pvalues list"""
        print(self.pvalues)
        
    def proportion(self, n_sims):
        
        for i in range(n_sims):
            pvalue = self.pvalues
            if pvalue[i] >= 0.05:
               self.result.append(0)
            else:
                self.result.append(1)
            
            
        print((sum(self.result))/n_sims)   
        
        
my_sims = HTSims()
my_sims.update(10000)
my_sims.print_pvalues()
my_sims.proportion(10000)


#Find out how often we will reject the null hypothesis
#Then use a GUI

