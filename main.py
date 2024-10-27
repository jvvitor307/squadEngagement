from fastapi import FastAPI

from handle.Squad.controller import router as squadRouter
from handle.Person.controller import router as personRouter


app = FastAPI()

app.include_router(squadRouter)
app.include_router(personRouter)



@app.get("/status")
def get_status():
    return {"msg": "Api funcionando"}