from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Script for sorting files in a folder',
      author='Serhii Hrabar',
      author_email='strategs89@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:clean_folder']},
      # clean-folder - команда, яка повинна виконатись в терміналі
      # після '=' пишемо шлях до файлу, де знаходиться функція
      # після ':' пишемо назву функції яку запускати треба
      )