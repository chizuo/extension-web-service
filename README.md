# extension-web-service

## dev setup

0. Download [Python 3.10](https://www.python.org/downloads/release/python-3108/) if you haven't already.
1. Navigate in a terminal to where you want the project's folder to appear.
2. `git clone https://github.com/chizuo/extension-web-service.git`.
3. `cd` into the new folder.
4. Create a virtual environment, such as with `py -3.10 -m venv venv` or `python3.10 -m venv venv`.
5. [Activate the virtual environment](https://python.land/virtual-environments/virtualenv).
6. Use `pip install -r requirements.txt` to install the dependencies.
7. If you will make edits, use `pip install -r requirements-dev.txt` to install the development dependencies.
8. If you will make commits, run `pre-commit install` to set up the Git pre-commit hooks.

Now you can run the site locally on a dev server with `flask run`! Optionally, use debug mode for faster iteration with `flask run --debug` (with this option, the server will automatically restart whenever you make a change).

## dependency docs

* [Python](https://docs.python.org/3/)
* [python-dotenv](https://saurabh-kumar.com/python-dotenv/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/)
* [PyJWT](https://github.com/jpadilla/pyjwt)
* [Scrapy](https://scrapy.org/)
* [pre-commit](https://pre-commit.com/)
* [Black](https://black.readthedocs.io/en/stable/)
* [mypy](https://mypy.readthedocs.io/en/stable/)
* [flake8](https://flake8.pycqa.org/en/latest/)

## endpoints

* [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
* [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### create account

POST `/v1/register`

```json
{
	"email": <string>,
	"password": <string>
}
```

returns 204 or 400

### log in

POST `/v1/login`

```json
{
	"email": <string>,
	"password": <string>
}
```

returns 204 or 401

### log out

POST `/v1/logout`

returns 204

### forgot password

POST `/v1/forgot-password`

```json
{
	"email": <string>,
}
```

returns 204 or 400
