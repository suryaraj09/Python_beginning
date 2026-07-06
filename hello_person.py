def hello(name, lang):
    greeting = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Halo",
    }

    msg = f"{greeting[lang]} {name}"
    print(msg)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting to the user."
    )

    parser.add_argument(
        "-n" , "--name", metavar = "name",
        required = True, help = "the name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar = "lang",
        required = True, choices=["English", "Spanish", "German"],
        help = "The language of the greeting"
    )

    args = parser.parse_args()

    hello(args.name, args.lang)