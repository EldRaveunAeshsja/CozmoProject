#!/usr/bin/env python

import twitter, sys
from time import gmtime, strftime
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
tweet = "";
for argument in sys.argv[1:]:
  if tweet == "":
    tweet = argument;
  else:


    tweet = tweet + " " + argument + " ("+strftime("%d-%m-%Y %H:%M:%S", gmtime())+")";
api.PostUpdates(tweet)


