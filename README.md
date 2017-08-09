# Django_NW

Check auto running django project by useing d_runscript.sh. need to mention the port and url. Set a cron to run the script.

For testing i am using direct demo log injection to the server url. Under testing folder the scrit is present kindly study the script and change server link and
pass hostname as argument

To run the project:
1. pip install virtualenv  #dounload virtualenv 
2. virtualenv Django #Create virtual enviorment named Django 
3. source Django/bin/activate
4. cd Django
5. git clone https://github.com/Sumontanaskar/django_local_library.git
6. cd django_local_library
7. pip install django
8. python manage.py makemigration
9. python manage.py makemigrations
10. python manage.py runserver 0.0.0.0:9192
11. Add server listen IP in the setting Allowed_hosts line
