# # Use an official Python runtime as a base image
# FROM python:3.11.4

# # Set the working directory in the container
# WORKDIR /E:/new_project/outlook 

# # Copy the requirements file into the container at /usr/src/app
# COPY requirements.txt ./

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the current directory contents into the container at /usr/src/app
# COPY . .

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
# CMD ["gunicorn", "-b", "0.0.0.0:8000", "your_project.wsgi"]

FROM python:3.11.4-alpine3.18

# ENV PYTHONBUFFERED=1
# ENV PATH="/scripts:${PATH}"

# Allows docker to cache installed dependencies between builds
WORKDIR /app
COPY requirements.txt requirements.txt
# RUN apk add --update ==no cache ==virtual .tmp gcc libc-dev linux-headers
# RUN apk del .tmp
RUN pip install -r requirements.txt

COPY . .
# Expose the port the application runs on
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000