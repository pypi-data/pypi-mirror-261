from rich import print
import typer

app = typer.Typer()


@app.command()
def main() -> None:
    print(
        "[bold green][!][/] Mike Moran",
        "[bold green][+][/] data scientist, threat researcher, detection engineer",
        "[bold green][+][/] Duo Security",
        "[bold blue][+][/] mike@mkmrn.dev",
        "[bold red][+][/] platforms",
        "    gitlab.com/mmoran0032",
        "    github.com/mmoran0032",
        "    linkedin.com/in/mmoran0032",
        sep="\n",
    )


if __name__ == "__main__":
    app()
