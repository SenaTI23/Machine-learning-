import numpy as np

data = np.array([
    [40, 5, 60, "Tolak"],
    [50, 8, 40, "Terima"],
    [60, 7, 30, "Tolak"],
    [70, 4, 60, "Terima"],
    [80, 4, 80, "Terima"],
    [60, 6, 60, "Tolak"]
])

query = np.array([50, 3, 40])

def euclidean_distance(a, b):
    return np.sum((a - b) ** 2)

distances = []
for row in data:
    x = row[:3].astype(float)  
    y = row[3]  
    distance = euclidean_distance(query, x)
    distances.append((distance, y))

distances.sort(key=lambda x: x[0])

k = 3
nearest_neighbors = distances[:k]

tolak_count = sum(1 for d in nearest_neighbors if d[1] == "Tolak")
terima_count = sum(1 for d in nearest_neighbors if d[1] == "Terima")


prediction = "Tolak" if tolak_count > terima_count else "Terima"


print("K=3 Nearest Neighbors:")
for d in nearest_neighbors:
    print(f"Jarak: {d[0]}, Kelas: {d[1]}")

print(f"\nPrediksi kelas untuk query {query} adalah: {prediction}")