import click
import os

@click.command()
@click.option('--h', default = "vizag", help = "Gives Weather at Yash Home")
@click.option('--c', prompt = "Please give in your city", help = "Gives Weather at a custom location")
def pictWeather(city):
#    result = os.popen("curl wttr.in/"+city).read()
    click.echo(city)

if __name__ == '__main__':
    pictWeather()
