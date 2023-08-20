import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.routes import notes, tags, auth




app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(tags.router, prefix='/api')
app.include_router(notes.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello World"}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)



if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", reload=True, log_level="info")