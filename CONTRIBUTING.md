# Contribution Guideline


## Picking Issues to Work on
Once you have gone through the steps in [GETTING_STARTED.md](https://github.com/lhain08/FitbitDashboard/blob/main/GETTING_STARTED.md) and have everything set up, it's time for you to get cracking! To do that: 

1. Go to the Issue tracker to find something to work on 
2. Once you have found an issue, assign yourself to that issue so that the other contributors know that you are working on that issue 

## Creating another branch
1. Near the bottom right of an issue page, under *Development*, you will see a hyperlink saying "Create a branch for this issue or link a pull request". Click on it and follow the on screen instructions to create a new branch for the issue. With this, the issue will automatically close after you finish your work. 
2. If you are planning on making a contribution that doesn't correspond to any issues in the tracker and you don't feel like making a new issue, you can instead create another branch off of master and go into it with a command like `git checkout -b mywork`.  
3. Make sure that you are in the master branch by doing `git checkout master`
4. Pull in updates any updates to the code using `git pull origin master`

## Before Committing
Before committing your work, navigate to the root directory of the project and run **`make fmt`**. You will likely encounter a couple of error messages due to the lack of certain packages in your system. On the other hand, the packages could be out of date. For instance, let's say you see one line that reads: 

`autoflake: Permission denied`

You can update the package by running: 

`$ pip install --upgrade autoflake`

## Pull Requests 
1. After committing your work to your branch, navigate to the FitbitDashboard Github page and open a new pull request for your branch
2. If it passes all checks, merge your pull request to the main branch
