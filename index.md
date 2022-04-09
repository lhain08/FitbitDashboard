## Welcome to Fitbit Dashboard

Fitbit Dashboard is a web app designed to allow users to connect with their fitbit account and access their data in ways that Fitbit does not provide!

## Join our Community!

We'd love to hear your feedback and suggestions, come give them to us in our community Discord server: https://discord.gg/5qYpnkN3uJ

## Getting Started  

To use this app, you will need the following:
- Docker Desktop https://www.docker.com/products/docker-desktop/
- A clone of this repository (run `git clone https://github.com/lhain08/FitbitDashboard.git`)
- A Fitbit Account, preferrably with data. Works best for users with trackers and plenty of data.
- A Fitbit Dev App (see below)
- Your Fitbit App Credentials

### Setting up your Fitbit Development App

- Go to https://dev.fitbit.com and select Manage -> Register an App
- Log in with your Fitbit account and create a new application as follows:
- Give it a name (ie. Dashboard App)
- Give it a description, what do you want to do with our application?
- Give it the project URL - https://github.com/lhain08/FitbitDashboard
- Organization is 'Myself'
- Organization URL may be https://github.com/lhain08/FitbitDashboard
- Terms of service is the link to Fitbit's Terms of Service: https://dev.fitbit.com/legal/platform-terms-of-service/
- Privacy poliy is Fitbit's Privacy Policy link: https://www.fitbit.com/global/us/legal/privacy-summary
- OAuth 2.0 Application Type is Personal
- Redirect URL Should be http://127.0.0.1:8080/authorize
- Select whichever permissions you would like our app to have and you're all set!

### Set up your application credentials

- Navigate to the your clone of the Fitbit Dashboard repository on your computer
- In FitbitDashboard/src/api create a new file called credentials.txt
- Paste your Client ID on Line 1 and your Client Secret on Line 2
- Save the file and you're good to go!

### Run the application!

- From the root directory of the FitbitDashboard repository, with Docker Desktop Running, run `docker-compose up --build`
- The logs should show a link, if it is your first time running the link will be http://127.0.0.1:8080. Click this link or enter it into your browser.
  - This will prompt you to set up your permissions and log in before redirecting you to the app
  - There may be a lag between authorization and the app getting started, if you get an error, wait a moment and refresh.
- If this is not your first time running, the link will be http://127.0.0.1:8000
- This will take you to the app, now you can start setting up your first dashboard!