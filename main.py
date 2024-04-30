from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_name():
    return {
        "first_name": "Вохидов ",
        "last_name": "Аминджон",
        "sur_name": "Акпарович",
    }


@app.get("/users")
def get_contact_info():
    return {
        "телефон": "+7 (999) 123-45-67",
    }


@app.get("/tools")
def get_info():
    return {
        "Навыки разработчика:": {
            "python": [
                "JavaScript",
                "HTML/CSS",
            ],
            "backend": [
                "lab1"
            ]
        },
    }