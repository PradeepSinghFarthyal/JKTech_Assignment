## `JKTech_Assignment` setup Guide

## Clone Git repository:

 `git clone https://github.com/PradeepSinghFarthyal/JKTech_Assignment.git`
 
## Setup Environment and Insatll Dependencies:

### Install virtual enviournment
>`pip install virtualenv`

>https://www.geeksforgeeks.org/python-virtual-environment/

#### Create virtual envoiurnment

```python -m venv <env_name>```
  
#### Activate virtual envoiurnment

```source <env_name>/bin/activate```

#### Install requirements / Dependencies

>`pip install --upgrade pip`
> 
>`pip install -r requirements.txt`

## Database Installation

>`update DB details in settings file`

## Update .env file:

>`update necessery details`

## Create DB Tables:

>`python manage.py makemigrations`
> 
`python manage.py migrate`

  
## Run Server:

>`python manage.py runserver`
> 
>OR
> 
>`python manage.py runserver host:port`


# Docker

Navigate to project directory. 
`Note:-` It should contain a Dockerfile. Navigate to project directory. 

# Run 
> docker build -t `image_name` .

### Steps to run Docker Image
Run 

`docker run  --name [ container_name ]  [docker _image]` . 


