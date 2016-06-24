# Picturelife API

## About Picturelife
Picturelife (https://picturelife.com/) is a free (with paid premium) cloud service that gets all of your personal and mobile photos in one place, secure, searchable and easy to share.

In early 2016, Picturelife was reportedly sold to another company. Shortly after the site went offline and since then the service has had numerous problems. The largest and most concerning issue was the inability to download any of the photos.

I believe that there are 2 employees currently working at Picturelife. The new company also doesn't seem to actually exist.

## Logging In

This python script requires you to login to your Picturelife account using your webbrowser first to get the session cookie and the 

1. Login to Picturelife https://picturelife.com/ If their site is down, which happens often, this won't work.
2. Open the developer tools to find your cookies
3. Find the Cookie named **_pl_session_id** and copy it to the session_id parameter in config.py (use the sample_config.py as an example)
```python
session_id = "32_random_letters_and_numbers"
```
4. Find the parameter **access_token** in the Form Data of any one of the requests named: index, since, trash, unread_count, prepare, and many more. Just remember this is in Form Data, not cookies. Add this to the config.py file.
```python
access_token = "1|and.then.56.other.letters.and.numbers"
```

## Downloading Photos

This script will download your photos from Picturelife in "1900" resolution. I tried to use the "original" format but it downloads the file in a large TIFF format that doesn't actually look correct. The "1900" version seems to be the best I can find.

### Usage
```bash
./download.py --help
```

Usage: download.py [options]
 -l --limit : Limit the number of photos to download
 -s --skip  : Skip downloading files. Used for troubleshooting

Example:

```bash
./download.py -l 10
```
