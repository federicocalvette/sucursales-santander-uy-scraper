from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
import bank_scrapper
import settings


app = FastAPI()


@app.get("/santander/sucursales")
async def create_item(req: Request):
    
    init_scrapper = bank_scrapper.Scrapper()
    response = init_scrapper.run()

    return JSONResponse(response)

@app.get("/")
async def root():

    data = {
        "links":{
            "documentation": f"{settings.BASE_PROJECT_URL}/docs",
            "branchScrapper": f"{settings.BASE_PROJECT_URL}/santander/sucursales"
        }
    }
    return data
