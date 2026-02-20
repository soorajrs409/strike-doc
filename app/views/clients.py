from fastapi import APIRouter, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.client_service import ClientService
from app.schemas.client import ClientCreate

router = APIRouter(tags=["Clients Views"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/clients")
async def clients_page(request: Request, db: AsyncSession = Depends(get_db)):
    clients = await ClientService.list_clients(db)

    return templates.TemplateResponse(
        "clients/index.html",
        {"request": request, "clients": clients}
    )



@router.post("/clients")
async def create_client(request: Request,
                        name: str = Form(...),
                        contact_email: str | None = Form(None),
                        db: AsyncSession = Depends(get_db)
                         ):
    
    client_data = ClientCreate(
        name=name,
        contact_email=contact_email
    )
    client = await ClientService.create_client(
        db,
        client_data
    )

    return templates.TemplateResponse(
        "clients/_client_row.html",
        {"request": request, "client": client}
    )