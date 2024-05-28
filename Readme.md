The Bookstore App mimics, well, an online bookstore - books, covers, reviews, etc. The App was built with Django, a powerful Python web development framework.

While keeping a relatively simple, Bootstrap-based user interface, the App features pretty complex internal logic and functionality, such as a custom user model and advanced user registration, complex search filters, image uploads, permissions, and a host of other goodies. 

App went through necessary performance optimizations including the addition of a debug toolbar to inspect queries and templates, database indexes, front-end assets, etc, as well as additional security configurations that can, and should, be added for a production environment. The app's functionality is extensively covered by unit tests. A production PostgreSQL cluster is used for storing all the data.

While working on this project, I went a bit further than the book itself and implemented OAuth social authentication with GitHub and Google, extended the DB model's external view with UUID while keeping the original auto-increment PK for internal foreign-key relationship between tables for performance reasons, ensured working DevOps solution for both local development with Docker Compose and a production one on the fly.io PaaS, etc. The room for improvement is still there, of course, but now it is time to move on to the REST API area.

Explore the deployed app here:
https://bookstore-lugres.fly.dev/

The project is based on the book "Django for Professionals v4.0" by William S. Vincent
https://djangoforprofessionals.com/