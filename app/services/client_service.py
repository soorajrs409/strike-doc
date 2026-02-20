from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.client import Client
from app.schemas.client import ClientCreate


class ClientService:

    @staticmethod
    async def create_client(db: AsyncSession, client_data: ClientCreate) -> Client:
        client = Client(**client_data.model_dump())

        db.add(client)
        await db.commit()
        await db.refresh(client)
        return client
    
    @staticmethod
    async def list_clients(db: AsyncSession) -> list[Client]:
        result = await db.execute(select(Client))
        return result.scalars().all()