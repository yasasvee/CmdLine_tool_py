#!/usr/bin/env python
# coding=utf-8
import click

@click.command()
def concat(str1, str2, delimitter):
    print(str1+delimitter+str2)

@click.command()
def lowerCase(string):
    print(string.lower())

@click.command()
def upperCase(string):
    print(string.upper())
