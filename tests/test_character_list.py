from app.database.character_repository import CharacterRepository


def main():

    repository = CharacterRepository()

    rows = repository.get_all()

    print()

    print("=" * 60)

    print("Characters")

    print("=" * 60)

    for row in rows:

        print(

            row["id"],

            row["name"],

            row["personality"]

        )


if __name__ == "__main__":

    main()