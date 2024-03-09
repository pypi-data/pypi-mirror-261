from setuptools import setup, find_packages

setup(
    name             = 'gifconvrt_seokwoolee',
    version          = '1.0.2',
    description      = 'Test package for distribution',
    author           = 'seokwoolee',
    author_email     = 'zkaqhel@gmail.com',
    url              = '',
    download_url     = '',
    install_requires = ['pillow'], # 자동 의존 관계 패키지 설치 목록
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['GIFCONVERTER', 'gifconverter'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 