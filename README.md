<img src="https://github.com/BORDVIZ/Custom-Authorization/blob/main/images/authentication.png" alt="" height="400" align="right">

# Custom-Authorization

> REST API authorization on FastAPI using Bearer JWT
>
> Implemented endpoints:
> - Register 🔒
> - Login ✅
> - Refresh token 🔄
> - Get current user 🙆‍♂️
> - Get user by id 🙋‍♂️
> - Get all users 👫

<br clear="right">

### Project Stack: 
 - FastAPI
 - PostgreSQL
 - FastAPI-Users
 - Websockets
 - Alembic
 - Pydantic

### Start the application
1. Create a virtual environment and install dependencies
2. Run `pip install -r requirements.txt` in the terminal
3. Create .env file (change the value of the variables to your own)
```
DB_HOST = localhost
DB_PORT = 5432
DB_NAME = postgres
DB_USER = postgres
DB_PASS = postgres

SECRET = secret
REFRESH_SECRET = secret
ALGORITHM = HS256
```

### Configuring Alembic for the asynchronous driver
1. From the root directory, start the 
`alembic init -t async migrations`

### Application launch
1. Go to the `src` folder
2. Run `uvicorn main:app --reload` in the terminal

<img src="https://github.com/BORDVIZ/Custom-Authorization/blob/main/images/swagger.png" alt="">
