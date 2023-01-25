from fastapi import FastAPI, Request
import bank_scrapper
import json
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/santander/sucursales")
async def create_item(req: Request):
    
    init_scrapper = bank_scrapper.Scrapper()
    response = init_scrapper.run()

    return JSONResponse(response)

@app.get("/")
async def root():
    return {"message": "Go to: http://127.0.0.1:8000/docs"}
