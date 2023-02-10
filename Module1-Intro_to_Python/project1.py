"""
This file perform. 

Author: Alex Cornwall
   
"""
from sys import argv
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

def pull_data(area_dict, cols):
    """[Summary]

    :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
    :type [ParamName]: [ParamType](, optional)
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]
    """
    for c in area_dict.keys():
        area_dict[c].append(float(cols[c]))
            
def call_report(stats_repos, area_dict, Name):
    """[Summary]

    :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
    :type [ParamName]: [ParamType](, optional)
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]
    """
    #writing in my wilderness area names
    stats_repos.write('--------------------------------------\n')
    stats_repos.write('{}\n'.format(Name))
    stats_repos.write('--------------------------------------\n')
    for c in area_dict.keys():
        stats_repos.write("Minimum {}: {}\n".format(COLUMNS[c], min(area_dict[c])))
        stats_repos.write("Maximum {}: {}\n".format(COLUMNS[c], max(area_dict[c])))
        stats_repos.write("Mean {}: {}\n".format(COLUMNS[c], round((sum(area_dict[c])/len(area_dict[c])))))
        stats_repos.write("\n")    
    
def main():
    
    """[Summary]This function ensures that the code is run when executed on a command line.

    :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
    :type [ParamName]: [ParamType](, optional)
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]
  
    """
    
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
        9: [],
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
        9: [],
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
        9: [],
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
        9: [],
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
        9: [],
    }
        
    
    script, file_name = argv
    file = open(file_name, encoding="UTF-8")
    stats_repos = open('./data/Data_summary.txt', 'w')    
     
    for row in file:
        cols = row.split(",")
        rawah, neota, comanche, cache = int(cols[10]), int(cols[11]), int(cols[12]), int(cols[13])
        pull_data(Data, cols)
        if rawah == 1:
            pull_data(Rawah, cols)
            
        elif neota == 1:
            pull_data(Neota, cols)
            
        elif comanche == 1:
            pull_data(Comanche, cols)
             
        elif cache == 1:
            pull_data(Cache, cols)
 
    call_report(stats_repos, Data, AREAS[0])
    call_report(stats_repos, Rawah, AREAS[1])
    call_report(stats_repos, Neota, AREAS[2])
    call_report(stats_repos, Comanche, AREAS[3])
    call_report(stats_repos, Cache, AREAS[4])
    
    
    
    
    stats_repos.close()
    file.close()



if __name__ == "__main__":
    main()