# VABT (Veterans Affairs Benefits Tracker) 

VABT is a web application for student veterans under the Military and Veterans Affairs Program at New Mexico State University. It is a system designed for ease of use for both the MVP employees and students. The main task of VABT is to help in certifying offical forms that NMSU requires for students to receive their benefits for schooling. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. There are two ways to go about installing this system, with our .sln file for visual studio, or through the command line.

#### Visual Studio

This method is as easy as cloning the repo to your local machine and opening the .sln file with Visual Studio

#### Command Line 

First, clone the repository to your local machine:

```bash
git clone https://github.com/McGovern95/VABT.git
```
###### From within the VABT directory

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## Documentation

All code documentation is through our admin interface. Please log in as a super user and click on the top right - "Documentation"


## Deployment

Additional development time is needed to deploy to a live server. 

## Built With

* [Django](https://www.djangoproject.com/start/overview/) - The web framework used
* [Visual Studio](https://visualstudio.microsoft.com/) - The IDE used

## User Guide

~ link to our user guide 

## Authors

* **Christian McGovern** - *Full Stack* - [McGovern95](https://github.com/McGovern95)
* **Joshua Rosencrans** - *Full Stack* - [rosencrans24](https://github.com/rosencrans24)
* **Ian Navarro** - *Full Stack* - [iannava13](https://github.com/iannava13)


## Acknowledgments

* MVP 
* NMSU 
* **Dr. William Hamilton** - *Senior Project Mentor* - [bilhamil](https://github.com/bilhamil)

