# Getting Started

## Fitbit App Registration 
1. Create a Fitbit account by going to [fitbit.com](https://www.fitbit.com/global/us/home)
2. After your account has been made, go to [dev.fitbit.com](https://dev.fitbit.com/login). Then, on the top right corner, go to ````Manage --> Register an App````. Click ````Log In````, and you will be automatically logged in with your Fitbit account you created in Step 1. 
3. Now you will need to register our app. Many of the fields don't matter, but use this image as reference for which fields are important: 

   ![registerFinal](https://user-images.githubusercontent.com/68397066/160022815-0e8bdd91-1e7e-4f86-ad57-b97101941ef9.jpg)
   
   Note that for *Application Name* and *Organization*, you can't use the word *Fitbit*. <br>For **Application Website Url**, use the URL of the Github page, [https://github.com/lhain08/FitbitDashboard](https://github.com/lhain08/FitbitDashboard). <br>For **Terms of Service Url**, use [https://dev.fitbit.com/legal/platform-terms-of-service/](https://dev.fitbit.com/legal/platform-terms-of-service/) <br>
For **Privacy Policy Url**, use [https://www.fitbit.com/global/us/legal/privacy-summary](https://www.fitbit.com/global/us/legal/privacy-summary) <br>
For the **Redirct URL**, use http://127.0.0.1:8080/authorize
   
4. After hitting submit, you will see a page of credentials regarding your web app. You will see two fields called **OAuth 2.0 Client ID** and **Client Secret**. The data in these two fields are unique to everyone who registers an app. Remember these two data fields for a later step. You can either write them down in another text file or take a screenshot. 
   
## Docker Installation 
1. We will be using Docker in order to run our project. To install Docker, use this [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/) to download Docker according to your operating system. <br>
Note that if you are using Windows, you need to download WSL as a prerequisite. If you don't have WSL, use [https://docs.microsoft.com/en-us/windows/wsl/install](https://docs.microsoft.com/en-us/windows/wsl/install) as guidance. <br>
Then, follow the instructions in [https://docs.docker.com/desktop/windows/wsl/](https://docs.docker.com/desktop/windows/wsl/) to get **Docker Desktop** working 

## Installing Requirements
1. You can clone the Github project by typing in ````git clone git@github.com:lhain08/FitbitDashboard.git```` in the command line in order to obtain a local copy of the project 
2. Create a text file called ````credentials.txt```` in ````src/api````. Refer back to *Step 4* in **Fitbit App Registration**. In this text file, use your data from those two fields to write this within ````credentials.txt````:

   ````
   <client id>
   <client secret>
   ````
   It may be wise to create a copy of this text file and put it somewhere else where you can easily copy and paste it back into your own local repository. 
   
## Running    
1. Open Docker Desktop. To run the project, run these two commands in your command prompt or bash window 

   ````
   docker-compose up --build
   ````
   2. Open the url http://localhost:8080/ if you have just rebuilt the docker container (this will get the api keys) then wait a moment and go to http://localhost:8000/ (the link should be displayed already at this point) to access your dashboard.
