from setuptools import setup,find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
	name='Btc_price1',
	version='0.1',
	packages=find_packages(),
	url="https://github.com/toy1v/Btc_priceforecast",
)

