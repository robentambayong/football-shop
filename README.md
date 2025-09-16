# Football Shop

**Deployed Application:** [https://roben-joseph-footballshop.pbp.cs.ui.ac.id]

---

## **Assignment 3:**

> **Note:** This section contains my work for Assignment 3.  
> The original Assignment 2 answers follows after the the assignment 3.

---

## 1. Why do we need data delivery in implementing a platform?

Data delivery (exposing application data as machine-readable formats such as JSON or XML) is essential because it makes an application **composable, automatable, and reusable**:

   - It lets different clients consume the same backend: web pages, single-page apps, mobile apps, other services, or third-party tools can all use the same endpoints.  
   - Data delivery enables integrations, automation, and scaling: analytics systems, external services, or other teams can consume data without relying on the UI.  
   - Practically, this means we can build a web UI now, and later a mobile app or partner integration without changing the core backend.

---

## 2. XML vs JSON - Which is better? Why is JSON more popular?

JSON is the more practical choice for modern web APIs, but XML still has useful features in certain domains.

**Why JSON is generally preferred**
   - **Lightweight and concise.** JSON payloads are smaller and easier to scan than equivalent XML.  
   - **Native mapping to JavaScript objects.** Web apps (and many tools) can parse JSON directly into usable objects (`JSON.parse()`), which speeds development.  
   - **Cleaner syntax.** No closing tag verbosity; easier to read and write.  
   - **Ecosystem and tooling.** Modern web frameworks and libraries expect or generate JSON by default.

**When XML is still useful**
   - XML supports attributes, mixed content, namespaces, and formal schema validation. These strengths make XML suitable for document-centric or some enterprise systems (e.g., legacy integrations, complex document formats).

**Conclusion:** For REST-style APIs and most web/mobile needs, JSON’s simplicity and native integration with JavaScript make it the better default. The course slides provide comparison context and historical reasons behind JSON’s rise.

---

## 3. What does `is_valid()` do in Django forms, and why do we need it?

`is_valid()` performs validation and cleaning of form input:

   - When you call `form.is_valid()` Django:
   - Runs each field’s validators (required flags, type checks, custom validators).
   - Converts and cleans raw input into Python types and stores them into `form.cleaned_data`.
   - Populates `form.errors` if validation fails and returns `False`.
   - Returns `True` when all validation checks pass.

**Why this matters**
   - It prevents invalid or malicious data from being saved into the database.
   - It centralizes validation logic (field validators, `clean_<field>()`, and `clean()`).
   - Always call `is_valid()` before using `form.cleaned_data` or calling `form.save()`.

---

## 4. Why do we need `{% csrf_token %}` in Django forms? What happens without it?

**What CSRF protection prevents**
   - CSRF (Cross-Site Request Forgery) protects authenticated users from unwanted actions triggered by third-party pages.  
   - If a user is logged into `example.com`, a malicious page could cause the browser to submit a POST request to `example.com` (using the user's cookies), performing actions on their behalf. unless the server verifies the request's origin.

**How Django defends**
   - Django includes `CsrfViewMiddleware` by default and expects every POST form to include a token generated per user session.
   - In templates, we add `{% csrf_token %}` inside `<form method="post">` so the token goes into the POST body and Django can verify it.

**What happens if we don't include CSRF protection**
   - Attackers can craft hidden forms or image requests that force the victim’s browser to perform state-changing actions (create/delete/update).  
   - Example exploit: a malicious page auto-submits a form to `example.com/transfer/` making the victim unknowingly transfer funds or change their account settings.

**Mitigations beyond `{% csrf_token %}`**
   - Keep `CsrfViewMiddleware` enabled (default).
   - For AJAX, send the token in a header (example: `X-CSRFToken`) or use fetch/fetch wrappers that include it.
   - Use `SameSite` cookie settings to further reduce cross-site request risk.

---

## 5. How I implemented the checklist — step-by-step (not just following the tutorial)

### A — Summary of what I added:
1. **Four data endpoints** to return products in XML and JSON:
   - `/api/products/json/` → all products (JSON)
   - `/api/products/xml/` → all products (XML)
   - `/api/products/json/<id>/` → single product by id (JSON)
   - `/api/products/xml/<id>/` → single product by id (XML)

2. **HTML pages**:
   - A **product list** page showing all products with an **Add** button and a **Detail** link for each product.
   - A **product add** page with a form to create new products.
   - A **product detail** page that displays one product’s data.

3. **Form**:
   - A `ProductForm` (`main/forms.py`) implemented as a **ModelForm** for easy validation and saving.

4. **Routing**:
   - URL patterns added to `main/urls.py` for both the HTML pages and the API endpoints.
   - Project `football_shop/urls.py` includes the `main` app’s URLs.

5. **Validation & security**:
   - The add form uses `form.is_valid()` to validate inputs before saving.
   - Templates use `{% csrf_token %}` to protect POST requests.

### B — Files I created or edited:
   - `main/forms.py` — `ProductForm` (ModelForm)
   - `main/views.py` — added:
   - `api_products_json`, `api_products_xml`, `api_product_json`, `api_product_xml` (these use `django.core.serializers.serialize()` to return XML/JSON)
   - `product_list`, `product_detail`, `product_add` (HTML views)
   - `main/urls.py` — added routes for API + pages
   - `main/templates/main/product_list.html` - shows list + Add + Detail links
   - `main/templates/main/product_form.html` — form to add product (includes `{% csrf_token %}`)
   - `main/templates/main/product_detail.html` — display single product details

### C — Implementation notes & small decisions:
   - I used **Django serializers** (`serializers.serialize("json", queryset)`) for consistent, simple JSON/XML output. This is quick for small projects and ensures field names match model fields.
   - For the HTML add form, I used `ModelForm` from the 2nd tutorial so validation and saving are straightforward.

---

## Feedback for Tutorial 2
   
   Overall the tutorial was very useful and practical, the hands-on exercises helped me understand forms and basic API endpoints. I think it would be way better if:

      - Add a short troubleshooting checklist for common deployment problems (requirements.txt placement, branch mismatch on PWS, Procfile basics).
      - A quick demo showing the same action performed via a Django form and via a JSON API (Postman) would make the conceptual difference clearer for us.

---

## Postman Testing & Screenshots

### JSON list
![JSON list screenshot](docs/postman/json_list.png)

### XML list
![XML list screenshot](docs/postman/xml_list.png)

### JSON by ID
![JSON by ID screenshot](docs/postman/json_by_id.png)

### XML by ID
![XML by ID screenshot](docs/postman/xml_by_id.png)



------------------------------------------------------------------------------------------------------------------------------



## **Assignment 2:**

> **Note:** This section contains my work for Assignment 2.  
> The Assignment 3 answers are abvailable above.

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