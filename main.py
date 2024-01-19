from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com/",
    "https://localhost.tiangolo.com/",
    "http://localhost/",
    "http://localhost:8080/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


@app.get("/")
def index():
    json_compatible_item_data = jsonable_encoder('toto')
    return JSONResponse(content=json_compatible_item_data)


if __name__ == '__main__':
    print_hi('PyCharm')
