# Login_with_outlook 

Develop an Microsoft Outlook OAuth system that enables users to both login and sign up while ensuring
the continuous management of user sessions and authentication tokens


## Table of Contents

- [Introduction]
- [Prerequisites]
- [Getting Started]
  - [Installation](#installation)
  - [Running the Application](#running-the-application)

## Introduction

The project aims to develop a robust Microsoft Outlook OAuth system, providing seamless user authentication and registration functionalities akin to popular "Sign up with Google" services. Implemented with Python, Django, and DRF, it ensures secure management of user sessions and authentication tokens, while adhering to coding standards and proper documentation. Additionally, the system supports scalability and offers bonus features including comprehensive API testing, user interface development, and an architecture diagram illustrating system components and interactions.

## Prerequisites

List the prerequisites required to run your project, such as:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Enable kubernetes
-Python 3.x installed
-Django web framework installed
-Knowledge of Django Rest Framework (DRF)
-Familiarity with relational databases (PostgreSQL or MySQL)
-Understanding of OAuth authentication flow
-Proficiency in using Git for version control
-Basic knowledge of front-end technologies if UI development is included (HTML, ReactJS, NextJS, AngularJS, or VueJS)
-Postman or Insomnia for API testing
-Optional: Experience with unit testing in Django
-Optional: Knowledge of system architecture design and schema modeling

## Getting Started

Through this you will be able to login with outlook account

### Installation and login in outlook

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/anshupy-09/django_outlook_project.git
   cd outlook 


2. Run with docker 
    Docker Compose up

4. Go to the URL 
   4.1: http://localhost:8000/home/
   4.2: Click on the Sign in on the upper signin
   4.3: Click on the Microsoft Graph
   4.4: Using the Sign in with Microsoft Graph Click continue
   4.5: Signin in your Microsoft outlook account


5. check the Scaling in the Kubernetes
   5.1 Go to the outlook/deployment
   5.2 Kubectl apply -f django_deployment  
   5.3 kubectl apply -f postgres 





   



