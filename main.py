'''
YouTube Video Downloader
@author : Zaheer Khan Niazi
https://pypi.org/project/pytube/
'''
# install pytube library :
# pip install pytube

# Import the YouTube class from pytube module
from pytube import YouTube

# Get video url and video resolution dynamically
vid_url = input("Enter Video URL: ")
# resolution = sys.argv[2]

# video list
video_list = [vid_url]

for counter in video_list:
    # Exception handling
    try:
        yt = YouTube(counter)
        print("\n*********************Video Link************************")
        # get Video Link
        print(counter)

        print("\n*********************Video Title************************")
        # get Video Title
        print(yt.streams[0].title)

        print("\n********************Tumbnail Image***********************")
        # get Thumbnail Image
        print(yt.thumbnail_url)

    except:
        print("Plz check your internet connection!")

    # set stream resolution
    stream = yt.streams.filter(progressive=True, res='720p').first()

    # Download video in the specific folder
    stream.download("Downloads/")
print("\nVideo Downloaded Successfully!")
