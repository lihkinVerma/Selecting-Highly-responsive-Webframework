
import os

cmd_RunAllTestScenarios = 'python3 allTestScenarios.py'
cmd_makeAHPFiles = 'python3 parseABtollOutcomes.py'

os.system(cmd_RunAllTestScenarios)
os.system(cmd_makeAHPFiles)

'''
ll = [i for i in os.listdir() if 'Results' in i]
for i in ll:
    os.system('rm -r %s'%str(i))
'''
