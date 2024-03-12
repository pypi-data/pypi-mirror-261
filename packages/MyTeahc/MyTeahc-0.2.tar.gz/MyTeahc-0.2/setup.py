from setuptools import setup, find_packages

setup(
    name='MyTeahc',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        # 任何依赖项都在这里列出
        'httpcat-sdk',
        'myhttpcat',
        'myhcat',
    ],
    author='richdwge',
    author_email='rich_dwge@outlook.com',
    description='MyTeahc',
    license='MIT',
    keywords='MyTeahc',
    url='https://github.com/richdwge/MyTeahc',
    download_url='https://github.com/richdwge/MyTeahc',
    project_url='https://github.com/richdwge/MyTeahc',
    project_urls={
        "Source":"https://github.com/richdwge/MyTeahc",
    }
)

