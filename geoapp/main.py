from fastapi import FastAPI
from api.routes.kingdom import kingdom_router

# create an app
app = FastAPI()

# include routes
app.include_router(kingdom_router)
