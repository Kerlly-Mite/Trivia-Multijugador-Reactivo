from fastapi import FastAPI
from reactpy.backend.fastapi import configure
import uvicorn

from app.components.game import Game


app = FastAPI()

configure(app, Game)


if __name__ == "__main__":

    uvicorn.run(

        app,

        host="127.0.0.1",

        port=8000

    )