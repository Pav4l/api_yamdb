### Project description
The YaMDb project collects user review on various titles.


### How to start the project:

Clone the repository and change into it on the command line:

```
git clone https://github.com/antonmakhnachev/api_yamdb.git
```

```
cd api_yamdb
```

Create and activate virtual environment:
(Depending on the operating system, command "python" or command "python3" is used.)

```
python  -m venv venv
```

```
source env/bin/activate
```

Install dependencies from requirements.txt file:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

```
cd api_yamdb
```

Run migrations:

```
python3 manage.py migrate
```

Run project:

```
python3 manage.py runserver
``` 
### **API request examples**

#### **AUTH. User registration and issuance of tokens**

- Creating a new user
```
POST http://127.0.0.1:8000/api/v1/auth/signup/
```

Receive a confirmation code to the sent email.
Access rights: Available without a token.
Using 'me' as a username is not allowed.
The email and username fields must be unique.

```
    # Request Body

	{
		"email": "user@example.com",
		"username": "string"
	}
```
- Getting a JWT token
```
GET http://127.0.0.1:8000/api/v1/auth/token/
```

Getting a JWT token in exchange for username and confirmation code.
Access rights: Available without a token.

```
    # Request Body

    {
		"username": "string",
		"confirmation_code": "string"
	}
```

#### **CATEGORIES**

- Getting a list of all categories
```
GET http://127.0.0.1:8000/api/v1/categories/
```
Get a list of all categories. Access rights: Available without a token

```
    # Request Body

    {
		"count": 0,
		"next": "string",
		"previous": "string",
		"results": [
			{
				"name": "string",
				"slug": "string"
			}
		]
	}
```

- Adding a new category
```
POST http://127.0.0.1:8000/api/v1/categories/
```
Create a category. Access rights: Administrator. The slug field of each category must be unique.

```
    # Request Body

    {
		"name": "string",
		"slug": "string"
	}
```

- Deleting a category
```
DELETE http://127.0.0.1:8000/api/v1/categories/{slug}/
```
Delete category. Access rights: Administrator.

#### **GENRES. Genre categories**

- Getting a list of all genres
```
GET http://127.0.0.1:8000/api/v1/genres/
```
Get a list of all genres. Access rights: Available without a token

```
    # Request Body

    {
		"count": 0,
		"next": "string",
		"previous": "string",
		"results": [
			{
				"name": "string",
				"slug": "string"
			}
		]
	}
```

- Adding a Genre
```
POST http://127.0.0.1:8000/api/v1/genres/
```
Add a genre. Access rights: Administrator. The slug field of each genre must be unique.

```
    # Request Body

    {
		"name": "string",
		"slug": "string"
	}
```

- Deleting a genre
```
DELETE http://127.0.0.1:8000/api/v1/genres/{slug}/
```
Delete a genre. Access rights: Administrator.

#### **TITLES. Titles to which they write reviews (a certain film, book or song).**

- Getting a list of all titles
```
GET http://127.0.0.1:8000/api/v1/titles/
```
Get a list of all objects. Access rights: Available without a token

```
    # Request Body

    {
		"count": 0,
		"next": "string",
		"previous": "string",
		"results": [
			{
				"id": 0,
				"name": "string",
				"year": 0,
				"rating": 0,
				"description": "string",
				"genre": [
					{
						"name": "string",
						"slug": "string"
					}
				],
				"category": {
					"name": "string",
					"slug": "string"
				}
			}
		]
	}
```


- Adding a title
```
POST http://127.0.0.1:8000/api/v1/titles/
```
Add a new title. Access rights: Administrator.
You can not add titles that have not yet been released (the year of release cannot be more than the current one).
When adding a new title, you must specify an existing category and genre.

```
    # Request Body

    {
		"name": "string",
		"year": 0,
		"description": "string",
		"genre": [
			"string"
		],
		"category": "string"
	}
```

- Getting information about a title
```
GET http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```
Information about the title. Access rights: Available without a token

```
    # Request Body

    {
		"id": 0,
		"name": "string",
		"year": 0,
		"rating": 0,
		"description": "string",
		"genre": [
			{
				"name": "string",
				"slug": "string"
			}
		],
		"category": {
			"name": "string",
			"slug": "string"
		}
	}
```

- Partial updating of information about the title
```
PATCH http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```
Update information about the title. Access rights: Administrator

```
    # Request Body

    {
		"name": "string",
		"year": 0,
		"description": "string",
		"genre": [
			"string"
		],
		"category": "string"
	}
```

- Deleting a title
```
DELETE http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```
Delete a title. Access rights: Administrator.

#### **REVIEWS**

- Getting a list of all reviews
```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```
Get a list of all reviews. Access rights: Available without a token.

```
    # Request Body

    {
		"count": 0,
		"next": "string",
		"previous": "string",
		"results": [
			{
				"id": 0,
				"text": "string",
				"author": "string",
				"score": 1,
				"pub_date": "2019-08-24T14:15:22Z"
			}
		]
	}
```

- Adding a new review
```
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```
Add a new review. A user can leave only one review per title. Access rights: Authenticated users.

```
    # Request Body

    {
		"text": "string",
		"score": 1
	}
```

- Getting review by id
```
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
```
Get review by id for sample selection. Access rights: Available without a token.

```
    # Request Body

    {
		"id": 0,
		"text": "string",
		"author": "string",
		"score": 1,
		"pub_date": "2019-08-24T14:15:22Z"
	}
```

- Partial review update by id
```
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
```
Partially update review by id. Access rights: Reviewer, moderator or administrator.

```
    # Request Body

    {
		text": "string",
		"score": 1
	}
```

- Deleting review by id
```
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
```
Delete review by id. Access rights: Reviewer, moderator or administrator.

#### **COMMENTS (on reviews)**

- Getting a list of all comments on a review
```
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
Get a list of all comments on a review by id. Access rights: Available without a token.

```
    # Request Body

    {
		"count": 0,
		"next": "string",
		"previous": "string",
		"results": [
			{
				"id": 0,
				"text": "string",
				"author": "string",
				"pub_date": "2019-08-24T14:15:22Z"
			}
		]
	}
```

- Adding a comment to a review
```
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
Add a new comment for the review. Access rights: Authenticated users.

```
    # Request Body

    {
		"text": "string"
	}
```

- Getting a comment on a review
```
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
Get a comment for a review by id. Access rights: Available without a token.

```
    # Request Body

    {
		"id": 0,
		"text": "string",
		"author": "string",
		"pub_date": "2019-08-24T14:15:22Z"
	}
```

- Partial updating of review comment
```
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
Partially update the review comment by id. Access rights: Commenter, moderator or administrator.

```
    # Request Body

    {
		"text": "string"
	}
```

- Deleting a review comment
```
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
Delete a review comment by id. Access rights: Commenter, moderator or administrator.

#### **USERS**

- Getting a list of all users
```
GET http://127.0.0.1:8000/api/v1/users/
```
Get a list of all users. Access rights: Administrator

```
    # Request Body

    {
		"count": 0,
		"next": "string",
		"previous": "string",
		"results": [
			{
				"username": "string",
				"email": "user@example.com",
				"first_name": "string",
				"last_name": "string",
				"bio": "string",
				"role": "user"
			}
		]
	}
```

- Adding a user
```
POST http://127.0.0.1:8000/api/v1/users/
```
Add a new user. Access rights: Administrator The email and username fields must be unique.

```
    # Request Body

    {
		"username": "string",
		"email": "user@example.com",
		"first_name": "string",
		"last_name": "string",
		"bio": "string",
		"role": "user"
	}
```

- Getting a user by username
```
GET http://127.0.0.1:8000/api/v1/users/{username}/
```
Get user by username. Access rights: Administrator

```
    # Request Body

    {
		"username": "string",
		"email": "user@example.com",
		"first_name": "string",
		"last_name": "string",
		"bio": "string",
		"role": "user"
	}
```

- Changing user data by username
```
PATCH http://127.0.0.1:8000/api/v1/users/{username}/
```
Change user data by username. Access rights: Administrator. The email and username fields must be unique.

```
    # Request Body

    {
		"username": "string",
		"email": "user@example.com",
		"first_name": "string",
		"last_name": "string",
		"bio": "string",
		"role": "user"
	}
```

- Deleting a user by username
```
DELETE http://127.0.0.1:8000/api/v1/users/{username}/
```
Delete user by username. Access rights: Administrator.

- Getting your account information
```
GET http://127.0.0.1:8000/api/v1/users/me/
```
Get your account information. Access rights: Any authorized user

```
    # Request Body

    {
		"username": "string",
		"email": "user@example.com",
		"first_name": "string",
		"last_name": "string",
		"bio": "string",
		"role": "user"
	}
```

- Changing your account information
```
PATCH http://127.0.0.1:8000/api/v1/users/me/
```
Change your account information. Access rights: Any authorized user. The email and username fields must be unique.

```
    # Request Body

    {
		"username": "string",
		"email": "user@example.com",
		"first_name": "string",
		"last_name": "string",
		"bio": "string",
		"role": "user"
	}
```


### Authors

 - Anton Makhnachev; email: makhnachev.anton@yandex.ru :
   
   registration and authentication system, access rights,
   working with a token, email confirmation system;	
 
 - Nebykov Artem; email: nbkrtm2000@icloud.com :

   models, views and endpoints for works, categories, genres;
   implements data import from csv files;
 
 - Pavel Gorev; email: pavel.gorev@gmail.com :

   models, views and endpoints for reviews, comments + rating of titles;