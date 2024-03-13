#!/usr/bin/env python3
import click
import pathlib
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import create_engine, schema
from sqlalchemy.engine import Engine


class Base(DeclarativeBase):
    pass


class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str]
    fullpath: Mapped[str]
    last_used: Mapped[datetime]


def get_db_cursor() -> Engine:
    # Create the database and table if they don't exist
    db_path = pathlib.Path.home() / ".smartvim.db"
    engine = create_engine(f"sqlite:///{str(db_path)}")

    with engine.begin() as conn:
        # Check if table exists
        if not conn.dialect.has_table(conn, "files"):
            Base.metadata.create_all(engine)

    return engine


@click.command()
@click.argument("filename")
def main(filename):
    with Session(get_db_cursor()) as session:
        # Check if file exists
        fullpath = pathlib.Path(filename).expanduser().resolve()
        if fullpath.exists():
            # File exists, save it to database and print full path
            file = File(filename=filename, fullpath=str(
                fullpath), last_used=datetime.now())
            session.add(file)
            session.commit()
            click.echo(fullpath)
        else:
            # File doesn't exist, check database for matches
            files = (
                session.query(File)
                .filter(File.filename.like(f"%{filename}%"))
                .order_by(File.last_used.desc())
                .limit(1)
                .all()
            )
            if files:
                # Found a file in database, update timestamp and print full path
                file = files[0]
                file.last_used = datetime.now()
                session.commit()
                click.echo(file.fullpath)
            else:
                exit(1)

def cli():
    try:
        main()
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == "__main__":
    cli()
