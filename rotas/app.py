from fastapi import FastAPI
from rotas  import pacote, pesquisas, novos, limpeza


def create_app():
    app = FastAPI()
    app.include_router(pacote.router)
    app.include_router(pesquisas.router)
    app.include_router(novos.router)
    app.include_router(limpeza.router)
    return app
