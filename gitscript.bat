@echo on  

ECHO GIT ADD .
git add .

ECHO GIT COMMIT -m "blah"
git commit -m "blah"
ECHO GIT PUSH
git push origin
ECHO GIT STATUS
git status

