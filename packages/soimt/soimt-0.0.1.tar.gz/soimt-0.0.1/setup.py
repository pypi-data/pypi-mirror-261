from setuptools import setup, find_packages

setup(
    name='soimt',
    version='0.0.1',
    description='Evaluate the reliability of image classification models',
    include_package_data=True,
    author='BUCT-IST',
    author_email='2023210599@buct.edu.cn',
    maintainer='cjlw',
    maintainer_email='2023210599@buct.edu.cn',
    license='MIT License',
    url='https://github.com/Agiraffea/model_test_program',
    packages=find_packages(),
    platforms=["Windows"],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    install_requires=[
        "torch==2.0.1",
        "torchvision==0.15.2",
        "numpy>1.20.0",
        "tqdm==4.65.0",
        "matplotlib>3.7.0",
    ],
    # entry_points={
    #     'console_scripts': [
    #         ''],
    # },
)
