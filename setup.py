from setuptools import setup

if __name__ == '__main__':
    setup(install_requires=[
    "setuptools>=42",
    "wheel",
    "ttkthemes",
    "opencv-contrib-python",
    "Pillow",
    'evdev; sys_platform == "Linux"',
    'python-uinput; sys_platform == "Linux"'
    ])

