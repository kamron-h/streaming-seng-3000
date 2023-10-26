# streaming-seng-3000

# Software Architecture and Design: Assignment 1

## Introduction
This assignment focuses on demonstrating skills related to database modeling, web API creation, ORM capabilities, and version control using Git. 

## Requirements

### **Models**
- **Entities**: We've chosen three models for this assignment:
  - `Video`
  - `Actor`
  - `Rating`
  
- **Annotations**: Ensure your models have:
  - Proper annotations for table names.
  - Column names, data types, and constraints.

- **Relationships**: Implement a 1-many relationship, e.g., an `Actor` can have multiple `Video` entries.

- **Seed Data**: Populate at least one table with initial data.

- **Custom Index**: Create a custom index on any of the model attributes.

### **Web API**
- **Endpoints**: Develop at least 10 endpoints distributed across the three models:
  - 2x GET All (e.g., Get all videos, Get all actors)
  - 2x GET Specific (e.g., Get a video by ID, Get an actor by ID)
  - 2x POST (e.g., Create a video, Add an actor)
  - 2x PUT (e.g., Update a video, Update an actor)
  - 2x DELETE (e.g., Delete a video, Remove an actor)

- **Relationship Access**: Retrieve related data, e.g., videos a specific actor has been in.

- **Data Filtering**: Implement data filtering in your GET specific endpoints.

- **CRUD Operations**: Ensure endpoints for CRUD operations.

- **Endpoint Testing**: Test endpoints using tools like Postman. Submit the test cases with your assignment.

### **ORM**
- **Model Updates**: Demonstrate database updates based on model changes. Provide before-and-after screenshots.

- **Schema Rollback**: Show that you can rollback the database. Include before-and-after screenshots.

### **GIT**
- **Repository**: Initialize your project as a git repository.

- **.gitignore**: Add an appropriate .gitignore file.

- **Commits**: Regularly commit your changes.

- **Submission**: Compress your `.git` folder into `Assignment1_LastName_FirstName.zip` for submission.

## Instructions
1. **Setup**: Choose a web framework and ORM.
2. **Database**: Design your database tables based on the models.
3. **API Development**: Develop and test your API endpoints.
4. **ORM Commands**: Update your database with ORM commands. Document each change.
5. **Git**: Commit your changes regularly.
6. **Testing**: Test each endpoint using Postman or another tool. Save the test cases.
7. **Documentation**: Write brief documentation for each endpoint.
8. **Submission**: Compress and submit your `.git` folder.
