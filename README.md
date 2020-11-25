# Basic internal instruction for the moment

- Do not commit the database
- As long as we do not have a fixed model do not use the migration procedure
    - just trash and repopulate
    ```
    rm -f db.sqlite3 results/migrations/0*; ./manage.py makemigrations; ./manage.py migrate
    ./manage.py populate_db
    ```
    - or squash them
- Use virtualenvironement (venv or pew) to make sure to use the proper version of libraries,
    - use requirement.txt to install the librairies
# euro
