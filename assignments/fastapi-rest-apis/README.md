# 🚀 Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API that manages task data using the FastAPI framework. You will practice defining routes, using request and response models, validating input, and returning clear JSON responses.

## 📝 Tasks

### 🛠️ Task 1: Create the API skeleton

#### Description
Build the foundation of a FastAPI application that can serve task information through HTTP endpoints.

#### Requirements
Completed program should:
- Create a FastAPI app with a health-check endpoint
- Define a task data model using Pydantic
- Provide a GET endpoint to list all tasks
- Return JSON data in a clean and readable format

### 🛠️ Task 2: Add CRUD operations

#### Description
Extend the API so it can create, read, update, and delete tasks through RESTful endpoints.

#### Requirements
Completed program should:
- Implement POST /tasks to create a new task
- Implement GET /tasks/{task_id} to retrieve one task
- Implement PUT or PATCH /tasks/{task_id} to update an existing task
- Implement DELETE /tasks/{task_id} to remove a task
- Return a 404 response when a task does not exist
- Validate input so empty task titles are rejected
