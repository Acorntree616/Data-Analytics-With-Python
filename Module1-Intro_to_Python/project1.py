"""
This file perform. 

Author: Alex Cornwall
   
"""
def main():
    """
    This function ensures that the code is run when executed on a command line.
   
    """
    # Global variables that are associated with data collection regions
    AREAS = {
        0: 'All',
        1: 'Rawah Wilderness Area',
        2: 'Neota Wilderness Area',
        3: 'Comanche Peak Wilderness Area',
        4: 'Cache la Poudre Wilderness Area'
    }

    #Global variables that are associated with data collection types
    COLUMNS = {
        0: 'Elevation',
        1: 'Aspect',
        2: 'Slope',
        3: 'Horizontal_Distance_To_Hydrology',
        4: 'Vertical_Distance_To_Hydrology',
        5: 'Horizontal_Distance_To_Roadways',
        6: 'Hillshade_9am',
        7: 'Hillshade_Noon',
        8: 'Hillshade_3pm',
        9: 'Horizontal_Distance_To_Fire_Points'
    }
    
    Data = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }
    
    Rawah = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }
    
    Neota = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }
    
    Comanche = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }
    
    Cache = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }
        
    from sys import argv
    script, file_name = argv
    file = open(file_name, encoding="UTF-8")
    
    #for row in file:
       # cols = row.split(",")
    def pull_data(area):    
        for c in Data.keys():
            x[c].append(float(cols[c]))
            
    def call_report(location):
        for report in location.keys():
            print("Minimum {}: {}".format(COLUMNS[report], min(x[report])))
            print("Maximum {}: {}".format(COLUMNS[report], max(x[report])))
            print("Mean {}: {}".format(COLUMNS[report], round((sum(x[report])/len(x[report])))))
            print("\n")
     
    for row in file:
        cols = row.split(",")
        rawah, neota, comanche, cache = int(cols[11]), int(cols[12]), int(cols[13]), int(cols[14])
        if rawah == 1:
            x = Rawah
            pull_data(cols)
            
        elif neota == 1:
            x = Neota
            pull_data(cols)
            
        elif comanche == 1:
            x = Comanche
            pull_data(cols)
            
                
        elif cache == 1:
            x = Cache
            pull_data(cols)
 
    
    call_report(Rawah)
    call_report(Neota)
    call_report(Comanche)
    call_report(Cache)
    
    
    
    
    
    file.close()



if __name__ == "__main__":
    main()