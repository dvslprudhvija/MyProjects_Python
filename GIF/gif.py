import imageio.v3 as iio
import os

filenames=['team-pic1.png', 'team-pic2.png']
images=[]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)


# files_gif2 = ["me1.jpg", "me2.jpg", "me3.jpg"]
# images_gif2 = []

# for file in files_gif2:
#     images_gif2.append(iio.imread(file))

# iio.imwrite("me_3_pics.gif", images_gif2, duration=500, loop=0)

# gifs=["team.gif", "me_3_pics.gif"]
# for gif in gifs:
  #os.startfile(gif)  
os.startfile("team.gif")  





