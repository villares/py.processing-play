import pickle

A = "to be saved"

with open("data/variableA.p", "wb") as f:
    pickle.dump(A, f)

A = "temp value"
print A

with open("data/variableA.p", "rb") as f2:
    A = pickle.load(f2)
    print A
