# for fabric2 - have issues

import random
from fabric import task
from patchwork.files import append, exists

REPO_URL = 'https://github.com/pklata/superlists.git'

@task
def deploy(c):
    site_folder = f'/home/{c.user}/sites/{c.host}'
    c.run(f'mkdir -p {site_folder}')
    with c.cd(site_folder):
        _get_latest_source(c)
        _update_virtualenv(c)
        _create_or_update_dotenv(c)
        _update_static_files(c)
        _update_database(c)


def _get_latest_source(c):
    print(c.run(f'ls -al'))
    if exists(c, '.git'):
        print("2")
        c.run('git fetch')
    else:
        print("3")
        c.run(f'git clone {REPO_URL} .')
    current_commit = c.local('git log -n --pretty:"format:%H"" 1', capture=True)
    c.run(f'git reset -- hard {current_commit}')


def _update_virtualenv(c):
    if not exists(c, 'virtualenv/bin/pip'):
        c.run(f'python3.6 -m venv virtualenv')
    c.run('./virtualenv/bin/pip install -r requirements.txt')


def _create_or_update_dotenv(c):
    append(c, '.env', 'DJANGO_DEBUG_FALSE=y')
    append(c, '.env', f'SITENAME={c.host}')
    current_ctents = c.run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_ctents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append(c, '.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files(c):
    c.run('./virtualenv/bin/python manage.py collectstatic --noinput')


def _update_database(c):
    c.run('./virtualenv/bin/python manage.py migrate --noinput')