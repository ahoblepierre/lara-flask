from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="lara-flask",  # 🔥 Nom de ton package (ce que les autres installeront)
    version="1.0.0",  # 🔥 Version de ton package
    description="Une structure Flask inspirée de Laravel",  # Description courte
    author="Pierre AHOBLE",
    author_email="pierreahoble@gmail.com",
    url="https://github.com/tonrepo/lara-flask",  # 🔥 Lien vers ton repo GitHub
    packages=find_packages(),  # 🔥 Inclut automatiquement tous les modules Python
    include_package_data=True,  # 🔥 Permet d'inclure les fichiers statiques / templates
    install_requires=requirements,  # 🔥 Liste des dépendances
    entry_points={
        "console_scripts": [
            "lara-flask=app.commands:cli"
        ]
    },  # 🔥 Ajoute une commande CLI `lara-flask` accessible globalement
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # 🔥 Version minimale requise de Python
)
