import random
import click
from english_words import english_words_lower_alpha_set as words

@click.command()
@click.argument("num", type=click.INT)
def gen(num: int):
    choices = random.choices(list(words), k=num)
    click.echo("".join([choices[0]] + [c.capitalize() for c in choices[1:]]))