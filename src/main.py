from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import all_routers

app = FastAPI(title='Custom Auth')

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                "Authorization"],
)

for router in all_routers:
    app.include_router(router)

