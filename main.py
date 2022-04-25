import uvicorn
from fastapi import FastAPI

from endpoints import routerStudent
from endpoints import routerTeacher

app = FastAPI()

app.include_router(routerStudent)
app.include_router(routerTeacher)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, log_level="info")

