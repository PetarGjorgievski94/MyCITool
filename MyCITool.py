import os
from git import Repo

def get_repo():
    repo = input("Enter a repository URL: \n")
    Repo.clone_from(repo, './crazylabs_demo/')
    os.chdir('./crazylabs_demo')
    os.system('make -f Makefile build')
    os.system('make -f Makefile run')

get_repo()