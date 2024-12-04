def read_and_write_file():
    # Prompt the user to enter the filename to read
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of '{filename}' has been read successfully.")

        # Modify the content (convert to uppercase in this example)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        # Handle the case where the file can't be read
        print(f"Error: There was an issue reading or writing the file '{filename}'.")

# Call the function to execute the program
read_and_write_file()