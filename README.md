## Application development for supervised and unsupervised machine learning, utilized on a dataset of building energy features recording.

**Scope**  
The scope of this repository is to present essential information related with the fields of Data Science and Machine Learning, and implement a Command Line Interface that offers 3 functionalities, explained below.

The theoretical part of this thesis is presented in Chapters 2 and 3 of *thesis_kougianos.pdf*, while the complete implementation is depicted in Chapter 4. The 3 main functionalities that are currently supported by the CLI are:  
*	Executing a supervised learning algorithm of your choice to a predefined dataset. Algorithm execution metrics along with other information (username, cpu info etc.) are then saved in a MongoDB cluster. Supported algorithms: <br>
  &nbsp;&nbsp;&nbsp;&nbsp; 1.	SVM   
  &nbsp;&nbsp;&nbsp;&nbsp; 2.	Logistic Regression  
  &nbsp;&nbsp;&nbsp;&nbsp; 3.	Naive Bayes  
  &nbsp;&nbsp;&nbsp;&nbsp; 4.	Decision Tree  
*	Open a dataset of your choice and create excel files with basic and extended information regarding the dataset. The files are saved in a user-defined destination folder.
*	Retrieve algorithm execution metrics from other users (including yourself) and save them to an excel file, in a folder of your choice.

**Design**  
![image](https://user-images.githubusercontent.com/23719920/127898453-69222725-6b53-440e-ba9f-d3005c17129f.png)

#
### Instructions and helpful information
**Install python3 and pip:**  
* Windows: https://phoenixnap.com/kb/how-to-install-python-3-windows
* Mac OS: https://docs.python-guide.org/starting/install3/osx/
* Linux: https://docs.python-guide.org/starting/install3/linux/

**Install any package that may be missing using pip:**  
Make sure `pip` command is added to PATH, then open a terminal and run   
`pip install package_name`

**Execute python script:**  
Make sure `python3/python` commands are added to PATH, then open a terminal where the python script is located, and run  
`python python_file_name.py` 

### How to run:
1. **Download source code.**  
You need to have Python 3, Pip and Git installed on your machine.
- `git clone https://github.com/kougianos/ds-thesis.git`
- `cd ds-thesis/app`
- `pip install -r requirements.txt`
- `python mainCLI.py`
- Follow on-screen instructions.  

OR  

2. **Download .exe file created with Pyinstaller (works only on Windows).**  
You don't need to have anything else installed on your machine.  
*Disclaimer: CPU and RAM information are not supported when running tha application as .exe, due to a probable bug.*
- Download file from https://grizzledwizard.eu/docs/kougianos_thesis.zip (~350MB)
- Unzip file.
- Open folder and locate file named *mainCLI.exe*, and double click on it.  
- Follow on-screen instructions.

