flask-starter
=============
      
A flask extension which contains a basic app and is configured in your local machine through a command line utility 

.. image:: https://img.shields.io/pypi/v/flask-starter
   :target: https://pypi.python.org/pypi/flask-starter/

.. image:: https://github.com/Agent-Hellboy/flask-starter/actions/workflows/python-app.yml/badge.svg
    :target: https://github.com/Agent-Hellboy/flask-starter/

.. image:: https://img.shields.io/pypi/pyversions/flask-starter.svg
   :target: https://pypi.python.org/pypi/flask-starter/

.. image:: https://img.shields.io/pypi/l/flask-starter.svg
   :target: https://pypi.python.org/pypi/flask-starter/

.. image:: https://pepy.tech/badge/flask-starter
   :target: https://pepy.tech/project/flask-starter

.. image:: https://img.shields.io/pypi/format/flask-starter.svg
   :target: https://pypi.python.org/pypi/flask-starter/

.. image:: https://coveralls.io/repos/github/Agent-Hellboy/flask-starter/badge.svg?branch=master
   :target: https://coveralls.io/github/Agent-Hellboy/flask-starter?branch=master

      
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
