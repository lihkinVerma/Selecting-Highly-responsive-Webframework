
# importing libraries
import os
import sys
import glob as g
import pandas as pd
import yaml
# Developer Nikhil Verma

#-----------------------------------------------------------
# Collecting results from all files to make final data frame
#-----------------------------------------------------------

# 1. locat directories to fetch data from
directories = ['falconResults', 'fastApiResults', 'flaskResults']
scenarios = ['Fibonacci', 'HelloWorld', 'FileRetrival']

# Defining data frame 
dff = pd.DataFrame(index = directories, columns = [
        'TimeTakenForTests',
        'TotalTransferred',
        'RequestsPerSecond',
        'TimePerRequest',
        'TimePerConcurrentRequests',
        'TransferRate'
        ])

# 2. Fetching data from each directory in loop
def PopulateDataFrame(dff, scenario):
    for dirName in directories: 
        now = os.getcwd()
        os.chdir(dirName)
        # Loading all files having ahp results 
        lof = g.glob("*"+scenario+"*.txt")

        df = pd.DataFrame(index = range(len(lof)), columns = [
            'Time taken for tests(sec)',
            'Total transferred(bytes)',
            'Requests per second(mean)',
            'Time per request(mean)',
            'Time per request(mean, across all concurrent requests)',
            'Transfer rate([Kbytes/sec] received)'
            ])

        for i in range(len(lof)):
            filename = lof[i]
            with open(filename, 'r') as f:
                data = f.readlines()

            df.iloc[i, 0] = float(data[15].strip().split(" ")[-2])
            df.iloc[i, 1] = int(data[18].strip().split(" ")[-2])
            df.iloc[i, 2] = float(data[20].strip().split(" ")[-3])
            df.iloc[i, 3] = float(data[21].strip().split(" ")[-3])
            df.iloc[i, 4] = float(data[22].strip().split(" ")[-7])
            df.iloc[i, 5] = float(data[23].strip().split(" ")[-3])

        os.chdir(now)
        #df.to_csv(dirName+'_combined.csv', index = False)
        dff.loc[dirName, 'TimeTakenForTests'] = df.iloc[:, 0].mean()
        dff.loc[dirName, 'TotalTransferred'] = df.iloc[:, 1].mean()
        dff.loc[dirName, 'RequestsPerSecond'] = df.iloc[:, 2].mean()
        dff.loc[dirName, 'TimePerRequest'] = df.iloc[:, 3].mean()
        dff.loc[dirName, 'TimePerConcurrentRequests'] = df.iloc[:, 4].mean() * 100
        dff.loc[dirName, 'TransferRate'] = df.iloc[:, 5].mean()

    # 3. Final data collected
    dff = dff.astype(int)
    #dff.to_csv("SavingOverallResultsOfAllFrameworks.csv")
    return dff

#-----------------------------------------------------------
# Making an .ahp file for applying AHP(MCDM) technique
#-----------------------------------------------------------

def MakeAHPFile(dff, scenario):
    # 1. Collecting Alternatives in race and their criterion value
    dictOfFrameworks = {}
    for direc in dff.index.tolist():
        dictOfFrameworks.update({direc.split('Results')[0] : dff.loc[direc].to_dict()})

    alternatives = {'Alternatives: &alternatives': dictOfFrameworks}

    # 2. Deining equal preference of all criterias
    criteriaPreference = ["["+dff.columns.tolist()[i]+", "+dff.columns.tolist()[j]+", 1]" for i in range(len(dff.columns.tolist())) for j in range(i+1, len(dff.columns.tolist()))]

    # 3. Deining preference function for criterion comparison
    def makePairWiseFunc(criteria):
        if 'time' in criteria.lower():
            # a2 has more preference than a1 ie minimizing
            return "function(a1, a2) min(9, max(1/9, a2${}/a1${}))".format(criteria, criteria)
        else:
            # a1 has more preference than a2 ie maximizing
            return "function(a1, a2) min(9, max(1/9, a1${}/a2${}))".format(criteria, criteria)

    # 4. Defining criterion function
    childDict = {}
    for criteria in dff.columns.tolist():
        criteriaFunc = {
                criteria : {
                    'preferences' : {
                        'pairwiseFunction' : makePairWiseFunc(criteria)
                        },
                    'children': '*alternatives'
                    }
                }
        childDict.update(criteriaFunc)

    # 5. Deining goal body
    goal = {'Goal':
            {'name': 'lightweight framework', 
                'author':'nikhil', 
                'preferences': {
                    'pairwise': criteriaPreference
                    },
                'children': childDict
                }
            }

    # 6. Overall AHP model
    ahpModel = [alternatives, goal]

    # 7. Saving AHP model to file and doing some syntax corrections from python to YAML
    with open('ahpModel.ahp', 'w') as f:
        yaml.safe_dump({'Version': 2.0}, f)
        yaml.safe_dump(alternatives, f)
        yaml.safe_dump(goal, f)

    with open('ahpModel.ahp', 'r') as f:
        data = f.read()
        data = data.replace('\'', '')
        data = data.replace('Alternatives: &alternatives:', 'Alternatives: &alternatives')

    with open('ahpModel_'+ scenario +'.ahp', 'w') as f:
        f.write(data)

    os.remove('ahpModel.ahp')

for scenario in scenarios:
    dff.loc[:,:] = 0
    dff = PopulateDataFrame(dff, scenario)
    MakeAHPFile(dff, scenario)
