from setuptools import find_packages, setup

package_name = 'eva_h1_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
        ('share/' + package_name + '/urdf', [
            'urdf/eva_h1.urdf.xacro',
            'urdf/eva_h1.urdf'
        ]),
     ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sahasra',
    maintainer_email='sahasra7733@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
