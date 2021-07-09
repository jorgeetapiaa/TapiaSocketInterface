
import socket
from pathlib import Path


class NoFileFoundError(Exception):
    pass


def catching_errors(the_text_file, the_client):  # This function checks if the text file sent by theclient exists or not
    try:
        if the_text_file.exists() == False:
            raise NoFileFoundError
        if the_text_file.is_file() == False:
            raise NoFileFoundError
        else:
            exists = "The text file exists."
            the_client.send(exists.encode("utf-8"))
            return exists
    except NoFileFoundError:
        exists = "The text file does not exist."
        print("No, it does not exist.")
        the_client.send(exists.encode("utf-8"))
        return exists


def main():  # Receives a file request from theclient and sends back the data in the file if it exists, line-by-line
    the_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("The server is running now.")
    host_address = "127.0.0.1"
    port = 9000
    the_server.bind((host_address, port))
    the_server.listen(5)

    while True:
        the_client, addr = the_server.accept()
        print("Got a new connection from", addr)

        receiving_data = the_client.recv(1024)
        print(receiving_data.decode("utf-8"))

        the_text_file = Path(receiving_data.decode("utf-8"))

        print("Obtained the info from the client module.")
        print("Now checking if the text file exists.")

        exists = catching_errors(the_text_file, the_client)  # Uses catching_errors to check if the text file exists

        while exists == "The text file does not exist.":  # If the text file does not exists, theserver and theclient will enter a while loop until a correct directory and text file is inputted
            print("The text file does not exist. Waiting to receive another input from theclient.")
            receiving_data = the_client.recv(1024)
            the_text_file = Path(receiving_data.decode("utf-8"))
            exists = catching_errors(the_text_file, the_client)

        print("The file exists. Now opening the file and sending it to client, line-by-line.")

        with open(the_text_file, 'r') as entire_file:  # Opens the file and sends its data to theclient, line-by-line
            all_lines = entire_file.readlines()
            for lines in all_lines:
                the_client.send(lines.encode("utf-8"))
        print("I am done sending lines.")
        the_client.close()


if __name__ == "__main__":
    main()
