#Yolofish


import numpy as np

reconstructed_history = np.load('./model_histories/6layer_data_augmentation.npy',allow_pickle='TRUE').item()

import matplotlib.pyplot as plt

acc = reconstructed_history['acc']
val_acc = reconstructed_history['val_acc']

loss = reconstructed_history['loss']
val_loss = reconstructed_history['val_loss']

top_5_acc = reconstructed_history['top_k_categorical_accuracy']
top_5_val_acc = reconstructed_history['val_top_k_categorical_accuracy']


epochs = range(len(acc))

plt.plot(epochs, acc, label='Training accuracy')
plt.plot(epochs, val_acc, label='Validation accuracy')
plt.title('Training and validation accuracy (top-1 accuracy)')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Accuracy')

plt.figure()

plt.plot(epochs, loss, label='Training loss')
plt.plot(epochs, val_loss, label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Loss')

plt.figure()

plt.plot(epochs, top_5_acc, label='Top 5 accuracy')
plt.plot(epochs, top_5_val_acc, label='Top 5 validation accuracy')
plt.title('Training and validation top-5 accuracy')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Accuracy')

plt.show()
