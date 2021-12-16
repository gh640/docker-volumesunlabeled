# Docker CLI plugin `volumesunlabeled`

A tiny Docker CLI plugin to list up only volumes without any label.

## Prerequisites

- Python `>=3.9`

## Installation

Check out the repository.

```sh
cd /path/to/repos
git clone [repo]
```

Install the dependencies.

```sh
cd /path/to/repos/[repo]
python3 -m pip install -r requirements.txt
```

Create the CLI plugin directory if not present.

```sh
mkdir ~/.docker/cli-plugins
```

Create a symbolic link to the script.

```sh
cd ~/.docker/cli-plugins
ln -s /path/to/repos/[repo]/docker-volumesunlabeled.py docker-volumesunlabeled
```

If you name the link `docker-volumesunlabeled`, the subcommand will be `volumesunlabeled`. The name can be changed.

If installed successfully, the subcommand `volumesunlabeled` will shows up in the subcommands list with `docker`.

```sh
docker 2>&1 | grep volumesunlabeled
  volumesunlabeled*List up Docker volumes without any label. (Goto Hayato, 0.1.0)
```

## Usage

```bash
docker volumesunlabeled
```

## Similar plugins

- [GitHub - gh640/docker-volumerename: Docker CLI plugin to rename volumes.](https://github.com/gh640/docker-volumerename)
