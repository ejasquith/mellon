# Mellon

# Project Overview

The purpose of this project is to provide users with a pared down microblogging experience. Many social media platforms in the current day place a strong emphasis on "the algorithm", where users have very little control over what they see. This infinite feed of content can lead to "doomscrolling", which [studies have suggested is linked to poor mental and physical health](https://www.theguardian.com/society/2022/sep/06/doomscrolling-linked-to-poor-physical-and-mental-health-study-finds).

The aim of Mellon is to focus on friendships - no algorithm, no influencers, no infinite feed, no adverts or sponsored posts. It will act as something inbetween a social network and a diary, where users can share short posts that are seen only by their friends, and can conversely check their friends' posts. The site will also provide functionality for liking and commenting on posts, as well as direct messaging users, in order to further facilitate human connection in the digital age.

### Side Note - Why Mellon?

Mellon is the Elvish word for 'friend' in Tolkien's "The Lord of the Rings" - and besides, who doesn't love a juicy melon on a summer day? Simple as that!

### A Note

This project was created under massive time constraints due to work, life events, mental illness, and various other confounding factors. Where this affected the project, it will be noted.

# Planning Stage

## Target Audience

The target audience of Mellon mainly consists of young people, 16-30, who are tired of sites like Twitter and are looking for a simpler way to connect with friends.

## Agile Methodologies

This project was designed using agile methodologies. Most features were described in user stories, which were then separated into epics to aid in the development cycle. Each epic was implemented in a sprint (due to time constraints, a sprint was more like a block of hours than days or weeks).

User stories can be found in the Product Backlog project on GitHub. There are discrepancies between this list and the product backlog; again, due to time constraints, there was not sufficient time spent on planning which means that some user stories and tasks are in the wrong milestone, and some are missed out altogether. This list is how the project was developed.

### EPIC 1: Setup

This epic included all tasks that needed to be done before work could begin on the complex parts of the project. This included:
- Set up Django app
- Create Postgresql database
- Set up static storage
- Create base.html template
    - Create site navigation and footer
- Create basic database models
- Set up admin dashboard
- Initial deployment to Heroku

### Epic 2: Authorisation

This epic included anything related to user authorisation & authentication.
- Login/out
- Register

### Epic 2: Posts & Comments

This epic included everything related to making, editing and deleting posts or comments.
- Make posts
- Comment on posts
- Like/unlike posts
- Delete post/comment
- Edit post/comment (not implemented)
- Add images to posts (not implemented)
- Flag posts (not implemented)

### Epic 3: Profiles & Friendships

This epic was not properly planned as some features slipped my mind during planning.
- View a profile
- Edit profile
- Send, accept, reject, and cancel friend requests

### Epic 4: Messaging

This epic was not implemented at all due to time constraints, and because I viewed it as an optional feature.
- Send, receive, and view messages

### Epic 5: Admin

Again, this epic was not implemented.
- Moderate posts & comments
- Warn users
- Ban users


### Epic 6: Misc

This epic consisted of miscellaneous tasks that did not fit anywhere else and were not required for any other parts of development.
- Create favicon
- Create custom 404, 403 and 500 pages

## ERD

After planning my user stories and sprints, I created an entity-relationship diagram (ERD) to plan how the database would look. 

![The ERD for this project](docs/erd.png)

Some of the fields aren't properly defined - for example, I included password_hash in the user entity, which is inherited from Django's base User model. I wasn't sure at the point of creating the ERD how this would be implemented, so I included it as a placeholder. Overall, the fields were less important than the entities and the relationships between them, so this was mainly a tool to understand how my models would interact.

## Wireframes

Before starting development, I created wireframes to help design how pages should look.

### Home Screen (not logged in)
![A wireframe for the home screen (not logged in)](docs/wireframes/home-screen-not-logged-in.png)

### Home Screen (logged in)
![A wireframe for the home screen (logged in)](docs/wireframes/home-screen-logged-in.png)]

### Login
![A wireframe for the login screen](docs/wireframes/login.png)

### Register
![A wireframe for the register screen](docs/wireframes/register.png)

### Create Post
![A wireframe for the create post form](docs/wireframes/create-post.png)

### Create Comment
![A wireframe for the comment form](docs/wireframes/comment.png)

### View Comments
![A wireframe for the comment view](docs/wireframes/comments-view.png)

### Profile
![A wireframe for the profile page](docs/wireframes/profile-page.png)

### Friends
![A wireframe for the friends screen](docs/wireframes/friends.png)

### Messages
![A wireframe for the messages screen](docs/wireframes/messages.png)

### Conversation
![A wireframe for the conversation screen](docs/wireframes/conversation.png)

## Design

Most of the project uses built-in Bootstrap designs. I was unable to plan and implement a design scheme for this project due to time constraints. That being said, my original vision for this project was clean & minimal with pops of colour throughout, which my current design does well.

The exception to this is django's default forms (login, register, and edit profile). These are not styled and, while functional, are a jarring break from the otherwise consistent design of the site.  
This is because, given the little development time I had, the easiest way to implement them was simply putting `{{ form.as_p }}` into the template. With more time, I would investigate how to style these properly.

# Features

The first thing the user sees when opening the site is a welcome message inviting them to login or register.

![A screenshot of the home page for users not logged in](docs/screenshots/home-not-logged-in-ss.png)

The user can log in:

![A screenshot of the login page](docs/screenshots/login-ss.png)

Or register:

![A screenshot of the register page](docs/screenshots/register-ss.png)

When they are logged in, the homepage displays a list of posts. This is each of their friends' most recent post. They can like a post by clicking the heart, which turns solid.

![A screenshot of the home page when logged in](docs/screenshots/home-logged-in-ss.png)

They can also click the comment icon to open the comments on the post as well as a form to submit a comment.

![A screenshot of the comment section of a post](docs/screenshots/comment-ss.png)

The user also sees a button to create a post in the bottom right of the screen. Clicking this opens a modal with a form to creare a post.

![A screenshot of the create post form](docs/screenshots/post-ss.png)

By clicking the user info section of a post, the user is taken to their profile page. If they are friends, the user info (profile picture, username, display name and bio if it exists) is displayed as well as all of that user's posts. If the current user has sent a pending friend request, that information is displayed. If that user has sent a friend request to the current user, there is a button to accept the request. If no friend request has been sent, there is a button to send a request. This page can also be accessed from the friends and find friends pages, hence the options for the two users not being friends.

![A screenshot of a profile where the user is friends](docs/screenshots/friend-ss.png)
![A screenshot of a profile with a pending request](docs/screenshots/user-fr-sent-ss.png)
![A screenshot of a profile with an incoming friend request](docs/screenshots/user-fr-received-ss.png)
![A screenshot of a profile where there is no friendship](docs/screenshots/user-no-fr-ss.png)

The user can also access their own profile page by clicking 'profile' in the navbar. This functions similarly to other profiles, except that there is an edit profile button. They can also delete their own posts by pressing the bin icon.

![A screenshot of the user's profile](docs/screenshots/profile-ss.png)

If the user clicks the edit profile button, they are sent to the edit profile form.

![A screenshot of the edit profile form](docs/screenshots/edit-profile-ss.png)

The friends page displays all incoming, outgoing, and active friendships, with options to accept/reject, cancel, and remove respectively.

![A screenshot of the friends page](docs/screenshots/friends-ss.png)

As it is difficult to find friends otherwise, there is a 'find friends' page. Currently this just displays all users that the current user is not friends with (or has an outgoing/incoming request). With more time, I would implement this to be a 'friends of friends' list. However, with the small scope of the project and because of the ease of use for testing purposes, this works fine for the moment.

![A screenshot of the find friends page](docs/screenshots/find-friends-ss.png)

Additionally, a notification is displayed when the user has incoming friend requests. This is checked when the user loads a page and ever 60 seconds thereafter.

![A screenshot of the friend request notification](docs/screenshots/friends-notification-ss.png)