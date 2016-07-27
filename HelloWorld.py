import click

@click.command()
@click.option('--count', default = 2, help = 'Number of iterations')
@click.option('-name', prompt = 'Your name', help = 'The user\'s name')
def helloWorld(count, name):
	"""Program that greets the guy"""
	for iter in range(count):
		click.echo("Hello world and "+name)
	
if __name__ == '__main__':
	helloWorld()
