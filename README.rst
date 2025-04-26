flask-starter
=============
      
A flask extension which contains a basic app and is configured in your local machine through a command line utility 

.. image:: https://img.shields.io/pypi/v/flask-starter
   :target: https://pypi.python.org/pypi/flask-starter/

.. image:: https://github.com/Agent-Hellboy/flask-starter/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/Agent-Hellboy/flask-starter/

.. image:: https://img.shields.io/pypi/pyversions/flask-starter.svg
   :target: https://pypi.python.org/pypi/flask-starter/

.. image:: https://img.shields.io/pypi/l/flask-starter.svg
   :target: https://pypi.python.org/pypi/flask-starter/

.. image:: https://pepy.tech/badge/flask-starter
   :target: https://pepy.tech/project/flask-starter

.. image:: https://img.shields.io/pypi/format/flask-starter.svg
   :target: https://pypi.python.org/pypi/flask-starter/



      
Installation
------------

    for stable version
       - pip install flask-starter

    for current_version
       - pip install git+https://github.com/Agent-Hellboy/flask-starter.git
	      

using
------

open the terminal and type 
    - ``flask-starter-project --name=your-project-name`` 
    - this will build a basic project with inbuilt auth and admin interface for you
    - cd `your-project-name`
    - create the virtualenv and Install the requirements which is there in `your-project-name` 
    - run `python3 server.py`

Project Structure
---------------

The generated project follows a clean and organized structure:

.. code::

    your-project-name/
    ├── app/
    │   ├── __init__.py          # App initialization and configuration
    │   ├── models.py            # Database models
    │   ├── views.py             # Route handlers and views
    │   ├── extension.py         # Flask extensions (SQLAlchemy, LoginManager, etc.)
    │   ├── libs/                # Custom business logic and utilities
    │   └── templates/           # Jinja2 templates
    │       ├── layout.html      # Base template
    │       ├── home.html        # Home page
    │       ├── login.html       # Login page
    │       ├── register.html    # Registration page
    │       └── profile.html     # User profile page
    ├── tests/                   # Test directory
    │   ├── __init__.py
    │   ├── conftest.py          # Test configuration and fixtures
    │   └── test_views.py        # View tests
    ├── requirements.txt         # Project dependencies
    └── server.py               # Application entry point

Key Components:
- **app/**: Main application package
  - **models.py**: Defines database models (User, etc.)
  - **views.py**: Contains route handlers and view logic
  - **extension.py**: Initializes Flask extensions
  - **templates/**: HTML templates with Jinja2
- **tests/**: Test suite with pytest
- **server.py**: Application entry point with development server

you will have below routes by default 

.. code:: py

        Endpoint           Methods    Rule                             
        -----------------  ---------  ---------------------------------
        admin.index        GET        /admin/                          
        admin.static       GET        /admin/static/<path:filename>    
        main.home          GET        /                                
        main.login         GET, POST  /login                           
        main.logout        GET        /logout                          
        main.profile       GET        /profile                         
        main.register      GET, POST  /register                        
        static             GET        /static/<path:filename>          
        user.action_view   POST       /admin/user/action/              
        user.ajax_lookup   GET        /admin/user/ajax/lookup/         
        user.ajax_update   POST       /admin/user/ajax/update/         
        user.create_view   GET, POST  /admin/user/new/                 
        user.delete_view   POST       /admin/user/delete/              
        user.details_view  GET        /admin/user/details/             
        user.edit_view     GET, POST  /admin/user/edit/                
        user.export        GET        /admin/user/export/<export_type>/
        user.index_view    GET        /admin/user/


 
  - you can access admin interface by adding `/admin` in your base url 
 
  - just write core logic in libs and present your prototype


Contributing
------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
