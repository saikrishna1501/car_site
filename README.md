# Django Car Site

Welcome to the Django Car Site, a small web application where users can list, add, and delete cars. This project serves as a practice exercise to reinforce my understanding of Django's core concepts, including templates, models, and the admin panel.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **Car Listing:** View a list of cars with details such as make, model, and year.
- **Add Car:** Add new cars to the site with relevant information.
- **Delete Car:** Remove cars from the site that are no longer needed.
- **Admin Panel:** Utilize the Django admin panel to manage cars efficiently.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/saikrishna1501/car_site.git
    ```

2. Navigate to the project directory:

    ```bash
    cd car-site
    ```

## Usage

1. Run database migrations:

    ```bash
    python manage.py migrate
    ```

2. Create a superuser account for the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

3. Start the development server:

    ```bash
    python manage.py runserver
    ```

4. Access the Django admin panel at `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

5. Visit the car site at `http://127.0.0.1:8000/` to explore and interact with the car listings.
