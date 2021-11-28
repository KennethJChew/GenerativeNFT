import subprocess

def main():
    subprocess.run("echo Installing necessary libraries for VQGAN...")
    subprocess.run("git clone https://github.com/openai/CLIP")
    subprocess.run("pip install taming-transformers")
    subprocess.run("git clone https://github.com/CompVis/taming-transformers.git")
    subprocess.run("pip3 install ftfy regex tqdm omegaconf pytorch-lightning")
    
    subprocess.run("pip install kornia")
    subprocess.run("pip install imageio-ffmpeg")
    subprocess.run("pip install einops")
    subprocess.run("mkdir steps")