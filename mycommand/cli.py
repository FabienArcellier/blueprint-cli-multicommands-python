#!/usr/bin/python
# coding=utf-8

import click
from mycommand.utils import hello


@click.group()
def cli():
    pass


@click.command('command1')
@click.option('--name')
def command1(name):
    hello_name = hello(name)
    print(hello_name)


cli.add_command(command1)

if __name__ == '__main__':
    cli()
