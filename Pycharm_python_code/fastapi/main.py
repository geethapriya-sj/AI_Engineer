from fastapi import FastAPI

app = FastAPI()

food_items = {
    "Indian": ["Samosa", "Dosa"],
    "American": ["Hot dog", "Apple pie"],
    "Italian": ["Pizza", "Burger"]
}

@app.get("/")
def hello():
    return {"message": "hello"}

@app.get("/item")
def item():
    return {"item": "indian"}
