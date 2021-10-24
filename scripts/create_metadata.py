from brownie import NFT,network
from metadata.metadata_template import metadata_template
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
import os
from pathlib import Path
import requests
import json

def create_metadata(imagepath):
    print("Getting NFT contract to create metadata\n")
    nft = NFT[-1]
    nftId = nft._tokenId()
    print("There are currently " + str(nftId) + " NFTs created\n")
    # Uploads the image and the metadata to Pinata
    nftUri = upload_to_pinata(imagepath,nftId)
    return nftUri
    # get metadata template
    # metadata = metadata_template
    
    # metadata["image"] = image_uri
    # if "isDuplicate" in response:
    #     metadata["duplicate"] = True
    # else:
    #     metadata["duplicate"] = False
    # metadata["description"] = "This is the test description"
    # metadata["attributes"]["corpus"] = "Lorem Ipsum Dolem - Test Word Corpus"
    

    


def upload_to_pinata(filePath:str,nftid:int) -> str:
    """
    Takes a filepath of the generated image and the nftID and uploads both the filepath and the metadata onto Pinata.
    Returns the metadata URI
    """
    PINATA_BASE_URL = "https://api.pinata.cloud"
    file_endpoint = "/pinning/pinFileToIPFS"

    headers = {
        "pinata_api_key": os.getenv("PINATA_API_KEY"),
        "pinata_secret_api_key": os.getenv("PINATA_API_SECRET")
    }

    print("Uploading to pinata\n")
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print("Running in local blockchain environment\n")

        # If we are calling this locally, split the filepath by slashes, and store them in array from last segment to first.
        # The first segment(filename) will be stored in the variable filename
        filename = filePath.split("/")[-1:][0]
        print("Filename acquired: " + filename + "\n")
        with Path(filePath).open("rb") as fp:
            image_binary = fp.read()
            print("Posting request to pinata")
            response = requests.post(url=PINATA_BASE_URL + file_endpoint,files={"file":(filename,image_binary)},headers=headers)
            print(response.json())
        ipfs_hash = response.json()["IpfsHash"]
        # image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}"
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"

        # Upload JSON metadata to Pinata
        # get metadata template
        print("Assembling metadata for upload to Pinata...\n")
        print("Acquiring metada template...\n")
        metadata = metadata_template

        print("Setting metadata image URI:" + str(image_uri) + "\n")
        metadata["image"] = image_uri

        print("Setting metadata duplicate...\n")
        if "isDuplicate" in response:
            metadata["attributes"][0]["value"] = True
        else:
            metadata["attributes"][0]["value"] = False
        print("Metadata duplicate status:" + str(metadata["attributes"][0]["value"]) + "\n")

        print("Setting metadata description...\n")
        metadata["description"] = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.Pellentesque ac tempus lacus.Vestibulum a convallis turpis. Mauris suscipit pretium lorem vestibulum vulputate. Sed posuere orci a mollis pretium. Aliquam eget accumsan libero, sodales eleifend orci. Donec mauris sapien, congue vel dolor et, euismod pellentesque libero. Sed sed malesuada odio. Praesent a diam metus. Nulla dui urna, accumsan nec felis a, rutrum tempor ipsum. Maecenas eu porta sem. Quisque scelerisque neque augue, in efficitur nisi ullamcorper nec. Curabitur vehicula nec nisl et ultrices.Aliquam vel dui eget massa elementum commodo. Proin vitae arcu orci. Proin nec lectus a urna tristique porttitor eget faucibus enim. Donec ultricies ex in augue scelerisque, et scelerisque tellus eleifend. Vivamus fermentum metus elit, quis dignissim nisl commodo ac. Praesent non diam nec sem tempor vestibulum id id elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In consequat euismod lacus id ultricies.Mauris gravida sapien eget sagittis imperdiet. Nulla sed tellus ipsum. Sed a malesuada mauris. Proin rutrum massa id velit interdum feugiat. Sed justo nisl, lobortis vitae nisi vitae, interdum facilisis velit. Cras dignissim tortor a tortor rutrum, cursus malesuada sapien iaculis. Curabitur convallis ac purus in blandit. Donec eu ligula vel augue dictum imperdiet in cursus nibh. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum sed odio et sem rutrum efficitur. Nullam malesuada ipsum pretium neque congue, vitae malesuada tellus finibus. Mauris sit amet laoreet lacus, ut ullamcorper metus. Nam imperdiet libero id erat hendrerit malesuada. Nulla vitae sollicitudin magna, nec aliquam nisi. Vivamus bibendum, ipsum eu euismod sodales, tortor ex rutrum arcu, eget pellentesque sapien diam nec sapien.
Curabitur nec dui dui. Nunc non molestie odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam consectetur consectetur quam, eu varius felis. Sed tristique pharetra porta. Cras cursus diam ipsum. Vivamus massa neque, auctor non justo in, fermentum malesuada risus. Nunc ut odio vitae sem efficitur pharetra id ut massa. Nunc bibendum odio ex, ut tincidunt sem congue vel. Cras vel mi quis ex porttitor sagittis. Aenean hendrerit congue massa. Donec convallis feugiat nisl. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent eget eleifend felis.
Vestibulum sodales molestie est nec facilisis. Quisque ut sem lacinia, faucibus nulla eu, facilisis lacus. Donec vestibulum erat justo. Vestibulum diam est, interdum eu ipsum non, accumsan viverra mauris. Ut lorem diam, egestas vitae nulla eu, mattis interdum augue. Cras rutrum sollicitudin massa, ut gravida lectus tristique ut. Nullam tincidunt turpis fringilla felis blandit mattis. In facilisis et lacus auctor venenatis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris pulvinar libero augue, id tempor odio ullamcorper vel. Maecenas congue a dui quis molestie. Vivamus eu fermentum augue. Donec consequat ultrices dapibus. Vivamus hendrerit quis mi quis mollis. Sed quis magna sagittis sem pulvinar laoreet a ac ipsum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;"""
        print("Metadata description set: " + str(metadata["description"]) + "\n")

        # print("Setting metadata attribute - corpus...\n")
        # metadata["attributes"][0]["corpus"] = "Lorem Ipsum Dolem - Test Word Corpus"
        # print("Set metadata attribute - corpus:" + str(metadata["attributes"][0]["corpus"]))

        print("Uploading metadata to Pinata\n")
        print(metadata)
        metadata_json = json.dumps(metadata)
        metadata_upload_response = requests.post(url=PINATA_BASE_URL + file_endpoint,files={"file":("metadata",metadata_json)},headers=headers)
        metadata_hash = metadata_upload_response.json()["IpfsHash"]
        metadata_json_uri = f"https://ipfs.io/ipfs/{metadata_hash}"
        print("Uploaded to Pinata successfully. Returning the following:")
        print("Metadata URI: " + str(metadata_json_uri) + "\n")
        return metadata_json_uri
    else:
        # TODO - get image name from image generator
        pass    
    
def upload_image():
    pass

def upload_metadata():
    pass

def main():
    create_metadata()