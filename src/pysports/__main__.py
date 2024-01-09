"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Py.Sports."""


if __name__ == "__main__":
    main(prog_name="py.sports")  # pragma: no cover
