#!/usr/bin/env python3
"""List up Docker volumes without any label."""
import argparse
import json
import sys
from pathlib import Path

try:
    import docker
    from docker.models.volumes import Volume
except ImportError:
    print('PyPI package `docker` is missing.', file=sys.stderr)

__vendor__ = 'Goto Hayato'
__version__ = '0.1.0'
COMMAND_NAME = 'volumesunlabeled'
METADATA_ARG = 'docker-cli-plugin-metadata'


def main():
    """Main function."""
    # Parser is only for the metadata arg.
    gen_parser().parse_args(clean_argv(sys.argv))

    client = docker.from_env()
    unlabeled_volumes = [v for v in volumes(client) if v.attrs['Labels'] is None]
    for v in unlabeled_volumes:
        print(v.name)


def volumes(client) -> list[Volume]:
    """List Docker volumes."""
    return client.volumes.list()


def metadata() -> str:
    """Return the metadata string."""
    meta = {
        'SchemaVersion': '0.1.0',
        'Vendor': __vendor__,
        'Version': __version__,
        'ShortDescription': __doc__,
        'URL': '',
    }
    return json.dumps(meta)


def clean_argv(raw_argv: list[str]) -> list[str]:
    """Remove script name and command name."""
    argv = raw_argv[:]

    if Path(argv[0]).name == Path(__file__).name:
        argv.pop(0)

    if argv and argv[0] == COMMAND_NAME:
        argv.pop(0)

    return argv


def gen_parser():
    """Generate parser."""
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument(
        'metadata_arg',
        nargs='?',
        type=metadata_arg_type,
        help=f'Only for CLI Plugin spec. Must be "{METADATA_ARG}" when passed.',
    )
    return parser


def metadata_arg_type(name: str):
    """Define type for `metadata_arg`."""
    if name == METADATA_ARG:
        print(metadata())
        sys.exit()

    raise ValueError(f'metadata_arg cannot be other than "{METADATA_ARG}".')


if __name__ == '__main__':
    main()
