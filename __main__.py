from fastapi import FastAPI
import uvicorn
from routes import pacote, pesquisas, novos


def create_app():
    app = FastAPI()
    app.include_router(pacote.router)
    app.include_router(pesquisas.router)
    app.include_router(novos.router)
    return app

app = create_app()
uvicorn.run(app)
