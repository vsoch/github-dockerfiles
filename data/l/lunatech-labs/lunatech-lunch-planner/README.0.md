To create docker image:
docker build -t lunatech-lunch-planner .

To run docker image:
docker run -it --rm -m 1024m --name postgres -p 5432:5432 lunatech-lunch-planner
#Lunatech Luch Planner functionalities

##Login
To be able to log in the user must have a Lunatech email address and provide permissions to the application

##Logout
In the side bar navigation the user can perform the logout

##Attending meals
After login the user is taken to the list of schedule meals.
In this list the user can see the date a meal is scheduled and all the menu detail: menu name, dishes name and the list of extra info associated to each meal like if the meal is a vegetarian meal, por example.


To say you wish to attend a meal in a certain day, just select the checkbox in the corresponding meal line and press "save selected meals".
You can remove attendance by unselecting the same checkbox and pressing "save selected meals".
Using the checkbox at the top level is possible to select or unselect all meals.

##Profile
In the profile separator the user can add information about diet restrictions and ingredients that he/she is allergic to.
This information will be available to the administrator that schedules the meals.

##Administrator
The administrator user can perform several actions:
- Manage Dishes
- Manages Menus


#####Management of dishes
To create a new dish select `Dishes` in the side navigation bar. Two separators will be available:
- Create new
- All dishes

`Create a new dish`:

In the `Create dish` separator, fill in the form fields. Name and description are mandatory. All other fields are optional.
Press Create. After creation of a new dish you will be taken to the list of all dishes, where you can see the new created dish.

`All dishes`

In this separator you can:
- see the list of dishes names available
- see the detail of a dish by clicking in a specific dish
- select one or more dishes and delete them

`Details of a dish`
When you press a dish to see its details, a new separator called `Dish details` opens. There you can make modifications to the details of the dish, delete it or just cancel and go back to the list of dishes.


#####Management of menus
To create a new menu select `Menus` in the side navigation bar. Two separators will be available:
- Create new
- All menus

`Create a new menu`:

In the `Create new` separator, fill in the form fields. Name is mandatory. All other fields are optional.
Press Create. After creation of a new menu you will be taken to the list of all menus, where you can see the new created menu.

`All menus`

In this separator you can:
- see the list of menu names and dishes that belong to the menu
- see the detail of a menu by clicking in a specific menu
- select one or more menus and delete them

`Details of a menu`
When you press a menu to see its details, a new separator called `Menu details` opens. There you can make modifications to the details of the menu, delete it or just cancel and go back to the list of menus.

#####Management of scheduling of menus
To create a new menu schedule select `Schedules` in the side navigation bar. Two separators will be available:
- Create new
- All schedules

`Create a new schedule`:

In the `Create new` separator, fill in the form fields. All fields are mandatory.
Press Create. After creation of a new schedule you will be taken to the list of all schedules, where you can see the new created schedule.

`All schedules`

In this separator you can:
- see the list of menu names and the day the menu will be served (schedule)
- see the detail of a schedule by clicking in a specific date
- select one or more schedules and delete them

`Details of a schedule`

When you press a date to see its details, a new separator called `Menu schedule details` opens. There you can make modifications to the details of the schedule, delete it or just cancel and go back to the list of schedules.

The list of people that is attending the meal in the scheduled day is available, together with extra information provided by the people (information that should contain ingredients the person is allergic to).

A total summary of diet restrictions of the people attending the meal is also provided.

The DB diagram was built using `https://www.draw.io/`

The DB is composed by 6 tables:
- User
- Dish
- Menu
- MenuDish
- MenuPerDay
- MenuPerDayPerPerson

**User table**

Whenever a new user logs in the application (using Google signin) a uuid is created for the user and saved in the DB, together with the name and email.
The user uuid will be need later to trace how many and who is attending a certain meal on a certain day.

**Dish table**

This table holds the information of all the dishes available and it's detailed information.

**Menu table**

This table holds the name and uuid of a menu.

**MenuDish table**

This tables makes the bridge between a menu and the dishes that are part of that menu.
Different menus can share the same dishes.

**MenuPerDay table**

This table holds the information about the day(s) a certain menu will be served.
The same menu can be served in different days.

**MenuPerDayPerPerson**

This table holds the information of the users that have said that day are attending a certain menu on a certain day (MenuPerDay).
