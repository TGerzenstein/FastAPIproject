from fastapi import FastAPI



#contexto FastAPI()
app = FastAPI(title="Rick and Morty", 
              description="API based on the television show Rick and Morty") 


#GET

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/character")
async def page():
    return {"character": "https://exampleurlpage"}

