import pandas
df = pandas.read_csv("sin_dataset.csv")

power_d = 0
power_c = 0
power_b = 0
node_d = ""
node_c = ""
node_b = ""

find_current_powers()
link_prediction()

def find_current_powers():
    power_d = degree_centrality()
    #power_c = closeness_centrality()
    #power_b = betweenness_centrality()
    message = "The initial power centers are: "
    printer(message)

def current_indian_power():
    power_d = degree_centrality(india)
    #power_c = closeness_centrality(india)
    #power_b = betweenness_centrality(india)
    message = "The centraility of India is: "
    printer(message)

def link_prediction():
    india = 8
    len = 23
    for fix in range(0:len):
        if fix == india:
            continue
        else if fix >= 1:
            if df[india,fix] == 1:
                continue
            else:
                df[india,fix]=1
                fixed = 1
        for col in range(1:len):
            if col == india:
                continue
            if df[india,col]==1:
                continue
            else:
                df[india,col]=1
                find_new_powers(india,col,fix)
                df[india,col]=0
        if fixed == 1:
            df[india,fix] = 0
    #changed_powers()

def find_new_powers(india,col,fix):
    power_d = degree_centrality(india)
    #power_c = closeness_centrality(india)
    #power_b = betweenness_centrality(india)
    message = "Case:"+counter+" If india makes relations with "
    if fix == 0:
        #do this
        message = message + df[0,col].toString()
    else:
        #do that
        message = message + df[0,col].toString + "and" + df[0,fix].toString
    message = ", its new centrality will be: "
    printer(message)

def changed_powers():
    d = power_d
    #c = power_c
    #b = power_c
    power_d = degree_centrality()
    #power_c = closeness_centrality()
    #power_b = betweenness_centrality()
    message = "If India does so, the power centers of the world will change to: "
    printer(message)

def printer(message):
    print(message)
    print("Degree centrality = "+power+" of node "+node_d)
    #print("Closeness centrality = "+power+" of node "+node_c)
    #print("Betweenness centrality = "+power+" of node "+node_b)

def degree_centrality():
    #print max degree
    #print column header of max sum

def degree_centrality(india):
    #print india's degree
    #print col sum of india