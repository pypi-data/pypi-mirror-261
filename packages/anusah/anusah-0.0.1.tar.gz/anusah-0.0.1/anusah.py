import click
from app import application

@click.group()
def cli() -> None:
    pass

@cli.group("ashutosh")
def ashutosh() -> None:
    pass

@cli.group("anurag")
def anurag() -> None:
    pass

@ashutosh.command("operation-ashutosh")
def operationAshutosh() -> None:
    click.echo("Operation Ashutosh")

@anurag.command("operation-anurag")
def operationAnurag() -> None:
    click.echo("Operation Anurag")
    click.echo(application.operationAnurag())

if __name__ == "__main__":
    cli()

