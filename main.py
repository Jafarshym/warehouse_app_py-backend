from fastapi import FastAPI
import uvicorn
from app.database import Base, engine
# Импортируем модели, чтобы они зарегистрировались в Base.metadata
from app.models import product, sale, purchase, inventory   # или конкретные пути к моделям
from fastapi.middleware.cors import CORSMiddleware

from app.api import sales
from app.api import purchases
from app.api import products
from app.api import inventory
from app.api import OneProduct
from app.api import search


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Warehouse ERP")
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sales.router)
app.include_router(purchases.router)
app.include_router(products.router)
app.include_router(inventory.router)
app.include_router(OneProduct.router)
app.include_router(search.router) 

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)