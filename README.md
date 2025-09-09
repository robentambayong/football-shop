# Football Shop

🔗 **Deployed Application:** [https://roben-joseph-footballshop.pbp.cs.ui.ac.id]

---

## 1. Step-by-Step Implementation

I implemented the Django project by following a checklist, but I went beyond simply copying a tutorial. Here’s the process in my own steps:

1. **Project Initialization**  
   - Created a new Django project with `django-admin startproject football_shop`.  
   - Set up a virtual environment (`python -m venv env`) and installed required dependencies from `requirements.txt`.

2. **App Creation**  
   - Generated the main app with `python manage.py startapp main`.  
   - Registered it in `INSTALLED_APPS` within `settings.py`.

3. **URL Routing**  
   - Added a `urls.py` inside the `main` app.  
   - Configured `football_shop/urls.py` to include routes from the `main` app.

4. **Views and Templates**  
   - Implemented functions in `views.py` to handle requests.  
   - Created corresponding HTML templates inside `main/templates/main/`.

5. **Models and Database**  
   - Designed models in `models.py`.  
   - Ran migrations with `python manage.py makemigrations` and `python manage.py migrate`.  
   - Verified database changes with the Django admin panel.

6. **Static Files & Whitenoise**  
   - Configured static files for deployment and enabled Whitenoise middleware for serving them.

7. **Deployment to PWS**  
   - Added `requirements.txt`.  
   - Pushed the project to the PWS GitLab remote (`git push pws main:master`).  
   - Fixed issues by ensuring all project files (including `requirements.txt`) were properly tracked in Git.

---

## 2. Django Request-Response Flow Diagram

Below is the flow of a client request to a Django web application:

Client (Browser)
      |
      v
  urls.py  --->  views.py  --->  models.py  ---> Database
      |               |
      |               v
      |           HTML Template (rendered)
      |               |
      v               v
   HTTP Response <--- Django

### Explanation:
- **`urls.py`**: Acts as a router. It decides which view function should handle the incoming request.  
- **`views.py`**: Contains the logic. It processes requests, interacts with models, and returns responses.  
- **`models.py`**: Defines the data structure and communicates with the database.  
- **HTML Templates**: Present the final output to the user, filled with data passed from the view.  

---

## 3. The Role of `settings.py`

- Central configuration file for the Django project.  
- Defines database settings, installed apps, middleware, templates, and static files.  
- Manages environment variables for sensitive information (e.g., `SECRET_KEY`, database credentials).  
- Controls debug mode and allowed hosts for development vs production environments.

---

## 4. Database Migration in Django

Migrations in Django translate changes in `models.py` into actual database schema updates:
1. `python manage.py makemigrations` → creates migration files that describe changes.  
2. `python manage.py migrate` → applies the changes to the database.  

This ensures the database stays synchronized with the Python model definitions while preserving existing data.

---

## 5. Why Django as a Starting Framework?

- **Batteries included**: Django provides ORM, authentication, admin panel, and more out of the box.  
- **Structured**: Encourages the MVC/MVT pattern, making it easier to learn software architecture.  
- **Scalable**: Can be used for small projects and scaled to large applications.  
- **Community & Documentation**: Django has excellent documentation and strong community support.  

For beginners, Django reduces the complexity of setting up a web application while teaching best practices.

---

## 6. Feedback for Tutorial 1

I really appreciated that the TA explained each step patiently.  
Some feedback:  
- It would be great if more real-world examples were provided (e.g., why we need migrations in practice).  
- Sometimes the pace was a bit fast — slowing down during tricky parts like database setup would help beginners.  

Overall, it was a helpful and enjoyable session! 🙌

---
