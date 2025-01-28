# Cat Lovers

![Cat Lovers responsive screenshot](https://github.com/tomokoelif/cat_lovers/blob/main/screen.png)

## Introduction

Cat Lovers is a social media and booking app for a cat rescue organization. Cat Lovrs was developed as my second project as part of the Full-Stack Developer course at Code Institute. It focuses on Django and Bootstrap frameworks, database operations and CRUD functionality. For educational purposes only.

View live site here : [Cat Lovers](https://cat-lovers-a986f59e9649.herokuapp.com/)  
  
For Admin access with relevant sign-in information: [CatLovers Admin](https://cat-lovers-a986f59e9649.herokuapp.com/admin/)

<hr>

## Table of Contents

- [Introduction](#introduction)
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
- [Scope Plane](#scope-plane)
- [Structural Plane](#structural-plane)
- [Skeleton & Surface Planes](#skeleton--surface-planes)
  - [Wireframes](#wireframes)
  - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
  - [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Future Features](#future-features)
- [Technologies & Languages Used](#technologies--languages-used)
  - [Libraries & Frameworks](#libraries--frameworks)
  - [Tools & Programs](#tools--programs)
- [Testing](#testing)
  - [Validation Testing](#validation-testing)
  - [User Testing](#user-testing)
- [Deployment](#deployment)
  - [Pre-Deployment](#pre-deployment)
  - [Deploying with Heroku](#deploying-with-heroku)
- [Privacy Policy](#privacy-policy)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
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

## UX - User Experience

### Design Inspiration
The design inspiration for Cat Lovers came from the fact that 350 cats are killed every day in Japan. Most of them are newborn cats. By adopting a very cute baby cat and showing it to many people through the internet, someone who likes it may become a foster parent. This is why I launched the Cat Lovers site.

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

Role-based access control (RBAC) is implemented using Django's Group and Permission systems. Patients, specialists, and admins are grouped based on their role, and their access to features and sensitive information is restricted accordingly. User can only access their own comment data and booking history. Admins have the broadest access for system management.

## Features

## User View - Registered/Unregistered

It was important to me from the beginning that Cat Lovers be accessible to non-registered users in some way. We wanted the website to encourage new users to adopt or support our work by instantly inviting them to join our community through information about our work and a gallery section of rescued cats that changes weekly. Below is a breakdown of the site's accessibility for registered and non-registered users:

| Feature   | Unregistered User | Registered, Logged-In User |
|-----------|-------------------|-----------------|
| Home Page | Visable           | Visable         |
| Articles  | Visable but not interactable via 'Likes/Comments', 'Add Article' button not visible | Visable and full feature interaction available |
| Messaging | Writeable         | Writeable       |
| Booking   | Icon visible but redirected to Sign In page/Sign Up through link | Visable and full feature interaction available |

### User Registration Process
When a new user registers, they will appear on the Admin Site. Regular users can comment on posts, edit their comments, and delete them.

**Administrators:** Admin accounts are created manually by other existing administrators or super users in the Django admin area. This ensures that the creation of admin-level accounts is tightly controlled and complies with the platform's internal policies.
This registration flow was chosen to ensure role-based control and security. Allowing users to register freely on the platform allows them easy access to services. However, administrators require a higher level of trust and verification, so a manual vetting process is undertaken. This ensures that only approved administrators can manage sensitive tasks such as consultations and platform configuration, maintaining the integrity and security of the system.

### Reservation System
Cat Lovers allows users to make reservations for cat hotels directly through the platform.

### Messaging System 
Cat Lovers provides a secure messaging system for communication between the administration and potential adopters of cats. You can send messages without registering on the ABOUT site.

### Profile Management 。
Superusers can view their own profile on the Admin Site and on the ABOUT Site.

### Confirmation Messages
- **User Feedback**: Confirmation messages are shown to users when important actions are performed, such as logging in, booking an appointment, or sending a message. These messages help ensure a smooth user experience by providing feedback on successful actions.

## CRUD Functionality

You can create, read, update and delete shared information in Cat Lovers. Some features will have full CRUD functionality available, while others will only show the options you need. Below is a breakdown of CRUD for Cat Lovers:

| Feature | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Profile | Created upon registration | Yes | Yes | Full Profile deletion is currently only available to Admin upon User Account deletion, the profile dashboard clears automatically if a user removes all of their articles or bookings |
| Articles | Yes | Yes | Yes | Yes |
| Bookings | Yes | Yes | Yes | Yes |
| Gallery | Yes | Yes | Yes | Yes |

## Future features
In future iterations, we plan to implement the following features:
- Video broadcasting function for Cat Hotel
- Online payments

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

## AI Implementation and Orchestration

### Use Cases and Reflections:
  - **Code Creation:** 
    - Reflection: Strategic use of AI allowed for rapid prototyping, with minor adjustments for alignment with project goals. 
    - I asked Copilot everything in Japanese. So the comment became japanese in the code. 
  - **Debugging:** 
    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.
  - **Performance and UX Optimization:** 
    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.
  - **Automated Unit Testing:**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.


## **Testing**
 testing result is here ! () 

### **Validation Testing**

All code has been validated through:
- **HTML**: [W3C Markup Validator](https://validator.w3.org/).
- **CSS**: [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
- **Python**: PEP8 validation to ensure code quality.

![HTML validator test](https://github.com/tomokoelif/cat_lovers/blob/main/html.png)

![CSS validator test](https://github.com/tomokoelif/cat_lovers/blob/main/css.png)

### **User Testing**

- **Browser Compatibility**: The website has been tested on Chrome, Firefox, Safari, and Edge.
- **Responsiveness**: The platform has been tested on mobile, tablet, and desktop devices to ensure optimal performance.
- **Automatic Assignment Testing:** Tests were conducted to verify that newly registered users are automatically assigned to the "Patient" group and that their PatientProfile was successfully created. This was confirmed through both the user interface and the Django admin panel.

**Outcome**
The problem was successfully resolved. 

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

## Privacy Policy

As part of my **Cat Lovers** project, I am dedicated to ensuring that users’ personal data is handled responsibly. The following privacy practices outline how information is collected, used, and stored within this academic project.

- **Data Collection**: Cat Lovers, as a project, collects personal data during user registration and profile setup. This includes:
  - First and Last Name
  - Contact Information (Email)
  - Cat information

- **Data Usage**: The information gathered is used solely for educational purposes, including:
  - Managing user profiles.
  - Facilitating appointment bookings for cat hotel.

- **Data Sharing**: As this is a student project, personal data will not be shared with any third parties. It will only be used for demonstrating the functionality of the project. All information remains confidential and will not be distributed beyond the scope of the Cat Lovers project.

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
- **Dillon Mc Caffrey** - Code Institute: For General guidance.
- **Mark Brisco** - Code Institute: For general guidance.
- **Ruairidh MacArthur** - Code Institute: For general guidance.
### Media
- Icons and images sourced from **Canva** and **ChatGPT**.
- ERD illustration was generated from **pygraphiz** - A django extension.

## Acknowledgements

I would like to extend my heartfelt gratitude to the following individuals and organizations whose support, guidance, and inspiration have been invaluable in the development of this project.

### Mentors and Advisors
- **Dillon Mc Caffery** – A heartfelt thank you to Amy, our tutor and facilitator. His unwavering guidance and expertise were crucial throughout this journey. His guidance provided the clarity and support I needed to get through challenges and ultimately enhanced the quality of this project. His dedication and encouragement had a profound impact on my progress and learning.

- **Ruairidh MacArthur** – A heartfelt thank you to Mark, our dedicated tutor. His unwavering support, insightful feedback and constructive criticism played a key role in helping me complete this project. His deep knowledge and encouragement not only deepened my understanding but also inspired me to constantly improve my work. This project would not have been the same without his invaluable guidance.


### Supportive Friends and Family
- My friends and family, especially, for their encouragement and patience during this project. Your belief in me kept me motivated and focused.

### Academic Institutions
- **Code Institute** – Thank you for providing the learning environment and resources that made this project possible. I am especially grateful to the professors and staff at Code Institute for their valuable insights.

### Final Note
This project would not have been possible without the support, advice, and inspiration of each individual and organization mentioned. Thank you for being a part of this journey.




