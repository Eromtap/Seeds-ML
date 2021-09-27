import csv




        









data = {}




csv_file = 'CsvTest.csv'






'''

this should take a csv with unknown num of rows and create a dict with it

ok, we have it creating the dict, now it needs to create the appropriate num
of nodes. OOP or functional?



'''



def import_data():  
    global row_count
    with open(csv_file) as file:
        
        data_index = 0
        
        csv_reader = csv.reader(file, delimiter=',')
        
        for row in csv_reader: 
            data[data_index] = []
            for data_point in range(len(row)):
            
                data[data_index].append(row[data_point])      
            

            
            data_index += 1
        
        row_count = len(data)
        
        
## Call above func
        
import_data()    











# create dict with acsending keys for number of datapoints. This makes our nodes
# dont know how to use them yet    
# also sets the initial ranges from -1 to 1
# may use int keys in this dict, probably will make it easier
# leave last column out of nodes, this is the output like subspecies name or 
# something like that, it doesnt have a node

# OK, so we just re-define the values to x num of keys foreach time we 
# want to change ranges. so basically nodes ranges are in a dict


node_dict = {}

for node in range(len(data[0])-1):
    
    node_dict['node' + str(node)] = [-1, 1]

























