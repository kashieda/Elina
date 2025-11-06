from setuptools import find_packages, setup

package_name = 'rear_wheel_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='elina',
    maintainer_email='elina@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'back_wheel_control_node = bis_wheel_control.back_wheel_control_node:main',
                'front_wheel_control_node = bis_wheel_control.front_wheel_control_node:main',
                'pico_serial_logger = bis_wheel_control.pico_serial_logger:main',
                'pico_com_node = bis_wheel_control.pico_com_node:main',
                'pico_com_back = bis_wheel_control.pico_com_back:main',
        ],
    },

)
