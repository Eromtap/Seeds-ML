'''

-UF stands for User Friendly

-This will be the main script that contains the UI and calls other modules

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