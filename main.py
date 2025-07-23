import argparse

if __name__ == "__main__":
    # TODO: Comment.
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u",
        "--url",
        dest="url",
        required=True,
        help="URL of the audio to be downloaded or of the user " +
        "whose audios you want to download."
    )

    args = parser.parse_args()

    # TODO: Download audio when the other files are ready.

    print("The file was downloaded successfully.")
