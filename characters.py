from fastapi import FastAPI
from pydantic import BaseModel



#contexto FastAPI()
app = FastAPI()



class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str

characters_list = [Character(id = 3, name = "Summer Smith", status = "Alive", species = "Human"),
                   Character(id = 4, name = "Beth Smith", status = "Alive", species = "Human"),
                   Character(id = 5, name = "Jerry Smith", status = "Alive", species = "Human"),
                   Character(id = 6, name	= "Abadango Cluster Princess", status=	"Alive", species=	"Alien")]


@app.get("/character")

async def charactersjson():
    return  [ {"id": 1, "name": "Rick Sanchez", "status": "Alive", "species":	"Human"}, 
              { "id":	2, "name": "Morty Smith", "status":	"Alive", "species": "Human",}
            ]


#Read class Character
@app.get("/names")

async def names():
    return characters_list


@app.get("/name/{id}")

async def name(id: int):
    names_list = filter(lambda name: name.id == id, characters_list)
    try:
        return list(names_list)[0]
    except:
        return {"Error": "User does not found"}
