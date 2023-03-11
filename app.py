import os

from dotenv import load_dotenv
from flask import Flask
from flask import request
from flask import Response
from flask import session


app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ.get("FLASK_SESSIONS_KEY")


@app.post("/v1/register")
def register():
    email = request.json["email"]
    password = request.json["password"]
    if __is_valid_registration(email, password):
        session["email"] = email
        return Response(status=204)
    return Response(status=400)


def __is_valid_registration(email: str, password: str) -> bool:
    # TODO
    return True


@app.post("/v1/login")
def login():
    email = request.json["email"]
    password = request.json["password"]
    if __is_valid_login(email, password):
        session["email"] = email
        return Response(status=204)
    return Response(status=401)


def __is_valid_login(email: str, password: str) -> bool:
    # TODO
    return True


@app.post("/v1/logout")
def logout():
    session.pop("email", None)
    return Response(status=204)


@app.post("/v1/forgot-password")
def forgot_password():
    email = request.json["email"]
    if __is_account(email):
        return Response(status=204)
    return Response(status=400)


def __is_account(email: str) -> bool:
    # TODO
    return True
