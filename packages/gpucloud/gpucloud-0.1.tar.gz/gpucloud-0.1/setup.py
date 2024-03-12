from setuptools import setup, find_packages

setup(
    name='gpucloud',  # ใส่ชื่อของ package ของคุณ
    version='0.1',  # ใส่เวอร์ชันของ package
    packages=find_packages(),
    install_requires=[
        'Flask>=1.1.2'  # ต้องการ Flask รุ่นอย่างน้อย 1.1.2
    ],
    author='gpucloud',
    author_email='admin@project2you.com',
    description='A simple Flask app',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
