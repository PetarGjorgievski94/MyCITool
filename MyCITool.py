import os
from time import sleep
import requests
from git import Repo

def get_repo():

    # Getting the repository
    repo = input("Enter a repository URL: \n") 
    branch_name = input("Enter your working branch: \n" )
    Repo.clone_from(repo, './crazylabs_demo/')

    # Checking targeted branch and pulling latest code
    os.chdir('./crazylabs_demo')
    os.system('git checkout '+branch_name)
    os.system('git pull')

    # Building and running container
    os.system('docker build -t crazylabs_demo .')
    os.system('docker run -d -it --entrypoint=python -p 8080:8080 crazylabs_demo src/main.py')

    # Checking responses
    sleep(5)
    print("Request homepage\n")
    try: 
        r = requests.get('http://localhost:8080')
        if r.status_code == 200:
            print('App is running on http://localhost:8080 \n') 
            print(r,"\n")
    except:
        print('An error was detected while performing "request homepage" check \n')
    
    print("Running selftest request \n")
    try:
        r = requests.get('http://localhost:8080/selftest')
        if r.status_code == 200:
            print('Self test successfull \n')
            print(r,"\n")
    except:
        print("Error while running 'selftest' \n")

    print("Running metrics request\n")
    try:
        r = requests.get('http://localhost:8080/metrics')
        if r.status_code == 200:
            print("Metrics request succesfull\n")
            print(type(r))
            print(r,"\n")
    except:
        print("Error while running 'metrics' request \n")


if __name__ == "__main__":
    get_repo()
