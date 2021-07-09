
import socket
from pathlib import Path


def create_client_folder(file_name):  # Creates the Client Folder and puts requested text file within the Client Folder
    client_folder = Path('Client Folder')
    if client_folder.exists() == False:
        client_folder.mkdir(exist_ok=True)
    the_file = client_folder/Path(file_name)
    creating_file = open(the_file, "w")
    creating_file.close()
    return the_file  # The requested text file within the Client Folder is returned


def main():  # Requests a text file from theserver and after receiving the data, stores it in a text file of the same name within the Client Folder
    the_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_address = "127.0.0.1"
    port = 9000
    the_client.connect((host_address, port))
    print("Please input a directory path that includes the text file you want to request.")
    text_file = input()
    print("Requesting copy of this text file:", text_file)
    the_client.sendall(text_file.encode("utf-8"))

    existence = the_client.recv(1024)

    while existence.decode("utf-8") == "The text file does not exist.":  # If theserver sends back this message, both theserver and theclient enter a while loop until a correct directory and text file is inputted
        print("Please enter a directory with a text file that exists.")
        text_file = input()
        the_client.sendall(text_file.encode("utf-8"))
        existence = the_client.recv(1024)

    print("theclient module is done checking if the directory exists or not.")
    print("The text file exists. Now receiving lines of data from theserver.")
    convert_to_list = text_file.split("\\")
    file_name = convert_to_list[-1]  # Catches the name of the text file that was requested without the rest of the path

    txt_file = create_client_folder(file_name)  # Catches requested text file that was created within the Client Folder
    file_copy = open(txt_file, "w")

    while True:  # Receives data from theserver line-by-line and writes it into the requested text file
        line = the_client.recv(1024)
        if not line:
            break
        file_copy.write(line.decode("utf-8"))
    file_copy.close()

    print("I am done receiving lines.")


if __name__ == "__main__":
    main()
