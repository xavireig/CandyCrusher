# CandyCrusher
Python script to beat any Candy Crush level through their Facebook app.

## Requirements
In order to run the script on your own machine you will need the following Python modules:
* requests
* hashlib
* json
* random
* time
* sys

You will also need a network sniffer and analizer to read the requests from the browser to the Candy Crush server. I recommend using [Wireshark](https://www.wireshark.org) or [Fiddler](www.telerik.com/fiddler)
 
## Getting started
First of all, you will need to launch the Candy Crush Facebook app: https://apps.facebook.com/candycrush/

Once the world is loaded, right click on the border of the Candy Crush box and select `View frame source`. Then, search for a string called `sessionKey` and save it, it should be something similar to `65xv6svgy7CO0IZl8oul7w.1`.

Install the network sniffer you downloaded if you haven't and launch it.

## Using the script
The script requires a few parameters in order to run correctly. You can get all of them by simply starting a game. Here are the steps:

1. Make sure that both the Facebook app and your network sniffer are running.
2. Start the level you want to skip.
3. Look for a request in your network sniffer that goes to the URL:

`https://candycrush.king.com/api/gameStart2?arg0=episodeID&arg1=levelID&arg2=seed&_session=sessionKey`

4. Extract from the URL the `episodeID`, the `levelID` and the `seed`.
5. Run the script using the following command:

`python CandyCrusher.py sessionKey episodeID levelID seed`

## Disclaimer

I do not have any intent to harm or damage in any way the King brand or the Candy Crush game. The worst thing you can do with this script is brag about how far you are on the Candy Crush world to your friends.
