# Django CRUD API

Project is created with
* Django 3.2
* Python 3.8

[Postman Collection Endpoint](https://drive.google.com/file/d/1VbtlKN0qtvuz61Tg0pR_j9Uyq-xgNBX2/view?usp=sharing)

Division Table Attribute
* id
* division_name
* created_at
* updated_at

Employee Table Attribute
* id
* first_name
* last_name
* hire_date
* created_at
* updated_at
* divisi (Foreign Key)

The Endpoint is
Division
| Method          | Endpoint                                                          |
| -------------   | -------------                                                     |
| POST            | http://djangotest.pythonanywhere.com/api/create-division/         |
| GET             | http://djangotest.pythonanywhere.com/api/division-detail/id       |
| GET             | http://djangotest.pythonanywhere.com/api/division-list/?page=1    |
| DEL             | http://djangotest.pythonanywhere.com/api/division-delete/id       |
| PUT             | http://djangotest.pythonanywhere.com/api/division-update/id       |


Employee
| Method          | Endpoint                                                          |
| -------------   | -------------                                                     |
| POST            | http://djangotest.pythonanywhere.com/api/create-employee/         |
| GET             | http://djangotest.pythonanywhere.com/api/employee-detail/id       |  
| GET             | http://djangotest.pythonanywhere.com/api/employee-list/?page=1    |
| DEL             | http://djangotest.pythonanywhere.com/api/employee-delete/id       |
| PUT             | http://djangotest.pythonanywhere.com/api/employee-update/id       |

List Record Using Pagination, that allow only 2 record every pages
