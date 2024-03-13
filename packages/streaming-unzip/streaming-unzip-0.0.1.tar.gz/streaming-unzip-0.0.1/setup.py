from setuptools import setup,find_packages
import io

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()


setup(
    name="streaming-unzip",
    license="MIT",
    version="0.0.1",
    keywords=["stream", "zip", "download"],
    author="ShiinaRinne",
    url="https://github.com/ShiinaRinne/stream_zip_downloader",
    packages=find_packages(),
    long_description=readme,
    platforms=["any"],
    install_requires=["aiohttp", "loguru", "requests", "argparse", "asyncio", "aiofiles", "bz2", "lzma" ],
    description="A streaming unzip tool for zip files",
)

