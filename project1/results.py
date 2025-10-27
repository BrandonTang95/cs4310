import matplotlib.pyplot as plt
import numpy as np

# --- YOUR "Run 3" DATA ---
results_5 = [46.56, 33.69, 51.69, 51.80]
results_10 = [86.69, 60.32, 102.91, 102.78]
results_15 = [121.01, 85.14, 151.33, 152.21]
# -------------------------

labels = ["FCFS", "SJF", "RR-2", "RR-5"]
job_sizes = ["5 jobs", "10 jobs", "15 jobs"]

# Re-organize data by algorithm
fcfs_data = [results_5[0], results_10[0], results_15[0]]
sjf_data = [results_5[1], results_10[1], results_15[1]]
rr2_data = [results_5[2], results_10[2], results_15[2]]
rr5_data = [results_5[3], results_10[3], results_15[3]]
all_data = [fcfs_data, sjf_data, rr2_data, rr5_data]

# --- 1. Four Individual Graphs ---
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Individual Algorithm Performance vs. Input Size (Run 3)")

for i, ax in enumerate(axs.flat):
    algo_name = labels[i]
    data = all_data[i]
    ax.plot(job_sizes, data, "o-", label=algo_name, color=f"C{i}")
    ax.set_title(f"Performance: {algo_name}")
    ax.set_xlabel("Input Size (# of Jobs)")
    ax.set_ylabel("Avg. Turnaround Time (ms)")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("individual_graphs.png")
print("Saved individual_graphs.png")

# --- 2. One Combined Graph ---
plt.figure(figsize=(10, 6))
plt.plot(job_sizes, fcfs_data, "o-", label="FCFS", color="C0")
plt.plot(job_sizes, sjf_data, "s-", label="SJF", color="C1")
plt.plot(job_sizes, rr2_data, "^-", label="RR-2", color="C2")
plt.plot(job_sizes, rr5_data, "d-", label="RR-5", color="C3")

plt.title("Performance Comparison of All Algorithms (Run 3)")
plt.xlabel("Input Size (# of Jobs)")
plt.ylabel("Avg. Turnaround Time (ms)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("combined_graph.png")
print("Saved combined_graph.png")

plt.show()  # Uncomment this to display the graphs
