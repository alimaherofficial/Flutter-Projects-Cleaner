# Flutter Projects Cleaner

This Python script automates the process of cleaning multiple Flutter projects located in the current directory. It checks each subdirectory for a `pubspec.yaml` file to identify valid Flutter projects, then runs `flutter clean` in each of them.

## Features

- Detects Flutter projects based on the presence of `pubspec.yaml`.
- Runs `flutter clean` in each detected project.
- Provides a summary of successful and failed cleanups.
- Handles errors gracefully without halting the entire process.

## Prerequisites

- Python 3.6+
- Flutter SDK installed and accessible via the command line
- `flutter` command added to system PATH

## Usage

1. Place the script in the parent directory containing all your Flutter projects.
2. Run the script using:

```bash
python flutter_clean.py
