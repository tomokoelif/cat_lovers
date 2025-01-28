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

 - Join the Cat Lovers community
 - Create your own profile
 - Add and interact with posts
 - Create and manage reservations
 - Upload photos
 - Learn more about Cat Cafe, Cat Hotel

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
  
![Color contrast](https://github.com/tomokoelif/cat_lovers/blob/main/color.png)  
This combination ensures clarity, accessibility, In keeping with the theme of animal welfare appearance, allowing for easy navigation throughout the site.

### Font
- For the logo and headers, I will be using **Cursive**.
- The rest of the body text and interactive elements will use **Catamaran** for its readability and clean look.

## Project Planning

### Strategy Plane
Cat Lovers' main goal is to support rescued cats and find them homes. We protect cats that would have been euthanized and find homes to care for them. We upload photos of rescued cats every week and make it easy for interested people to comment. Users can send us an email, interact with them at the cat cafe, and become their foster parents.

### Site Goals
- Provides a platform where cat lovers can always see fun photos.
- Provides a Cat Hotel where you can leave your cat while traveling, and can easily book from the site.
- Communication between users and administrators is easy, and commenters can edit or delete their comments, and administrators of posts with comments can hide comments until they are approved.

### Agile Methodologies - Project Management
I used an agile approach to project management. The Cat Lovers development process was broken into sprints, and tasks were added to the GitHub project board to be tracked and managed through issues.

### MoSCoW Prioritization
- **Must-Haves:** User registration and login, Post article and photo .
- **Should-Haves:** messaging system, comment system.
- **Could-Haves:**  Hotel booking system, Comment delite Edit function.
- **Won’t-Haves:** Full payment integration, All user can post photo.  
  https://github.com/users/tomokoelif/projects/6

### Sprints
- **Sprint 1:** Initial Setup - Project, repository, environment setup.
- **Sprint 2:** User Authentication & Log in, Log out system.
- **Sprint 3:** Messaging & comment system.
- **Sprint 4:** Booking system, comment edit delite functions.
- **Sprint 5:** Deployment & Testing.

## User Stories
- As a user (user/admin), I want to register and log in securely so that I can access my registration site and manage my activities.
- As a user, I want to contact to Cat Lovers. So I can submit a request for collaboration
- As a user, I want to comment to the posts. So I can writet a comment and edit and delete.
- As a user, I want to book the cat hote, So I can book by booking site.
- As a visitor, I want to see a well-designed home page that introduces Cat Lovers so that I understand the platform's purpose and value.
- As a Site Admin I post the photos and change about site. So I can manage the photo and article of the site.
- As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

## Scope Plane
The Cat Lovers platform will include the following MVP functionalities:
- User registration.
- Post photos and articles.
- Comment to the post. And user can edit and delete without admin site.
- Booking site.

## Structural Plane
The site is structured around an easy-to-use interface. The primary menu includes links to Post, About, hotel bookings.

## Skeleton & Surface Planes

### Wireframes
Wireframes were created for the following key pages to ensure an intuitive user journey:
- **Home Page**

![Homepage Wireframe](https://github.com/tomokoelif/cat_lovers/blob/main/Cat%20Lovers%20PC%20Home.png)

![Homepage Wireframe](https://github.com/tomokoelif/cat_lovers/blob/main/Cat%20Lovers%20mobile%20Home.png)

- **Specialist Search Results**

![Homepage Wireframe](https://github.com/tomokoelif/cat_lovers/blob/main/Cat%20Lovers%20PC%20About.png)

![Homepage Wireframe](https://github.com/tomokoelif/cat_lovers/blob/main/Cat%20Lovers%20mobile%20About.png)

- **Appointment Booking**

![Homepage Wireframe](https://github.com/tomokoelif/cat_lovers/blob/main/Cat%20Lovers%20PC%20Book.png)

![Homepage Wireframe](https://github.com/tomokoelif/cat_lovers/blob/main/Cat%20Lovers%20mobile%20Book.png)

- **Appointment Booking**

![Homepage Wireframe](https://github.com/tomokoelif/cat_lovers/blob/main/Cat%20Lovers%20PC%20Form.png)

![Homepage Wireframe](https://github.com/tomokoelif/cat_lovers/blob/main/Cat%20Lovers%20mobile%20Form.png)

Wireframes were designed using [Balsamiq](https://balsamiq.com/), ensuring responsiveness across devices.

## Database Schema - Entity Relationship Diagram
Cat Lovers' ERD shows relationships between users, admins, reservations, etc. This is essential to show the relationships between the various models in the PostgreSQL database.

The ERD also shows the role-based structure of the platform. Each user is assigned to a specific group (unregistered, registered admins) that determines their level of access. Unregistered and registered users models are linked to the user model, and each profile type has specific fields related to its role. Administrators have broader access to manage both registered users and platform data.

![ERD Illustration](docs/erd/erd-healmate.png)

The above ERD was generated using Python Extension - pygraphviz and pydotplus. Documentation at https://django-extensions.readthedocs.io/en/latest/graph_models.html.

## Security
All data is securely handled with Django’s security features, including:
- CSRF protection for form submissions.
- Data encryption for sensitive information like passwords using Django's built-in authentication.
- Role-based access control to restrict sensitive data to authorized users.

Role-based access control (RBAC) is implemented using Django's Group and Permission systems. Patients, specialists, and admins are grouped based on their role, and their access to features and sensitive information is restricted accordingly. Patients can only access their own medical data and booking history, while specialists can only view data related to their consultations. Admins have the broadest access for system management.

## Features

## User View - Registered/Unregistered

It was important to me from the beginning that FreeFido be accessible to an unregistered user, in some capacitites. I wanted the website to sell the product to a new user quickly by immediately inviting them into the community through the park's information, articles and gallery sections. The following is a breakdown of the site's accessibility for registered/unregistered users:

| Feature   | Unregistered User | Registered, Logged-In User |
|-----------|-------------------|-----------------|
| Home Page | Visable           | Visable         |
| Profile   | Not Visible - 'Profile' icon only appears for registered, logged-in users | Visable and full feature interaction available |
| Articles  | Visable but not interactable via 'Likes/Comments', 'Add Article' button not visible | Visable and full feature interaction available |
| Booking   | Icon visible but redirected to Sign In page/Sign Up through link | Visable and full feature interaction available |
| Gallery   | Visable but no option to 'Add Photo' | Visable and full feature interaction available |
| Visit Us  | Visable and map interaction available | Visible and map interaction available |

## CRUD Functionality

Users are able to Create, Read, Update and Delete their shared information on FreeFido. Some features make full CRUD functionality available, whilst others present the necessary options only. Here is my CRUD breakdown for FreeFido:

| Feature | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Profile | Created upon registration | Yes | Yes | Full Profile deletion is currently only available to Admin upon User Account deletion, the profile dashboard clears automatically if a user removes all of their articles or bookings |
| Articles | Yes | Yes | Yes | Yes |
| Bookings | Yes | Yes | Yes | Yes |
| Gallery | Yes | Yes | No - this feature felt unneccessary as it's intention is a 'quick-sharing' of a photo, a minimal amount of information is required and users are able to delete the image if they wish | Yes |

### User View - Registered/Unregistered
HealMate offers distinct user views. Unregistered users can search for specialists, but registered users have full access to the appointment system and dashboard functionalities.

### User Registration Process
- **Patients:** When a new user registers, they are automatically assigned to the "Patient" group. This ensures that all users begin with patient privileges and access, allowing them to book appointments and view specialist profiles. During the registration process, essential patient profile information is captured (e.g., contact number, address, date of birth, gender). After the registration is complete, a corresponding PatientProfile is automatically created and associated with the user.

- **Specialists:** During the registration process, essential patient profile information is captured (e.g., contact number, address, date of birth, gender). After the registration is complete, a corresponding PatientProfile is automatically created and associated with the user.

- **Admins:** Admin accounts are created manually by other existing admins or superusers within the Django administration area. This ensures that the creation of administrative-level accounts is strictly controlled and follows the platform's internal policies.

This registration flow was chosen to ensure role-based control and security. Patients are the primary users of the platform, and allowing them to register freely makes the service accessible. However, specialists and admins require a higher level of trust and validation, so they undergo a manual vetting process. This ensures that only qualified professionals and authorized admins can manage sensitive tasks such as consultations and platform settings, which helps maintain the integrity and security of the system.

### Role-Based Dashboard Features

**HealMate includes role-based dashboards for different types of users:**
- **Patient Dashboard:** Allows patients to view their profile, manage appointments, and access medical records.

- **Specialist Dashboard:** Specialists can manage their availability, view and approve appointments, and review patient profiles.

- **Admin Dashboard:** Admins can manage users (patients, specialists) and vet specialist applications. They also have access to system-wide settings.

### Role-Based Navigation
(Not the same as Role-Based Dashboard Features)

The navigation bar in HealMate adapts dynamically based on the user's role. This feature ensures that users see only the relevant options for their role, improving usability and reducing clutter in the interface.

- **Specialists**: When logged in, specialists will only see links to their dashboard, profile, password change, and logout options. General site navigation like "Home," "About," or "Join Us" will be hidden.
- **Patients**: Logged-in patients have access to their dashboard, profile, password change, and logout options, while still seeing general navigation links like "Home" and "About."
- **Admins**: Admins will see their dedicated dashboard link and other relevant options.
- **Non-Authenticated Users**: Users who are not logged in will only see options to log in or register on the platform.

This role-based navigation provides a tailored experience for every user type, streamlining access to the most relevant pages.


### Soft Delete/Archiving for Patient Accounts
HealMate includes a soft delete mechanism to ensure data integrity and prevent accidental loss of important user information. Instead of permanently deleting accounts, users can request a soft deletion, which deactivates their account while retaining their data in the system.

**How It Works:**
- **Patient Account Deactivation:** Patients can request to have their account deactivated through a user-friendly option on their dashboard.
- **Data Preservation:** When a patient requests account deletion, their profile is marked as inactive rather than removed from the database. This means the patient’s information, appointments, and records remain available for future use or audit purposes.
- **Admin Reactivation:** Admins have the ability to reactivate patient accounts from the Django admin panel. This ensures that patients can return to the platform with all their previous data intact, avoiding any data loss or system disruptions.

**Benefits:**
- **System Integrity:** Prevents errors that could arise from full account deletions, such as broken relationships with other models (e.g., appointments, messages, feedback).
- **User Flexibility:** Patients can choose to deactivate their account temporarily and return at a later date without losing their medical history or profile information.
- **Security:** Only admins have the power to fully manage account reactivations, ensuring oversight and control over patient data.


### Appointment Booking System
HealMate allows patients to book appointments with specialists directly through the platform. The system includes:
- **Specialist Search**: Patients can search for specialists based on name, specialty, or location.
- **Book Appointment**: Patients can book an appointment directly from the specialist's profile page.
- **Appointment Management**: Specialists and patients can view and manage upcoming appointments through their respective dashboards.
- **Appointment Cancellation**: Patients and specialists have the ability to cancel appointments with a confirmation prompt.


### Messaging System
HealMate provides a secure messaging system for communication between patients and specialists:
- **Inbox**: Users can view received messages and reply to messages directly from their inbox.
- **Send Message**: Patients can send messages to specialists they have appointments with, and vice versa.
- **Message History**: All sent and received messages are stored and displayed in the user's message history.
- **Real-Time Messaging**: The system is designed to support real-time messaging between users.


### Profile Management
Each user can manage their profile through the dashboard:
- **Patient Profile**: Patients can view and update personal details such as contact information, medical history, and emergency contacts.
- **Specialist Profile**: Specialists can view and update their bio, specialty, location, and upload profile images.
- **Profile Images**: Specialists can upload and update their profile image, which appears on the search results and specialist details page.

### Confirmation Messages
- **User Feedback**: Confirmation messages are shown to users when important actions are performed, such as logging in, booking an appointment, or sending a message. These messages help ensure a smooth user experience by providing feedback on successful actions.

### CRUD Functionality

The following **CRUD** functionalities are implemented within HealMate:

- **Create**: Patients are automatically assigned a profile upon registration. This profile includes key fields such as contact information, address, and medical history.
  
- **Read**: Patients can view their profile and associated information, including medical history and emergency contact details, from their dashboard.

- **Update**: Patients have the ability to update their profile information, including personal data (e.g., contact number, address, and medical history), via a dedicated "Edit Profile" page.

- **Delete (Soft Delete)**: Patients can request to deactivate their account through a **soft delete** mechanism. This deactivation preserves the patient’s data within the system while preventing further access until reactivation by an admin. The admin can reactivate the account from the Django admin panel at any time, restoring full access for the patient.

This CRUD cycle is central to the **PatientProfile** model, ensuring that users can fully manage their personal information while providing system integrity with the soft delete functionality.


## Future Features
I plan to implement the following in future iterations:
- Push notifications for upcoming appointments.
- Integrate payment system for paid consultations.

## Technologies & Languages Used
- HTML5 - Markup language for structuring the website
- CSS3 - Styling language for designing the layout and visual aesthetics
- JavaScript - For interactivity and DOM manipulation on the frontend
- Python (Django) - Backend web framework for server-side logic and management
- PostgreSQL - Database management system for storing data
- Cloudinary - Cloud-based image storage solution
- Whitenoise - For serving static files directly from Django

## Libraries & Frameworks
- **Django** - Backend framework
- **Django Crispy Forms** - For elegant form rendering
- **Cloudinary** - Media storage
- **Whitenoise** - For serving static files

## Tools & Programs
- **GitHub Projects** - Project management and tracking
- **Heroku** - Deployment and hosting
- **Balsamiq** - Wireframes and design prototypes

## **Testing**

### **Validation Testing**

All code has been validated through:
- **HTML**: [W3C Markup Validator](https://validator.w3.org/).
- **CSS**: [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
- **Python**: PEP8 validation to ensure code quality.

![HTML validator test](docs/project-images/Screenshot%202024-10-04%20164347.png)

![CSS validator test](docs/project-images/Screenshot%202024-10-04%20164642.png)

### **User Testing**

- **Browser Compatibility**: The website has been tested on Chrome, Firefox, Safari, and Edge.
- **Responsiveness**: The platform has been tested on mobile, tablet, and desktop devices to ensure optimal performance.
- **Role-Based Dashboard Testing:** Each user type (patient, specialist, admin) was tested to ensure they were directed to the correct dashboard after login. Patients were assigned to the correct group during registration, and specialists were manually added by admins. The redirection logic was thoroughly tested by registering new users and ensuring role-based access was properly applied.
- **Automatic Assignment Testing:** Tests were conducted to verify that newly registered users are automatically assigned to the "Patient" group and that their PatientProfile was successfully created. This was confirmed through both the user interface and the Django admin panel.

### **Bugs**
- ### Bug Fix #1: `DISABLE_COLLECTSTATIC` Setting Causing Heroku Deployment Failure

**Issue:**  
During the deployment to Heroku, the following error occurred:

The error was caused by the absence of proper static file handling and a misconfiguration in the `INSTALLED_APPS` list in `settings.py`.

**Cause:**  
- The `DISABLE_COLLECTSTATIC=1` config variable was used in Heroku to prevent collectstatic from running during the initial setup.
- There was a duplicate entry for `django.contrib.staticfiles` in `INSTALLED_APPS`, which caused an error when trying to collect static files.

**Steps Taken to Fix:**
1. Fixed the duplicate `django.contrib.staticfiles` entry in `INSTALLED_APPS`.
2. Ensured the static and media handling was properly set up with Cloudinary and Whitenoise.
3. Deleted the `DISABLE_COLLECTSTATIC=1` from Heroku's Config Vars.
4. Deployed again, which successfully collected static files and completed the deployment.


### Bug Fix #2: Permission Issues with Dashboard Access

**Issue**

Users are unable to access the Admin, Patient, and Specialist dashboards even though they are assigned to the correct user groups in the Django admin panel. The application either throws a 403 Forbidden error or does not recognize the users' group memberships.

**Cause**

The issue seems to be related to incorrect handling of group membership checks in the views or misconfiguration of user group assignments within the Django admin panel.

### Steps Taken to Fix

1. **Investigate Group Check Functions**:
   - Reviewed the group-check functions (`is_admin`, `is_patient`, `is_specialist`) in `views.py` to ensure they correctly identify user groups.
   - Confirmed that the group names match those set in the Django admin.

2. **Validate Group Assignments**:
   - Ensured that users are properly assigned to the correct groups (Admin, Patient, Specialist) in the Django Admin panel.
   - Verified that the group names in the code match the group names set up in Django admin.

3. **Testing**:
   - Tested access with both existing and newly created users to ensure they can access their respective dashboards without issues.
   - Verified that group membership was properly recognized for all users.

4. **Revert Changes**:
   - Once the issue was resolved, reverted any temporary modifications to the views back to their original implementation.

5. **Verify Access Control**:
   - Tested edge cases, such as users without group assignments attempting to access dashboards, to ensure proper behavior.
   - Confirmed that custom `PermissionDenied` logic displayed the correct 403 error page for unauthorized access attempts.

**Outcome**

The problem was successfully resolved, allowing users to access their respective dashboards based on group membership without encountering 403 errors or redirection issues.

### Bug Fix #3: Form Not Visible on Homepage Due to Conflicting View Usage

### Issue
The form on the homepage not visible due to conflicting view usage. The homepage should display a form that allows users to search for specialists, but the form did not appear as expected.

### Cause
The conflict arises from the use of both a class-based `HomePage` view and a function-based `home` view. The class-based view does not properly pass the `specialties` context required to render the form on the homepage.

### Steps Taken to Fix

1. **Update URLs**:
   - Updated `core/urls.py` to replace the class-based `HomePage` view with the function-based `home` view to ensure the correct context is passed.

2. **Verify Context Passing**:
   - Verified that the `specialties` context was properly passed to `index.html` so that the form could display the list of specialties dynamically.

3. **Test Form Visibility and Functionality**:
   - Tested the homepage to ensure that the form was visible and correctly populated with the list of specialties from the database.

4. **Commit Changes**:
   - Added and committed the changes after confirming that the issue was resolved.

### Outcome
The form is now visible on the homepage and correctly displays the list of specialties, allowing users to search for specialists as intended. The conflict between the views was resolved by using the appropriate function-based view that properly passes the necessary context.


### Bug Fix #4: Signal Not Triggering on User Registration

### Issue
A Django signal intended to automatically assign new users to the "Patients" group and create a `PatientProfile` upon registration was not firing. This led to no profile being created and no group being assigned after user registration.

### Cause
The issue was caused by an incorrect configuration of the `AccountsConfig` class in `INSTALLED_APPS` in `settings.py` and missing signal imports in the `ready()` method of `accounts/apps.py`.

### Steps Taken to Fix

1. **Correct Configuration in INSTALLED_APPS**:
   - Updated `INSTALLED_APPS` in `settings.py` to reference `'accounts.apps.AccountsConfig'` instead of just `'accounts'`. This ensured that the custom AppConfig class was properly loaded.

2. **Add Signal Imports in `ready()` Method**:
   - Added a `ready()` method in `accounts/apps.py` to correctly import the signal handlers, ensuring they were registered when the app was loaded.

3. **Remove Debug Statements**:
   - Removed unnecessary print statements that were used for debugging to keep the code clean and efficient.

### Outcome
The signal is now correctly triggered upon user registration, resulting in the automatic assignment of new users to the "Patients" group and the creation of a `PatientProfile` as intended. The configuration in `INSTALLED_APPS` and signal registration were successfully fixed.


### Bug Fix #5: Specialist Availability Submission and Display Issues

### Issue
Specialists encountered multiple issues when trying to set their availability. Initially, a 405 Method Not Allowed error occurred upon form submission. After fixing that, the start time was not displayed on the specialist dashboard, while the end time appeared correctly.

### Cause
1. **405 Method Not Allowed**:
   - The `post` method was missing from the `SpecialistDashboardView` class in `dashboard/views.py`, resulting in the 405 error when attempting to submit availability.

2. **Missing Start Time**:
   - The `start_time` was not displayed on the specialist dashboard due to a missing template tag (`{{ availability.start_time }}`) in the "Your Availability" section.

### Steps Taken to Fix

1. **Handle POST Method in View**:
   - Added a `post` method to `SpecialistDashboardView` in `dashboard/views.py` to properly handle form submissions, resolving the 405 Method Not Allowed error.

2. **Fix Start Time Rendering in Template**:
   - Updated the specialist dashboard template to include the `{{ availability.start_time }}` tag, ensuring that both the `start_time` and `end_time` are displayed in the "Your Availability" section.

### Outcome
Specialists can now successfully submit their availability without encountering the 405 error. Both `start_time` and `end_time` are displayed correctly on the specialist dashboard, providing a complete view of their available times for appointments.


### Bug Fix #6: Incorrect Template Rendered for Specialist Search Results

### Issue
The incorrect template was being rendered for specialist search results on the HealMate platform. A secondary `search_results.html` template in a different directory was causing confusion, leading to a simplified search results page being displayed. Key features like specialist bio, profile image, and pagination were missing.

### Cause
An additional `search_results.html` template was located inside the global `/templates/specialists/` directory. This template had minimal content and was unintentionally overriding the correct `search_results.html` template in the `/specialists/templates/specialists/` directory.

### Steps Taken to Fix

1. **Isolate Problematic Template**:
   - Renamed the global `/templates/specialists/` directory to determine if it was the source of the issue.

2. **Confirm and Resolve Issue**:
   - After confirming the issue was caused by the additional template, deleted the `/templates/specialists/` directory and its contents.

3. **Verify Correct Template Rendering**:
   - Verified that the correct `search_results.html` template inside `/specialists/templates/specialists/` is now rendering, displaying all necessary features, including the specialist bio, profile image, and pagination.

### Outcome
The correct template for specialist search results is now rendering as intended. The page displays all relevant information, including specialist bio, profile images, and pagination, providing users with a complete view of search results.



## Deployment

All code for this project was written in Visual Studio/Gitpod as the integrated development environment. GitHub was used for version control, and the application was deployed to Heroku from GitHub.

### Pre-Deployment

To ensure a successful deployment to Heroku, the following practices are to be followed (Experience from previous Django projects):

- **Requirements File:** The `requirements.txt` file must be kept up to date to ensure all imported Python modules are configured correctly for Heroku.
- **Procfile:** A `Procfile` was added to configure the application as a Gunicorn web app on Heroku.
- **Allowed Hosts:** In `settings.py`, the `ALLOWED_HOSTS` list was configured to include the Heroku app name and `localhost`. Example format:
    ```python
    ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost']
    ```
- **Environment Variables:** All sensitive data such as the `DATABASE_URL`, `CLOUDINARY_URL`, and `SECRET_KEY` were added to the `.env` file, which is ignored by Git using `.gitignore`. These variables are added to Heroku manually through the Config Vars section.

### Deploying with Heroku

The steps for deploying to Heroku are as follows (Experience from previous Django projects):

1. **Create New App:** Log in to your Heroku account and click on the "Create New App" button.
2. **App Name:** Choose a unique name for your app.
3. **Select Region:** Choose the appropriate region (Europe was selected for this project).
4. **Create App:** Click the "Create App" button to proceed.
5. **Deployment Method:** In the "Deploy" tab, select GitHub as the deployment method.
6. **Connect to GitHub:** Search for the repository name and click "Connect".
7. **Manual or Automatic Deployment:** Select either manual or automatic deployment. Ensure the main branch is selected for deployment.
8. **Config Vars:** In the "Settings" tab, click "Reveal Config Vars" and input the required environment variables.
9. **Buildpack:** Select Node.js and Python as the buildpacks for your project.
10. **Deploy:** Once the configuration is complete, click the "Deploy Branch" button. After successful deployment, a "View" button will appear to take you to the live site.

The live link for this project can be found here: <a href="https://healmate-378e458234ec.herokuapp.com/" target="_blank">HealMate</a>

### Fork this Repository

1. Go to the GitHub repository.
2. Click the "Fork" button in the upper right-hand corner.

### Clone this Repository

1. Go to the GitHub repository.
2. Click the "Code" button at the top of the page.
3. Choose between 'HTTPS', 'SSH', or 'GitHub CLI' depending on your preference.
4. Click the copy button to copy the URL.
5. Open Git Bash.
6. Change the working directory to where you want to clone the directory.
7. Type:
    ```bash
    git clone https://github.com/easybulb/healmate
    ```
8. Press Enter to create the local clone.

**Note:** The difference between a clone and a fork is that with a clone, you need permission to push changes to the original repository, whereas a fork creates an entirely new project under your GitHub account.

## Privacy Policy

As part of my **HealMate** project, I am dedicated to ensuring that users’ personal data is handled responsibly. The following privacy practices outline how information is collected, used, and stored within this academic project.

- **Data Collection**: HealMate, as a project, collects personal data during user registration and profile setup. This includes:
  - First and Last Name
  - Contact Information (Phone Number, Email)
  - Date of Birth
  - Gender
  - Medical History
  - Emergency Contact Information

- **Data Usage**: The information gathered is used solely for educational purposes, including:
  - Managing user profiles.
  - Facilitating appointment bookings between patients and specialists.
  - Sending notifications related to appointments or system updates.

- **Data Sharing**: As this is a student project, personal data will not be shared with any third parties. It will only be used for demonstrating the functionality of the project. All information remains confidential and will not be distributed beyond the scope of the HealMate project.

- **Security**: While this project is intended for educational use, I strive to implement best practices for data security using the Django framework’s built-in tools. Personal information is securely stored in the database and protected against unauthorized access.

- **User Rights**: Users of this platform, as part of this project, have the right to request modifications or deletion of their data. For any requests or concerns about personal data usage in this project, please contact the project owner at the provided email address.

Since this is an educational project, the privacy and data handling policies may evolve over time as more features are added and refined.


## Credits

### Code
- **Django Documentation**: The official docs were invaluable in setting up the project structure and solving specific issues.
- **Django Crispy Forms Documentation**: Used to streamline form rendering.
- **Chatgpt AI**: For images and some coding ideas
- **Favicon.io**: For Favicon generation.
- **Google Fonts**: For typography.
- **Mark Brisco** - Code Institute: For general guidance.
- **Amy Richardson** - Code Institute: General guidance.

### Media
- Icons and images sourced from **Canva** and **ChatGPT**.
- ERD illustration was generated from **pygraphiz** - A django extension.

### Additional reading/tutorials/books/blogs
- **Django for Beginners** by William S. Vincent.

## Acknowledgements

I would like to extend my heartfelt gratitude to the following individuals and organizations whose support, guidance, and inspiration have been invaluable in the development of this project.

### Mentors and Advisors
- **Amy Richardson** – Sincere gratitude to Amy, our tutor and facilitator, whose unwavering guidance and expertise were pivotal throughout this journey. Her mentorship provided the clarity and support needed to navigate challenges, ultimately elevating the quality of this project. Her dedication and encouragement made a profound impact on my progress and learning.

- **Mark Briscoe** – A heartfelt thank you to Mark, our dedicated tutor, whose unwavering support, insightful feedback, and constructive criticism were instrumental in guiding this project to completion. His depth of knowledge and encouragement not only enhanced my understanding but also inspired me to consistently improve my work. This project would not have been the same without his invaluable mentorship.


### Supportive Friends and Family
- My friends and family, especially, for their encouragement and patience during this project. Your belief in me kept me motivated and focused.

### Academic Institutions
- **Code Institute** – Thank you for providing the learning environment and resources that made this project possible. I am especially grateful to the professors and staff at Code Institute for their valuable insights.

### Final Note
This project would not have been possible without the support, advice, and inspiration of each individual and organization mentioned. Thank you for being a part of this journey.




