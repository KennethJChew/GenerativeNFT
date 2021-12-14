import subprocess
import generation.model_selection_download
# Clone CLIP and taming transformers repos
# Runs installation of libraries

subprocess.run("git clone https://github.com/openai/CLIP")
subprocess.run("git clone https://github.com/CompVis/taming-transformers.git")
subprocess.run("pip install taming-transformers")
subprocess.run("pip install ftfy regex tqdm omegaconf pytorch-lightning")
subprocess.run("pip install kornia")
subprocess.run("pip install imageio-ffmpeg")
subprocess.run("pip install einops")
subprocess.run("mkdir steps")
subprocess.run("mkdir ./steps/intervals")

install()