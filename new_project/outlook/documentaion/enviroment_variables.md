# Environment Variables

This document provides a list of environment variables used in the project and their purposes. Environment variables are a secure way to store sensitive information and configuration settings.

## Project-specific Environment Variables

### `SECRET_KEY`

- **Purpose**: Django's secret key used for cryptographic operations.
- **Value**: A long, random string of characters.
- **Storage**: Set this environment variable to ensure the security of your Django project.

### `DATABASE_URL`

- **Purpose**: Database connection URL, including the database type, username, password, host, and port.
- **Value**: Example: `postgres://myuser:mypassword@localhost:5432/mydatabase`
- **Storage**: Store the database connection details in this environment variable.

### `OUTLOOK_OAUTH_APP_ID`

- **Purpose**: Microsoft Outlook OAuth App ID for authentication.
- **Value**: Your Outlook App ID obtained from the Microsoft Developer Portal.
- **Storage**: Securely store your Outlook OAuth App ID to enable authentication with Outlook.

### `OUTLOOK_OAUTH_APP_SECRET`

- **Purpose**: Microsoft Outlook OAuth App Secret for authentication.
- **Value**: Your Outlook App Secret obtained from the Microsoft Developer Portal.
- **Storage**: Securely store your Outlook OAuth App Secret.

## Setting Environment Variables

To set environment variables in your development environment, you can use different methods depending on your operating system:

- **Linux/macOS**:
  - In your terminal, use the `export` command to set environment variables.

    ```shell
    export VARIABLE_NAME="variable_value"
    ```

- **Windows**:
  - Use the `set` command in the Command Prompt to set environment variables.

    ```shell
    set VARIABLE_NAME=variable_value
    ```

To ensure that environment variables are available each time you start your project, you can use a `.env` file and a tool like `python-dotenv` to load them. Create a file named `.env` in your project's root directory and add your environment variables:

```shell
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://myuser:mypassword@localhost:5432/mydatabase
OUTLOOK_OAUTH_APP_ID=Your-Outlook-App-ID
OUTLOOK_OAUTH_APP_SECRET=Your-Outlook-App-Secret
