# Django Stack Overflow Clone

This web application is a replica of Stack Overflow, built using Python, Django, HTML, and CSS. Here's an in-depth guide to the project's features:

## 1. Basic Project Setup with Django

- Created a new Django project.
- Configured project settings including database setup, static files, and templates.

## 2. Creating Frontend with HTML and CSS

- Developed the frontend of the application using HTML and CSS to create a user-friendly interface.
  
  ![SS1](https://github.com/samagra44/StackoverflowClone/assets/77968722/219ec0be-73f2-47a1-a376-34489f22f98e)

## 3. Making Admin Page and Database

- Set up the Django admin page for managing database records.
- Defined database models to store user profiles, questions, answers, comments, and more.

## 4. User Registration, Login, and Logout

- Implemented user authentication with features for user registration, login, and logout.
  
![SS2](https://github.com/samagra44/StackoverflowClone/assets/77968722/e02618e1-e4e0-413d-aede-e0c5cc9d732c)

![SS3](https://github.com/samagra44/StackoverflowClone/assets/77968722/b5b9a9d5-5b42-4d0d-b8c4-1a914baa5a3f)

## 5. Uploading Profile Picture and Profile Information

- Enabled users to upload profile pictures.
- Created forms to collect and display user profile information.

## 6. Editing Profile Details

- Implemented functionality for users to edit their profile details.
  
![SS4](https://github.com/samagra44/StackoverflowClone/assets/77968722/a5d870b3-5528-4c8e-bfd3-096c22d8a5dc)

## 7. Post Question Detail

- Developed the ability for users to post questions with details such as title, description, and tags.
  
![SS6](https://github.com/samagra44/StackoverflowClone/assets/77968722/4418ecfc-a98c-42a6-affa-b10bcbf97725)

## 8. Post Question in More Detail

![SS5](https://github.com/samagra44/StackoverflowClone/assets/77968722/883dfdfe-eea9-4407-b409-342904b61092)

- Enhanced the question posting feature to include more detailed information.

## 9. Updating Answers and Deleting Answers

- Enabled users to update and delete their answers.

## 10. Comment Feature

- Implemented a commenting system for users to add comments to questions and answers.
  
![SS7](https://github.com/samagra44/StackoverflowClone/assets/77968722/0078380e-5ab0-43ba-af52-0356e4fc835b)

## 11. Making Rich Text Editor

- Integrated a rich text editor for users to format their questions, answers, and comments.
  
![SS7](https://github.com/samagra44/StackoverflowClone/assets/77968722/a2a82872-3c99-4d64-b8ef-5ea66bb39a2a)

## 12. Adding User Restrictions

- Implemented user restrictions to control access to certain features based on user roles.

## 13. Upvote and Downvote the Question Feature

- Implemented the ability for users to upvote and downvote questions.
  
![SS6](https://github.com/samagra44/StackoverflowClone/assets/77968722/e77038c2-d88b-4c1b-9e47-46bc5500197b)

## 14. Search Feature

- Developed a search feature to allow users to search for questions based on keywords, tags, or content.

## How to Run the Project

1. Clone the repository:

    ```bash
    git clone https://github.com/samagra44/StackoverflowClone.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py makemigrations
    ```
4. Migrate the changes:
   
   ```bash
    python manage.py migrate
    ```
5. Create Super USer:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application at [http://localhost:8000](http://localhost:8000).

Feel free to explore and use the application as you would with Stack Overflow!

## Contribution

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-new-feature`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-new-feature`.
5. Submit a pull request.

Thank you for contributing!
