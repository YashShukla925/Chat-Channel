# Chat Channels

## Overview

Welcome to the Chat Channels project, a real-time chat application built using Django Channels. This project leverages Django Channels to handle WebSockets, enabling real-time communication between users. Whether you're looking to create a simple chat room or a complex messaging system, this guide will help you get started.

## Features

- Real-time messaging using WebSockets
- User authentication
- Chat rooms
- Private messaging
- Message history
- Online user status

## Requirements

- Python 3.8+
- Django 3.2+
- Django Channels 3.0+
- Redis (for channel layer)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/chat-channels.git
    cd chat-channels
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Redis:**

    Ensure that Redis is installed and running on your machine. You can download Redis from [https://redis.io/download](https://redis.io/download).

5. **Configure environment variables:**

    Create a `.env` file in the project root and add the following variables:

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```

6. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    In a separate terminal, start the Django Channels development server:

    ```bash
    daphne -p 8001 chat_channels.asgi:application
    ```

## Usage

1. **Access the application:**

    Open your browser and navigate to `http://localhost:8000`.

2. **Register and login:**

    Create a new account or log in with your existing credentials.

3. **Join or create chat rooms:**

    Once logged in, you can join existing chat rooms or create new ones.

4. **Start chatting:**

    Enter a chat room to start sending and receiving messages in real-time.

## Project Structure

- `chat_channels/`: Main project directory
  - `asgi.py`: ASGI application configuration
  - `settings.py`: Django settings
  - `urls.py`: URL routing
- `chat/`: Chat app directory
  - `consumers.py`: WebSocket consumers
  - `models.py`: Data models
  - `routing.py`: WebSocket routing
  - `views.py`: HTTP views
  - `templates/chat/`: HTML templates
- `static/`: Static files (CSS, JavaScript)
- `requirements.txt`: Project dependencies

## Deployment

1. **Configure production settings:**

    Update the `settings.py` file with production settings and environment variables.

2. **Collect static files:**

    ```bash
    python manage.py collectstatic
    ```

3. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Start the server:**

    Use a production-ready server like Daphne, and configure your web server (Nginx, Apache) to proxy WebSocket connections to Daphne.

## Contributing

We welcome contributions to this project! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django Channels](https://channels.readthedocs.io/)
- [Redis](https://redis.io/)

## Contact

For any inquiries or support, please contact [yourname@example.com](mailto:yourname@example.com).

---

Thank you for using Chat Channels! We hope this guide helps you get started quickly and efficiently. Happy chatting!
