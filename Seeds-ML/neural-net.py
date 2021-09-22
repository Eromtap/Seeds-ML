


import csv
import random
from playsound import playsound

csv_file = 'testing-100.csv'

row_count = sum(1 for line in open(csv_file))

desired_accuracy = 0
percentage = desired_accuracy / 100

counter = 0

for i in range (100_000):
    
    
    ## just a counter to keep track of our correct predictions
    
    correct = 0

    
    
    '''
    Below is the node and weight section. The first section where nodes equal a random number between -1 and 1
    is used to let the machine try random weights until a satisfactory set is found
    
    The next block is to copy and paste the weights to give them static values.
    basically comment out one block to use the other. It's ugly, but it works
    
    As you can see, I abandoned my idea of incrementing the weights. This works
    too well using random weights for me to bother with incrementing. I still
    think it could be a good idea and will be exploring it more
    
    
    '''
    
    
    
    # Block for generating random weights, comment out to use static ##############
    '''
    found that by narrowing down ranges when a decent accuracy is found, we can improve it and greatly speed up
    searches. So when a weight (just using one, but apply to all) like 0.09354299, change the range to 0 - 1 or even 
    0 - .1. If negative, do the reverse. So -.08473 means change search range to -1 to 0 or like -.9 - 0. basically, 
    0 to something a tiny bit further from zero than the current weight. We need to figure out how to do this
    
    or maybe narrowing it down even further so like .4 - .9 and keep stepping closer and closer. 
    
    OK, when we get too close, it stops improving I've noticed'
    
    we also need to increase the desired accuracy in the background. So maybe start at 10% less than the users
    desired accuracy and slowly increase until we hit it. If we never hit it, we need a way to stop and print the
    weights that got the best results. Or just lower user accuracy and start again
    
    this way, weights can actually end up going outside the range we set, I think thats a good thing
    
    when we fail a certain number of times, increase range by .1 in either direction, do not increase 
    accuracy threshold and try again. If we hit target, go back to weights + and - 2 on new weights and .4 range again
    
    increase the target up to the correct percentage so we dont do unneccesary loops. so if our target is 65 and 
    we get 69, the new target should be 69
    
    
    if it never hits target, we need to print best outcome after x amount of tries
    
    
    lower accuracy target when we have to expande range
    
    could be a good idea to alter one node at a time once we get close, not sure though
    
    I think best range is current weight + .1 and current weight - .1. no a .2 range, then it increases 
    if no btr weights found as described above
    
    '''
    
    # area_node = random.uniform(-1, 1)
    # perm_node = random.uniform(-1, 1)
    # comp_node = random.uniform(-1, 1)
    # len_node = random.uniform(-1, 1)
    # wid_node = random.uniform(-1, 1)
    # asym_node = random.uniform(-1, 1)
    # groo_node = random.uniform(-1, 1)
    
    
    # below is after a bunch of iterations and narrowing it down
    
    
    # area_node = random.uniform(1.1, 1.3)
    # perm_node = random.uniform(-1.2, -1)
    # comp_node = random.uniform(-.3, -.1)
    # len_node = random.uniform(-.3, -.1)
    # wid_node = random.uniform(-.8, -.6)
    # asym_node = random.uniform(-.2, 0)
    # groo_node = random.uniform(-.1, .1)
    
    
#round(random.uniform(-1, 1), 5)
    
#random.uniform(-1, 1)

    
    
    # Block for setting static weights, comment out to use random ##################
    
    #93.94% with these weights in training. 87% on test-100 and 90.45% on whole set, not too bad
    
    area_node =  1.2620326505948167     
    perm_node =  -1.027798307903441 
    comp_node =  -0.22918149070703575 
    len_node =  -0.24935475131119084 
    wid_node =  -0.791618183038666 
    asym_node =  -0.16138564674085215 
    groo_node =  0.0786410795871553

        

        
        
        
     ## Giant space so the blocks where you're supposed to tinker around are nice and far from other stuff   
        
        
        
        
        
        
        

    # func to add up weighted nodes and input values    
    def nodes(s_area, s_perm, s_comp, s_len, s_wid, s_asym, s_groo):
        
        bias = 1

        return (s_area * area_node) + (s_perm * perm_node) \
            + (s_comp * comp_node) + (s_len * len_node) \
            + (s_wid * wid_node) + (s_asym  * asym_node) \
            + (s_groo * groo_node) + bias
            

    
    ## Pretty straight forward here, open the csv file and assign the values
    ## of length, width, etc to variables and call the nodes func to do the 
    ## math. Then assign a prediction based on the range the result 
    ## falls into. Change the file name to switch between training and test sets
    
    with open(csv_file) as file:
        
        csv_reader = csv.reader(file, delimiter=',')
        
        for row in csv_reader: 
            s_area = float(row[0])
            s_perm = float(row[1])
            s_comp = float(row[2])
            s_len = float(row[3])
            s_wid = float(row[4])
            s_asym = float(row[5])
            s_groo = float(row[6])
            
            species = row[7]
            
            #this block is where the species values matter
            
            if nodes(s_area, s_perm, s_comp, s_len, s_wid, s_asym, s_groo) >= 1:  
                prediction = '2'
            elif nodes(s_area, s_perm, s_comp, s_len, s_wid, s_asym, s_groo) < 1\
                and nodes(s_area, s_perm, s_comp, s_len, s_wid, s_asym, s_groo) > -1:
                    prediction = '1'
            elif nodes(s_area, s_perm, s_comp, s_len, s_wid, s_asym, s_groo) <= -1:#\
                #and nodes(s_area, s_perm, s_comp, s_len, s_wid, s_asym, s_groo) > -1:
                prediction = '3'
                
            else:
                prediction = ''
            
            if prediction == species:
                correct += 1
                #print(row, 'correct')
                
            else:
                answer = ''
                #print(row, prediction, 'Wrogng***************')

    counter += 1
            
     
    if correct / (row_count) > percentage: ## this guy right here, change this num to adjust accuracy target
        break
    

print(round((correct / row_count) * 100, 2), 'percent accuracy', '\n\narea_node = ', area_node, '\nperm_node = ', perm_node, '\ncomp_node = ', comp_node, 
      '\nlen_node = ', len_node, '\nwid_node = ', wid_node, '\nasym_node = ', asym_node,
      '\ngroo_node = ', groo_node)


print(counter)


# while 1:
#     playsound('ding.mp3')
















'''

I think we can do this by creating a few functions. the first function uses random weights and calls the main loop
then once it terminates, if we hit our accuracy, we call the same function with set weights in the appropriate range. 
Rinse and repeat. 

If it doesnt hit accuracy, we use the new larger range and run again till we hit our target. I really think 
this can work!!

IDK what you would call this sort of random selections inside set ranges that change, but it is an algorithm!

We can also make this more dynamic and use command args. I'd like to turn this into a library that could be 
used for multiple different datasets easily

'''



















