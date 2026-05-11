import numpy as np
import matplotlib.pyplot as plt

def generate_dummy_data(samples=100, features=10):
    X = np.random.rand(samples, features)
    y = np.random.randint(0, 2, size=samples)
    return X, y

class AIRS:
    def __init__(self, num_detectors=10, mutation_rate=0.1):
        self.num_detectors = num_detectors
        self.mutation_rate = mutation_rate

    def train(self, X, y):
        indices = np.random.choice(len(X), self.num_detectors, replace=False)
        self.detectors = X[indices]
        self.detector_labels = y[indices]
        for i in range(len(self.detectors)):
            if np.random.rand() < self.mutation_rate:
                self.detectors[i] += np.random.normal(0, 0.1, size=self.detectors[i].shape)

    def predict(self, X):
        predictions = []
        for sample in X:
            distances = np.linalg.norm(self.detectors - sample, axis=1)
            predictions.append(self.detector_labels[np.argmin(distances)])
        return np.array(predictions)

X, y = generate_dummy_data()
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = AIRS(num_detectors=70, mutation_rate=0.05)
model.train(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = np.mean(y_pred == y_test)
print(f"Accuracy: {accuracy:.2f}")