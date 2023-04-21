# Simple Blog Project with Django and Vue.js

This project is a simple blog built with Django and Vue.js. The backend is built with Django and the frontend with Vue.js. The communication between the two is done through the Axios API.

## Features available:

- Landing page
- Backend CMS-CRUD to add content to website
- Posts about Testing

## Features to add

- User authentication: Users can register and login to create, edit and delete their own posts.
- Posts: Users can create, edit and delete posts. Each post has a title, a body and a timestamp.
- Comments: Users can leave comments on posts. Each comment has a name, an email, a body and a timestamp.
- Responsive Design: The blog is designed to look good on any device.

## Technologies Used

- Django
- Django REST Framework
- Vue.js
- Axios

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
- -> `python -m venv venv`
- -> `venv\Scripts\activate`
3. Install the dependencies with
- -> `pip install -r requirements.txt`.
4. Run the migrations with
- -> `python manage.py migrate`.
5. Start the development server with
- -> `python manage.py runserver`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
