================examples github =======================
echo "# myFirstTestGit" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/gjdragon/myFirstTestGit.git
git push -u origin main

=====K learning ======
git help config
git status
git add filename
git --cached filename

git add .
git commit -m "First message"
git diff

git add file_name
git restore --staged file_name
git commit -a -m "update comments"

git log
git log --oneline
#update the last commit message
git commit -m "change file name to real" --amend
git log -p

git branch tmpbugfix
git branch
git switch tmpbugfix
git branch
git commit -a -m "bug fix in tmp branch"
git switch main
git merge -m "merge fix to main" tmpbugfix
git branch
git rm branch tmpbugfix
#sync to github
git push -u origin main









