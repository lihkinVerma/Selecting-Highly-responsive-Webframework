# Selecting-Highly-Responsive-Webframework
This codebase aims to propose a solution for selection of highly responsive web framework from options available in python. In particular I have shown comparison of Flask, FastApi and Falcon web framework for selecting lightIight micro web framework with only requirement of serving to write and deploy backend code. I used Apache benchmarking tool for finding relevant criterions for framework comparison and with an optimization problem statement at hand, I used Analytical Hierarchy Processing algorithm for finding solution to Multiple Criterion Decison making problem.

Below are steps involved to run the comparison and some basic introduction to code files:-

## Code Design
`
The code has 3 files namely testFlask.py, testFastApi.py and testFalcon.py that define basic syntax to make a resource and API endpoint to call either of the utilities defined in utilityFunctions.py; The utilities include 3 different test case scenarios as basic Hello_Word, CPU intensive Fibonacci series computation and IO intensive File Retrival from database.

The file runApacheBenchmarkingOnRunningFramework.py will call Apache Benchmarking tool for noting required criterion parameter values for 10000 requests with a concurrency of 20. This experiment is repeated 5 times for taking an average result and iterated for all test case scenarios for all frameworks with help of file allTestScenarios.py

The results so collected are then parsed from simple file to 2D dataframe and from them an AHP model file(.ahp) is then created using file parseABtollOutcomes.py

The process of running whole code includes calling file runTestScenariosAndCreateAHP.py which computes mentioned AHP model file by running test case scenarios.

FIle with name AHP.r defines Running GUI which can compute AHP results when given an AHP model file as input.
`

## Commands to run Code
1. Install all required dependencies mentioned in requirements.txt file
`
	$ python3 -m pip install -r requirements.txt
`

2. Run final code file to check all testcase scenarios
`
	$ python3 runTestScenariosAndCreateAHP.py
`

3. Obtain final AHP model files with names
`
	$ ahpModel_HelloWorld.ahp
	$ ahpModel_Fibonacci.ahp
	$ ahpModel_FileRetrival.ahp
`

## Running AHP Analysis
1. Obtain AHP model files from using above mentioned commands
2. Run AHP.r file and start using RunGUI() method
3. Now GUI will start and enter here model files computed say 'ahpModel_HelloWorld.ahp'
![Input AHP model file to the GUI](https://github.com/lihkinVerma/Selecting-Highly-responsive-Webframework/blob/master/imagesForGit/ahpModel.png)
4. Now change tab to Visualize and look obtain AHP graph for the model file given as input
![Visualize AHP Graph for the problem statement](https://github.com/lihkinVerma/Selecting-Highly-responsive-Webframework/blob/master/imagesForGit/ahpGraph.png)
5. Now change tab to Analyze and obtain final results to see Ranking of various alternatives for achieving goal
![Obtain AHP results for the problem statement](https://github.com/lihkinVerma/Selecting-Highly-responsive-Webframework/blob/master/imagesForGit/ahpResults.png)
