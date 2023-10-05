
# Profiles App

The Profiles app is a Django application that provides user profile management features for your MedGPT project. Users can view and edit their profile information, including personal details and medical information.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the MedGPT repository to your local machine:

   ```bash
   git clone https://github.com/your-username/MedGPT.git
   ```

2. Navigate to the `profiles` app directory:

   ```bash
   cd MedGPT/medgpt/profiles
   ```

3. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

The Profiles app is now running at `http://127.0.0.1:8000/profiles/`.

## Usage

- **Profile Editing**: Users can edit their profile information, including name, date of birth, gender, and more, by clicking the "Edit Profile" link from the navigation menu.

- **Medical Information**: Users can access and edit their medical information by navigating to the "Medical Info" page from the navigation menu.

- **Diagnostic Reports**: Users can view their diagnostic reports on the "My Reports" page. They can also delete reports if needed.

## Features

- Profile editing
- Medical information management
- Diagnostic report viewing and deletion

## Contributing

If you'd like to contribute to the Profiles app, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them.
4. Push your branch to your forked repository: `git push origin feature/your-feature-name`.
5. Open a pull request on the original repository, explaining your changes and why they should be merged.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
```

You can copy and paste this content into a `Readme.md` file in your project.
