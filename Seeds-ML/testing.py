    

def main():
    
    import csv
    
    '''
    
    This will be the testing module. Need to add functionality to import node weights
    
    '''
    
    ## Csv file we want to use for testing
    csv_file = 'testing-200.csv'
    
    ## Number of rows in csv file used for calculating accuracy
    #row_count = sum(1 for line in open(csv_file))
    
    
    ## Dict we create from the csv file
    data = {}
    
    
    ## Create dict from csv data
    
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
    
    '''
    need to get these weights from a file. So Training module needs to 
    save the weights it finds
    '''
    
    area_node =  0.9858725966017494 
    perm_node =  -0.6501985649657807 
    comp_node =  -0.33984304230361784 
    len_node =  -0.12613610298582834 
    wid_node =  -0.5921460571759212 
    asym_node =  -0.07785799886672606 
    groo_node =  -0.3206700620069862
    
    
    
    
    def nodes(s_area, s_perm, s_comp, s_len, s_wid, s_asym, s_groo):
        

    
        return (s_area * area_node) + (s_perm * perm_node) \
            + (s_comp * comp_node) + (s_len * len_node) \
            + (s_wid * wid_node) + (s_asym  * asym_node) \
            + (s_groo * groo_node)
            
    
    ## Pretty straight forward here, open the csv file and assign the values
    ## of length, width, etc to variables and call the nodes func to do the 
    ## math. Then assign a prediction based on the range the result 
    ## falls into. Change the file name to switch between training and test sets
    
    correct = 0
    
    
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
    
        else:
            answer = ''
            
            
            
            
            
            
            
            
    print(round((correct / row_count) * 100, 2), 'percent accuracy', '\n\narea_node = ', area_node, '\nperm_node = ', perm_node, '\ncomp_node = ', comp_node, 
          '\nlen_node = ', len_node, '\nwid_node = ', wid_node, '\nasym_node = ', asym_node,
          '\ngroo_node = ', groo_node)        
    
    
    
    
if __name__ == '__main__':
    main()    
