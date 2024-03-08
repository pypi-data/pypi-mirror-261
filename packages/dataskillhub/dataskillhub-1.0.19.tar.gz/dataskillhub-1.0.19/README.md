# Projet Dossier Compétence

## Table of contents

- [Installation for DEV](#installation-for-dev)
  
- [Installation for USER](#installation-for-user)
  
- [Usage](#usage)
  
- [Example](#example)
  
***

## Installation for DEV

**Clone the repository and install dependencies:**

```
$ git clone https://gitlab-datalyo.francecentral.cloudapp.azure.com/dossier-de-comp-tences/dossiercompetence.git
```

**If the clone is successful, enter ```ls``` and you will see a folder named 'dossiercompetence', as shown below:**

```
$ ls
>>  dossiercompetence
```

**Change into the example folder:**

```
$ cd dossiercompetence/
```

**Create a python virtual environment for the project:**

```
$ python3 -m venv .venv
```

**If the environment is created successfully, enter `ls -a` and you will see a folder named '.venv', as shown below:**

```
$ ls -a
>> .   .git        .gitlab-ci.yml  .venv        README.md  data_skill_hub  dossiercompetence.egg-info  setup.py         src
..  .gitignore  .pytest_cache   MANIFEST.in  build      dist            requirements.txt            sources_exemple  test

```

**Active the environment:**

```
$ source .venv/bin/activate
```

**Install modules:**

```
$ pip install -r requirements.txt
```

**Copy the required static files to the local computer.:**

```
$ python -m data_skill_hub.main init
>> dossier créé
>> fichiers prêt
```

**Now you have all for run this projet 😊**

**Enter the folder where ``main.py`` is located and you can follow [Example](#example) for run it:**

```
$ python -m data_skill_hub.main consultant export plop.pipo
```

***

## Installation for USER

**Create a folder, for example named 'test' :**

```
$ mkdir test
```

**Go into this folder:**

```
$ cd test
```

**Create a python virtual environment for this upcoming projet:**

```
$ python3 -m venv .venv
```

**Active the environment:**

```
$ source .venv/bin/activate
```

**Install the projet:**

```
$ pip install dossiercompetence
```

**Copy the required static files to the local computer.:**

```
$ dossier_competence_copy_file
>> dossier créé
>> fichiers prêt
```

**Now you can use it like as shown below, or you can follow [Example](#example) for run it:**

```
$ dossier_competence -i "plop.pipo/CV_modele.md" -style  "file_static/test.css" -all

```

***

## Usage

```
usage: 

>> data_skill_hub init

Equipé des documents requis.

>> data_skill_hub consultant export [nom.prenom]

Convertir le fichier Markdown en fichier HTML ou PDF.

```

***

## Example

```
$ python -m data_skill_hub.main consultant export plop.pipo

```