from utils.core import soup
from utils.core import console
from time import sleep, ctime, time
import datetime
import random
 
class Downloader:
  __datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '/'
  __referrer = 'https://www.720yun.com'
  __dir = 'download/'
  __sleep = .1

  def __init__(self):
    return
  
  def start(self):
    soup.createFolder(self.__dir + self.__datetime)
    self.creatImgList()
  
  def download(self, imgurl):
    rand = random.randint(10, 99)
    sleep(self.__sleep + rand * 0.001)
    fileName = soup.getFileName(imgurl)
    path = self.__dir + self.__datetime + str(fileName)
    refer = soup.getReferrer(imgurl, self.__referrer)
    try:
      soup.downloadImage(imgurl, path, refer)
    except BaseException as msg:
      console.log(msg)

  def creatImgList(self):
    imgList = self.initImg()
    startTime = time()
    for index, item in enumerate(imgList):
      console.loading(item, index, len(imgList))
      self.download(item)
    console.clear()
    console.log(str(len(imgList)) + ' pictures downloaded.')
    console.log('Download time: ' + str(round((time() - startTime), 2)) + 's')
  
  def initImg(self):
    basePath = 'https://ssl-panoimg9.720static.com/resource/prod/9f6i611d5r5/c9e23cpuqcf/1090647/imgs/'
    noodles = ['b', 'd', 'f', 'l', 'r', 'u']
    mode = 'l4'
    length = 9
    isFill = True
    suffix = '.jpg'
    imgs = []
    for k in noodles:
      for i in range(1, (length + 1)):
        for j in range(1, (length + 1)):
          if (isFill):
            i = str(i).zfill(2)
            j = str(j).zfill(2)
          file = mode + '_' + k + '_' + str(i) + '_' + str(j) + suffix
          folder = k + '/'+ mode +'/' + str(i) + '/'
          imgs.append(basePath + folder + file)
    return imgs

if __name__ == '__main__':
  downloader = Downloader()
  downloader.start()


'''
https://ssl-panoimg135.720static.com/resource/prod/6393d249s3h/103jOpmazO2/45968224/imgs/r/l3/09/l3_r_09_09.jpg
'''
