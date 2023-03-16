from fastapi import FastAPI
from api.routes.kingdom import kingdom_router
from api.utils.database import database

# create an app
app = FastAPI()

# include routes
app.include_router(kingdom_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
