from setuptools import setup

setup(name='fets',
      version='0.0.1',
      packages=['fets',
                'fets.models',
                'fets.models.pytorch',
                'fets.models.pytorch.pt_3dresunet',
                'fets.models.pytorch.brainmage',
                'fets.data',
                'fets.data.pytorch'],
      install_requires=['protobuf', 'pyyaml', 'grpcio', 'tqdm', 'coloredlogs', 'nibabel', 'sklearn', 'SimpleITK', 'pandas', 'torchio==0.18.4']
)
