import requests
import os

imagenet_1024 = False # dl
imagenet_16384 = False # dl
gumbel_8192 = False #dl
coco = False #Dl
faceshq = True
wikiart_1024 = False #url invalid
wikiart_16384 = True
sflckr = False # dl
ade20k = True
ffhq = True
celebahq = True

models = {"imagenet_1024":True,"imagenet_16384":False,"gumbel_8192":False,"coco":False,
"faceshq":False,"wikiart_1024":False,"wikiart_16384":False,"sflckr":False,"ade20k":False,
"ffhq":False,"celebahq":False}

def is_downloadable(url):
  h = requests.head(url=url,allow_redirects=True)
  header = h.headers
  print(header)
  content_type = header.get("content-type")
  if "text" in content_type.lower():
    return False
  if "html" in content_type.lower():
    return False
  print(url + " is downloadable")
  return True

def download(url,filename):
  print("Downloading " + filename)
  dl = requests.get(url=url,allow_redirects=True)
  open("models/"+filename,"wb").write(dl.content)

def install():
  if imagenet_1024 == True:
    imagenet_1024_yaml_url = "https://heibox.uni-heidelberg.de/d/8088892a516d4e3baf92/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1"
    imagenet_1024_ckpt_url = "https://heibox.uni-heidelberg.de/d/8088892a516d4e3baf92/files/?p=%2Fckpts%2Flast.ckpt&dl=1"
    download(imagenet_1024_yaml_url,"vqgan_imagenet_f16_1024.yaml")
    download(imagenet_1024_ckpt_url,"vqgan_imagenet_f16_1024.ckpt")
  if imagenet_16384:
    imagenet_16384_yaml_url = "https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1"
    imagenet_16384_ckpt_url = "https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1"
    download(imagenet_16384_yaml_url,"vqgan_imagenet_f16_16384.yaml")
    download(imagenet_16384_ckpt_url,"vqgan_imagenet_f16_16384.ckpt")
  if gumbel_8192:
    gumbel_8192_yaml_url = "https://heibox.uni-heidelberg.de/d/2e5662443a6b4307b470/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1"
    gumbel_8192_ckpt_url = "https://heibox.uni-heidelberg.de/d/2e5662443a6b4307b470/files/?p=%2Fckpts%2Flast.ckpt&dl=1"
    download(gumbel_8192_yaml_url,"gumbel_8192.yaml")
    download(gumbel_8192_ckpt_url,"gumbel_8192.ckpt")
  if coco:
    coco_yaml_url = "https://dl.nmkd.de/ai/clip/coco/coco.yaml"
    coco_ckpt_url = "https://dl.nmkd.de/ai/clip/coco/coco.ckpt"
    download(coco_yaml_url,"coco.yaml")
    download(coco_ckpt_url,"coco.ckpt")
  if faceshq:
    faceshq_yaml_url = "https://drive.google.com/uc?export=download&id=1fHwGx_hnBtC8nsq7hesJvs-Klv-P0gzT"
    faces_ckpt_url = "https://app.koofr.net/content/links/a04deec9-0c59-4673-8b37-3d696fe63a5d/files/get/last.ckpt?path=%2F2020-11-13T21-41-45_faceshq_transformer%2Fcheckpoints%2Flast.ckpt"
    download(faceshq_yaml_url,"faceshq.yaml")
    download(faces_ckpt_url,"faceshq.ckpt")
  if wikiart_1024:
    wikiart_1024_yaml_url = "http://mirror.io.community/blob/vqgan/wikiart.yaml"
    wikiart_1024_ckpt_url = "http://mirror.io.community/blob/vqgan/wikiart.ckpt"
    download(wikiart_1024_yaml_url,"wikiart_1024.yaml")
    download(wikiart_1024_ckpt_url,"wikiart_1024.ckpt")
  if wikiart_16384:
    wikiart_16384_yaml_url = "http://eaidata.bmk.sh/data/Wikiart_16384/wikiart_f16_16384_8145600.yaml"
    wikiart_16384_ckpt_url = "http://eaidata.bmk.sh/data/Wikiart_16384/wikiart_f16_16384_8145600.ckpt"
    download(wikiart_16384_yaml_url,"wikiart_16384.yaml")
    download(wikiart_16384_ckpt_url,"wikiart_16384.ckpt")
  if sflckr:
    sflckr_yaml_url = "https://heibox.uni-heidelberg.de/d/73487ab6e5314cb5adba/files/?p=%2Fconfigs%2F2020-11-09T13-31-51-project.yaml&dl=1"
    sflckr_ckpt_url = "https://heibox.uni-heidelberg.de/d/73487ab6e5314cb5adba/files/?p=%2Fcheckpoints%2Flast.ckpt&dl=1"
    download(sflckr_yaml_url,"sflckr.yaml")
    download(sflckr_ckpt_url,"sflckr.ckpt")
  if ade20k:
    ade20k_yaml_url = "https://static.miraheze.org/intercriaturaswiki/b/bf/Ade20k.txt"
    ade20k_ckpt_url = "https://app.koofr.net/content/links/0f65c2cd-7102-4550-a2bd-07fd383aac9e/files/get/last.ckpt?path=%2F2020-11-20T21-45-44_ade20k_transformer%2Fcheckpoints%2Flast.ckpt"
    download(ade20k_yaml_url,"ade20k.yaml")
    download(ade20k_ckpt_url,"ade20k.ckpt")
  if ffhq:
    ffhq_yaml_url = "https://app.koofr.net/content/links/0fc005bf-3dca-4079-9d40-cdf38d42cd7a/files/get/2021-04-23T18-19-01-project.yaml?path=%2F2021-04-23T18-19-01_ffhq_transformer%2Fconfigs%2F2021-04-23T18-19-01-project.yaml&force"
    ffhq_ckpt_url = "https://app.koofr.net/content/links/0fc005bf-3dca-4079-9d40-cdf38d42cd7a/files/get/last.ckpt?path=%2F2021-04-23T18-19-01_ffhq_transformer%2Fcheckpoints%2Flast.ckpt&force"
    download(ffhq_yaml_url,"ffhq.yaml")
    download(ffhq_ckpt_url,"ffhq.ckpt")
  if celebahq:
    celebahq_yaml_url = "https://app.koofr.net/content/links/6dddf083-40c8-470a-9360-a9dab2a94e96/files/get/2021-04-23T18-11-19-project.yaml?path=%2F2021-04-23T18-11-19_celebahq_transformer%2Fconfigs%2F2021-04-23T18-11-19-project.yaml&force"
    celebahq_ckpt_url = "https://app.koofr.net/content/links/6dddf083-40c8-470a-9360-a9dab2a94e96/files/get/last.ckpt?path=%2F2021-04-23T18-11-19_celebahq_transformer%2Fcheckpoints%2Flast.ckpt&force"
    download(celebahq_yaml_url,"celebahq.yaml")
    download(celebahq_ckpt_url,"celebahq.ckpt")

def main():
  install()