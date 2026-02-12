from db import init_db
from collector import run as collect
from exporter import run as export


def main():
    init_db()
    collect()
    export()


if __name__ == "__main__":
    main()
