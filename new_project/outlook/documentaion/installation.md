# Installation Guide

## Prerequisites
Before you begin, ensure you have the following installed:
- Python (version 3.11.4)
- Django (version X.X.X)
- PostgreSQL

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/anshupy-09/outlook.git
    cd outlook
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Environment Variables**

    Create a `.env` file in the project root and add the necessary environment variables. (If applicable)

6. **Apply Database Migrations**

    ```bash
    python manage.py migrate
    ```

7. **Start the Development Server**

    ```bash
    python manage.py runserver
    ```

8. **Access the Application**

    Open your web browser and go to [http://localhost:8000](http://localhost:8000/accounts/login)(http://localhost:8000/home/)

---

**Note**: 
This `installation.md` document provides clear instructions on how to set up and install your project, covering prerequisites, cloning the repository, creating a virtual environment, installing dependencies, configuring Outlook OAuth, running migrations, starting the development server, and accessing the project. Users should be able to follow these steps to get your project up and running on their local development environment.


For more detailed information, refer to the [official documentation](link_to_more_detailed_installation_guide).

