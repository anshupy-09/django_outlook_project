# API Endpoints

This document provides information about the available API endpoints and how to use them. You can use Postman or a similar tool to test and interact with the project's API.

## Authentication

Before you can access the API endpoints, ensure that you have registered and logged in with your Outlook credentials through the project's web interface.

## Endpoints

### User Registration

- **URL:** `/api/register/`
- **Method:** POST
- **Description:** Register a new user in the system.

#### Request Example

```json
{
  "username": "newuser",
  "password": "mypassword",
  "email": "newuser@example.com"
}

Response Example

{
  "id": 1,
  "username": "newuser",
  "email": "newuser@example.com"
}

USER LOGIN

    URL: /api/login/
    Method: GET
    Description: Log in as an existing user.


USER PROFILE(Authenticated)

    URL: /api/user/
    Method: GET
    Description: Get user profile information.


Logout (Authenticated)

    URL: /api/logout/
    Method: GET
    Description: Log out the currently authenticated user.


Error Handling

    The API provides error responses for invalid requests or authentication issues.
    Ensure you handle error responses gracefully in your application.

Testing with Postman

   - Open Postman.

   - Create a new collection for your project.

   - Create requests for each of the API endpoints listed above.

    - Use the provided request examples for user registration and test the API.

    - Authenticate as a user, and then test the user profile and logout endpoints.


## Conclusion
This `api_endpoints.md` document describes the available API endpoints, provides examples of request and response formats, and suggests how to test the endpoints using Postman. Users and developers can refer to this document to understand the available API functionality and how to interact with it for testing or integration into their applications.
