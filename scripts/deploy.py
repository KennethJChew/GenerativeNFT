from brownie import NFT, network, config
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from scripts.upload_to_pinata import upload_to_pinata
from scripts.create_metadata import create_metadata
import os
import json


def deploy():
    print("Deploying...\n")

    
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print("Getting owner account..\n")
        account = get_account(index=0)
        print("Owner account acquired: " + str(account) + "\n")
        print("Getting 2nd account..\n")
        account2 = get_account(index=1)
        print("2nd account acquired: " + str(account2) + "\n")
    else:
        account = get_account()
    print("Deploying NFT contract\n")
    nft = NFT.deploy({"from": account})
    print("NFT contract deployed at " + str(nft) + "\n")

    print("Generating image...\n")
    """
    TODO - Generate Image
    """
    image = generateImage()
    print("Image generated!\n")
    # print("IMAGE IS " + str(image))
    print("Creating Metadata...\n")
    nftUri = create_metadata(image)
    print("Metadata created, URI: " + str(nftUri) + "\n")
    print("Minting NFT...\n")
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        mint_tx = nft.createNFT(account2, nftUri)
    else:
        mint_tx = nft.createNFT(account, nftUri)
    mint_tx.wait(1)
    print(mint_tx)
    print("NFT Minted!\n")


def generateImage():
    # get image
    print("Generating image....")
    print("Getting image path..")
    img_path = "./img/ghost.png"
    print("Acquired image path...")
    return img_path


def main():
    deploy()
