#!/usr/local/bin/python

import sys, getopt, os
import urllib, urllib2
import json, time
import config

api = "http://api.picturelife.com"
folder = "files"

limit = 0
skip = False

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', '_pl_session_id=' + config.session_id))

def main(argv):
  global starttime, total, counter
  starttime = time.time()

  setOptions(argv)
  medias = query()
  total = len(medias)
  counter = 0
  mkdir(folder)
  files = os.listdir(folder)
  for media in medias:
    download(media[u'id'], files)

def usage():
  print "Usage: download.py [options]"
  print " -l --limit : Limit the number of photos to download"
  print " -s --skip  : Skip downloading files. Used for troubleshooting"

def setOptions(argv):
  global limit, skip
  try:
    opts, args = getopt.getopt(argv, "hsl:", ["help", "limit=", "skip"])
    for opt, arg in opts:
      if opt in ("-h", "--help"):
        usage()
        sys.exit()
      elif opt in ("-l", "--limit"):
        limit = int(arg)
      elif opt in ("-s", "--skip"):
        skip = True
  except getopt.GetoptError:
    usage()
    sys.exit(2)

def query():
  payload = {'access_token': config.access_token}
  if limit > 0:
    payload['limit'] = limit

  print "using limit = {}".format(limit)

  response = opener.open(api + '/medias/index', data=urllib.urlencode(payload))
  data = json.load(response) 

  if data[u'status'] != 20000:
    print "Error: " + data[u'error_for_humans']
    print "Try adding a _pl_session_id and access_token"
    exit(1)

  return data[u'media']

def mkdir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)

def download(id, files):
  global starttime, total, counter
  if skip:
    total = total - 1
    print "Skipping " + id
  elif id + ".jpg" in files:
    total = total - 1
    print "Already Downloaded " + id
  else:
    global folder
    if counter > 0:
      secondsRemaining = round((total - counter) * (time.time() - starttime) / counter)
    else: secondsRemaining = "some unknown"
    print "Downloading {} with {} second(s) and {} files() remaining".format(id, secondsRemaining, total - counter)
    path = "{}/{}.jpg".format(folder, id)
    try:
      f = opener.open('http://picturelife.com/v/1900/' + id + '/')
      data = f.read()
      with open(path, "wb") as code:
        code.write(data)
    except urllib2.HTTPError:
      print "Failed to download " + id
      with open(path, "wb") as code:
        code.write("0")
    counter = counter + 1

if __name__ == "__main__":
   main(sys.argv[1:])
