# In[3]: fitur ektraksi
model.fit(train_input, train_labels, epochs=10, batch_size=32,
          validation_split=0.2)