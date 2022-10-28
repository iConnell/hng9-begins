from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    bio = "I am a backend developer, with experience in python web frameworks like django, flask and fastap"
    return { "slackUsername": "McConnell", "backend": True, "age": 22, "bio": bio}
