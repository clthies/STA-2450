# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:06:35 2021

@author: cac61
"""
#simulations for a hyp test (t test)

import numpy as np
from scipy.stats import ttest_1samp



# v1 = np.random.normal(mean = 10, sd = 25, size=100)
# v2 = np.random.normal(mean = 10, sd = 25, size=100)

# res1 = ttest_ind(v1, v2)
# res2 = ttest_ind(v1, v2).pvalue
# print(res1)
# print(res2)

alpha = 0.05
N = 30

#sim data from this
#x == norm(10, 25)

#take this data and do a t test

#determine p-value (how many are below 0.05)
#be able to tell what to sample from

#data = normal_dist(x, mean = 10, sd = 25, size = N)

class CISims:
    """for generating t confidence intervals"""
    def __init__(self, distribution, dist_params, true_mean, conf_level = [1-alpha]):
        """initialize the simulations"""
        
        self.sim_func = distribution
        self.dist_params = dist_params
        self.mu = true_mean
        self.p_val = []  
        
    def update(self, n_sims):
        """conduct n_sims more simulations"""
        
        
        for i in range(n_sims):
            
            #simulate the data from the given distribution
            dat = self.sim_func(**self.dist_params)
            
            
            
            #find T-interval
            res = ttest_1samp(dat, 10)
            res_p = res.pvalue
            
            self.p_val.append(res_p)
            print(res_p)
            print(res)
            
param_dict = dict(loc = 10, scale=5, size = 30)
my_sims = CISims(np.random.normal, param_dict, 10, "")
my_sims.update(100)
            
        #     #find the statsitics
        #     xbar = np.mean(dat)
        #     s = np.std(dat)
            
        #     #find the t critical value
        #     t_cv = stats.t.ppf(1-self.alpha/2, len(dat)-1)
            
        #     #calculate the confidence interval
        #     ll = xbar - t_cv*s/np.sqrt(len(dat))
        #     ul = xbar + t_cv*s/np.sqrt(len(dat))
        
        
        
        # v1 = np.random.normal(mean = 10, sd = 25, size=100)
        # v2 = np.random.normal(mean = 10, sd = 25, size=100)
        
        
    
        # #if conf_level is a string, catch and use the default value
        # try:
        #     if conf_level <=0 or conf_level>= 1:
        #         print("Make sure your confidence level is between 0 and 1.")
        #         print("Using a .95 confidence level by default")
        #         self.alpha = 0.05
        #     else:
        #         self.alpha = 1-conf_level
        # except TypeError:
        #     print("Make sure your confidence level is between 0 and 1.")
        #     print("Using a .95 confidence level by default")
        #     self.alpha = 0.05
            
    
    
   
    