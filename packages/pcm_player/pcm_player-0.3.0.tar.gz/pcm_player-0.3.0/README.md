# PCM Player

PCM Player is a Python-based commandline application for playing and testing PCM audio files that are used for creating MSU packs to be used with various emulated games and randomizers, such as A Link to the Past.

## Installation

### Pre-requisites

- Python 3.9 or above
- PortAudio 
    - Ubuntu/Debian: apt-get install libportaudio2
    - RHEL: dnf install portaudio
    - Arch: pacman -S portaudio

### Installation Option 1: pipx (recommended)

pipx is recommended it installs PCM Player into an isolated environment to avoid dependency conflicts with other Python applications, and it also creates it standalone application which can be ran directly via commandline.

First, you will want to install [pipx](https://pypa.github.io/pipx/).

```
$ pipx install pcm_player

$ pcm_player test.pcm
```

### Installation Option 2: pip

First, make sure you have pip installed and running: https://packaging.python.org/en/latest/tutorials/installing-packages/

```
$ pip install pcm_player

$ python3 -m pcm_player test.pcm
```

## Usage

Depending on your environment and how you installed, you may be able to run it either directly or as a Python module:

```
# Run directly
$ pcm_player test.pcm

# Run as Python module
$ python3 -m pcm_player test.pcm
```

The application has two main modes:

- Play the full file, then loop and play around 15 seconds
- Test the loop by playing the last 5 seconds of the file, then loop and play 5 seconds after the loop point
  - If a longer loop is desired, it can be specified in the -s argument

You can run them like below:

```
# Play the full PCM file, loop, then play 15 seconds
$ pcm_player test.pcm

# Play the last 5 seconds of the PCM file, loop, then play 5 seconds
$ pcm_player -l test.pcm

# Play the last 8 seconds of the PCM file, loop, then play 8 seconds
$ pcm_player -l -s 8 test.pcm
```

## Credits

- [Hazem Nabil (arkrow)](https://github.com/arkrow) for the PyMusicLooper application, which I used as inspiration for how to play sound files and to use Poetry for making/distributing Python applications.