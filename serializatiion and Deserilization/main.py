# Pydnatic Acts as your serialization and deserialization engine.
#  It validates incoming raw JSON into strongly-typed Python objects,
#  and serializes Python models back into clean JSON for HTTP responses.


from fastapi import FastAPI
from pydantic import BaseModel, Field,EmailStr
from uvicorn import run as app_run


app=FastAPI(
    title="Serialization and Deserialization"
)

class UserCreate(BaseModel):
    #This is going to be our deserialization schema (incoming from client)
    name:str=Field(...,example="John Doe")
    Age:int=Field(...,gt=0,description="Age must be greater than 0")
    email:EmailStr=Field(...,example="john.doe@example.com")

class UserResponse(BaseModel):
    #This is going to be our serialization schema (outgoing to client)
    id_:int=Field(...,gt=0,description="Id must be greater than 0")
    name:str=Field(...,example="John Doe")
    email:EmailStr=Field(...,example="john.doe@example.com")
    is_active:bool=Field(...,description="Indicates if the user is active")



#How it works: when a client sends a post request to create the user then my user_create model will validate the incoming data and if it is valid then it will create a user and return the user_response model to the client.  


DB=[]
id_counter=0

@app.post("/users",response_model=UserResponse,status_code=201)
def create_user(user:UserCreate):
    
    global id_counter
    new_user={
        "id_":id_counter,
        "name":user.name,
        "email":user.email,
        "is_active":True

    }

    DB.append(new_user)

    id_counter+=1

    return new_user


if __name__=="__main__":
    app_run("main:app",host='127.0.0.1',port=8001,reload=True)