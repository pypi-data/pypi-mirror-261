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
    'version': '0.0.2',
    'description': 'BitMoE - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# BitMoE\n1 bit Mixture of Experts utilizing BitNet ++ Mixture of Experts. Also will add distribution amongst GPUs.\n\n## install\n`$ pip3 install bitmoe`\n\n## usage\n```python\nimport torch\nfrom bitmoe.main import BitMoE\n\n# Set the parameters\ndim = 10  # Dimension of the input\nhidden_dim = 20  # Dimension of the hidden layer\noutput_dim = 30  # Dimension of the output\nnum_experts = 5  # Number of experts in the BitMoE model\n\n# Create the model\nmodel = BitMoE(dim, hidden_dim, output_dim, num_experts)\n\n# Create random inputs\nbatch_size = 32  # Number of samples in a batch\nsequence_length = 100  # Length of the input sequence\nx = torch.randn(batch_size, sequence_length, dim)  # Random input tensor\n\n# Forward pass\noutput = model(x)  # Perform forward pass using the model\n\n# Print the output shape\nprint(output)  # Print the output tensor\nprint(output.shape)  # Print the shape of the output tensor\n```\n\n\n# License\nMIT\n\n\n# Todo\n\n- [ ] Implement better gating mechanisms\n- [ ] Implement better routing algorithm\n- [ ] Implement better BitFeedForward\n- [ ] Implement ',
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
