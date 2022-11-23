import uvicorn
from rotas.app import create_app

uvicorn.run(
    create_app()
)
