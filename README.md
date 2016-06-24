# Picturelife API

## About Picturelife
Picturelife (https://picturelife.com/) is a free (with paid premium) cloud service that gets all of your personal and mobile photos in one place, secure, searchable and easy to share.

In early 2016, Picturelife was reportedly sold to another company. Shortly after the site went offline and since then the service has had numerous problems. The largest and most concerning issue was the inability to download any of the photos.

I believe that there are 2 employees currently working at Picturelife. The new company also doesn't seem to actually exist.

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
