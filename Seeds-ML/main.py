'''

-UF stands for User Friendly

-This will be the main script that contains the UI and calls other modules

-May put import data func into this script so we arent utilizing multiple times

-Need to set training attempt limit. Maybe we let user define like num in millions attempts

-If desired accuracy not achieved after num of attempts, print something like
oops, i failed, best i could get is (accuracy). Would you like to try again, or
Save the best values I found.

-Weights and nodes need to be saved to a file (possibly csv) for use with the testing and predicting
modules

-Also, if we really want this to be truly User Friendly, we need to make this a 
gui application
'''


import training 



while 1:
    
    
    print('UF Machine Learning')
    selection = input('''Enter 1 to train.
Enter 2 to test
Enter 3 to predict

''')
    if selection == '1':
        
        training.main()
        break
