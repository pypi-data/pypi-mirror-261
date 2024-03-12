from setuptools import setup, find_packages

VERSION = '0.0.12' 
DESCRIPTION = 'NAS-Network-Controller'
LONG_DESCRIPTION = 'Ejemplo de un network controller creado por NAS para curso de ILP'

# Configurando
setup(
        name="netController", 
        version=VERSION,
        author="Emiliano Rosico",
        author_email="<emiliano19@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=["netmiko==2.4.2","Cryptography==36.0.1"],
        keywords=['python', 'networController', 'MAT', 'IQUALL'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)