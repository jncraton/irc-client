IRC Client
==========

This project implements a very basic [Internet Relay Chat (IRC)](https://en.wikipedia.org/wiki/Internet_Relay_Chat) client. It is missing some implementation details.

The original [IRC RFC 1459](https://www.rfc-editor.org/rfc/rfc1459) may be a helpful reference as you work to complete this application.

Once complete, this application should automatically connect to the "#andersonu" IRC channel on `irc.libera.chat`. You can also interact with this room via the [Libera web client](https://web.libera.chat/) to confirm that your program works as expected.

Testing
-------

The functions lacking implementations include unit tests to verify that they are working correctly. These can be run using:

```
python3 -m doctest irc.py
```

Or if make is available:

```
make
```