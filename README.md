# extension-web-service

## dev setup

1. Navigate in a terminal to where you want the project's folder to appear.
2. `git clone https://github.com/chizuo/extension-web-service.git`.
3. Create a virtual environment, such as with `py -m venv venv` or `python3 -m venv venv`.
4. [Activate the virtual environment](https://python.land/virtual-environments/virtualenv).
5. Use `pip install -r requirements.txt` to install the dependencies.
6. If you will make edits, use `pip install -r requirements-dev.txt` to install the development dependencies.
7. If you will make commits, run `pre-commit install` to set up the Git pre-commit hooks.

## dependency docs

* [Python](https://docs.python.org/3/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [Scrapy](https://scrapy.org/)
* [pre-commit](https://pre-commit.com/)
* [Black](https://black.readthedocs.io/en/stable/)
* [mypy](https://mypy.readthedocs.io/en/stable/)
* [flake8](https://flake8.pycqa.org/en/latest/)
