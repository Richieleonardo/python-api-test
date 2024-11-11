from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def getUser():
    return {"username":"testuser1",
            "email":"testemail@email.com"}