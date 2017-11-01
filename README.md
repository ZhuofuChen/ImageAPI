You can use the following commands to install the packages you need
	pip install -r requirements.txt
	
After installation, you need to configure your own database information, configuration files in Image\settings.py

Synchronous database file

	python manage.py makemigrations
	python manage.py migrate
When everything is done, you can use the following command to start ImageAPI
	python manage.py runserver

