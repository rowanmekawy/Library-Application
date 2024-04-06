# Library Management Application

This application is a simple Library Management System that allows users to manage a collection of books. It includes a frontend built with Vue3 and a backend API that performs CRUD operations on book data stored in a MongoDB database.

## Technology Used

- **Frontend:** Vue3, Vuetify
- **Backend:** Flask (Python)
- **Database:** MongoDB
- **Testing:** pytest
- **Containerization:** Docker, Docker Compose

## Running the Application with Docker

To run the application using Docker, follow these steps:

1. Build the Docker images:

   ```bash
   docker-compose build
    ```
2. Start the containers:

    ```bash
   docker-compose up
    ```
## Running Tests
1. Activate your enviroment

2. Run test
    ```bash
    python -m pytest
