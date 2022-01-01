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
    
    print('\n')
    print('-'*50)
    print('\n\nUF Machine Learning')
    selection = input('''Enter 1 to train.
Enter 2 to test
Enter 3 to predict
Enter Q to quit

''')

    # If training, program will ask for desired accuracy and keep trying until
    # that accuracy target is met or after a certain number of tries
    # Still need to add a stopping point for if it can't meet accuracy
    if selection == '1':
        training_set = input('Please enter path to training dataset: ')
        accuracy = int(input('Enter Desired Accuracy: '))
        training.main(accuracy, training_set)
        #break
    
    # If testing, program asks for location of testing set and weights found from 
    # training module
    # Then it will output the accuracy achieved with set weights
    elif selection == '2':
        testing.main()

    
    
    elif selection == 'Q' or selection == 'q':
        print('\n\nThank you for using UF Machine Learning')
        break
    
    
    else:
        print('\n\nCommand Not Recognized')
