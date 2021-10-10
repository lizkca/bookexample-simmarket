"""a cli game,use keyboard a lot."""

import click

@click.command()
def cli():
    click.echo("hello world simmarket")

if __name__ == '__main__':
    cli()
