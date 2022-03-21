# Getting Started

## Installing Requirements
1. You can clone the Github project by typing in ````git clone git@github.com:lhain08/FitbitDashboard.git```` in the command line in order to obtain a local copy of the project 
2. This project contains the [python-fitbit](https://github.com/orcasgit/python-fitbit/tree/6a0a7cba26c26e6c8096bf51d4cf7f19e113ed96) Github project as a submodule. However, after cloning this repository, you will see that in ````src/api/python_fitbit```` is empty in your local repo. To obtain the files from the project, run this in your command line: 

   ````git submodule update --init --recursive````

3. Navigate to ````dev.txt```` via ````src/api/python_fitbit/requirements````. Open the text file, and you will see 1 line that reads: ````cherrypy>=3.7,<3.9````. Delete this line. 
4. Navigate back to the ````src```` directory. You will see a text file called ````requirements.txt````. This contains the main libraries and packages you need to run the project. From the command line, run:

   ````pip3 install -r requirements.txt````
 
## Fitbit App Registration 
1. Create a Fitbit account by going to [fitbit.com](fitbit.com)
2. After your account has been made, go to [dev.fitbit.com](dev.fitbit.com). Then, on the top right corner, go to ````Manage --> Register an App````. Click ````Log In````, and you will be automatically logged in with your Fitbit account you created in Step 1. 
3. Now you will need to register our app. Many of the fields don't matter, but use this image as reference for which fields are important: 

   ![registerFinal](https://user-images.githubusercontent.com/68397066/159187525-b4eaf2c1-ffd3-47da-85d5-e122275f5e73.jpg)
   
   Note that for *Application Name* and *Organization*, you can't use the word *Fitbit*. <br>For **Application Website Url**, use the URL of the Github page, [https://github.com/lhain08/FitbitDashboard](https://github.com/lhain08/FitbitDashboard). <br>For **Terms of Service Url**, use [https://dev.fitbit.com/legal/platform-terms-of-service/](https://dev.fitbit.com/legal/platform-terms-of-service/) <br>
For **Privacy Policy Url**, use [https://www.fitbit.com/global/us/legal/privacy-summary](https://www.fitbit.com/global/us/legal/privacy-summary) <br>
For the **Redirct URL**, use http://127.0.0.1:8080/
   
4. After hitting submit, you will see a page of credentials regarding your web app. You will see two fields called **OAuth 2.0 Client ID** and **Client Secret**. The data in these two fields are unique to everyone who registers an app. Create a text file called ````credentials.txt```` in ````src/api````. In this file, use your data from those two fields to write this within ````credentials.txt````:

   ````
   <client id>
   <client secret>
   ````
   It may be wise to create a copy of this text file and put it somewhere else where you can easily copy and paste it back into your own local repository. 
   
## Running   
1. After completing all previous steps, you can run the project with ````python3 src/main.py````
