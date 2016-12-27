# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 13:58:04 2016

@author: Jediyanu Wigas Tu'u
"""

import gaussElimination
import numpy as np
"""
a = np.array([[4,-2,1,11],
             [-2,4,-2,-16],
             [1,-2,4,17]]
)
"""
a = np.array([[4,8,4,80],
             [2,1,-4,7],
             [3,-1,2,22]]
)
result = gaussElimination.gaussElimination(a)
print "the result is" ,result