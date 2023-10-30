# Database Schema

This document provides an overview of the database schema used in the project. It outlines the tables, their relationships, and the data stored in the database.

## Tables

### Users Table

- **Table Name:** `auth_user`
- **Description:** This table stores user data, including usernames, passwords, and email addresses.
- **Columns:**
  - `id`: Unique identifier for each user.
  - `username`: User's username.
  - `password`: User's hashed password.
  - `email`: User's email address.

### User Profile Table

- **Table Name:** `outlook_oauth_app_userprofile`
- **Description:** This table stores additional user profile information.
- **Columns:**
  - `id`: Unique identifier for each user profile.
  - `user_id`: Foreign key to the `auth_user` table, linking each user profile to a user.
  - Additional columns for user profile information.

### OAuth User Data Table

- **Table Name:** (Table name specific to your project)
- **Description:** This table stores user data retrieved from the Outlook OAuth authentication process.
- **Columns:**
  - `id`: Unique identifier for each OAuth user data record.
  - `user_id`: Foreign key to the `auth_user` table, linking each record to a user.
  - Additional columns for Outlook OAuth user data.

## Relationships

- The `auth_user` table and the `outlook_oauth_app_userprofile` table are linked by the `user_id` foreign key, creating a one-to-one relationship between user data and user profiles.

- The `auth_user` table is connected to the table storing Outlook OAuth user data, which can be referenced by the user ID.

## Additional Tables

Your project may include additional tables for features, content, or any specific functionality. Ensure that you document those tables and their relationships separately.

## Database Migration

To create or update the database schema, use Django's database migration tools. Run the following command to apply migrations:

python manage.py migrate


## Conclusion


This `database_schema.md` document provides an overview of the database schema used in your project, describing the primary tables, their relationships, and how to perform database migrations. Users and developers can refer to this document to understand the project's data structure and the relationships between different tables.
