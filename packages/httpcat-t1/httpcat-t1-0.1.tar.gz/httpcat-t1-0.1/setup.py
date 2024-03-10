from setuptools import setup, find_packages

setup(
    name='httpcat-t1',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 任何依赖项都在这里列出
        'httpcat-sdk',
        'myhttpcat'
    ],
    author='dwge1',
    author_email='dwge1234@outlook.com',
    description='httpcat-t1',
    license='MIT',
    keywords='httpcat-t1',
    url='https://github.com/dwge1/httpcat-t1',
    download_url='https://github.com/dwge1/httpcat-t1',
    project_urls={
        'Source':'https://github.com/dwge1/httpcat-t1',
    }
)

