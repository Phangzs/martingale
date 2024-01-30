""""""
"""Assess a betting strategy.  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		   	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		   	 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		   	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		   	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		   	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		   	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		   	 		  		  		    	 		 		   		 		  
or edited.  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		   	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		   	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		   	 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		   	 		  		  		    	 		 		   		 		  
  		  	   		   	 		  		  		    	 		 		   		 		  
Student Name: N/A (replace with your name)  		  	   		   	 		  		  		    	 		 		   		 		  
GT User ID: N/A (replace with your User ID)  		  	   		   	 		  		  		    	 		 		   		 		  
GT ID: -1 (replace with your GT ID)  		  	   		   	 		  		  		    	 		 		   		 		  
"""

# Copied from Georgia Tech to exercise skills. I just completed the template

import numpy as np
import matplotlib.pyplot as plt

def author():
    """  		  	   		   	 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		   	 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		   	 		  		  		    	 		 		   		 		  
    """
    return "N/A"  # replace tb34 with your Georgia Tech username.


def gtid():
    """  		  	   		   	 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		   	 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		   	 		  		  		    	 		 		   		 		  
    """
    return -1  # replace with your GT ID number


def get_spin_result(win_prob):
    """  		  	   		   	 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		   	 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning
    :type win_prob: float  		  	   		   	 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		   	 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		   	 		  		  		    	 		 		   		 		  
    """
    result = False
    if np.random.random() <= win_prob:
        result = True
    return result


def erik_function(win, money=float("inf")):
    total_winnings = 0
    winnings = [0]
    while -money < total_winnings < 80 and len(winnings) < 1001:
        won = False
        bet_amount = 1
        while not won:
            won = get_spin_result(win)
            if won:
                total_winnings += bet_amount
            else:
                total_winnings -= bet_amount
                bet_amount = min(bet_amount*2, total_winnings + money)
            winnings.append(total_winnings)
    while len(winnings) < 1001:
        winnings.append(total_winnings)
    return np.array(winnings)


def initialize_plot():
    plt.figure(figsize=(16, 9))
    plt.xlim((0, 300))
    plt.ylim((-256, 100))
    plt.xlabel("Spin")
    plt.ylabel("Earnings")



def test_code():
    """  		  	   		   	 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		   	 		  		  		    	 		 		   		 		  
    """
    win_prob = 0.4737  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    print(get_spin_result(win_prob))  # test the roulette spin
    # add your code here to implement the experiments
    #Figure 1
    initialize_plot()
    for _ in range(10):
        array = erik_function(win_prob, 256)
        plt.plot(array)
    plt.show()
    #Figure 2
    table = []
    for _ in range(1000):
        array = erik_function(win_prob, 256)
        table.append(array)
    table = np.array(table)

    means = np.mean(table, axis=0)
    medians = np.median(table, axis=0)
    stds = np.std(table, axis=0)
    means_upper = means + stds
    means_lower = means - stds
    medians_upper = medians + stds
    medians_lower = medians - stds
    initialize_plot()
    plt.plot(means)
    plt.plot(means_upper)
    plt.plot(means_lower)
    plt.fill_between(np.arange(len(means)), means_upper, means_lower, alpha=0.3, color="grey")
    plt.show()
    initialize_plot()
    plt.plot(medians)
    plt.plot(medians_upper)
    plt.plot(medians_lower)
    plt.show()

if __name__ == "__main__":
    test_code()
