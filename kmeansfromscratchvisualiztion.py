'''
Pseudocode (from wikipedia for Lloyd's algorithm)
function kmeans(k, points) is
    // Initialize centroids
    centroids ← list of k starting centroids
    converged ← false

    while converged == false do
        // Create empty clusters
        clusters ← list of k empty lists

        // Assign each point to the nearest centroid
        for i ← 0 to length(points) - 1 do
            point ← points[i]
            closestIndex ← 0
            minDistance ← distance(point, centroids[0])
            for j ← 1 to k - 1 do
                d ← distance(point, centroids[j])
                if d < minDistance THEN
                    minDistance ← d
                    closestIndex ← j
            clusters[closestIndex].append(point)

        // Recalculate centroids as the mean of each cluster
        newCentroids ← empty list
        for i ← 0 to k - 1 do
            newCentroid ← calculateCentroid(clusters[i])
            newCentroids.append(newCentroid)

        // Check for convergence
        if newCentroids == centroids THEN
            converged ← true
        else
            centroids ← newCentroids

    return clusters


Problem statement formally:
k-means clustering:
given data set S={x1, x2, x3, ..., xn}
find partition into k clusters
Ω={Ω1, Ω2, Ω3, ..., Ωk}
argmin_Ω sum_{i=1}^n sum_{x∈Ω_i} d(x, μ_i)'''


import numpy as np
import matplotlib.pyplot as plt


def initialize_scatter_gaussian(num_points, num_clusters, std):
    sigma=std
    output=np.empty((num_points,2,num_clusters))
    for cluster in range(num_clusters):
        mu_x=np.random.uniform(low=-1, high=1)
        mu_y=np.random.uniform(low=-1, high=1)
        random_points_x = np.random.normal(loc=mu_x, scale=sigma, size=num_points)
        random_points_y = np.random.normal(loc=mu_y, scale=sigma, size=num_points)
        # Keep all gaussian distributed points inside the unit 
        output[:, 0, cluster] = np.clip(random_points_x, -1.5, 1.5)
        output[:, 1, cluster] = np.clip(random_points_y, -1.5, 1.5)
    return output


def plot(data, centroid_values=None, labels=None, xlim=None, ylim=None):
    S = data.reshape(-1, 2)
    plt.figure(figsize=(8, 6))
    if labels is not None:
        plt.scatter(S[:, 0], S[:, 1], c=labels, cmap='tab10', s=50, alpha=0.8, edgecolors='white', linewidths=0.5)
    else:
        plt.scatter(S[:, 0], S[:, 1], c='steelblue', s=50, alpha=0.8, edgecolors='white', linewidths=0.5)
    if centroid_values is not None:
        plt.scatter(centroid_values[:, 0], centroid_values[:, 1], c=range(len(centroid_values)), cmap='tab10', s=200, marker='X', edgecolors='black', linewidths=1.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('K-means: points by nearest centroid')
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def assign_nearest(S, centroids):
    nearest_centroids = []
    for point in S:
        inf_dist = np.inf
        nearest_centroid_index = 0
        for centroid_index in range(len(centroids)):
            dist = distance(point, centroids[centroid_index])
            if dist < inf_dist:
                inf_dist = dist
                nearest_centroid_index = centroid_index
        nearest_centroids.append(nearest_centroid_index)
    return nearest_centroids

def distance(p1,p2):
    return np.sqrt(np.sum((p1 - p2)**2))


k = 4
sigma=.15 #distance in the end should converge to around sigma^2*numberofpoints*k*2
S = initialize_scatter_gaussian(300, k, sigma)
# make it just array of points in 2d
S = S.reshape(-1, 2)
# Initialize centroids from data so each starts near a real cluster (avoids bad local optimum)
centroids = S[np.random.choice(len(S), size=k, replace=False)]
epsilon = 0.001
#print(S.shape)
#print(S)
#print(centroids)
xlim = (-1.5, 1.5)
ylim = (-1.5, 1.5)



plot(S, xlim=xlim, ylim=ylim) #just points
centroid_history=[centroids.copy()]
nearest_centroids = assign_nearest(S, centroids)
plot(S, centroids, nearest_centroids, xlim=xlim, ylim=ylim) #points with initial cluster assignments (bad)
frames = [(centroids.copy(), nearest_centroids, None, None)]  # None = no move yet (initial)
converged = False
iter = 0
while not converged:
    iter+=1
    labels = np.array(nearest_centroids) #array of k points' nearest centroid value
    new_centroids = np.zeros((k, 2)) #creating new array for recalculating centroids from mean of each cluster
    for i in range(k):
        mask = labels == i
        if np.any(mask):
            new_centroids[i] = np.mean(S[mask], axis=0)
        else:
            new_centroids[i] = centroids[i]
    dist_moved = distance(centroids, new_centroids)
    if dist_moved < epsilon:
        converged = True
    centroids = new_centroids
    centroid_history.append(centroids.copy())
    nearest_centroids = assign_nearest(S, centroids)
    within_cluster_sums = sum(distance(S[j], centroids[labels[j]])**2 for j in range(len(S)))
    frames.append((centroids.copy(), nearest_centroids, dist_moved, within_cluster_sums))


# Animated output: 1 sec/frame, centroid paths (done with ChatGPT)
plt.ion()
fig, ax = plt.subplots(figsize=(8, 6))
for i in range(len(frames)):
    if not plt.fignum_exists(fig.number):
        break
    ax.clear()
    ax.set(xlim=xlim, ylim=ylim, xlabel='x', ylabel='y', title=f'K-means: iteration {i}  |  ε = {epsilon}' + (f'  |  Δ = {frames[i][2]:.4f}' if frames[i][2] is not None else '') + (f'  |  Σ = {frames[i][3]:.4f}' if frames[i][3] is not None else ''))
    ax.grid(True, alpha=0.3)
    ax.scatter(S[:, 0], S[:, 1], c=frames[i][1], cmap='tab10', s=50, alpha=0.8, edgecolors='white', linewidths=0.5, zorder=1)
    ax.scatter(frames[i][0][:, 0], frames[i][0][:, 1], c=range(k), cmap='tab10', s=200, marker='X', edgecolors='black', linewidths=1.5, zorder=2)
    for c in range(k):
        pts = [centroid_history[t][c] for t in range(i + 1)]
        if len(pts) >= 2:
            ax.plot(*zip(*pts), color='black', linestyle='dashed', linewidth=2.5, alpha=0.9, zorder=3)
    fig.canvas.draw()
    plt.pause(1)
plt.ioff()
plt.show()

