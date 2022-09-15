import socket
import PySimpleGUI as sg


def get_join_bytes(channel):
    """
    Returns the UTF-8 encoded data to send to the server to join a channel.

    The JOIN message is described in the following RFC:

    https://www.rfc-editor.org/rfc/rfc1459#section-4.2.1

    >>> get_join_bytes("ch")[:4]
    b'JOIN'

    >>> get_join_bytes("#ch")[-6:-2]
    b' #ch'

    >>> get_join_bytes("#mychannel")[-13:-2]
    b' #mychannel'

    >>> get_join_bytes("chan")[-2:]
    b'\\r\\n'
    """

    return b''


def get_message_bytes(receiver, message):
    """
    Returns the UTF-8 encoded data to transmit to the server to send a
    message to a user or channel.

    This function supports only a single receiver.

    The PRIVMSG message needed for this is described in the follow RFC:

    https://www.rfc-editor.org/rfc/rfc1459#section-4.4.1

    >>> get_message_bytes("grievous", "Hello there")[:7]
    b'PRIVMSG'

    >>> get_message_bytes("grievous", "Hello there")[-14:-2]
    b':Hello there'

    >>> get_message_bytes("grievous", "Hello there")[8:16]
    b'grievous'

    >>> get_message_bytes("user", "message")[8:12]
    b'user'

    >>> get_message_bytes("user", "message")[-9:-2]
    b'message'

    >>> get_message_bytes("user", "message")[-2:]
    b'\\r\\n'

    >>> get_message_bytes("user", "message")[-10:]
    b':message\\r\\n'
    """

    return b''



def get_registration_bytes(user, password):
    """
    Returns the UTF-8 encoded registration data to send to IRC server to
    register a user.

    The three messages needed are described in the following RFC:

    https://www.rfc-editor.org/rfc/rfc1459#section-4.1

    This function simply uses the passed `user` parameter for the `user`,
    `nick`, and `real name` fields sent to the server.

    Our client also does not support sending specific `hostname` and
    `servername` information. "0" should be sent for the `hostname` with
    "*" being used for the `servername`.

    https://stackoverflow.com/questions/31666247/what-is-the-difference-between-the-nick-username-and-real-name-in-irc-and-wha


    >>> len(get_registration_bytes("user", "pass").splitlines())
    3

    >>> get_registration_bytes("user", "pass").splitlines()[0][:4]
    b'PASS'

    >>> get_registration_bytes("user", "1234").splitlines()[0][-4:]
    b'1234'

    >>> get_registration_bytes("user", "pass").splitlines()[1][:4]
    b'NICK'

    >>> get_registration_bytes("fred", "pass").splitlines()[1][-4:]
    b'fred'

    >>> get_registration_bytes("user", "pass").splitlines()[2][:4]
    b'USER'

    >>> get_registration_bytes("jordan", "pass").splitlines()[2][-6:]
    b'jordan'

    >>> get_registration_bytes("beth", "pass").splitlines()[2][-4:]
    b'beth'

    >>> get_registration_bytes("beth", "pass").splitlines()[2][10:11]
    b'0'

    >>> get_registration_bytes("beth", "pass").splitlines()[2][12:13]
    b'*'

    >>> get_registration_bytes("beth", "pass")[-2:]
    b'\\r\\n'
    """

    return b''


def main():
    """
    Main program entry point

    This function manages creation of the GUI and the main event loop

    There are a few sections of this function that must be completed. These
    have been marked with `TODO` comments
    """

    window = create_window()

    # TODO: Create a new IPv4 streaming socket named `sock`
    # e.g. sock = ...

    assert sock.family == socket.AF_INET, "Socket family should be AF_INET"
    assert sock.type == socket.SOCK_STREAM, "Socket type should be SOCK_STREAM"

    # TODO: Connect to irc.libera.chat on port 6665

    assert sock.getpeername()[1] == 6665, "Incorrect port for connection"

    # TODO: Send registration information for your user
    # You may choose an appropriate username and any password for yourself

    # TODO: Send join message to join the "#andersonu" channel

    # Set socket to non-blocking
    sock.settimeout(0)

    while True:
        event, values = window.read(50)
        if event == sg.WINDOW_CLOSED or event == "Quit":
            break

        if event == "Send":
            # TODO: Send message to server
            # Hint: The message is stored in `values['message']`

            # Echo sent message locally
            window["output"].update(f"You: {values['message']}\n", append=True)

            # Clear message input
            window["message"].update("")

        try:
            window["output"].update(sock.recv(4096).decode("utf8"), append=True)
        except BlockingIOError:
            pass

    sock.close()
    window.close()


#######################################################################################
# It is not recommended to modify any code below this point
#######################################################################################


def create_window():
    """
    Creates the main window for the application

    This function is complete.
    """

    layout = [
        [sg.Multiline(key="output", size=(80, 20), autoscroll=True, write_only=True)],
        [sg.Text("Message")],
        [sg.Input(key="message")],
        [sg.Button("Send", visible=True, bind_return_key=True)],
        [sg.Button("Quit")],
    ]

    # Create the window
    return sg.Window("IRC Client", layout)


if __name__ == "__main__":
    main()
