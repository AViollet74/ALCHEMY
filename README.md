# project-template
Template repostiory for accelerate your project

## Work on your project
1) Activate the environement
```bash
workon ALCHEMY
```
2) If you want to deactivate the environnement
```bash
deactivate
```
3) To list all the current module on the environnement
```bash
pip freeze
```
## Installation
- Clone the repo

```bash
git clone https://github.com/edouardkoehn/WM_Atlas.git
```
- Create your virtual env
```bash
mkvirtualenv ALCHEMY
```
- Install poetry
```bash
pip install poetry
```
- install the modul and set up the precommit
```bash
poetry install
```

## Managing dependancies
- to add an dependancy with poetry for exemple numpy
```bash
poetry add numpy
```
It would automatically install and udpate the pyproject.toml file. If you didn't specifie it, it would add it to the tool.poetry.dependencies.


## Working with git
1) Check wich files have been modified:
```bash
git status
```
2) Add the modified files to your working tree:
```bash
git add edi_bg.py
```
3) Commit the changes on the working tree:
```bash
git commit -m "J'aimes les mouches"
```
4) Push your new code on the server:
```bash
git push
```
If you have any issues: 1) Read the error and google it 2) Use git status to ensure that all the modified files have been save 3) Cry if you see the error conflict.