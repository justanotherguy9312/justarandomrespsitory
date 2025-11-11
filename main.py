from fastapi import FastAPI

app = FastAPI()

confirmed = False  # you can change this anytime

@app.get("/confirm")
def get_confirmation():
    return {"confirmed": confirmed}
