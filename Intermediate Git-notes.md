<!-- Creating new branches
You are working on updates to the DataCamp website, inside of a Git repo called datacamp.

You've been working in the main branch of your repo, but you now know that you should create a new branch for a specific task and make edits to your project there instead.

You have unsaved changes in main, so you're going to save those, then move into the llm-upgrade branch to look into improving the relevance of the responses that the AI model returns to users.

Add the updated file main.py to the staging area.
Make a commit with the log message "Update source code".
In a single command, create and move to a new branch called llm-upgrade. -->

git add main.py
git commit -m "Update source code"
git switch -c llm-upgrade

<!-- _____________________________________________________ -->

<!-- Checking the number of branches
You've seen how to create new branches and develop in them, but it's also important to be able to identify the number of branches in a repo so you can keep track of concurrent development across your project.

You are in the datacamp repo.

How many branches are there? -->

git branch

<!-- _____________________________________________________ -->

<!-- Renaming branches
You receive a service desk ticket fw2959 highlighting an issue with how bold text renders on the website.

You decide to create a new branch for this work, but, in your haste, you've chosen the branch name txt.

While you think this branch name should be clear to your colleagues, they've expressed confusion about what this branch represents.

As a general rule, when working on a ticket in your company, the branch should include the ticket number at the start of the branch name. You decide it is best to rename it for consistency and clarity.

Change the name of the txt branch to fw2959-text-bug. -->

git branch -m txt fw2959-text-bug

<!-- _____________________________________________________ -->

<!-- Deleting branches
Generally, branches aren't deleted until the contents have been merged back into the main branch (or wherever the live system lives).

However, it's worthwhile knowing how to delete a branch that has not been merged, in case you find the scope of your project changing and a specific branch's contents are no longer required.

Forcibly delete the llm-upgrade branch from your repo. -->

git branch -D llm-upgrade

<!-- _____________________________________________________ -->

<!-- Comparing branches
If you're working across multiple branches then you may want to compare the state of repos between branches from time to time.

You are in the datacamp repository and would like to compare two branches.

Execute a command to compare the front-end and documentation branches. -->

git diff front-end documentation

<!-- _____________________________________________________ -->

<!-- Merging two branches
You've updated some code in the ai-assistant branch, and now need to merge ai-assistant into main to keep it accurate and up to date.

You are currently in the main branch.

Merge the ai-assistant branch into the main branch. -->

git merge ai-assistant main

<!-- _____________________________________________________ -->

<!-- Resolving a merge conflict
You are in the main branch, and want to merge your recent edits from the documentation branch.

Merge the documentation branch into your current branch, main.
Edit task_list.txt, removing the conflict syntax and saving so it contains the content listed in the Context section; the final document should look like this:
TODO: Add unit tests
TODO: Increase font size on courses pages -->

git merge documentation
nano task_list.txt

<!-- _____________________________________________________ -->

<!-- Cloning a repo
You are making local back-up copies of all your Git repos, which you will then move to cloud storage.

You want to start by cloning the datacamp Git repo into your current directory, archive.

Clone /home/repl/datacamp in your current directory. -->

git clone /home/repl/datacamp

<!-- _____________________________________________________ -->

<!-- Defining and identifying remotes
Now that you have cloned the repo locally, you decide you want to name the remote as back-up so you can quickly identify remotes going forward.

Add the name back-up for the /home/repl/datacamp repo.
List all remotes including their URL(s). -->

git remote add back-up  /home/repl/datacamp
git remote -v

<!-- _____________________________________________________ -->

<!-- Fetching from a remote
If you are not sure how the contents of a remote repo compare to your local repo, then you can gather the remote contents from a specific branch and then compare them to your local branch.

Your colleague John has set up a remote repo so that his work is backed up in the cloud and accessible to others.

Run a command to find out the name(s) of remote repos linked to your project.
Fetch from the remote origin repo into your local main branch. -->

git remote -v
git fetch origin main

<!-- _____________________________________________________ -->

<!-- Pulling from a remote
Fetching is great, but this only updates local references to a remote repo.

If you want to develop on top of your remote repo's contents then you need to synchronize the contents with your local repo before you can continue to edit.

Pull the remote origin repo's front-end branch into your current local branch.
Compare origin's main branch with your local branch. -->

git pull origin front-end
git diff origin front-end

<!-- _____________________________________________________ -->

<!-- Pushing to a remote
You've been working in the documentation branch of the dc-back-up repo.

All of your local changes have been saved and you're ready to push your local changes to the origin remote.

Push your local documentation branch to the origin remote repo. -->

git push origin documentation
