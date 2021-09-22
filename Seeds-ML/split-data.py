
# -*- coding: utf-8 -*-


"""
-Here split the dataset into training and test sets 

-dataset contains 3 different subspieces of iris with 50 samples each.

-each sample has the measurements of flower sepal length, sepal width and petal
 width
 
-these measurements will be used to differentiate the subspecies

-we will be using 100 random samples as our training set, then the remaining 50
 as a test set
                                                     

"""

import csv
import random



row_count = sum(1 for line in open('seeds.csv'))
# print(row_count)






def main():
    
    row_count = sum(1 for line in open('seeds.csv'))
    
    
    seed_dict = {}
    train_set = {}
    test_set = {}
    
    
    ## open dataset and create dict from all rows
    
    with open('seeds.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
            
        # for i in enumerate(file, start=-1):
        #     if 'Area' in i:
        #         pass
        #     else:
        #         seed_dict[i[0]] = i[1:]
                
        # del seed_dict[-1]
        
        indexer = 0
        
        for row in csv_reader: 
            if indexer  != 0:
                seed_dict[indexer] = row
            indexer += 1

                
    
        print('seed_dict')
        print(len(seed_dict))
        
        
        

    ## create training set dict
    
    key_list = []
    

    
    while len(key_list) < (row_count - 2) // 2:
        selection = random.randint(1, row_count-2)
        if selection not in key_list:
            train_set[selection] = seed_dict[selection]
            key_list.append(selection)
    
    print('train_set')
    print(len(train_set))
            
# #     ## create then randomize test dict
    
    for k, v in seed_dict.items():
        if k not in key_list:
            test_set[k] = v
    
    test_list = list(test_set.items())
    random.shuffle(test_list)
    test_set = {}
    for i in test_list:
        key = i[0]
        value = i[1]
        test_set[key] = value
        
    print('test_set')
    print(len(test_set))
    
    
# #     ## create training set csv from training set dict
    
    with open('training.csv', 'w', newline='') as training_file:
        writer = csv.writer(training_file, delimiter=',')
        
        for k, v in train_set.items():
            writer.writerow(v)
    
    
    
    
#     ## create test set csv from test set dict
    
    with open('testing.csv', 'w', newline='') as testing_file:
        writer = csv.writer(testing_file, delimiter=',')
        
        for k, v in test_set.items():
            writer.writerow(v)



if __name__ == '__main__':
    main()











