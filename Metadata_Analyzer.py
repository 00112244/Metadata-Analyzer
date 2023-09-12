import argparse
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from colorama import Fore, Style

# Function to print text in a rectangle with colored text and no background color
def print_text_in_rectangle(text, text_color=Fore.GREEN):
    box_width = 90
    box_height = 4
    border_horizontal = f"{Fore.WHITE}+{'-' * (box_width - 2)}+{Style.RESET_ALL}"
    empty_line = f"{Fore.WHITE}|{' ' * (box_width - 2)}|{Style.RESET_ALL}"

    boxed_text = [border_horizontal] + [empty_line] * ((box_height - 2) // 2)
    boxed_text.extend(f"{Fore.WHITE}| {text_color}{Style.BRIGHT}{line.center(box_width - 4)}{Style.RESET_ALL} |{Style.RESET_ALL}" for line in text.splitlines())
    boxed_text.extend([empty_line] * ((box_height - 2) // 2) + [border_horizontal])

    return "\n".join(boxed_text)

# Function to extract image metadata and GPS info
def extract_metadata_and_gps(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Extract EXIF data
        exif_data = image._getexif()

        if exif_data:
            # Initialize metadata dictionary
            metadata = {}

            # Check if GPSInfo tag is present
            if 34853 in exif_data:
                gps_info = exif_data[34853]  # GPSInfo tag ID
                latitude_degrees = gps_info[2][0]
                latitude_minutes = gps_info[2][1]
                latitude_seconds = gps_info[2][2] / 100
                latitude_direction = "N" if gps_info[3] == "N" else "S"

                longitude_degrees = gps_info[4][0]
                longitude_minutes = gps_info[4][1]
                longitude_seconds = gps_info[4][2] / 100
                longitude_direction = "E" if gps_info[5] == "E" else "W"

                formatted_latitude = f"{latitude_degrees}° {latitude_minutes}' {latitude_seconds:.2f}\" {latitude_direction}"
                formatted_longitude = f"{longitude_degrees}° {longitude_minutes}' {longitude_seconds:.2f}\" {longitude_direction}"

                metadata['GPS Latitude'] = formatted_latitude
                metadata['GPS Longitude'] = formatted_longitude
            else:
                metadata['GPS Latitude'] = "N/A"
                metadata['GPS Longitude'] = "N/A"

            # Extract other EXIF metadata
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                metadata[tag_name] = value

            return metadata
        else:
            return None  # No metadata found
    except Exception as e:
        return None  # No metadata found

# Function to analyze image timestamp
def analyze_timestamp(metadata, reference_time):
    try:
        if 'DateTimeOriginal' in metadata:
            image_timestamp = datetime.strptime(metadata['DateTimeOriginal'], "%Y:%m:%d %H:%M:%S")
            time_difference = image_timestamp - reference_time
            return f"Time Difference: {time_difference}"
        else:
            return "DateTimeOriginal not found in metadata."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Create a command-line argument parser
    parser = argparse.ArgumentParser(description="Image Metadata Analysis Tool")
    parser.add_argument("image_path", nargs='?', help="Path to the image file to analyze")
    parser.add_argument("-o", "--output", default=None, help="Path to save the output as a text file")
    parser.add_argument("-i", "--info", action="store_true", help="Display information in the console")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the current date and time as reference_time
    reference_time = datetime.now()

    # Welcome message
    welcome_message = """
    Welcome to the Image Metadata Analysis Tool!
    This tool allows you to analyze metadata from an image file.
    """
    # Print the welcome message with green-colored bold text in a rectangle
    boxed_welcome_message = print_text_in_rectangle(welcome_message)
    print(boxed_welcome_message)
    print("                                               A tool for Image Metadata Analysis")
    print("                                                       By: Hariharan (00112244)\n")

    if args.image_path:
        # Print reference time when an image path is provided
        print("\nReference Time (Current Date and Time):", reference_time)

        # Analyze the image metadata if an image path is provided
        metadata = extract_metadata_and_gps(args.image_path)

        if metadata is None:
            print("No metadata found in the image.")
        else:
            if args.info:
                print("\nImage Metadata:")
                for key, value in metadata.items():
                    print(f"{key}: {value}")

                timestamp_analysis = analyze_timestamp(metadata, reference_time)
                print("\nTimestamp Analysis:")
                print(timestamp_analysis)

        # Save the output to the specified file if -o is provided
        if args.output is not None:
            with open(args.output, 'w', encoding='utf-8') as file:
                for key, value in metadata.items():
                    file.write(f"{key}: {value}\n")
            if not args.info:  # Print "save success" only when -o is provided and args.info is False
                print("Output saved successfully to", args.output)

    # Display the "save success" message only when -o is provided
    elif not args.info and args.output is not None:
        print("Output saved successfully to", args.output)

if __name__ == "__main__":
    main()
