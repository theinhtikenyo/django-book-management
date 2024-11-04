# Django Book Management Project

This is a simple Django project for managing books.

## Setup Instructions

1. **Install Pipenv**: Make sure you have `pipenv` installed. If not, you can install it using: ```bash pip install pipenv ```

2. **Activate the Virtual Environment**: Run the following command to activate the virtual environment: ```bash pipenv shell ```

3. **Install Dependencies**: Install the required packages: ```bash pipenv install ```

4. **Migrate Database**: Create and apply database migrations: ```bash python manage.py makemigrations python manage.py migrate ```

5. **Create Superuser**: Set up a superuser for the Django admin: ```bash python manage.py createsuperuser ```

6. **Run the Development Server**: Start the Django development server: ```bash python manage.py runserver ```

7. **Access Django Admin**: Log in to the Django admin interface at `http://localhost:8000/admin` and create new books.

8. **Get All Books**: Use `curl` or Postman to retrieve all books with a GET request to: `http://localhost:8000/api/books`

9. **Post New Book Data**: The API supports both JSON body data and HTML form data for posting new books. For JSON, use the following format: ```json { "title": "Example Book", "author": "John Doe", "price": "6.9" } ```

## Enjoy managing your books!
