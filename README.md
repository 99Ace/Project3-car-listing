# USED CAR LISTING
## PROJECT  3 :  DaATA CENTRIC DEVELOPMENT MILESTONE PROJECT

This Website is built to allow Create, Read, Update and Delete from DATABASE for the car listing. 
There is also a search function that allows user to filter and view according to user's selection

## SCOPE
The website allows user to

_CREATE_
- user can enter their information for their car and list in our website for sale. 
- data will be stored in our database

_EDIT_
- user can edit their listing, in instance where they want to re-write their desciption or review their listed price.
- allow user to put their car to Sold

_READ (DISPLAY)_
- basic function to show all listing from databases

_DELETE_
- user can choose to delete their listing anytime


## Demo

A live demo can be found here. https://ace-carlisting.herokuapp.com/

## UX
My Considerations for the website:

_User :_
Car Owners

_Considerations :_  
- they must be able to view, add, edit and delete a vehicle listing
- they need a channel to market their car to attract buyer



## Technologies
1. HTML
2. CSS
3. Bootstrap (3.3.7)
4. MongoDB
5. Python 3

## Features
The page will show the full listing from the database by default

My Design of the site:
- User can add a vehicle listing by clicking on the ADD button on top left
- User can edit or delete the listing by click on the 2 link on the right of the listing
- User can use the search bar to do search for the car they looking for; they can search using 1-4 options combine

_Limitations & Future development:_
There are more search fields to be added and more UI/UX to be improved on. 
Images are not able to be uploaded and will be enhanced in near future.
Click on the selected vehicle will reveal more details about the vehicle (part of future development)

## Testing
Manual Testing is done to ensure that the all functions are functional.


*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
1a | `Click on 'Add New Vehicle' red button located on top left` | `Show a form to allow user to enter car details` | **Pass** 
1b | `Enter the details in form and submit`|`Return to main listing page and data is added` | **Pass** 
2a | `Click on 'Edit' on right of each listing`|`Show a form to allow user to edit existing car details with current data pre-entered in field` | **Pass** 
2b | `Make changes to form and submit`|`Return to main listing page and data is updated` | **Pass** 
3a | `Click on 'Edit' on right of each listing` | `Check for confirmation to delete` | **Pass** 
3b | `Click on 'Confirm Delete' on right of each listing` | `Delete and return to show listing page` | **Pass** 
4 | `Select from each drop down in search bar below the nav bar, then click 'Find Used'` | `Show vehicles that fulfil the search requirement` | **Pass** 

## Deployment

This site is hosted using Heroku App 
Link : https://ace-carlisting.herokuapp.com
All codes are uploaded to GitHub and links are made to Heroku by installing in bash terminal in projects.

Once project is complete, it is being push to heroku to deploy

## Credits

All templates are used from my own Project 1 : Car website
It is an extension from my Project 1
 
