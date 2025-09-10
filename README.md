# Football Shop

**Deployed Application:** [https://roben-joseph-footballshop.pbp.cs.ui.ac.id]

---

## 1. Step-by-Step Implementation

I implemented the Django project by following a checklist, but I made sure I actually understood each step and adapted it to my own workflow. Here’s how it went:

1. **Project Initialization**
   
   I started by setting up the project environment. First, I created a fresh Django project using `django-admin startproject football_shop`.

   To keep everything organized and avoid dependency issues, I also created a virtual environment `python -m venv env` and activated it. Inside this environment, I installed all the required dependencies listed in `requirements.txt`. This way, my project had a clean and isolated setup.

2. **App Creation**  
   
   Once the project structure was ready, I created the core app for my project with `python manage.py startapp main`.
   
   Then, I registered `main` in the`INSTALLED_APPS` section of `settings.py` so Django could recognize and use it.

3. **URL Routing**  
   
   For the URLs, I wanted to keep things modular. I created a separate `urls.py` file inside the `main` app and set up all the routes there. Then, in the main `football_shop/urls.py`, I included those routes so the app and project were properly connected. This made the project structure cleaner and easier to scale.

4. **Views and Templates**  
   
   I worked on building the logic inside `views.py` to handle different requests. For each view, I created corresponding HTML templates inside `main/templates/main/`. This followed Django’s MTV (Model–Template–View) pattern and made sure everything lined up logically, views handled the logic, while templates handled the presentation.

5. **Models and Database**  
   
    Next, I designed my models inside `models.py` to represent the data I wanted to store. After defining the models, I applied them to the database with `python manage.py makemigrations` and `python manage.py migrate`. 
    
    To double-check everything worked, I opened the Django admin panel and verified that the tables and records matched my expectations.

6. **Static Files**  
   
   For local development, Django automatically serves static files when `DEBUG=True`. Since this project is primarily for learning purposes and small-scale deployment, I relied on Django’s built-in static file handling during development. No additional configuration was added.

7. **Deployment to PWS**  
   
   Finally, I prepared the project for deployment. I made sure my `requirements.txt` included everything needed (django, gunicorn, whitenoise, etc.), then pushed my local repository to the PWS GitLab remote with `git push pws master`. In some cases, when my local branch was still named main, I used `git push pws main:master` to match the remote branch.
   
   There were some issues along the way. For example, the project didn’t build at first because my requirements.txt wasn’t included properly. To fix it, I double-checked that all the necessary files were committed and pushed, then retried the deployment. After that, the app finally ran successfully on PWS.

---

## 2. Django Request-Response Flow Diagram

Below is the flow of a client request to a Django web application:

```
        HTTP Request
              |
              v
        +-------------+
        |   URLS      |   (urls.py)
        +-------------+
              |
              | Forward request
              v
        +-------------+
        |   View      |   (views.py)
        +-------------+
         /     |      \
        /      |       \
       v       v        v
+-------------+  +---------------+
|   Model     |  |  Template     |
| (models.py) |  | (<file>.html) |
+-------------+  +---------------+
     ^                |
     |  read/write    |  Render HTML
     |     data       v
     +----------------+
              |
              v
        HTTP Response (HTML)
```

### Explanation:
- **urls.py**: Acts as a router. It decides which view function should handle the incoming request.  

- **views.py**: Contains the logic. It processes requests, interacts with models, and returns responses.  

- **models.py**: Defines the data structure and communicates with the database.  

- **HTML Templates**: Present the final output to the user, filled with data passed from the view.  

### Analogy: A Company Visit
- **urls.py** → The Receptionist:
Decides which office (view) the visitor should go to based on the URL.

- **views.py** → The Office Worker:
Handles the visitor’s request, talks to the filing cabinet, and prepares a response.

- **models.py** → The Filing Cabinet:
Stores and retrieves data (database).

- **HTML Templates** → The Brochure:
The final presentation handed back to the visitor.

---

## 3. The Role of `settings.py`

Think of `settings.py` as the **control center** of your Django project. Almost everything your project does looks here for instructions. Some of the key things it manages:

- **Database configuration** → tells Django which database to use (SQLite, PostgreSQL, MySQL, etc.) and how to connect.  
- **Installed apps** → lists all the Django apps (both built-in and custom) that your project needs.  
- **Middleware** → defines a chain of hooks that process requests and responses (e.g., authentication, security, sessions).  
- **Templates and static files** → where Django should look for HTML templates, CSS, JavaScript, and images.  
- **Sensitive settings** → things like `SECRET_KEY`, API keys, and database credentials. In real projects, these are usually stored as environment variables instead of hardcoding them.  
- **Debugging and security** → `DEBUG=True` for development shows detailed errors, while in production you switch it off and configure `ALLOWED_HOSTS` to specify which domains can serve your site.  

In short, `settings.py` is the **instruction manual** that Django follows every time the server runs.

---

## 4. Database Migration in Django

Migrations in Django translate changes in `models.py` into actual database schema updates:
1. `python manage.py makemigrations` → creates migration files that describe changes.  
2. `python manage.py migrate` → applies the changes to the database.  

This ensures the database stays synchronized with the Python model definitions while preserving existing data.

---

## 5. Why Django as a Starting Framework?

Django is often recommended for beginners and professionals alike because it balances power with simplicity:

- **Batteries included** philosophy:
Out of the box, Django gives you a powerful ORM, authentication system, form handling, session management, admin dashboard, and much more. You don’t have to reinvent the wheel.

- **Encourages good structure**:
Django follows the MVT (Model–View–Template) architecture. This separation of concerns helps beginners understand how web apps are organized and makes the project easier to maintain as it grows.

- **Scales with you**:
You can start small (a personal blog, a simple API) and later scale up to enterprise-level applications (Django powers Instagram, Pinterest, Disqus).

- **Strong community & documentation**
Django’s documentation is considered one of the best in open source. On top of that, the community is huge, meaning plenty of tutorials, StackOverflow answers, and open-source packages to help you. For beginners, Django reduces the complexity of setting up a web application while teaching best practices.

---

## 6. Feedback for Tutorial 1

I really appreciated that the TAs explained each step patiently with a very clear and straight-forward instructions.

Some feedback:  
- It would be great if more real-world examples were provided (e.g., why we need migrations in practice).  
- Sometimes the pace felt a bit fast, especially during trickier parts like setting up the database or running migrations. It might help to slow down at those points, give a little extra explanation, or pause for questions so everyone can follow along. 

Overall, it was a helpful and enjoyable session! 🙌

---