# A recreation for ursetup

for a setup, when user links a product, try to pull image
profiles
drag and drop images for users to show how we have setup
nav bar should have logo that takes to home page, profile with a dropdown, notifications
profile dropdown should have home, favorites, my setups, profile, logout
add a button to add a new setup if your logged in
favorites page has

home page should list all the setups nicely
each setup should show amount of views it has, username of who created it, title, date posted, how much spent, amount of likes it has, and show the description
sort between latest published and most popular(popular based of likes)
also the list should have images that either the user uploaded for or first product links
have search bar at top of page to serach for setups

when clicked into a setup, display username, date posted, views, follow button, star button
name
description

URL with button to copy link to the setup, report button send admin notification
list all parts and the costs, should have a total price at the bottom
comment section, with a most popular and latest option for comments

each setup will have a list of Parts, Items, Ingredients or Steps.
a setup will have to have at least one of something, the item must have a title, a description, a url box to the url to purchase an item, an image section to also drag and drop(for DIY projects), quantity of item and price of item, price should multiply by quantity, and there should be a total price of the entire setup.

add the ability to signup with Google

NavBar:

1. Logo that takes to home page

if not logged in

1. Login/Register

else

1. new setup button

1. Notification icon (that will display new followers and new comments)

1. when logged in, show users pfp and username,

    a. clicking the button takes to profile page

    b. hover over it to reveal Favorites, My Setups and Logout buttons

## Notes for deployment

Setting Up the Site Record

Before configuring the social application, make sure the Sites framework is correctly set up:

In the admin panel, look for the Sites section.

Click on Sites to view the site records.

You'll likely see a site with the domain example.com - click on it to edit.

Change the domain name to localhost and display name to localhost:8000 for your development environment. Save the changes.

Note: In a production environment, you would use your actual domain name.

Also must do some change in the credentials in Google Cloud Console
