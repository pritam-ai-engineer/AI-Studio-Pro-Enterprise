from app.models.character import Character


def main():

    character = Character(
        name="CaptainChimp"
    )

    print("UUID:", character.uuid)

    print("Created:", character.created_at)

    print("Updated:", character.updated_at)

    print("Validation:", character.validate())


if __name__ == "__main__":
    main()