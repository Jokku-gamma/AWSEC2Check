from fastapi import FastAPI
app=FastAPI()


@app.get("/")
def get_route():
    return f"This is a sample route check"