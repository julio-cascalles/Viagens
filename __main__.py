from fastapi import FastAPI
import uvicorn
from routes import pacote, pesquisas


def create_app():
    app = FastAPI()
    app.include_router(pacote.router)
    app.include_router(pesquisas.router)
    return app

app = create_app()
uvicorn.run(app)
