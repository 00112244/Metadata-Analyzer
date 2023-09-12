# Metadata Analyzer Tool

Welcome to the Metadata Analyzer Tool! This versatile tool allows you to delve deep into the metadata of image files, extract GPS information if available, and analyze timestamps for valuable insights.

![Metadata Analyzer Tool](gif.jpg)

## Why Use This Tool?

Modern image files contain a wealth of metadata, including camera settings, GPS coordinates, and timestamps. This tool is designed to:

- Help photographers and investigators extract valuable metadata from images.
- Geolocate images using GPS data and convert coordinates into readable format.
- Calculate the time difference between when an image was taken and the reference time.

## Features

- Extracts a wide range of metadata tags from images using the Exchangeable image file format (Exif).
- Converts GPS coordinates into a human-readable format with latitude and longitude.
- Calculates the time difference between the image's timestamp and the current reference time.
- Provides options for saving analysis results or displaying them in the console.

## Getting Started

### Prerequisites

Before using the Metadata Analyzer Tool, ensure you have Python (version 3.6 or higher) and the Pillow library installed on your system:

```bash
pip install pillow
```

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/00112244/Metadata-Analyzer.git
   ```
   ```bash
    cd Metadata-Analyzer
   ``` 

2. Run the tool with your preferred image file path:

   ```bash
   python Metadata_Analyzer.py [options] [image_path]
   ```

## Usage

### Analyzing Metadata

To analyze metadata and view information from an image, use the following command:

```bash
python Metadata_Analyzer.py -i [image_path]
```

- This command will display information about the image's metadata, GPS coordinates, and timestamp analysis.

### Analyzing and Save the output

If you want to save the metadata information as a file, utilize the `-o` or `--output` option:

```bash
python Metadata_Analyzer.py [image_path] -o [file name]
```
- This commnad will analyze the image and directly save the output to the given filename.

- Output file will be saved, where the tool is located.

## Options

The Image Metadata Analysis Tool supports the following command-line options:

- `-o`, `--output`: Specify the path to save the output as a text file.
- `-i`, `--info_only`: Display information only, do not save it to a file.
      
## Author

This tool was developed by **Hariharan.T**

  Thank you for using Metadata Analyzer, and we hope it simplifies your image metadata analysis tasks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

