from typing import List
from uuid import UUID
from fastapi import FastAPI,HTTPException
from starlette.responses import Response

from models import User,Gender,Role, UserUpdateRequest

app = FastAPI()

db: List[User]= [
    User(id=UUID("d34bd4b9-6c9a-484e-9cea-ee8cb52f4d03"),firstName="walterio",lastName="Pancho",gender=Gender.male,roles=[Role.student,Role.admin]),
    User(id=UUID("f9472b28-18af-4e3a-a603-8560278872e9"),firstName="Josefa", middleName="",lastName="Pancho-MAS",gender=Gender.female,roles=[Role.student])
]


@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"New User!!! UserId:": user.id}

@app.get("/api/v1/users/{user_id}")
async def find_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404, 
         detail=f"This User:{user_id} does not exits"           
     )



@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"This User:{user_id} does not exits"
        
    )        

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update:UserUpdateRequest,user_id:UUID):
    for user in db:
        if user.id == user_id:
            if user_update.firstName is not None:
                user.firstName=user_update.firstName
            if user_update.lastName is not None:
                user.lastName=user_update.lastName
            if user_update.middleName is not None:
                user.middleName=user_update.middleName
            if user_update.gender is not None:
                user.gender=user_update.gender    
            if user_update.roles is not None:
                user.roles=user_update.roles
            return user   
    raise HTTPException(
        status_code=404,
        detail=f"This User:{user_id} does not exits"
    )