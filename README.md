# Summary
This program can scrap data from the twitter user profile to save it in postgres. It can also retrieve the saved data for the user.

# Prequisites
1. Python
2. Docker
3. sqlalchemy
4. FastApi
5. uvicorn
6. psycopg2

# Building steps:
1. Run postgres in docker using this command:
    ```
    docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=password postgres
    ```
2. Run the main.py file
3. Open localhost:8000

# API usage & endpoints
1. **/** with get method: Goes to home page.
2. **/scrape_user/<user_name>** with post method: It can scrap the user for the given user name then it stores the scrapped data the the postgres database. It also returns the scrapped data to the user.
3. **/get_user/<user_name>** with get method: Gets the scrapped data of the user with the given username if found in the database.