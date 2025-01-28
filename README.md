# Cat Lovers

![Cat Lovers responsive screenshot](https://github.com/tomokoelif/cat_lovers/blob/main/screen.png)

## Introduction

Cat Lovers is a social media and booking app for a cat rescue organization. Cat Lovrs was developed as my second project as part of the Full-Stack Developer course at Code Institute. It focuses on Django and Bootstrap frameworks, database operations and CRUD functionality. For educational purposes only.

View live site here : [Cat Lovers](https://cat-lovers-a986f59e9649.herokuapp.com/)  
  
For Admin access with relevant sign-in information: [CatLovers Admin](https://cat-lovers-a986f59e9649.herokuapp.com/admin/)

<hr>

## Table of Contents

- [Cat Lovers](#Cat Lovers)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Epic - User Profile](#epic---user-profile)
    - [Epic - Articles](#epic---articles)
    - [Epic - Booking](#epic---booking)
    - [Epic - Photo Gallery](#epic---photo-gallery)
    - [Epic - Visit Us/Reviews](#epic---visit-usreviews)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Feature Showcase](#feature-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Elephant SQL](#elephant-sql)
  - [Heroku deployment](#heroku-deployment)
  - [Clone project](#clone-project)
  - [Fork Project](#fork-project)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)

## Overview

Cat Lovers is a social media and booking app for cat rescue organizations. Users can:

 -Join the Cat Lovers community
 -Create your own profile
 -Add and interact with posts
 -Create and manage reservations
 -Upload photos
 -Learn more about Cat Cafe, Cat Hotel

Cat Lovers is accessible from all browsers and is fully responsive on different screen sizes. Its purpose is to create a safe and informed community where cat lovers can browse cute cat photos, interact with each other at Cat Cafe, and make essential bookings for Cat Hotel reservations. I created this site to help people find homes for rescue cats. I want people to first get interested in the photos on the site, play with the cats at the cat cafe, and then become a foster parent. I also run a cat hotel where you can leave your own cat while traveling.

Cat Lovrs allows you to book a cat hotel for a night or a month through a basic booking system.
In future developments of this project, I would like to provide users with an upgraded booking system with payment options, and the opportunity to connect with other cat lovers who have compatible cats through adding friends and direct messaging.

### Colour Scheme
In keeping with the theme of animal welfare, I chose wood colors that evoke nature.:
- **Primary Color:** #00660A (Green)
- **Secondary Color:** #664D00 (Brown)
- **Button Color:** #1C55A6 (Blue)
- **Button Color:** #B60202 (Red)
- **Background:** #FFFFFF (White)
This combination ensures clarity, accessibility, In keeping with the theme of animal welfare appearance, allowing for easy navigation throughout the site.

### Font
- For the logo and headers, I will be using **Cursive**.
- The rest of the body text and interactive elements will use **Catamaran** for its readability and clean look.

## Project Planning
Cat Lovers' main goal is to support rescued cats and find them homes. We protect cats that would have been euthanized and upload photos of rescued cats every week, or meet them at a cat cafe to help them find homes that will take good care of them
### Strategy Plane
Cat Lovers' main goal is to support rescued cats and find them homes. We protect cats that would have been euthanized and find homes to care for them. We upload photos of rescued cats every week and make it easy for interested people to comment. Users can send us an email, interact with them at the cat cafe, and become their foster parents.

### Site Goals
- Provides a platform where cat lovers can always see fun photos.
- Provides a Cat Hotel where you can leave your cat while traveling, and can easily book from the site.
- Communication between users and administrators is easy, and commenters can edit or delete their comments, and administrators of posts with comments can hide comments until they are approved.

### Agile Methodologies - Project Management
I used an agile approach to project management. The Cat Lovers development process was broken into sprints, and tasks were added to the GitHub project board to be tracked and managed through issues.

### MoSCoW Prioritization
- **Must-Haves:** User registration and login, Hotel booking, Post article and photo, comment function, contact function.
- **Should-Haves:** Feedback system, health tools, advanced filtering options.
- **Could-Haves:** Profile pictures for users and specialists, messaging system.
- **Won’t-Haves:** Full payment integration, doctor-patient messaging for now.
  https://github.com/users/tomokoelif/projects/6

