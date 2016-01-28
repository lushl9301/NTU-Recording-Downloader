# NTU-Recording-Downloader
A python command line tool for downloading lecture recordings, with order.

## Requirements


#### python3

    pip install urllib
    pip install beautifulsoup4


#### curl
    
    apt-get install curl # ubuntu
    brew install curl # os x
    Install Linux # windows

## Usage

1. Go to NTULearn, click one of your courses
2. On the left of the page, select "Recorded Lectures"
3. Find the RSS feed for this course:
    
    For example: 15S2-CE3006-CPE301-DIGITAL COMMUNICATIONS **MP4** Podcast
    Press "**Get the RSS feed**"
4. Copy the URL of this page.
    
    It should be in a format like
    http://presentur.ntu.edu.sg/podcast/rss/rss5456_2.xml

    **Please pay attention that you should copy url that ends with "_2.xml". This is for mp4 recording.**

5. Run the following command in your terminal
```shell
python3 get_video.py http://presentur.ntu.edu.sg/podcast/rss/rss5456_2.xml
```
**The progress will be shown. It may take quite a long time.**
    
Or you could run as the command in silence
```shell
python3 get_video.py http://presentur.ntu.edu.sg/podcast/rss/rss5456_2.xml > /dev/null &
```

## Filename

You can rename the file by editing the code

Or you can use the following command. (Just for your information)
```shell
rename 's/(\d+)\s[\w\-\s]+/nameyouwang\ $1/' *.mp4
```
