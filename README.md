# FoodieGuide

FoodieGuide is a Django-based web application for managing and exploring recipes. It provides features to add, search, and view detailed recipes with images and descriptions.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- (Optional but recommended) Virtual environment tool such as `venv` or `virtualenv`

## Installation and Setup

1. Clone the repository or download the project files.

2. Navigate to the project root directory (where `manage.py` is located):

   ```bash
   cd FoodieGuide
   ```

3. (Optional) Create and activate a virtual environment:

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install django
   ```

   Note: This project uses Django 5.2 as per the settings.

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. (Optional) Create a superuser to access the Django admin:

   ```bash
   python manage.py createsuperuser
   ```

## Running the Development Server

Start the Django development server with the following command:

```bash
python manage.py runserver
```

By default, the server will run at `http://127.0.0.1:8000/`.

## Accessing the Application

- Open your web browser and go to `http://127.0.0.1:8000/` to access the FoodieGuide application.
- To access the Django admin panel (if superuser created), go to `http://127.0.0.1:8000/admin/`.

## Static and Media Files

- Static files (CSS, JavaScript) are located in the `foodieguide/static/` directory.
- Media files (uploaded recipe images) are stored in the `media/` directory.
- During development, Django serves these files automatically.

## Notes

- This project uses SQLite as the default database.
- Debug mode is enabled by default for development purposes. Do not use this configuration in production.

## License

This project is open source and free to use.

## Author and Repository

Created by Sameer Ahmed Indikar

GitHub Repository: [https://github.com/SameerAhmedIndikar/FoodieGuide.git](https://github.com/SameerAhmedIndikar/FoodieGuide.git)

## Docker Usage

To build and run the project in a Docker container, follow these steps:

1. Build the Docker image:

```bash
docker build -t foodieguide .
```

2. Run the Docker container:

```bash
docker run -p 8000:8000 foodieguide
```

3. Open your web browser and go to `http://127.0.0.1:8000/` to access the FoodieGuide application running inside the container.
