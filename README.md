# Intro To Database

Introduction to Database Course Materials

## Software Tools

- Docker, git, python3, sqlite3, Jupyter notebook, DBeaver Community, MongoDB, etc.

## Run Jupyter Notebook

### Local System

- install python and jupyter notebook on your system
- clone this repository
- run jupyter notebook from within the repository folder

```bash
$ jupyter notebook
```

### Using Docker Containter

#### Initial setup

- Install Docker Desktop: [https://docs.docker.com/desktop/](https://docs.docker.com/desktop/)

- On Windows System, it takes a bit of extra work:

  1. Install git along with git-bash: [https://git-scm.com/download/win](https://git-scm.com/download/win)
  2. Follow the instructions here: [https://www.makeuseof.com/how-to-install-docker-windows-10-11/](https://www.makeuseof.com/how-to-install-docker-windows-10-11/)

- Create a course folder
    - e.g., `Users/<username>/<semester>/<course>`
    - `Users/rbasnet/fall2023/intro-database`
    - NOTE - course folder must be lowercase as it's the name used for docker image

- Copy all the files (except README.md) from python folder into your course folder

- Using a Terminal (git-bash on Windows) do the following:

    - change working directory to your course folder
    
    ```bash
    $ cd <Users/rbasnet/fall2023/beg-python>
    $ pwd
    $ ls
    ```

    - run the run.sh script using bash program

    ```bash
    $ bash run.sh
    ```
    - if all goes well, you'll see a Ubuntu Bash Terminal
    - Note that the initial setup may take some time to build docker image.
    - type the following for a quick test:

    ```bash
    $ uname -a
    $ pwd
    $ ls
    $ sqlite3 --version
    $ python --version
    $ python hello.py
    ```

- Clone the course jupyter notebook repository

#### Run Jupyter Notebook server

- Open a Terminal (git-bash on Windows)
- Change current working directory to your course folder
  
  ```bash
  $ cd intro-database
  ```

- Run run-jupyter.sh script

  ```bash
  $ bash run-jupyter.sh
  ```

- Press Ctrl+C to quit the jupyter notebook server
- Copy the URL to the browswer
