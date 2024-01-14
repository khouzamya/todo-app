<div align="center">
  <h1>Django Todo APP</h1>
</div>

## Introduction 🧚

Django TODO APP to manage todo-lists and to-do items inside every list.


### Setting up the project 👷

Clone the repository and navigate to its directory:

    $ git clone https://github.com/khouzamya/todo-app.git
    $ docker build -t todo-python .
    $ docker run -d -p 8000:8000 todo-python

The default username and password for the super user are:

    Username: demo
    Password: Test@12345

Use Django admin console to create more users

To make the deployment simpler, Django debug is enabled ( Django server can serve static files for admin console)


### APIS

To get access token

    POST http://localhost:8000/api/token/

        Request:

            
            {
                "username": "demo",
                "password": "Test@12345"
            }
            
        Response:

            
            {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNTI3NTUwMSwiaWF0IjoxNzA1MTg5MTAxLCJqdGkiOiIwNmI2OWFiYjI3YWM0MDcwOWFiZjBhNDU2OTA2YzQ1YSIsInVzZXJfaWQiOjJ9.Us930UpUxSAQO_kcnyV2MWweKSIboEA0wWfKcS_MYoE",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1MTkyNzAxLCJpYXQiOjE3MDUxODkxMDEsImp0aSI6IjNjZGYwMzA1MGFmNTRiY2ZiZGQ2MWYxNjk1NmRmM2ZhIiwidXNlcl9pZCI6Mn0.zQrZY5nAfmpb5Q0oEOGq_aFaPrKT8glJsfq52cnRwVI"
            }
            


To get refresh token

    POST http://localhost:8000/api/token/refresh/

        Request:

            
            {
                "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNTI3NTUwMSwiaWF0IjoxNzA1MTg5MTAxLCJqdGkiOiIwNmI2OWFiYjI3YWM0MDcwOWFiZjBhNDU2OTA2YzQ1YSIsInVzZXJfaWQiOjJ9.Us930UpUxSAQO_kcnyV2MWweKSIboEA0wWfKcS_MYoE",
            }
            
        Response:

            
            {
                "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1MjM1MTMwLCJpYXQiOjE3MDUyMzE1MTAsImp0aSI6ImJjMWY0YWFhZmU0YTRmMTg5ZDAwYjMxMmM2MDYzOTAyIiwidXNlcl9pZCI6MX0.H2LEnK1KKRsuhpAGZpe9LPNS5x6ih5IFm7tmVEoqnVI"
            }
            

Need to send the access token in all requests in the header using bearer token authentication

To create a TODO list

    $ POST http://localhost:8000/api/v1/todos/ 

        Request:

            
            {
            "title": "Todo List 1"
            }
            
        Response:

            
            {
            "id": 1,
            "user_info": {
                "fname": "",
                "lname": "",
                "username": "demo",
                "id": 1
            },
            "title": "Todo List 1",
            "completed_at": null,
            "created_at": "2024-01-14T11:40:10.938619Z",
            "updated_at": "2024-01-14T11:40:10.938631Z"
            }
            

To update a TODO list

    $ PUT http://localhost:8500/api/v1/todos/<todo_list_id>/

        Request:

            
            {
            "title": "Todo List 1 Updated",
            "completed": true
            }
            
            The completed field is optional to mark todo list as completed.

        Response:

            
            {
            "id": 1,
            "title": "Todo List 1 Upated",
            "completed_at": null,
            "updated_at": "2024-01-14T11:45:40.900845Z",
            "todoitem": []
            }
            


To delete a TODO list (soft delete)

    $ DELETE http://localhost:8500/api/v1/todos/<todo_list_id>/

To get details of a TODO list

    $ GET http://localhost:8500/api/v1/todos/<todo_list_id>/

        Response:

            
            {
            "id": 1,
            "title": "Todo List 1 Upated",
            "completed_at": null,
            "updated_at": "2024-01-14T11:45:40.900845Z",
            "todoitem": [
                {
                "id": 1,
                "list": 1,
                "description": "Todo item for todo list 1",
                "completed_at": null,
                "created_at": "2024-01-14T11:50:51.804635Z",
                "updated_at": "2024-01-14T11:50:51.804644Z"
                },
                {
                "id": 2,
                "list": 1,
                "description": "Todo item 1 for todo list 1",
                "completed_at": null,
                "created_at": "2024-01-14T11:50:56.597440Z",
                "updated_at": "2024-01-14T11:50:56.597446Z"
                },
                {
                "id": 3,
                "list": 1,
                "description": "Todo item 2 for todo list 1",
                "completed_at": null,
                "created_at": "2024-01-14T11:50:59.430304Z",
                "updated_at": "2024-01-14T11:50:59.430309Z"
                }
            ]
            }
            


To get list of TODO lists

    $ GET http://localhost:8000/api/v1/todos/ 

        Request (Query params):

            $ search: (Optional) search by title or by user 
            $ page: (Default 1) page number

        Response:

            
            {
            "count": 4,
            "next": null,
            "previous": null,
            "results": [
                {
                "id": 1,
                "user_info": {
                    "fname": "",
                    "lname": "",
                    "username": "demo",
                    "id": 1
                },
                "title": "Todo List 1",
                "completed_at": null,
                "created_at": "2024-01-14T11:40:10.938619Z",
                "updated_at": "2024-01-14T11:40:10.938631Z"
                },
                {
                "id": 2,
                "user_info": {
                    "fname": "",
                    "lname": "",
                    "username": "demo",
                    "id": 1
                },
                "title": "Todo List 2",
                "completed_at": null,
                "created_at": "2024-01-14T11:41:34.518774Z",
                "updated_at": "2024-01-14T11:41:34.518780Z"
                },
                {
                "id": 3,
                "user_info": {
                    "fname": "",
                    "lname": "",
                    "username": "demo",
                    "id": 1
                },
                "title": "Todo List 3",
                "completed_at": null,
                "created_at": "2024-01-14T11:41:37.345191Z",
                "updated_at": "2024-01-14T11:41:37.345197Z"
                },
                {
                "id": 4,
                "user_info": {
                    "fname": "",
                    "lname": "",
                    "username": "demo",
                    "id": 1
                },
                "title": "Todo List 4",
                "completed_at": null,
                "created_at": "2024-01-14T11:41:39.920514Z",
                "updated_at": "2024-01-14T11:41:39.920517Z"
                }
            ]
            }
            


To create a TODO item inside a todo list

    $ POST http://localhost:8000/api/v1/todo/items/<todo_list_id>/

        Request:

            
            {
            "description": "Todo item 2 for todo list 2"
            }
            
        Response:

            
            {
            "id": 5,
            "list": 2,
            "description": "Todo item 2 for todo list 2",
            "completed_at": null,
            "created_at": "2024-01-14T11:51:12.585233Z",
            "updated_at": "2024-01-14T11:51:12.585237Z"
            }
            

To update a TODO item inside a todo list

    $ POST http://localhost:8000/api/v1/todo/items/<todo_list_id>/<todo_item_id>/

        Request:

            
            {
            "description": "Todo item 2 for todo list 2 (updated)",
            "completed": true
            }
            

            The completed field is optional to mark todo item as completed.

        Response:

            
            {
            "id": 5,
            "description": "Todo item 2 for todo list 2 (updated)",
            "completed_at": null,
            "updated_at": "2024-01-14T11:54:58.977196Z"
            }
            

To delete a TODO item inside a todo list

    $ DELETE http://localhost:8000/api/v1/todo/items/<todo_list_id>/<todo_item_id>/


To get details of a TODO item

    $ GET http://localhost:8000/api/v1/todo/items/<todo_list_id>/<todo_item_id>/

        Response:

            
            {
            "id": 5,
            "description": "Todo item 2 for todo list 2 (updated)",
            "completed_at": null,
            "updated_at": "2024-01-14T11:54:58.977196Z"
            }
            

To get list of a TODO items for a specific todo list

    $ GET http://localhost:8000/api/v1/todo/items/<todo_list_id>/

        Request (Query params):

            $ page: (Default 1) page number

        Response:

            
            {
            "count": 2,
            "next": null,
            "previous": null,
            "results": [
                {
                "id": 4,
                "list": 2,
                "description": "Todo item 1 for todo list 2",
                "completed_at": null,
                "created_at": "2024-01-14T11:51:09.962653Z",
                "updated_at": "2024-01-14T11:51:09.962654Z"
                },
                {
                "id": 5,
                "list": 2,
                "description": "Todo item 2 for todo list 2 (updated)",
                "completed_at": null,
                "created_at": "2024-01-14T11:51:12.585233Z",
                "updated_at": "2024-01-14T11:54:58.977196Z"
                }
            ]
            }
            
