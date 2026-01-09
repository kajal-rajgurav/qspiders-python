
Git HUB

git add . // to stage all the changes 
git commit -m "message" // to commit changes
git push  // it saves the changes locally (not goes to git hub)
git push origin daily_practice  // to push your change to the github

// daily merge
git checkout main
git merge daily_practice
git push origin main

today is a day
n=5
for i in range(1,n+1)
    for j in range(i)
print(i,j)