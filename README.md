# gstbillingapp
Step 1:
virtualenv -p python3 venv
Step 2: *Activate Virtual Environment*
.\venv\Scripts\activate
Step 3: *Install dependencies*
pip install django social-auth-app-django num2words
Step 4: *Make migrations*
python manage.py migrate
Step 5: *Run the main file which is named as manage.py*
python manage.py runserver
