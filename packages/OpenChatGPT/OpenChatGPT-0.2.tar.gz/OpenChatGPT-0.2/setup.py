from setuptools import setup, find_packages

setup(
    name='OpenChatGPT',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'uuid',
    ],
    author='Amir Agassi',
    author_email='amiragassi04@gmail.com',
    description='A Python package for integrating with the internal OpenAI Chat API.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
