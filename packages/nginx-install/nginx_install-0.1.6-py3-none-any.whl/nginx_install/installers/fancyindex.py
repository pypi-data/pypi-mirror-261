from pydantic import Field
from .general_git import GeneralGitInstaller


class FancyIndexInstaller(GeneralGitInstaller):
    enabled: bool = False
    dynamic: bool = False
    name: str = Field(default="ngx-fancyindex", exclude=True)
    url: str = Field(
        default="https://github.com/aperezdc/ngx-fancyindex.git", exclude=True)
