# 
# pip3 install typer[all]
# this is based on the basic tutorial + the what I wanted for a service (start|stop|restart),
# status is not needed.

import typer

app = typer.Typer()

def run():
    print("doing stuff")

@app.command()
def start(name: str = "DEFAULT VALUE"):
    print(f"Hello {name}")
    run()

@app.command()
def stop(name: str = "DEFAULT VALUE"):
    print(f"Goodbye {name}")
    run()

@app.command()
def restart(name: str):
    print(f"Hi again {name}")
    run()

if __name__ == "__main__":
    app()