from setuptools import find_packages, setup
setup(name="autogpu",
      version="0.1",
      description="A GPU utility for PyTorch",
      author="Patrick Deutschmann",
      author_email='patrick.deutschmann@me.com',
      platforms=["any"],
      license="BSD",
      url="https://github.com/deutschmn/autogpu",
      packages=find_packages(),
      )