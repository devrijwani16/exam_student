from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import studentRouter
from routers.studentRouter import studentRouter

app = FastAPI()
app.include_router(studentRouter)

@app.get("/")
def home():
    return RedirectResponse(url="/docs")

