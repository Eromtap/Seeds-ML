'''
This is going to be the dynamic version of the training module
'''


def main(accuracy, training_set):    
    import csv
    import random
    
    '''
    
    -This ML program uses each input of a dataset as it's own weighted node.
    
    -It starts with random weights somewhere in range -1 to 1
    
    -It then runs with these weights (changing them on each iteration, but same range) 
    until one of three things happens:
        -it finds the level of accuracy the user desires
        -it finds an acceptable accuracy then narrows the ranges to search a smaller
        range for better weights
        -it doesnt find the desired accuracy or an acceptable accuracy 
        after a certain amount of iterations and extends the search ranges.
        
    -This process repeats until desired accuracy is found, or, after a certain
    number of tries, program terminates and gives user the best accuracy it could find
    
    -Upon completion, program prints accuracy attained, weights used and number of iterations
        
    
    
    
    ----------------------THOUGHTS ON IMPORVING PROJECT----------------------------
    
    -We need to add the functionality that ends program if it can't attain desired 
    accuracy. 
    
    -We need to make this dynamic. I'd like to create an actual useable library or module
    
    -This will require program to make it's own dict categories given a csv file
    that has an unknown num of inputs IE unknow num of rows
    
    -It will also have to come up with the ranges for each output.
    for instance, this version uses <-1, >-1 <1 and >1. If there are more or fewer 
    than 3 possible output values, these ranges will need to be changed obviously.
    
    -Maybe it can scan the last colunm of the csv and decide how many different 
    prediction outputs there should be. then divide the -1 to 1 range accordingly
    
    -One issue I found is that if the different outputs are put in the wrong range,
    it will give unsatisfactory results. I had to switch outputs 1 and 2 to get 
    btr accuracy with this version. 
    
    -Maybe in addition to changing weights, we need to have it automatically 
    change output ranges if acceptable accuracy isnt found
    
    -Then when program terms, it shoud also print out the appropriate ranges for each
    output category
    
    -It also needs to have a training and testing function.
    
    -So if user requests training, it searches weights and ranges as described above.
    
    -If user requests testing, it uses weights and ranges saved to some file to perform predictions
    
    -So that means training inputs, weights and output ranges need to be saved to a file
    
    -Then it will have to read this file for testing.
    
    -Ultimate goal:
        -User has dataset as csv file
        -User starts program, it asks if they are training, testing or predicitng unknown
        -If training, program asks for dataset csv name (full path or relative)
        -Program asks for desired accuracy
        -Program splits set into training set and testing sets. (needs to ask how large traing set should be
            probably by displaying number of rows in csv and asking user to choose a training amount)
        -Program trains and displays weights, accuracy and output ranges
        -It also saves this output to file for testing
        -User restarts program and instead chooses testing
        -User inputs testing csv path and file that contains training output
        -It then uses this output to test and outputs accuracy results
        -We also need a function for predicting on a set without known outputs.
        -So basically a dataset with the inputs but no known outputs to compare
        -This is the whole purpose afterall, predicting unknowns. 
        -This function would work basically the same as the test function,
            except it doesn't check preditcions after each iterations, just outputs
            those predictions, or saves them in some way. Plotting, csv etc
            
    -All these functions can easily be different modules called from the main.py
    
    -Possible GUI using Tkinter
    
    -May have CLI and GUI client, that would be neat
    
    -For creating dict automagically, probably need to go into OOP
    
    -Create class instance for each input maybe, then when no more inputs,
    use these class instances to create the dict.
    
    -Luckily, the names are meaningless in this case, they could just be node1, node2 etc.
    
    
    ----------------------THOUGHTS ON EXPANDING ALGORITHM--------------------------
    
    -So far, this is only useful with datasets that have numeric values like
    csv files. How do we expand this to other types of datasets? Like pictures,
    sounds etc.
    
    -Pixels can be given weights, so there would be an input for each pixel,
    how do we do this?
    
    -Handwriting would be similar to pictures, but fewer inputs (pixels) obv.
    
    -How does an ML algorithm deal with pixels that are not really part of the object?
    like background grass or sky???
    
    -Would need to add functionality to import data from files other than csv
    
    -Why do more complicated algorithms need multiple layers with more nodes?
    There must be a reason, but as well as this works, I can't see it....Need
    to find the reason and figure out if this is as good (or close) as those
    
    -If we achieve a lvl of accuracy close to that of more complicated algorithms,
    I'd say we are doing well. This uses much less computational power than 
    many of those....I think it does at least.
    
    '''
    
    
    
    
    ## Csv file we want to use for training or testing
    csv_file = training_set
    
    ## Number of rows in csv file used for calculating accuracy
    row_count = sum(1 for line in open(csv_file))
    
    
    ## Accuracy we want to achieve, can be changed to anything below 100
    desired_accuracy = accuracy
    
    percentage = desired_accuracy / 100
    
    ## Lower percentage target to hit. This is increased as we hit it until
    ## we hit main target
    temp_percentage = percentage - .2
    
    
    ## Just how many iterations we've gone thru
    counter = 1
    
    
    ## Amount we extend range if accuracy target not achieved
    ## Increased when we need to extend range
    range_counter = .1
    
    
    ## Dict we create from the csv file
    data = {}
    
    
    ## beggining weight ranges
    areaL = -1
    areaH = 1
    
    permL =  -1
    permH = 1
    
    compL = -1
    compH = 1
    
    lenL = -1
    lenH = 1
    
    widL = -1
    widH = 1
    
    asymL = -1 
    asymH = 1
    
    grooL =  -1
    grooH =  1
    
    
    ## Create dict from csv data
    '''
    This needs to be changed to the func from figuring_out_processes to be dynamic
    
    Looks like just about every func is going to need to be changed. So everything,
    we are basically using this as a general structure and will go func by func replacing 
    non-dynamic code with dynamic
    
    Import data will have to be the first func, everything else will depend on the 
    dict it creates. May even put it in the main.py script and pass dict in as an arguement.
    '''
    
    def import_data():  
        global row_count
        with open(csv_file) as file:
            
            data_index = 0
            
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
                
                data[data_index] = [s_area, s_perm, s_comp, s_len, 
                                    s_wid, s_asym, s_groo, species]
                
                data_index += 1
            
            row_count = len(data)
            
            
    ## Call above func
            
    import_data()    
    
    
    
    ## when acceptable accuracy is found, reduce range closer to current weights
    ## so it's a smaller range to search in
    
    def get_closer(areaW, permW, compW, lenW, widW, asymW, grooW):
    
        global areaL
        global areaH
        global permL
        global permH
        global compL
        global compH
        global lenL
        global lenH
        global widL
        global widH
        global asymL
        global asymH
        global asymH
        global grooL
        global grooH
    
        
        areaL = round(areaW, 1) - .1 
        areaH = round(areaW, 1) + .1
    
        permL = round(permW, 1) - .1 
        permH = round(permW, 1) + .1
    
        compL = round(compW, 1) - .1 
        compH = round(compW, 1) + .1
    
        lenL = round(lenW, 1) - .1 
        lenH = round(lenW, 1) + .1
    
        widL = round(widW, 1) - .1 
        widH = round(widW, 1) + .1
    
        asymL = round(asymW, 1) - .1 
        asymH = round(asymW, 1) + .1
    
        grooL = round(grooW, 1) - .1 
        grooH = round(grooW, 1) + .1    
    
            
    ## If acceptable accuracy isn't found, expand range
        
    def get_further(areaW, permW, compW, lenW, widW, asymW, grooW, delta):
        global areaL
        global areaH
        global permL
        global permH
        global compL
        global compH
        global lenL
        global lenH
        global widL
        global widH
        global asymL
        global asymH
        global asymH
        global grooL
        global grooH
        
    
        areaL = round(areaW, 1) - delta 
        areaH = round(areaW, 1) + delta
    
        permL = round(permW, 1) - delta 
        permH = round(permW, 1) + delta
    
        compL = round(compW, 1) - delta 
        compH = round(compW, 1) + delta
    
        lenL = round(lenW, 1) - delta
        lenH = round(lenW, 1) + delta
    
        widL = round(widW, 1) - delta
        widH = round(widW, 1) + delta
    
        asymL = round(asymW, 1) - delta
        asymH = round(asymW, 1) + delta
    
        grooL = round(grooW, 1) - delta
        grooH = round(grooW, 1) + delta
        
    
    
        
    ## If we have gone thru too many iterations, start over. Resets weight ranges and range counter
        
    def start_over(): 
        '''
        All of this needs to be changed for unknown dicts
        '''
        
        global range_counter
        global temp_percentage
        
        global areaL
        global areaH
        global permL
        global permH
        global compL
        global compH
        global lenL
        global lenH
        global widL
        global widH
        global asymL
        global asymH
        global asymH
        global grooL
        global grooH
        
        range_counter = .1
        temp_percentage = percentage - .2
        
        areaL = -1
        areaH = 1
        
        permL =  -1
        permH = 1
        
        compL = -1
        compH = 1
        
        lenL = -1
        lenH = 1
        
        widL = -1
        widH = 1
        
        asymL = -1 
        asymH = 1
        
        grooL =  -1
        grooH =  1
        
    
    while 1:
         
        '''
        This will also need to be chaged to accomodate dicts of different lengths
        '''
        correct = 0
    
        area_node = random.uniform(areaL, areaH)
        perm_node = random.uniform(permL, permH)
        comp_node = random.uniform(compL, compH)
        len_node = random.uniform(lenL, lenH)
        wid_node = random.uniform(widL, widH)
        asym_node = random.uniform(asymL, asymH)
        groo_node = random.uniform(grooL, grooH)
            
    
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
                
        '''
        So, we have a function in figuring out processes that creates a dict from
        a csv file with unknown number of rows and columns. We need to use this 
        to create the appropriate number of nodes. Id say this is the next step
        
        Shouldn't be too hard. iterate thru the dict and just create nodes for each
        datapoint in a single row. So name them node + i (iteration)
        
        Obviously we need to add the dynamic dict creation function to this script in place of the current import_data func
        '''
        
        for v in data.values():
            area = v[0]
            perm = v[1]
            comp = v[2]
            leng = v[3]
            wide = v[4]
            asym = v[5]
            groo = v[6]
            
            spec = v[7]
                
            if nodes(area, perm, comp, leng, wide, asym, groo) >= 1:  
                prediction = '2'
                
            elif nodes(area, perm, comp, leng, wide, asym, groo) < 1\
                and nodes(area, perm, comp, leng, wide, asym, groo) > -1:
                    prediction = '1'
                    
            elif nodes(area, perm, comp, leng, wide, asym, groo) <= -1:
                prediction = '3'
        
            else:
                prediction = ''
            
            if prediction == spec:
                correct += 1
        
            # else:
            #     answer = '' ### dont think we need this anymore, but not sure#############
    
        if correct / (row_count) >= percentage:
            break
        
        elif correct / (row_count)  >= temp_percentage:
            temp_percentage = correct / (row_count) 
            get_closer(area_node, perm_node, comp_node, len_node, wid_node, asym_node, groo_node)
            range_counter = .1
            # print(correct, temp_percentage)
            
        
        
        elif correct / (row_count) < temp_percentage and counter != 0 and counter % 100_000 == 0:
            get_further(area_node, perm_node, comp_node, len_node, wid_node, asym_node, groo_node, range_counter)
            range_counter += .1
            temp_percentage = percentage - .2
        
        counter += 1
        
        if counter % 100_000 == 0:
            print(counter)
        
        if counter % 1_000_000 == 0:        
            start_over()
            
    
    print(round((correct / row_count) * 100, 2), 'percent accuracy', '\n\narea_node = ', area_node, '\nperm_node = ', perm_node, '\ncomp_node = ', comp_node, 
          '\nlen_node = ', len_node, '\nwid_node = ', wid_node, '\nasym_node = ', asym_node,
          '\ngroo_node = ', groo_node)
    
    
    print(counter)
    
    
    
    
if __name__ =='__main__':
    main(90, 'training.csv')    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
