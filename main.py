import click

from password import generate as gen
from db import Dub
from gui import GUI


@click.group()
def cli() -> None:
    """
        Start the CLI Application
    """
    pass


@click.command()
@click.option('--length', default=11, help='The length of the generated password.   Default = 11')
@click.option('--strength', default="normal", help='The strength of the generated password.'
                                                   'OPTIONS: Normal (default), Advanced')
def generate(length, strength) -> None:
    """
        CREATE a Password
    """
    db = Dub()

    while click.confirm("Make a new password?"):
        password = gen(length, strength)

        click.echo("Generated Password: " + password)
        if click.confirm("Would you like to save the password?"):
            click.echo("Enter a name to save the password")
            name = input("Name:")
            db.save(name, password)

    quit()


@click.command()
def show_all():
    """
        SHOW ALL Saved Passwords
    """
    db = Dub()
    for row in db.get_all():
        click.echo(row)


@click.command()
@click.argument('name')
def get(name):
    """
        GET a Saved Password by Name
    """
    db = Dub()
    for row in db.get_by_name(name):
        click.echo(row)


@click.command()
@click.argument('name')
def delete(name):
    """
        DELETE a Saved Password by Name
    """
    db = Dub()
    db.remove_by_name(name)


@click.command()
def gui():
    """
        Start the GUI Application
    """
    GUI()


cli.add_command(generate)
cli.add_command(show_all)
cli.add_command(get)
cli.add_command(delete)
cli.add_command(gui)
