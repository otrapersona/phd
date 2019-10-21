import matplotlib.pyplot as plt
plt.figure()
plt.plot([1,2], [1,2])
manager = plt.get_current_fig_manager()
#manager.resize(*manager.window.maxsize())
manager.resize(1024,600)
plt.show()
