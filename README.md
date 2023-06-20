# Django Blog App

![Blog App Banner](https://i.imgur.com/oN71fj9.jpg)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAkash1362000%2FDjango_BlogApp%2F&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Akash1362000/Django_BlogApp/graphs/commit-activity)

### Demo 🎥

![BlogApp Demo](https://i.imgur.com/mpntklM.gif)

### Checkout the live website [here](https://blog-app-w21y.onrender.com)

### Development 👨‍💻
**Note** : Make sure you have Python version 3.8+

### Environment Setup 🚀

`$ git clone https://github.com/Akash1362000/django_project_blogapp.git`

`$ cd django_project_blogapp/`

If virtualenv is not installed [(What is virtualenv?)](https://www.youtube.com/watch?v=N5vscPTWKOk&t=313s):

`$ pip install virtualenv`

Create a virtual environment

`$ virtualenv venv`

Activate the environment everytime you open the project

`$ source venv/Scripts/activate`

Install requirements 🛠

`$ pip install -r requirements.txt`

`$ pre-commit install`

Run migrations for Database


`$ python manage.py migrate`

Create superuser for Admin Login 🔐

`$ python manage.py createsuperuser`

Enter your desired username, email and password. Make sure you remember them as you'll need them in future.

eg.

    Username: admin

    Email: admin@admin.com

    Password: HighlyConfidentialPassword

All Set! 🤩

Now you can run the server to see your application up & running 🚀

`$ python manage.py runserver`

To exit the environment ❎

`$ deactivate`

Every time you want to open the application in browser, make sure you run:

`$ source venv/Scripts/activate`

`$ python manage.py runserver`


---
## Docker Setup (Optional) ![](https://skillicons.dev/icons?i=docker)

If you want to use Docker to run this project, you need to do the following steps:
- Install Docker for your OS from [here](https://www.docker.com/products/docker-desktop/)
- Run `docker --version` and `docker compose --version` [In Windows, you need to run `docker-compose --version` to check the version]
- If you see both the versions, then Docker is successfully installed on your system and you can follow along
- If you don't see the version, check with your Docker installation
- Run `docker compose up -d`
- Run `docker exec -it blog_app sh -c "python manage.py createsuperuser"` to create a new superuser
- Access the app at [http://localhost:8000](http://localhost:8000)
- To stop the container, run `docker compose stop` from the project root
- To restart the container, run `docker compose start` from the project root
- To delete the container, run `docker compose down` from the project root

---


## Stargazers

[![Stargazers](https://reporoster.com/stars/Akash1362000/Django_BlogApp)](https://github.com/Akash1362000/Django_BlogApp/stargazers)

Leave a ⭐ from [here](https://github.com/Akash1362000/Django_BlogApp) if you like 😁

---

### License ✍

```
MIT License

Copyright (c) 2020 Akash Shrivastava

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
