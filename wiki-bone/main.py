from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# @TODO remove this in production..
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/article/{title}")
async def read_article(title: str):
    return {"title": title.replace("_", " "), "content": "This is some lorem ipsum"}