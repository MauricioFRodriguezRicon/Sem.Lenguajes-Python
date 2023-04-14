evaluar = """ título: Experiences in Developing a Distributed Agent-based 
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance 
computing resources provides the promise of capturing unprecedented details 
of large-scale complex systems. However, the specialized knowledge required 
for developing such ABMs creates barriers to wider adoption and utilization. 
Here we present our experiences in developing an initial implementation of 
Repast4Py, a Python-based distributed ABM toolkit. We build on our 
experiences in developing ABM toolkits, including Repast for High 
Performance Computing (Repast HPC), to identify the key elements of a useful 
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages 
and the Python C-API to create a scalable modeling system that can exploit 
the largest HPC resources and emerging computing architectures.
"""


desarmar = evaluar.split()

inicio_texto=desarmar.index("resumen:")

titulo = []

for i in range(1,inicio_texto):
    titulo.append(desarmar[i])

for i in range(inicio_texto+1):
    desarmar.pop(0)

oraciones = []

oracion = []

for palabra in desarmar:
    oracion.append(palabra)
    if(palabra.endswith('.')):
        oraciones.append(oracion.copy())
        oracion.clear()

if(len(titulo) <= 10):
    print('Titulo:Ok')
else:
    print('Titulo:No Ok')


oracionesFaciles = 0
oracionesMedias = 0
oracionesDificiles = 0
oracionesMuyDificiles = 0

for linea in oraciones:  
    if(len(linea)<=12):
        oracionesFaciles +=1
    elif(len(linea)<=17):
        oracionesMedias+=1
    elif(len(linea)<=25):
        oracionesDificiles += 1
    else:
        oracionesMuyDificiles+=1

print('Cantidad de oraciones fáciles de leer:',oracionesFaciles,', aceptables para leer:',oracionesMedias, ', dificil de leer:',oracionesDificiles ,', muy difícil de leer:',oracionesMuyDificiles)