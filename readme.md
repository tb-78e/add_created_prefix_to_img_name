# Image Renaming and Processing Tool

## Overview

This tool processes images by adding a creation date prefix to their filenames and moves them to a destination folder. It supports basic logging of operations, including any errors encountered during processing. The destination folder can be specified or defaults to a `processed_images` folder inside the source folder.

## Features

- **Add Creation Date Prefix**: Renames image files to include their creation date.
- **Move Files**: Moves renamed files to a specified or default destination folder.
- **Logging**: Logs operations and errors to a timestamped log file for tracking.

## Requirements

- Python 3.x
- Standard Python libraries (`os`, `shutil`, `time`, `argparse`, `datetime`)

## Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/tb-78e/add_created_prefix_to_img_name.git
cd add_created_prefix_to_img_name
```

2. **No additional installation is required** as the script relies on standard Python libraries.

## Usage

### Command Line Interface

Run the script with the following command:

```bash
python main.py -s /path/to/source/folder [-d /path/to/destination/folder] 
```

## Command-Line Options

- `-s / --source`: Path to the source folder containing images. Default is `source`.
- `-d / --dest`: Path to the destination folder where images will be moved. If not provided, defaults to `processed_images` inside the source folder.

## Example

### Process Images with Default Destination

```bash
python main.py -s /path/to/source/folder
```

This will use /path/to/source/folder as the source and create or use a processed_images folder inside the source folder as the destination.

### Process Images with Custom Destination
```bash
python main.py -s /path/to/source/folder -d /path/to/destination/folder
```

This will use /path/to/source/folder as the source and /path/to/destination/folder as the destination.

## Logfiles
Log files are saved in the logs folder with filenames starting with the current date and time. This folder will be created if it does not already exist.

## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
