import pickle
y = open("q_7record.txt","ab")
r = pickle.dump(y)
y.close()
y = open("q_7record.txt","rb")
q = pickle.load(y)
y.close()
