import sys
import typer
from typing_extensions import List
from getpass import getpass
from ..tools.gitea import GiteaManager
from ..core.base import format_data

app = typer.Typer(add_completion=False)

default_name = 'default'


@app.command()
def login(url, token=None, name=default_name):
    if not token:
        token = getpass('Please input token:')
    GiteaManager(name).login(url, token)


@app.command()
def logout(name=default_name):
    GiteaManager(name).logout()


@app.command()
def init(name=default_name):
    sys.stdout.write(GiteaManager(name).init())


@app.command()
def upload(name=default_name):
    GiteaManager(name).upload()


@app.command()
def fetch(org_project_tag_environment, path=None, out=None, fmt=None, name=default_name):
    org, project, tag, environment = org_project_tag_environment.split('/')
    data = GiteaManager(name).fetch(org, project, tag, environment)
    if path:
        for p in path.split('.'):
            p = p.strip()
            if p:
                data = data.get(p, {})
    format_data(data, out, fmt)


@app.command()
def clone(orgs=List[str], name=default_name):
    GiteaManager(name).fetch_all(orgs)
