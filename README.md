# Kigali Sustainability Dashboard

## Overview

The Kigali Sustainability Dashboard is a Django-based web application designed to manage and visualize sustainability data for Kigali City, Rwanda. This project provides a comprehensive CRUD (Create, Read, Update, Delete) interface for various sustainability metrics across different districts and sectors of Kigali.

## Features

- Manage data for Districts, Sectors, Energy Consumption, Waste Management, Green Spaces, Public Transportation, Air Quality, and Citizen Initiatives
- User-friendly interface for data entry and visualization
- CRUD operations for all data models
- Responsive design for desktop and mobile use

## Technologies Used

- Python 3.x
- Django 3.x
- PostgreSQL
- HTML/CSS
- JavaScript (optional for enhanced UI)

## Installation

1. Clone the repository:
      git clone URL
      cd kigali-sustainability

2. Create a virtual environment and activate it:
      python -m venv venv
      source venv/bin/activate  # On Windows use venv\Scripts\activate
3. Install the required packages:
     pip install -r requirements.txt
4. Set up the PostgreSQL database and update the `DATABASES` configuration in `settings.py`

5. Apply migrations:
    python manage.py migrate
6. Create a superuser:
     python manage.py createsuperuser
7. Run the development server:
    <!-- To Specify Port number just add the port number after runserver command EX :  python manage.py runserver 8000 --> 
    python manage.py runserver 8000
8. Access the application at `http://localhost:8000`

## Usage

- Use the navigation menu to access different data categories
- Add, view, edit, and delete records for each category
- Use the admin interface (`/admin`) for advanced data management

## Project Structure

- `sustainability/`: Main Django app directory
- `models.py`: Data models for the application
- `views.py`: View functions for handling requests
- `forms.py`: Form classes for data input
- `urls.py`: URL configurations for the app
- `templates/`: HTML templates for rendering pages
- `kigali_sustainability/`: Project settings directory
- `manage.py`: Django's command-line utility for administrative tasks

## Contributing

Contributions to improve the Kigali Sustainability Dashboard are welcome. Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Kigali City Council for providing the initial dataset and project requirements
- Django community for the excellent web framework and documentation   
