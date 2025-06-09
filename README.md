# Comfort Foods.de

Comfort Foods.de is a Restaurant Booking System. The site is for a restaurant that sells South African Food and it is based in Europe. The target market are people who come from Africa that have not indulged in the meals in a long time and also for tourists from around the globe that like to try new food from different cultures. Customers may use the site to make a booking to come visit the store. The restaurant does not allow walk-ins, strictly bookings are allowed. The aim of the restaurant is to allow people from different cultures to experience the warmth and love added into the dishes. The restaurant does not allow online ordering, customers would have to experience the meals inside the establishment.

## Features
### Navigation Bar
 - A customer uses the navigation bar to navigate around the site
 - Each link clicked directs the customer to a page where they can find more information
 - When a customer is not on the home page, they can click on the restaurant name to be redirected back to the menu.
 - A user can click the Reservation link at the top of any page to make a reservation.
 - The visible links on the navigation bar are only visible when a user is logged in. Please see below:

 ![Navigation bar](readme.md_file/navigation-bar.png)

 - When a user is not logged in, the only links visble are as shown below:

 ![Logged out](readme.md_file/logout-nav.png)

### Home Page
 - This page has a callout message welcoming the user to the site
 - It has a carousel effect which shows a few of our dishes served at the restaurant
 - Below the images is a paragraph inviting users to signup in order to get rewards. Please see image below:

 ![Home-page](/readme.md_file/home-page.png)
 
### Footer
 - Users can visit our social media sites to find out more information on a site
 - They can also contact us to make bookings. Please see below:

 ![Footer](readme.md_file/footer.png)

### Menu Page
  -	The menu page shows the types of meals and drinks offered at the restaurant.
  -	The restaurant offers the following: *Braai Platters* – meat platters that consist of different grilled meat types; *Hearty Meals* – consists of meals that are slowly cooked that bring comfort to the heart; *Sides* – these sides can be added to the hearty meals or Braai meat platters; and *Drinks* – these drinks are especially made in South Africa
  -	The menu shows the prices as well, so a customer is aware of what the meals cost. which allows them to be well prepared. Please see image below:

  ![Menu page](readme.md_file/menu-page.png)
  
  - A user has the ability to view details of a meal by clicking 'View detailed meal' which will take them to a detailed page
  - This page with give the user a brief description of the history of the meal. Please see image below:

  ![View detailed meal](readme.md_file/detailed-meal.png)

  - On the same page, a user is able to leave a comment on the meal once they have visited the restaurant. Please see below:

  ![Feedback section](readme.md_file/feedback.png)

### About Us
  -	If a customer is logged in, they are able to read out the restaurants history
  -	The page also consist of an image of the founders
  
  ![About page](readme.md_file/about-page.png)
  

### Reservations Page
  -	This page is used to make reservations to visit the restaurant.
  -	In order for a customer to make a reservation, they would need to sign up and log in 
  -	A customer would have to select the date, time and as well a table with the number of people being booked.
  
  ![Reservation form](readme.md_file/reserv-form.png)
  

### Logout Page
  - When a user logs out, the below pops up:

  ![Log out](readme.md_file/log-out.png)


### Login Page
  - When a user is registered, they can simply login the site to browse. Please see below:

  ![Log-in](readme.md_file/log-in.png)
  

### Register Page
  - New users have to register in order to have access to the site. Please see below:

  ![Register form](readme.md_file/register-form.png)
  

## Features to be implemented
  - Have a rewards page where users can view the amount of rewards hey have so they can get discounts depending on how often they visit the restaurant.
  -	Create a system to allow online bookings 
  -	Add more food to the menu

## Testing
### Manual Testing

#### Register Page
  - The sign up form has a defensive design which does not allow a user to submit the form without filling out all required fields. Please see below:

  ![Responsive signu up page](readme.md_file/responsive-signup.png)

#### Login
  - When a user is logged in, a success message pops-up with the username.
  - There is another log in message that shows if a user is logged in or not

  ![Log in success message](readme.md_file/login-message.png)

#### Detailed Menu
  - When a user clicks on the 'view detailed menu' link, the url changes
  - The menu has a paginate function that allows a user to view the next and previous page of the menu

  ![Next page](readme.md_file/next-page-menu.png)

  ![Previous page](readme.md_file/prev-page-menu.png)

  ![URL](readme.md_file/url.png)

#### Validator Testing
  - I have manually tested my code using PEP8 Python Validator.

  ![Python Linter with errors](readme.md_file/pl-views-reserv.png)
  
  * There is an error due to long line that cannot be fixed.
  ![pep8-error](/readme.md_file/long-line.png)

  - 
  ![alt text](image.png)

### Planning Project
  - I used Balsamiq to plan my project. Please see below images:



## Deployment
  This project was deployed using Code Institute mock terminal for Heroku.

  * Steps for deployement
    - Create a repository on GitHub
    - On VS-code, connect the repository with the workspace and use git push command to push work into GitHub
    - Ensure GitHub project has public visibility on Github
    - Create a new Heroku App
    - Create configuration variables to connect the VS-Code with Heroku
    - Link the Heroku app to the GitHub repository
    - Click on Deploy


## Credits
### Content
  * For the better understanding of creating a Restaurant Booking System, I used google to search for restaurants. The one restaurant that stood out for me was [Amrit-Restaurant](https://amrit.de/en/)
  * For a better understanding of how to create such a website I used the CI walkthrough, 'I think therefore I blog'.
  * Roman, Tutor CI, for assisting with how to create edit for comments
  * My Mentor, Moritz
  * Sarah, Tutor CI

### Media

  

