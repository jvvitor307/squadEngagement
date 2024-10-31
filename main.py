from fastapi import FastAPI
from database.utils import init_db
from handle.Squad.controller import router as squadRouter
from handle.Person.controller import router as personRouter


app = FastAPI()

app.include_router(squadRouter)
app.include_router(personRouter)

init_db()

@app.get("/status")
def get_status():
    return {"msg": "Api funcionando"}