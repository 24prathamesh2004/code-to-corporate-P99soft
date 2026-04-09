# Git Commands Quick Guide

## Initialization
git init  
Initialize a new repository

git clone <url>  
Clone a remote repository

---

## Basic Workflow
git status  
Check file status

git add .  
Stage all changes

git add <file>  
Stage specific file

git commit -m "message"  
Commit changes

git push origin <branch>  
Push to remote

git pull origin <branch>  
Pull latest changes

---

## Branching
git branch  
List branches

git branch <name>  
Create branch

git checkout <branch>  
Switch branch

git checkout -b <branch>  
Create and switch branch

git merge <branch>  
Merge branch

git branch -d <branch>  
Delete branch

git push origin --delete <branch>  
Delete remote branch

---

## Rebase
git rebase <branch>  
Reapply commits on another branch

git rebase -i HEAD~n  
Interactive rebase

git rebase --continue  
Continue after conflict

git rebase --abort  
Cancel rebase

---

## Reset and Undo
git reset --soft HEAD~1  
Undo commit keep changes staged

git reset --mixed HEAD~1  
Undo commit unstage changes

git reset --hard HEAD~1  
Remove commit and changes

---

## Amend
git commit --amend  
Modify last commit

---

## Stash
git stash  
Save changes temporarily

git stash apply  
Restore stash

git stash pop  
Restore and remove stash

---

## Logs and History
git log  
Full history

git log --oneline  
Short history

git reflog  
Track all actions

---

## Diff
git diff  
Show unstaged changes

git diff --staged  
Show staged changes

git diff <branch1> <branch2>  
Compare branches

---

## Cherry Pick
git cherry-pick <commit>  
Apply specific commit

---

## Ignore
.gitignore  
Exclude files from tracking

---

## Merge Conflicts
Resolve conflicts manually in files  
git add .  
git commit  

---

## Recovery
git reflog  
Find lost commits

git checkout -b <branch> <commit>  
Recover branch from commit

---

## Best Practices
Keep commits small  
Write clear messages  
Use branches for features  
Avoid force push on shared branches  