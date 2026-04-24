<!-- Navigating the shell
Git commands are typically performed using the shell.

Understanding some common shell commands allows you to perform more of your Git workflow in the shell without spending time navigating different programs.

In this exercise, you will practice some of these commands. -->

<!-- Print the current working directory.
Move to the data directory.
List all files and sub-directories. -->

pwd
cd data
ls

<!-- ________________________________________________________________ -->

<!-- Checking the version of Git
Just like you need to know what version of a file you are working with, it's important to understand which version of Git is installed on your computer so you're aware of what functionality it offers.

Using the terminal, enter the command to find out what version of Git is installed. -->

git --version

<!-- ________________________________________________________________ -->

<!-- Converting an existing project
Imagine you've been working on the mental health survey project but are only now learning about the benefits of Git!

You want to convert your project into a Git repo so you can track your files moving forward.

You're inside the mh_survey directory.

Turn your current directory into a Git repo. -->

git init

<!-- ________________________________________________________________ -->

<!-- Creating a new repo
You've secured funding for an additional project that examines the relationship between stress and performance in the workplace.

You plan to use Git to manage version control with your documents and data, so you'll need to create a new repo to track everything.

Create a new Git repo called stress-performance.
Change into the stress-performance directory.
Check the status of the new repo. -->

git init stress-performance
cd stress-performance 
git status

<!-- ________________________________________________________________ -->

<!-- Adding a file to the staging area
The staging area is used by Git to track changes to files within your current directory and sub-directories.

You've created a report.md file for your mental health project. In this exercise, you'll add this file to the staging area.

Place report.md, which is in your current working directory, in the staging area. -->

git add report.md

<!-- ________________________________________________________________ -->

<!-- Saving files
You've made further edits to report.md as well as the mental_health_survey.csv, which is in the data subdirectory. Time to save these files!

Use a single command to add the two modified files to the staging area.
Check the state of files in the repo.
Make a commit, including an appropriate flag so you can provide a log message "Add 2 participants and update to-do list." as part of the command. -->

git add .
git status
git commit -m "Add 2 participants and update to-do list."

<!-- ________________________________________________________________ -->

Viewing a repository's history
Recall that every commit has a unique identifier called a hash.

Git has a command you can use to display all commits made to a repo, along with the hash, author, and time of the commit.

Using the console, run a command to find the hash of the most recent commit.

git log

<!-- ________________________________________________________________ -->

Finding the log message
Log messages are a great way to summarize the changes made during a commit.

What message was included for the commit hash starting with 36b761e?

git log

<!-- ________________________________________________________________ -->

<!-- Limiting the view of a repo's history
Generally, suppose you need to look at a repo's history. In that case, you are seeking specific information, such as how an individual file has changed over time, who made the last edit to a file, or what changes have been made in a given period.

Customizing how you view your repo's history will make it easy to find what you need as quickly as possible!

View information about the last two commits only. -->

git log -2

<!-- ________________________________________________________________ -->

<!-- Viewing a file's history
You've practiced limiting the view of a repo's history based on a specific number of commits. Now you'll extend this to also filter by filename.

View information about the last two commits made for report.md only. -->

git log -2 report.md

<!-- ________________________________________________________________ -->

<!-- Filtering commits by date
It's the end of a busy day working on the mental health survey project. You've made several commits throughout the day and want to quickly review what you accomplished before heading home.

Rather than scrolling through the entire commit history or guessing how many commits to display, you can filter the log by date to see exactly what was done today.

Display only the commit(s) made since yesterday using the appropriate flag. -->

git log --since='yesterday'

<!-- ________________________________________________________________ -->

<!-- Comparing staged files
You've added two new rows of participant data to the mental_health_survey.csv file. You've now placed the updated file in the staging area.

Before you commit the file, you want to check the difference between the recently modified file and the latest committed version.

You are based in the data directory, where mental_health_survey.csv is located.

Run a command to compare the last committed version of mental_health_survey.csv against the version in the staging area. -->

git diff --staged mental_health_survey.csv

<!-- ________________________________________________________________ -->

Comparing to the second most recent commit
Being able to look at what happened in a specific commit is useful to check how files have changed over time.

Find out what changes occurred between the most recent and the second most recent commits and select the appropriate answer.

git diff HEAD~1 HEAD

<!-- ________________________________________________________________ -->

<!-- Unstaging a file
You've updated report.md and mental_health_survey.csv, adding both files to the staging area.

However, you've realized that there's an incorrect data entry in the CSV file. You want to commit the report, but need to move the data out of the staging area so you can fix the error before saving that file.

Move into the data directory.
Move mental_health_survey.csv out of the staging area.
Make a commit with the log message "Add task to fix plot in report", without opening the text editor. -->

cd data
git restore --staged mental_health_survey.csv 
git commit -m 'Add task to fix plot in report'

<!-- ________________________________________________________________ -->

<!-- Reverting a commit
You have added one more row of participant data to mental_health_survey.csv. However, you've now realized that you put the data in the wrong order.

In this exercise, you will revert the state of your repo to that of the previous commit.

Revert mental_health_survey.csv to the state in the last commit, using an appropriate flag to avoid opening the text editor. -->

git revert HEAD --no-edit -- mental_health_survey.csv
