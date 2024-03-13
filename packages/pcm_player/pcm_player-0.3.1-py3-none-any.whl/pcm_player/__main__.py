import logging
import argparse

from player import PcmPlayer
from version import Version


def cli():
    try:
        parser = argparse.ArgumentParser("pcm_player",
                                         description="Commandline Python application for playing MSU PCM files")
        parser.add_argument("-l", "--loop", help="Test the loop point by playing just the end of the song and the loop",
                            action='store_true')
        parser.add_argument("-f", "--file", help="The PCM file to play", type=str)
        parser.add_argument("-v", "--version", help="Get the version number", action='store_true')
        parser.add_argument("-s", "--seconds", help="Number of seconds back from the end of the file to play when testing a loop",
                            type=int)
        parser.add_argument('filepath', nargs=argparse.REMAINDER, help="The path to the PCM file to play")
        args = parser.parse_args()

        if args.version:
            print("pcm_player v" + Version.name())
            return

        if (not args.filepath or len(args.filepath) > 1) and not args.file:
            print("usage: pcm_player [-h] [-l] [-v] filepath")
            return

        file = args.file
        if not file:
            file = args.filepath[0]

        player = PcmPlayer(file)

        result = player.validate_file()
        if not result:
            return

        if args.loop:
            player.test_loop(args.seconds)
        else:
            player.play_song()

    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    cli()
