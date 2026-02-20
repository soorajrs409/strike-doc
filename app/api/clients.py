from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.client import ClientCreate, ClientRead
from app.services.client_service import ClientService

router = APIRouter(prefix="/api/clients", tags=["Clients API"])


@router.post("/", response_model=ClientRead)
async def create_client(client: ClientCreate, db: AsyncSession = Depends(get_db)):
    return await ClientService.create_client(db, client)


@router.get("/", response_model=list[ClientRead])
async def list_clients(db: AsyncSession = Depends(get_db)):
    return await ClientService.list_clients(db)
