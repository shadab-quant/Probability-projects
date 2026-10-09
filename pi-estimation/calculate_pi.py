import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def calculate_pi(N):
 
 x = np.random.uniform(-1, 1, N)
 y = np.random.uniform(-1, 1, N)

 inside = x**2 + y**2 <= 1 
 inside_count = np.sum(inside)

 estimate_pi = 4 * inside_count / N
 
 return estimate_pi, x, y, inside


N_values = [100, 1000, 10000, 100000, 1000000]
num_trial = 100
std_values = []

for N in N_values:

    errors = []
    
    for trial in range(num_trial):
      estimate, x, y, inside = calculate_pi(N)

      error = abs(np.pi - estimate)
      errors.append(error)

      percentage_error = (error / np.pi) * 100


    average = np.mean(errors)
    std= np.std(errors)
    constant_factor = std * np.sqrt(N)
    std_values.append(std)

    print (N, "Mean: ", average)
    print (N, "standard deviation: ", std, constant_factor)


    

log_N = np.log(N_values)
log_std = np.log(std_values)
slope, intercept = np.polyfit(log_N, log_std, 1)
print("Slope", slope)

print(estimate)
print(x.shape)
print(y.shape)
print(inside.shape)


N_plot = 1000
estimate, x, y, inside = calculate_pi(N_plot)
plt.figure()
plt.scatter(x[inside], y[inside])
plt.scatter(x[~inside], y[~inside])

square = patches.Rectangle(
  (-1, -1),
  2,
  2,
  fill = False
)

circle = patches.Circle(
  (0, 0),
  1,
  fill = False
)

plt.gca().add_patch(square)
plt.gca().add_patch(circle)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte carlo simulation")
plt.axis("equal")
plt.show


plt.figure()
plt.loglog(N_values, std_values, marker= "o")
plt.xlabel("N")
plt.ylabel("standard deviation")
plt.title("monto carlo convergence")
plt.show()