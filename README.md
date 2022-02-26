# Social Gaming

Social Gaming is an app built for gamers. It is a social media application where gamers can interact with each other. They can create profile, write uo new posts and view other gamers posts. Also, why not add a comment too.

# Features

## Profiles

* Users can create their own profiles.
* Users can edit their profiles and upload image.
* They can create posts too and upload image to it..
* Users can edit their posts.

## User Login

* Users are able to login in to the platform usign new username and password.

* Only unique username per user.

* Any errors will be checked via allauth. 

## User Profile

* Users can view their current profile.

* They can make changed to their profile via neat modal system.

* User are able to upload new image to the site.

* They have sidebar where they can visit post feed or their own post feed.

## My Post Feed


* This is where users can view their posts.

* List of all their posts will be shown in time order


## Post Feed

* User can see everyones posts here.

* They can also click on username of the author and visit their profile.

* If user is logged in they can edit or delete thwir own posts.

## Likes


* User like other users posts.

* Or they can unlike the post.

## Comments

![Post Feedt](readme-files/screenshots/bmi-info.png)

* User can create new comments on others posts.

* User can edit or even delete their own posts.


# Features Left to Implement

* Create a Friends or Followers list so you users interact with each other more personally.

* Create messaging system for users to direct message each other.

* Create forum so all users can interact with each other.

* Create Social Media login.

* Show users own profile image on posts. I have tried this but I ran out of time because of staticfile heroku bug. 

# Deployment

* Fitness Buddy was deployed using GitHub Pages. Below are the steps:

    * Visit [Heroku](https://github.com/dushanka-dev/fitness-buddy)
    * Login
    * Go to settings
    * Make sure DEBUG False
    * Set up Github repo connection Heroku
    * Click deploy	

# Testing

* Login

    * Used simple password which display error asking user to create stronger password
    * Username has to be correct for the user to login	

* Profile

    * Checked user profile only has authincated users details
    * Tested if user is able to update their details
    * Checked user profile only has authinticated users details
    * Checked database to ensure users details are been posted


## Bugs and Fixes
        
* Error: Heroku was not uploading staticfiles
* Fix: Change the css and js file paths in base.html. Set debug to false.
* Error: User wasn't able to edit their own post
* Fix: Use pk to locate the correct post.


## Responsive Testing

* For Responsive testing Google Devtools was used to minimise the app to view in different device sizes.

* Used Media Queries to add styling for different device screen sizes. 


# Credits

* [Gitpod](https://www.gitpod.io/)
* [GitHub](https://github.com/)
* [Google](https://www.google.com/)
* [Google Fonts](https://fonts.google.com/)
* [Stack Overflow](https://stackoverflow.com/)
* [W3Schools](https://www.w3schools.com/)
* [Coolors](https://coolors.co/palettes/trending)
* [YouTube](https://www.youtube.com/)
* [Spell Checker](https://www.internetmarketingninjas.com/online-spell-checker.php)