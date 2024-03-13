from setuptools import setup,find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
	name='Btc_price1',
	description="基于Paddle构建简单神经网络比特币价格预测",
	version='0.1.1',
	long_description=long_description,
    long_description_content_type='text/markdown',
	packages=find_packages(),
	url="https://github.com/toy1v/Btc_priceforecast",
)

