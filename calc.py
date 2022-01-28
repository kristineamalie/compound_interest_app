'''
Athor: Kristine Petersen
calculator named monthly compound function for our app
'''

def monthly_compound(initial, monthly, annual_rate, years):
    
    final_sum = initial
    months = years * 12

    for month in range(int(months)):
        final_sum = final_sum*(1 + annual_rate/1200) + monthly
    
    return final_sum