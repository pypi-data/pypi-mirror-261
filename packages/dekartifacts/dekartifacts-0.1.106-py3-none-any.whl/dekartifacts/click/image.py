import os.path
import typing
import shlex
import typer
from typing import List
from typing_extensions import Annotated
from dektools.file import read_lines, remove_path
from dektools.typer import command_mixin, multi_options_to_dict
from ..artifacts.docker import DockerArtifact

app = typer.Typer(add_completion=False)


@app.command()
def login(registry, username, password):
    DockerArtifact.login(registry, username, password)


@app.command()
def exports(path, items=''):
    if items:
        images = read_lines(items, skip_empty=True)
    else:
        images = DockerArtifact.images()
    DockerArtifact.exports(images, path)


@app.command()
def imports(path, skip=True):
    DockerArtifact.imports(path, skip)


@app.command()
def sync(path, force: Annotated[bool, typer.Option("--force/--no-force")] = True):
    if os.path.exists(path) or force:
        DockerArtifact.exports(DockerArtifact.images(), path)
        DockerArtifact.imports(path)


@app.command()
def sync_keep(path, images: List[str], running: Annotated[bool, typer.Option("--running/--no-running")] = True):
    for image in DockerArtifact.images():
        if image not in images:
            if not running and list(DockerArtifact.container_active(True)):
                # if `docker ps` is not empty
                continue
            DockerArtifact.remove(image)
            remove_path(os.path.join(path, DockerArtifact.url_to_filename(image)))


@command_mixin(app)
def cp(args, image):
    DockerArtifact.cp(image, *shlex.split(args))


@app.command()
def migrate(path, items, registry, ga='', la=''):
    DockerArtifact.imports(path, False)
    for image in read_lines(items, skip_empty=True):
        image_new = f"{registry}/{image.split('/', 1)[-1]}"
        DockerArtifact.tag(image, image_new)
        DockerArtifact.push(image_new, ga=ga, la=la)
        DockerArtifact.remove(image)
        DockerArtifact.remove(image_new)


@app.command()
def clean_none(args=''):
    DockerArtifact.clean_none_images(args)


@app.command()
def build(
        path,
        image: typing.Optional[typing.List[str]] = typer.Option(None),
        basic=None, step=None, base=None,
        arg: typing.Optional[typing.List[str]] = typer.Option(None),
        push=True,
        push_only_last: Annotated[bool, typer.Option("--last/--no-last")] = False
):
    images = multi_options_to_dict(image)
    args = multi_options_to_dict(arg)
    DockerArtifact.build_fast(path, images, basic, step, base, args, push, push_only_last)
