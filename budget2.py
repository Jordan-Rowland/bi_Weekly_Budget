import os, sys

os.chdir('D:\\Documents\\Budget\\')

def budget(check, date):
    # Monthly expenses, flat fees are divided by 2 for bi-weekly paychecks
    outcome = {'Rent': 850 / 2, 'Utilities': 100 / 2,
               'Therapy': 120 / 2, 'Healthcare': 100 / 2,
               'Groceries/Food': check * .05, 'Transportation': 50,
               'Entertainment': check * .08, 'Savings': check * .1}
    vAdjust = 0

    # Loops through items in budget, prints each one, the shows total cost, and replaining budget
    print('Check: $' + str(check) + ' -- Date: ' + str(date) + '\n')
    for k, v in outcome.items():
        vAdjust += v
        print(k + ': ' + str(v))
    
    print('\n' + 'Total Cost: ' + str(vAdjust) + '\n')
    print('Remaining Funds: ' + str(check - vAdjust))


    # Prints to Budget.txt file
    sys.stdout=open("budget.txt","a")

    vAdjust = 0
    
    print('Check: $' + str(check) + ' -- Date: ' + str(date) + '\n')
    for k, v in outcome.items():
        vAdjust += v
        print(k + ': ' + str(v))
    
    print('\n' + 'Total Cost: ' + str(vAdjust) + '\n')
    print('Remaining Funds: ' + str(check - vAdjust) + '\n\n')

    sys.stdout.close()

# Call functions
budget(1380, 'Mar-19')
