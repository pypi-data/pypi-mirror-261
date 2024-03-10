# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bitmoe']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'swarms', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'bitmoe',
    'version': '0.0.1',
    'description': 'BitMoE - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# BitMoE\n1 bit Mixture of Experts utilizing BitNet ++ Mixture of Experts. Also will add distribution amongst GPUs.\n\n## install\n`$ pip3 install bitmoe`\n\n\n# License\nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/BitMoE',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
