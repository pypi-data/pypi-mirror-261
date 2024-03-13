from setuptools import setup, find_packages
import requests
import re

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

def get_latest_tarball():
    url = "https://api.github.com/repos/pfeinsper/drone-swarm-search/releases/latest"
    response = requests.get(url, timeout=100)
    response.raise_for_status()
    data = response.json()
    tarball_url = data["tarball_url"]
    tarball_url = re.sub(r"{.*?}", "", tarball_url)
    return tarball_url

download_url = get_latest_tarball()
print(f"Download URL: {download_url}")

setup(
    name="DSSE",
    version="0.2.2",
    author="Luis Filipe Carrete, Manuel Castanares, Enrico Damiani, Leonardo Malta, Joras Oliveira, Ricardo Ribeiro Rodrigues, Renato Lafrachi Falcao, Pedro Andrade, Fabricio Barth",
    description="An environment to train drones to search and find a shipwrecked person lost in the ocean using reinforcement learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pfeinsper/drone-swarm-search",
    license="MIT",
    keywords=["Reinforcement Learning", "AI", "SAR", "Multi Agent"],
    download_url=download_url,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "numpy",
        "gymnasium",
        "pygame",
        "pettingzoo",
        "matplotlib",
        "numba",
    ],
)
