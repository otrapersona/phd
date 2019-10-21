import matplotlib.pyplot as plt
from sys import argv
elDPI = int(argv[1])
ancho = 1024/float(elDPI)
alto = 600/float(elDPI)
#print(argv[1],eldpi,ancho,alto)
plt.figure(figsize=(ancho,alto),dpi=elDPI)

#plt.figure(figsize=(6.4,3.75),dpi=160)
#plt.figure(figsize=(5.12,3),dpi=200)
#plt.figure(figsize=(2.56,1.5),dpi=400)
#plt.figure(figsize=(1.28,0.75),dpi=800)

#plt.figure()
plt.plot([1,2], [1,2])

#manager = plt.get_current_fig_manager()
#manager.resize(*manager.window.maxsize())
#manager.resize(1024,600)
#plt.show()

plt.savefig(str(elDPI)+'.png')
