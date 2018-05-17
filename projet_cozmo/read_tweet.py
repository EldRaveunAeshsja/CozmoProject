#!/usr/bin/env python

import sys, twitter, threading, time, cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from time import sleep, gmtime, strftime
nb = 0
api = twitter.Api()
consumer_key = 'aZ3CpdYVI4OrM9KZxWsaziJaW'
consumer_secret = 'P6YTyc4AASAJ8g3kdPed4apnMvQxASqasZUfrRexJIyh5NHHT4'
access_token_key = '971707060239859712-SeXrm9p59mnZ02CubnM5mFG3aggbB1w'
access_token_secret = 'HntnjiidWfpnGrH3ucwJw2aN5z10l1JjQek0J12TWWCJ8'
api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret
)
tweet = ""

def say(robot, text):
    robot.say_text(text).wait_for_completed()

def run(robot: cozmo.robot.Robot):
    global nb, tweet
    robot.turn_in_place(degrees(-90), in_parallel=True).wait_for_completed()
    robot.drive_straight(distance_mm(75), speed_mmps(200), in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(90), in_parallel=True).wait_for_completed()
    robot.drive_straight(distance_mm(500), speed_mmps(200), in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(90), in_parallel=True).wait_for_completed()
    robot.drive_straight(distance_mm(150), speed_mmps(200), in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(90), in_parallel=True).wait_for_completed()
    robot.drive_straight(distance_mm(500), speed_mmps(200), in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(90), in_parallel=True).wait_for_completed()
    robot.drive_straight(distance_mm(75), speed_mmps(200), in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(90), in_parallel=True).wait_for_completed()
    nb += 1
    api.CreateFavorite(tweet)
    say(robot, str(nb)+"e tour du parcours !");
    api.PostUpdates(str(nb)+"e tour du parcours !"+ " ("+strftime("%d-%m-%Y %H:%M:%S", gmtime())+")")

def loop():
    global tweet
    tweets = api.GetUserTimeline(screen_name="CozmoEPSI")
    if len(tweets) > 0:
        tweet = tweets[0]
        if tweet.favorite_count == 0:
            if ("cozmo parcours" in tweet.text) or ("tour" in tweet.text and "parcours" in tweet.text):
                cozmo.run_program(run)
    sleep(2)
    loop()



loop()


