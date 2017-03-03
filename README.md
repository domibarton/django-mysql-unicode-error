Use case
========

I'd like to have a "special" model field which is inherited from the `models.TextField`.
Instead of returning a generic `unicode` object, the model shall return a `unicode` object "on steroids".

This works fine as long as MySQL isn't involved!  

Problem with MySQL
------------------

As soon as MySQL is used as the database backend, everything gets a little tricky.

Apparently, `MySQLdb` will "check" the value and returns it as `str` or `unicode` object.  
Unfortunately, this check isn't very clever, because as soon as your value is no longer a `unicode` object, it expects it should be `str` and calls `string_literal` instead of `unicode_literal`.

Usage of test case
==================

Prepare
-------

- Clone this repository
- Run `pip install -r requirements.txt` (you might want to use a `virtualenv`)
- Create a new MySQL database
- Configure `settings.py` to use the database
- Run `./manage.py migrate`
- Run `./manage.py runserver`

Now you should be able to connect to http://localhost:8000/app/prepare/  
This creates the required database records!

Test Cases
----------

Now go to the following URL: http://localhost:8000/app/test/value1/  
This will copy the `value1` value of one object to another, which should work without any problems.

Now go to the following URL: http://localhost:8000/app/test/value2/  
This will copy the `value2` value of one object to another, which now fails!

Please have a look at the code:

- `app/keyvalue.py`
- `app/models.py`
- `app/views.py`

