import os
import tempfile
import functools
from dektools.yaml import yaml
from dektools.file import remove_path, list_dir, sure_dir
from dektools.zip import compress_files, decompress_files
from dektools.cfg import ObjectCfg
from ..core.gitea import get_ins, fetch_file, upload_file


class Gitea:
    package_ext = '.zip'
    data_ext = '.yaml'

    def __init__(self, url, token):
        self.url = url
        self.token = token

    @property
    @functools.lru_cache(None)
    def ins(self):
        return get_ins(self.url, self.token)

    def upload(self, path):
        for path_org, org_name in list_dir(path, True):
            for path_project, project_name in list_dir(path_org, True):
                for path_version, version in list_dir(path_project, True):
                    file = tempfile.mktemp(suffix=self.package_ext)
                    compress_files(path_version, file)
                    upload_file(self.ins, org_name, project_name, version, file)
                    remove_path(file)

    def fetch_data(self, org, project, version, environment):
        file = tempfile.mktemp(suffix=self.package_ext)
        fetch_file(self.ins, org, project, version, file)
        path_out = decompress_files(file)
        remove_path(file)
        data = yaml.load(os.path.join(path_out, f"{environment}{self.data_ext}"))
        remove_path(path_out)
        return data


class GiteaManager:
    gitea_cls = Gitea

    def __init__(self, name):
        self.name = name
        self.cfg = ObjectCfg(__name__, 'gitea', self.name, module=True)

    @property
    def gitea(self):
        data = self.cfg.get()
        return self.gitea_cls(data['url'], data['token'])

    def login(self, url, token):
        self.cfg.set(dict(
            url=url,
            token=token
        ))

    def logout(self):
        self.cfg.set({})

    def init(self):
        return sure_dir(self.cfg.path_dir)

    def upload(self):
        self.gitea.upload(self.cfg.path_dir)

    def fetch(self, org, project, version, environment):
        return self.gitea.fetch_data(org, project, version, environment)
