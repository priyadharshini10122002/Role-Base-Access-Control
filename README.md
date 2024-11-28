# Role-Based Access Control (RBAC) in Django
This repository demonstrates the implementation of Role-Based Access Control (RBAC) using Django. The project features user authentication and permission management through groups, aligning permissions with user roles like Admin, Staff, and Basic User.

# Features
- User Authentication: Secure login and token-based authentication using Django REST Framework.
- Role-Based Permissions: Permissions are assigned to groups (Admin_User, Staff_User, Basic_User) rather than individual users.
- CRUD Operations: Users can perform actions on resources (e.g., News) based on their assigned role.
- Groups and Permissions: Automatically assigns permissions to groups via management commands.
- REST API Integration: Includes endpoints for managing News models and user roles.

# Technologies Used
- Python 3.x
- Django 4.x
- Django REST Framework (DRF)
- PostgreSQL 17
- Git for version control
  
# PostMan Collection 
  https://api.postman.com/collections/35061861-85dd2d53-bd03-44f6-bbb6-6b09d8477a28?access_key=PMAT-01JDS6428VWMJ1C2PA1KMH1GGE
