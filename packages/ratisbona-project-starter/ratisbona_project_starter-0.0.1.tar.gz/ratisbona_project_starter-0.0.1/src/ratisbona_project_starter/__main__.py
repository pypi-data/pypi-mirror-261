import typer
from ratisbona_project_starter.packager import create_package_strut


def main():
    typer.run(create_package_strut)


if __name__ == "__main__":
    main()