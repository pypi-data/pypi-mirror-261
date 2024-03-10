from setuptools import setup, find_packages

with open(r'README.md','r',encoding='utf-8') as f:
    descricao_longa = f.read()

setup(
    name='pre_processing_text_basic_tools',
    version='0.1',
    packages=find_packages(),
    install_requires = ['regex'],
    description='Toolkit for basic steps on Natural Language Processing - aimed on portuguese BR language.',
    long_description=descricao_longa,
    long_description_content_type="text/markdown",
    author='Igor Caetano de Souza',
    project_urls={
        "GitHub Repository":"https://github.com/IgorCaetano/pre_processing_text_basic_tools"        
    }
)