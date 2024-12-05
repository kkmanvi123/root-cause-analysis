# Root Cause Analysis for Cadence Design Systems

## Project Description
### Purpose
The goal of this project was to develop a machine learning model that classifies software program failures (bugs) by type, helping developers quickly identify the nature of the issue. By analyzing historical failure data, the model detects patterns and correlations associated with specific bug categories, providing insights to guide debugging efforts and improve development efficiency. 

### Project Overview, Objectives and Goals
 The overview of the project is to create a machine learning model that finds the root cause for a software program failure(bug). This complex challenge offered our team the freedom to explore different approaches for solving the problem effectively. 
Our goal is to create a solution that can classify the failure type of a bug, identify the most suitable machine learning algorithm, and integrate the implementation into a user-friendly terminal-based tool. This project is critical as it addresses the significant time spent debugging software, a key issue for companies like Cadence Design Systems, where debugging faulty software is both time-sensitive and resource intensive. 
Currently, engineers spend up to 70% of their time debugging code. Moreover, team-developed software often requires years of expertise for engineers to master. By simplifying the process of determining bug types from  code snippets, our project aims to significantly reduce debugging time, allowing developers to focus more on productive development tasks. 

### Objectives
1. Understand and Define the Problem: Clearly analyze the scope and specifics of software failures and identify the key factors contributing to debugging challenges. 
2. Determine the ML methodology: Evaluate and select the most appropriate machine learning approach to classify and address the root causes of bugs. 
3. Break down the project into subtasks

### Methodology


### Potential Next Steps


### Installation
1.Download files: from the bttai-debugger folder in the GitHub Repository.
Random_forest_model.pkl (the model from downloaded from google collab)
debugger.py (python script that debugs using the model)
PreparedStatementGenerator.java (the buggy code snippet in java to be predicted)
2.Install Python: Ensure Python is installed on your system. 
You can download it from python.org
3. Organize Files: Place all the downloaded files in the same folder on your computer
4.Open Command Prompt: Navigate to the folder containing the files using the cd command.
cd C:\this\is\your\folderpath\
5. Run the Program on the Terminal:
Obtain the path for the .java file 
Execute the following command in the terminal: 
		py debugger.py C:\This\is\your\folderpath\PreparedStatementGenerator.java
6. View the Output: The program will display the predicted bug type in the .java file. 
Possible types include : Null Dereference, Resource Leak , and Thread Safety Violation.
7. Test with Different Code Snippets: Remember that the code snippet must be in the code language JAVA. 
Modify the content of the .java file with another code snippet.
 Save the file and repeat steps 4-6 to see the model's prediction for the updated snippet. 

### Contributing
If you are looking to reproduce the project, then you can use the .ipynb model in the github repository once edited it should be downloaded as a .pkl file. The steps above should be followed to test the new model. 
The original .ipynb Google Colab file should not be modified. A copy of the file should be made in order to use it. You can make suggestions and develop a better version or add more features to the copy of the .ipynb file. As mentioned if you want to test the new model you can follow the steps above. You can modify the .java file to have the code snippet of your preference to test the model. However the .py file should not be modified unless you add new features, add more bugs, or change the name of your .pkl file. The steps above will not work if the right information is not found inside of the .py file. 

### License
Purpose: State the licensing under which the project is released.
Suggested Content: A short statement about the license, typically linking to the full license file.
Credits and Acknowledgments
Resources Leveraged
	Github Repository for data: Microsoft Inferred Bugs
	Google Colab: To train and develop the model
	Scikit learn, Pandas, numpy
	Jira: Project management
	Google Drive: File documentation management

### Acknowledgements
We've learned so much throughout this project, and we’re so thankful for everyone at Cadence Design Systems who shared their knowledge and guidance with us. Huge thanks to our amazing Challenge Advisors, Francoise Martinolle and Yosinori Watanabe, for always being there to support us and offer great advice.
We’d also like to thank Break Through Tech and the Cornell Tech AI Program team for giving us this incredible opportunity. A special shoutout to our AI Studio TA, Kailey Bridgeman, for all her help and encouragement along the way.
We’re so grateful for everything and everyone who’s been part of this journey—thank you!

AI Studio Challenge Advisors (Cadence):
Francoise Martinolle
Yosinori Watanabe
AI Studio TA (BTTAI):
Kailey Bridgeman
Fellow Studio Project Team (BTTAI):
Sarah Goldman
Manvi Kottakota
Lee Mabhena
Hema Motiani
Alison Ramirez
