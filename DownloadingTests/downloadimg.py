import urllib.request
import os

# print(os.chdir(".."))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
os.chdir("DownloadingTests")

url = 'https://imgs.xkcd.com/comics/python.png'
# os.chdir("/")
urllib.request.urlretrieve(url, 'xkcd_comic.png')

# os.chdir(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
os.chdir("..")
url = "https://th.bing.com/th/id/R.d940962745d7da1b3cb3273577b2bf79?rik=kYZriq%2bFIq5o%2bw&riu=http%3a%2f%2fclipart-library.com%2fdata_images%2f6103.png&ehk=7e3qMt68PNk4bS5Oyw7CsQ8ktBSCIrFDRHHBCKp9mcM%3d&risl=&pid=ImgRaw&r=0"
urllib.request.urlretrieve(url, 'stockphoto.png')