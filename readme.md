# Setup Local Environment

```bash
# Clone this repository to your local env
$ git clone git@github.com:<user>/movie_search_app.git

# Go to project directory
$ cd movie_search_app

# Install composer
$ composer install

# Create .env
$ mv .env.example .env

# Create generate key
$ php artisan key:generate

# Confirm to operation Laravel project on your local environment
$ php artisan serve
Laravel development server started: http://127.0.0.1:8000
```