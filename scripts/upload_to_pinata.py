import os
from pathlib import Path
from brownie import network
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
import requests

PINATA_BASE_URL = "https://api.pinata.cloud"
endpoint = "/pinning/pinFileToIPFS"
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET")
}


def upload_to_pinata(filePath):
    print("Uploading to pinata")
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print("Running in local blockchain environment")
        # If we are calling this locally, split the filepath by slashes, and store them in array from last segment to first.
        # The first segment(filename) will be stored in the variable filename
        filename = filePath.split("/")[-1:][0]
        print("Filename acquired: " + filename)
        with Path(filePath).open("rb") as fp:
            image_binary = fp.read()
            print("Posting request to pinata")
            response = requests.post(url=PINATA_BASE_URL + endpoint,files={"file":(filename,image_binary)},headers=headers)
            print(response.json())
        return response.json()
    else:
        # TODO - get image name from image generator
        pass

