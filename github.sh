#!/bin/sh

# migrate your repo

git remote add github https://github.com/username/repo.git
git push --mirror github
git remote set-url origin https://github.com/username/repo.git
git remote rm github