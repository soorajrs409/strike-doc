from fastapi import FastAPI
from app.db.session import engine
from app.api.clients import router as api_clients_router
from fastapi.templating import Jinja2Templates
from app.views.clients import router as views_clients_router
app = FastAPI(title="strike-doc")

templates = Jinja2Templates(directory="app/templates")

app.include_router(api_clients_router)
app.include_router(views_clients_router)

@app.get("/")
async def root():
    return {"message": "strike-doc is operational"}