# Dream-TODO

###### cs50 final project

#### Video Demo: https://www.youtube.com/watch?v=OYtgy9iNxWE

#### Live url: https://dreamtodo.up.railway.app/

#### Description:

Easy to use TODO list that keeps you organized, your TODOs saved and available through any device browser.

Drag and drop to reorder your TODOs, keeping what you need the way you want.

<img src='static/drag_drop_gif.gif' height='400px'>

<br/>
<br/>

No need to save, it auto syncs.

<img src='static/sync_loader_gif.gif' height='400px'>

---

<br/>

##### Features:

- Register/Login

- Data persistence

- Auto sync

- Todos Reordering via Drag and Drop

- 100% responsive

- Light/Dark mode

##### Techs used:

- Django
- Jquery
- Ajax
- Bootstrap
- Sass

##### Extra tools:

- Font Awesome
- Favicon.io

##### deployed via: https://railway.app/

### Challenges

This project was a big challenge for me mostly because i've never user the Django witch is a backend framework and also for the fact that i did not used any frontend framework, so i had to rely on jquery and jinja templates witch i think is not ideal, anyways it worked well and the result was satisfying for me. Anyway lets run trough some specific challenges:

##### Register/Login:

Thankfully django comes with member management out of the box, but i wanted it using my css theme so tinkering with django was necessary, learning how to use django forms its not easy as it seems, but reding the docs a couple of times did the work.

##### Data persistence:

To persist data it was necessary to create a db in django witch is not hard, what really got me was discovering how to pass the csrf token through ajax. Moreover i decided to also persist data when user is not authenticated using local storage witch is pretty easy. The secret feature here and the biggest challenge of this part is that when you log in, if you had data on local storage it will sync with your personal db. Cool right!

##### Todos Reordering via Drag and Drop:

Definitely the hardest feature of the project because the implementation is totally different between mobile and desktop, to make it work it's necessary to handle a bunch of events witch are different for desktop and mobile. For desktop you can set a component as draggable and manage click events witch is pretty straight forward. But for mobile you only have three touch events so its kinda awkward to handle it, to give the impression that it's dragging, 1) it's necessary to listen to a touch event for x seconds to start the 'dragging', 2) you duplicate the target dom element and insert it with it's position set to fixed and change it's x/y collecting the touch move event, 3) on the touch cancel event you get the clientX and clientY and use it to find what element is at that position, 4) using these information simply swap the elements in a data list and insert it in the dom.

##### 100% responsive:

Quite easy to do thanks to the simple layout, bootstrap and flexbox literally saved the day.

##### Light/Dark mode:

The dark mode trick was made by using vars as values to all classes and changing the vars values by setting a class that redefines it in the body element.

### Future Improvements:

As straight forward a TODO list project can look like, i think it definitely has room for soo much great ideas and techs, so besides the ones i've implemented in this one im gonna list possible improvements for this project:

- Possibility to store

  - images
  - drawings
  - audio
  - files

- hot updates

  - e.g. example if you connected in two devices and alter something it auto updates in the other device

- offline support

- date and time integration

  - e.g. having TODO's in a calendar

- push notifications
- TODO's templates for complex tasks
- integration with other apps
- trash for viewing/retrieving recently deleted tasks
- better user management
  - e.g.
    - change password
    - two factor authentication
    - email integration
    - account recovering

### How to run this project:

In the `pyvenv.cfg` file there's the requirements to create a virtual environment to run the project, so in this case you need to create a virtual environment with python version = 3.10.7 and virtualenv version = 20.16.5.
Then once in your virtual environment you need to install the `requirements.txt` dependencies with the command `$ pip3 install -r requirements.txt`.
You may as well change de DATABASES settings at DreamTODO/settings.py and also create a `.env` file following the .env.example.
If all went well it's now possible to start the django dev server with `$ python manage.py runserver`.
