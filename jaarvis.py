import click

@click.command()
@click.option('--h', default = "vizag", help = "Gives Weather at Yash Home")
@click.option('--w', default = "hyderabad", help = "Gives Weather at Yash work")
@click.option('--c', prompt = "Please give in your city", help = "Gives Weather at a custom location")
def pictWeather(city):
	click.echo("curl wttr.in/"+city)

	
