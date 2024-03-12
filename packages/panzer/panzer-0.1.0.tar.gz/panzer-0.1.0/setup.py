from setuptools import setup, find_packages

setup(
    name='panzer',
    version='0.1.0',
    author='nand0san',
    author_email='',
    description='REST API manager under development.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nand0san/panzer',  # Asegúrate de poner la URL correcta
    packages=find_packages(),
    install_requires=[
        # Aquí puedes poner una lista de dependencias necesarias, por ejemplo:
        # 'requests',
        # 'urllib3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # 3 - Alpha/4 - Beta/5 - Production/Stable
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',  # Asegúrate de especificar las versiones que soporta
        # 'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',  # Asegúrate de especificar la versión de Python necesaria
    # Incluye archivos no Python si es necesario
    include_package_data=False,
    package_data={
        # Si hay datos como .json o .txt que necesitas incluir, especifica aquí
    },
    # Opcionalmente, si tu paquete es una herramienta de línea de comandos
    # entry_points={
    #     'console_scripts': [
    #         # 'nombre-del-comando = modulo.paquete:funcion'
    #     ],
    # },
)
