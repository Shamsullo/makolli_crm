from fastapi import FastAPI
from src.services.users import main as users_main
from src.services.public import main as public_main
from src.services.company import main as company_main
from src.services.transaction import main as transaction_main
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi


app = FastAPI(
    title="Makoli CRM API",
    description="This API was built with FastAPI and provides endpoints for eDonish platform functionality.",
    version="1.3.0",
)

get_openapi(
    title="Makoli CRM API",
    description="This API was built with FastAPI and provides endpoints for eDonish platform functionality.",
    version="1.3.0",
    routes=app.routes,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_main.router, prefix='/v1')
app.include_router(public_main.router, prefix='/v1')
app.include_router(company_main.router, prefix='/v1')
app.include_router(transaction_main.router, prefix='/v1')


@app.get('/v1')
def index():
    return {
        "title": "Makoli CRM API",
        "description": "This API was built with FastAPI and provides endpoints for eDonish platform functionality.",
        "version": "1.0.0"
    }
