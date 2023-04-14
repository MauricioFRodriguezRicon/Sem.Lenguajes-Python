jupyter_info = """ JupyterLab is a web-based interactive development 
environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user 
interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. 
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing 
ones.
"""

jupyter_info.lower()

por_palabra = jupyter_info.split()

print('Ingrese una letra')
letra = input()

for palabra in por_palabra:
    if(palabra.startswith(letra)):
        print(palabra)
