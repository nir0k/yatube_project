# Yatube Project

Welcome to the Yatube Project, a social network for writers to share their original content. This README is available in multiple languages:

- [English](README.md)
- [Русский](README.ru.md)

Please select your preferred language to continue.

## Description
Yatube is a social network designed for writers who wish to share their original content with a like-minded community. It offers a welcoming space for creative expression and connection among authors.

### Features
- **Latest Posts:** Users can browse the most recent submissions to stay up-to-date with community content.
- **Group Posts:** Explore posts shared within specific interest groups for targeted inspiration.
- **Post Submission:** Leveraging an administrative panel, users can easily publish their writings.
- **Groups:** Create or join groups to foster a more engaged community around common interests.

## Technologies
- **Python 3.9:** For backend functionality, ensuring fast and reliable service.
- **Django 2.2.19:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Getting Started

### Prerequisites
- Python 3.9
- Pip (Python package installer)

### Installation
1. **Clone the Repository**
    ```sh
    git clone git@github.com:nir0k/yatube_project.git
    cd yatube_project
    ```

2. **Set Up a Virtual Environment**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```sh
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. **Database Migrations and Superuser Creation**
    Navigate to the project directory where `manage.py` is located:
    ```sh
    cd yatube
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```

5. **Run the Development Server**
    ```sh
    python3 manage.py runserver
    ```

### Usage
- **View Posts:** Access http://localhost:8000 to see the latest posts from the community.
- **Admin Console:** Manage posts and groups by navigating to http://localhost:8000/admin.

## Support
For support, please open an issue in the GitHub repository or contact the project maintainers directly.

## Contributing
We welcome contributions! Please refer to our contribution guidelines for more information on how you can contribute to the Yatube Project.

## License
This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.
