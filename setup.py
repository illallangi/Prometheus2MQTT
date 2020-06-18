import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="prometheus2mqtt-illallangi", # Replace with your own username
  version="0.0.1",
  author="Andrew Cole",
  author_email="andrew.cole@illallangi.com",
  description="Acts as a bridge between Prometheus and MQTT",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/illallangi/Prometheus2MQTT",
  packages=setuptools.find_packages(),
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  entry_points = {
    'console_scripts': ['prometheus2mqtt=prometheus2mqtt.__cli__:main'],
  }
)