'''
Author: Kristine Petersen
This programme tests a compound interest calculator
Version: 1.0
'''

# comments to be added like this

#need to call the calc file as an imported file

from calc import monthly_compound

# tautology are words that mean the same thing e.g. rules are rules. no need to say it twice
def test_tautology():
    assert 3 == 2 + 1

#if we invest nothing what will we end up with

def test_zeros_in_zeros_out():
    #establish input values
    
    initial = 0
    monthly = 0
    annual_rate = 0
    years = 0
# calculate an output
    final_sum = monthly_compound(initial, monthly, annual_rate, years)
    assert final_sum == 0
    
#if we enter annual rate of 0, inputting £100 a month for 10 years what do we get
def test_cash():
    #establish input values
    
    initial = 1000
    monthly = 100
    annual_rate = 0
    years = 1
# calculate an output
    final_sum = monthly_compound(initial, monthly, annual_rate, years)
    assert final_sum == 2200

# this does not work if we have a calc that says our return is the same as initial
# changing this to be a beter calculation would work


# create a new test 
def test_interest_rate():
    #establish input values
    
    initial = 1000
    monthly = 100
    annual_rate = 12
    years = 1/12
# calculate an output
    final_sum = monthly_compound(initial, monthly, annual_rate, years)
    assert final_sum == 1110
    