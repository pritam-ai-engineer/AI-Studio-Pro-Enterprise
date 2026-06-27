from app.services.character_service import CharacterService


def main():

    service = CharacterService()

    service.create_character(

        name="Batman",

        personality="Serious",

        voice="Deep"

    )

    service.create_character(

        name="Iron Man",

        personality="Funny",

        voice="Confident"

    )

    print()

    print("=" * 60)

    print("Characters")

    print("=" * 60)

    print()

    for character in service.get_all_characters():

        print(

            character["id"],

            character["name"],

            character["personality"]

        )


if __name__ == "__main__":

    main()