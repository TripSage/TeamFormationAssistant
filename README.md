[![Build Status](https://travis-ci.com/TripSage/TeamFormationAssistant.svg?branch=master)](https://travis-ci.com/TripSage/TeamFormationAssistant)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4135147.svg)](https://doi.org/10.5281/zenodo.4135147)
[![Coverage Status](https://coveralls.io/repos/github/TripSage/TeamFormationAssistant/badge.svg)](https://coveralls.io/github/TripSage/TeamFormationAssistant)
[![Maintainability](https://api.codeclimate.com/v1/badges/12e167617376b4d23a0a/maintainability)](https://codeclimate.com/github/TripSage/TeamFormationAssistant/maintainability)
![GitHub issues](https://img.shields.io/github/issues-raw/TripSage/TeamFormationAssistant)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/TripSage/TeamFormationAssistant)
# Team Formation Assistant

## Table Of Contents
1. [Video](#Video)

2. [Why?](#Problem-Statement)

3. [What?](#Project-Objectives)

4. [How?](#Project-Structure)

5. [Documentation](https://github.com/TripSage/TeamFormationAssistant/wiki)

6. [Test Plan](https://github.com/TripSage/TeamFormationAssistant/wiki/Test-Plan)

## Video
[<img src = "https://github.com/TripSage/TeamFormationAssistant/blob/master/Assets/Video.png">](https://youtu.be/jtYDAEjDmlM)
</br>
</br>
</br>
## Problem Statement              
Build an assistant which will take the project requirements, team members
availability, skill level, tools preferred, etc. as input and assigns the members for
the new team.
<br/>
## Project Objectives
➢ Design a form for the user to enter data<br/>
➢ Design a dashboard to showcase the generated team assignments<br/>
➢ Create and Manage a database with team members, Projects, Assignments
data.<br/>
➢ Write an algorithm which will take the project requirements, team
members availability, skill level, tools preferred, etc. as input and assigns
the members for the new team.<br/>

## Project Structure
### Algorithm Implementation
We plan to code the application in Python3. Python ML libraries will be used for
Cluster identification.<br/>
### Database Implementation:
We plan to store team members into an MySQL with Fallback to AWS database. Python files import the
data and process it and store the final result back to the database.<br/>
### Frontend Implementation:
Team members will be able to submit a form to consider them as part of project
assignment. Final team assignment will posted on the homepage dashboard. We plan to
implement the dashboard and form using HTML, CSS, JavaScript

##### We have created a wiki page containing project details including project workflow, setup, and Test Plan 
### [Wiki](https://github.com/TripSage/TeamFormationAssistant/wiki)

Here are a few screenshots of the project<br>
![](https://github.com/TripSage/TeamFormationAssistant/blob/master/Assets/ss1.jpeg)<br>
![](https://github.com/TripSage/TeamFormationAssistant/blob/master/Assets/ss2.jpeg)<br>
![](https://github.com/TripSage/TeamFormationAssistant/blob/master/Assets/ss3.jpeg)


