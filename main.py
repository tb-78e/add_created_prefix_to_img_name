import os
import shutil
import time
import argparse
from datetime import datetime

# Function to set up the log file
def setup_log_file():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_folder = 'logs'
    os.makedirs(log_folder, exist_ok=True)
    log_filename = os.path.join(log_folder, f'{timestamp}_process_log.txt')
    return log_filename

# Function to log messages to the console and a log file
def log_message(message, log_file):
    with open(log_file, 'a') as f:
        f.write(message + "\n")
    print(message)  # Optionally keep printing to the console

# Function to list files in a folder
def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return [os.path.join(folder_path, f) for f in files if os.path.isfile(os.path.join(folder_path, f))]
    except Exception as e:
        log_message(f"An error occurred: {e}", log_file)
        return []

# Function to detect images in a list of files
def detect_images(file_list):
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.heic')
    return [file_path for file_path in file_list if file_path.lower().endswith(image_extensions)]

# Function to format time in min:sec
def format_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    return f"{minutes:02}:{seconds:02}"

# Function to add creation date prefix to a file
def add_creation_date_prefix(file_path, log_file):
    try:
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d_%H-%M-%S')
        file_name = os.path.basename(file_path)
        new_file_name = f"{creation_date}_{file_name}"
        return new_file_name
    except Exception as e:
        log_message(f"An error occurred while processing {file_path}: {e}", log_file)
        return None

# Function to move an image to the destination folder
def move_image(file_path, new_file_name, dest_folder, log_file):
    try:
        new_file_path = os.path.join(dest_folder, new_file_name)
        if os.path.exists(new_file_path):
            log_message(f"File already exists and will be skipped: {new_file_path}", log_file)
            return False
        shutil.copy2(file_path, new_file_path)
        return True
    except Exception as e:
        log_message(f"An error occurred while moving {file_path}: {e}", log_file)
        return False

# Function to add creation date prefix and move images
def process_images(source_folder, dest_folder, log_file):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    files_in_folder = list_files_in_folder(source_folder)
    images_in_folder = detect_images(files_in_folder)
    total_images = len(images_in_folder)
    total_images_skipped = 0

    if total_images == 0:
        log_message("No images found to process.", log_file)
        return

    start_time = time.time()

    for index, file_path in enumerate(images_in_folder):
        new_file_name = add_creation_date_prefix(file_path, log_file)
        if new_file_name:
            if not move_image(file_path, new_file_name, dest_folder, log_file):
                total_images_skipped += 1
            
            elapsed_time = time.time() - start_time
            percentage_complete = ((index + 1) / total_images) * 100
            avg_time_per_image = elapsed_time / (index + 1)
            time_remaining = avg_time_per_image * (total_images - (index + 1))

            log_message(f"Processing image {index + 1}/{total_images} ({percentage_complete:.2f}%)", log_file)
            log_message(f"Estimated time remaining: {format_time(time_remaining)}", log_file)

    total_elapsed_time = time.time() - start_time
    log_message(f"Total Images Processed: {total_images - total_images_skipped}", log_file)
    log_message(f"Total Images Skipped: {total_images_skipped}", log_file)
    log_message(f"Total Operation Time: {format_time(total_elapsed_time)}", log_file)

# Main function to parse arguments and start processing
def main():
    parser = argparse.ArgumentParser(description="Process images by adding creation date prefix and moving them to a destination folder.")
    parser.add_argument("-s", "--source", default="source", help="Path to the source folder containing images. Default is 'source'.")
    parser.add_argument("-d", "--dest", help="Path to the destination folder where images will be moved. Default is a 'processed_images' folder inside the source folder.")

    args = parser.parse_args()
    
    source_folder = args.source
    dest_folder = args.dest if args.dest else os.path.join(source_folder, 'processed_images')

    if not os.path.isdir(source_folder):
        print("Invalid source folder path.")
        return

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    log_file = setup_log_file()

    process_images(source_folder, dest_folder, log_file)
    print("Processing completed.")

if __name__ == "__main__":
    main()
