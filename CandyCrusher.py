import random
import time
import sys
import requests
import hashlib
import json


class CandyCrush(object):
    def __init__(self, session):
        
        self.session = session
        
    def poll(self):
    
        params = {"_session": self.session}
        response = requests.get("http://candycrush.king.com/api/poll", params=params)
        self.userId = response.json()['currentUser']['userId']
        return

    def extra_life(self):
        
        params = {"_session": self.session}
        response = requests.get("http://candycrush.king.com/api/addLife", params=params)
        print "--------------------------------------------------------------------------------------------------"
        print "Life given to player"
        print "--------------------------------------------------------------------------------------------------"
        return response

    def start_level(self, episode, level, seed):
        
        print "Starting episode " + str(episode) + " level " + str(level)
        params = {"_session": self.session, "arg0": episode, "arg1": level, "arg2": seed}
        print "Request sent:"
        print params
        response = requests.get("http://candycrush.king.com/api/gameStart2", params=params)
        print "Response received:"
        print response
        print "--------------------------------------------------------------------------------------------------"
        return

    def end_level(self, episode, level, seed, score=None):
        
        print "Finishing episode " + str(episode) + " level " + str(level)
        if score is None:
            score = random.randrange(90000, 200000)
        
        dic = {
            "score":score,
            "reason":0,
            "movesMade":1,
            "episodeId":episode,
            "movesLeft":0,
            "timeLeftPercent":-1,
            "movesInit":5,
            "levelId":level,
            "seed":seed,
            "variant":0
        }
        
        # The hash secret BuFu6gBFv79BH9hk was obtained decompiling the flash application
        hashSecret = "BuFu6gBFv79BH9hk"
        myHash = "%(episodeId)s:%(levelId)s:%(score)s:%(timeLeftPercent)s:" % dic + str(self.userId) + ":%(seed)s:" % dic + hashSecret
        dic["cs"] = hashlib.md5(myHash).hexdigest()[:6]
        params = {"_session": self.session, "arg0": json.dumps(dic)}
        print "Request sent: "
        print params
        response = requests.get("http://candycrush.king.com/api/gameEnd3", params=params)
        print "Response received:"
        print response
        print "--------------------------------------------------------------------------------------------------"
        return response


if __name__ == "__main__":
    
    if len(sys.argv) < 5:
        print ""
        print "--------------------------------------------------------------------------------------------------"
        print "This application needs the following 4 parameters:"
        print "     session ID: you can get this from viewing the source of the Facebook Candy Crush app frame"
        print "     episode ID: world ID in Candy Crush's world"
        print "     level ID: level identifier that you want to skip"
        print "     seed: unique identifier generated based on the level you want to skip"
        print "\n"
        print "All parameters can be obtained intercepting the requests that the Facebook app makes with software like Feedly or Wireshark. Enjoy!"
        print "--------------------------------------------------------------------------------------------------"
    else:
        crusher = CandyCrush(sys.argv[1])
        episode = int(sys.argv[2])
        level = int(sys.argv[3])
        seed = int(sys.argv[4])
        
        # poll the server for information
        crusher.poll()
        
        # start by giving ourselves an extra life
        crusher.extra_life()
        
        # start level
        crusher.start_level(episode, level, seed)
        
        # pass level
        result = crusher.end_level(episode, level, seed)
        if (result.status_code == 200):
            print "Level passed successfully!\n"
