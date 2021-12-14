import requests
import os

imagenet_1024 = True# dl
imagenet_16384 = True # dl
gumbel_8192 = True #dl
coco = True #Dl
faceshq = True
wikiart_1024 = True #url invalid
wikiart_16384 = True
sflckr = True # dl
ade20k = True
ffhq = True
celebahq = True

downloaded = {"imagenet_1024_yaml":False,"imagenet_1024_model":False,"imagenet_16384_yaml":False,"imagenet_16384_model":False,"gumbel_8192_yaml":False,"gumbel_8192_model":False,"coco_yaml":False,"coco_model":False,
"faceshq_yaml":False,"faceshq_model":False,"wikiart_1024_yaml":False,"wikiart_1024_model":False,"wikiart_16384_yaml":False,"wikiart_16384_model":False,"sflckr_yaml":False,"sflckr_model":False,"ade20k_yaml":False,"ade20k_model":False,
"ffhq_yaml":False,"ffhq_model":False,"celebahq_yaml":False,"celebahq_model":False}


def download(url,filename):
  folder = "modelstest"
  filepath = folder + "/" + filename
  print("Downloading " + filename)
  
  if not os.path.exists(folder):
    os.mkdir(folder)

  if os.path.exists(filepath):
    print("File already exists at " + filepath + " , download cancelled.")
  else:
    try:
      dl = requests.get(url=url,allow_redirects=True)
      with open(filepath,"wb") as f:
        f.write(dl.content)
      print(os.getcwd())
      print(filename + " downloaded succesfully. File saved in " + filepath)
      return True
    except Exception as e:
      print("Failed to download " + filename)
      print("Error: " + str(e))
      return False
  

def install():
  print("Downloading models...")

  if imagenet_1024:
    imagenet_1024_yaml_url = "https://heibox.uni-heidelberg.de/d/8088892a516d4e3baf92/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1"
    imagenet_1024_ckpt_url = "https://heibox.uni-heidelberg.de/d/8088892a516d4e3baf92/files/?p=%2Fckpts%2Flast.ckpt&dl=1"
    downloaded["imagenet_1024_yaml"] = download(imagenet_1024_yaml_url,"vqgan_imagenet_f16_1024.yaml")
    downloaded["imagenet_1024_model"] = download(imagenet_1024_ckpt_url,"vqgan_imagenet_f16_1024.ckpt")
  if imagenet_16384:
    imagenet_16384_yaml_url = "https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1"
    imagenet_16384_ckpt_url = "https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1"
    downloaded["imagenet_16384_yaml"] = download(imagenet_16384_yaml_url,"vqgan_imagenet_f16_16384.yaml")
    downloaded["imagenet_16384_model"] = download(imagenet_16384_ckpt_url,"vqgan_imagenet_f16_16384.ckpt")
  if gumbel_8192:
    gumbel_8192_yaml_url = "https://heibox.uni-heidelberg.de/d/2e5662443a6b4307b470/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1"
    gumbel_8192_ckpt_url = "https://heibox.uni-heidelberg.de/d/2e5662443a6b4307b470/files/?p=%2Fckpts%2Flast.ckpt&dl=1"
    downloaded["gumbel_8192_yaml"] = download(gumbel_8192_yaml_url,"gumbel_8192.yaml")
    downloaded["gumbel_8192_model"] = download(gumbel_8192_ckpt_url,"gumbel_8192.ckpt")
  if coco:
    coco_yaml_url = "https://dl.nmkd.de/ai/clip/coco/coco.yaml"
    coco_ckpt_url = "https://dl.nmkd.de/ai/clip/coco/coco.ckpt"
    downloaded["coco_yaml"] = download(coco_yaml_url,"coco.yaml")
    downloaded["coco_model"] = download(coco_ckpt_url,"coco.ckpt")
  if faceshq:
    faceshq_yaml_url = "https://drive.google.com/uc?export=download&id=1fHwGx_hnBtC8nsq7hesJvs-Klv-P0gzT"
    faces_ckpt_url = "https://app.koofr.net/content/links/a04deec9-0c59-4673-8b37-3d696fe63a5d/files/get/last.ckpt?path=%2F2020-11-13T21-41-45_faceshq_transformer%2Fcheckpoints%2Flast.ckpt"
    downloaded["faceshq_yaml"] = download(faceshq_yaml_url,"faceshq.yaml")
    downloaded["faceshq_model"] = download(faces_ckpt_url,"faceshq.ckpt")
  if wikiart_1024:
    wikiart_1024_yaml_url = "http://mirror.io.community/blob/vqgan/wikiart.yaml"
    wikiart_1024_ckpt_url = "http://mirror.io.community/blob/vqgan/wikiart.ckpt"
    downloaded["wikiart_1024_yaml"] = download(wikiart_1024_yaml_url,"wikiart_1024.yaml")
    downloaded["wikiart_1024_model"] = download(wikiart_1024_ckpt_url,"wikiart_1024.ckpt")
  if wikiart_16384:
    wikiart_16384_yaml_url = "http://eaidata.bmk.sh/data/Wikiart_16384/wikiart_f16_16384_8145600.yaml"
    wikiart_16384_ckpt_url = "http://eaidata.bmk.sh/data/Wikiart_16384/wikiart_f16_16384_8145600.ckpt"
    downloaded["wikiart_16384_yaml"] = download(wikiart_16384_yaml_url,"wikiart_16384.yaml")
    downloaded["wikiart_16384_model"] = download(wikiart_16384_ckpt_url,"wikiart_16384.ckpt")
  if sflckr:
    sflckr_yaml_url = "https://heibox.uni-heidelberg.de/d/73487ab6e5314cb5adba/files/?p=%2Fconfigs%2F2020-11-09T13-31-51-project.yaml&dl=1"
    sflckr_ckpt_url = "https://heibox.uni-heidelberg.de/d/73487ab6e5314cb5adba/files/?p=%2Fcheckpoints%2Flast.ckpt&dl=1"
    downloaded["sflckr_yaml"] = download(sflckr_yaml_url,"sflckr.yaml")
    downloaded["sflckr+model"] = download(sflckr_ckpt_url,"sflckr.ckpt")
  if ade20k:
    ade20k_yaml_url = "https://static.miraheze.org/intercriaturaswiki/b/bf/Ade20k.txt"
    ade20k_ckpt_url = "https://app.koofr.net/content/links/0f65c2cd-7102-4550-a2bd-07fd383aac9e/files/get/last.ckpt?path=%2F2020-11-20T21-45-44_ade20k_transformer%2Fcheckpoints%2Flast.ckpt"
    downloaded["ade20k_yaml"] = download(ade20k_yaml_url,"ade20k.yaml")
    downloaded["ade20k_yaml"] = download(ade20k_ckpt_url,"ade20k.ckpt")
  if ffhq:
    ffhq_yaml_url = "https://app.koofr.net/content/links/0fc005bf-3dca-4079-9d40-cdf38d42cd7a/files/get/2021-04-23T18-19-01-project.yaml?path=%2F2021-04-23T18-19-01_ffhq_transformer%2Fconfigs%2F2021-04-23T18-19-01-project.yaml&force"
    ffhq_ckpt_url = "https://app.koofr.net/content/links/0fc005bf-3dca-4079-9d40-cdf38d42cd7a/files/get/last.ckpt?path=%2F2021-04-23T18-19-01_ffhq_transformer%2Fcheckpoints%2Flast.ckpt&force"
    downloaded["ffhq_yaml"] = download(ffhq_yaml_url,"ffhq.yaml")
    downloaded["ffhq_model"] = download(ffhq_ckpt_url,"ffhq.ckpt")
  if celebahq:
    celebahq_yaml_url = "https://app.koofr.net/content/links/6dddf083-40c8-470a-9360-a9dab2a94e96/files/get/2021-04-23T18-11-19-project.yaml?path=%2F2021-04-23T18-11-19_celebahq_transformer%2Fconfigs%2F2021-04-23T18-11-19-project.yaml&force"
    celebahq_ckpt_url = "https://app.koofr.net/content/links/6dddf083-40c8-470a-9360-a9dab2a94e96/files/get/last.ckpt?path=%2F2021-04-23T18-11-19_celebahq_transformer%2Fcheckpoints%2Flast.ckpt&force"
    downloaded["celebhq_yaml"] = download(celebahq_yaml_url,"celebahq.yaml")
    downloaded["celebhq_model"] = download(celebahq_ckpt_url,"celebahq.ckpt")
  
  print("Status of downloads:" + str(downloaded))

if __name__ == "__main__":
  print("Downloading models...")
  install()