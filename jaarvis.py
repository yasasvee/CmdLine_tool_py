import click
import os

@click.command()
@click.option('--browser', default='http://www.google.co.in', help='Opens google chrome')
def runCmd(browser):
    click.echo('Opening browser with '+browser)
    os.system("start chrome "+browser)
if __name__ == '__main__':
    runCmd()
