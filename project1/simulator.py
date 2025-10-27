"""
CS 4310 Project 1: Performance Analysis Simulator
Part 3a: Run Experiment

This program runs the simulation as designed in Part 1c.
It imports the scheduling functions from the other files,
runs 20 trials for each job size (5, 10, 15), and
prints the final results table.
"""

import random
from copy import deepcopy

# Import the scheduler functions from your files
# Make sure they are in the same directory!
from fcfs import fcfs_scheduler
from sjf import sjf_scheduler
from rr2 import rr_scheduler as rr2_scheduler  # Rename rr_scheduler
from rr5 import rr_scheduler as rr5_scheduler  # Rename rr_scheduler

# --- Helper Class and Functions ---


class Job:
    """
    A simple class to store job data.
    This is needed for the simulator to create new jobs.
    """

    def __init__(self, job_id, burst_time):
        self.id = job_id
        self.burst_time = burst_time
        # --- Tracking ---
        self.remaining_time = burst_time
        # --- Metrics ---
        self.completion_time = 0
        self.turnaround_time = 0


def generate_random_jobs(num_jobs, max_burst_time):
    """Generates a list of new Job objects."""
    jobs = []
    for i in range(1, num_jobs + 1):
        burst = random.randint(1, max_burst_time)
        jobs.append(Job(f"Job{i}", burst))
    return jobs


# --- Simulation Parameters ---
JOB_SIZES = [5, 10, 15]  # [cite: 61]
NUM_TRIALS = 20  # [cite: 65]
MAX_BURST_TIME = 30  # From Part 1c (must be >= 20) [cite: 63, 69]


def run_simulation():
    """Main simulation loop."""

    # This dictionary will hold the final results
    results = {
        5: {"FCFS": 0, "SJF": 0, "RR-2": 0, "RR-5": 0},
        10: {"FCFS": 0, "SJF": 0, "RR-2": 0, "RR-5": 0},
        15: {"FCFS": 0, "SJF": 0, "RR-2": 0, "RR-5": 0},
    }

    print("Running Performance Analysis Simulation...")
    print(f"(Trials per job size: {NUM_TRIALS}, Max Burst Time: {MAX_BURST_TIME}ms)")

    for size in JOB_SIZES:
        print(f"\n--- Testing for Input Size n = {size} jobs ---")

        # Store the 20 trial results for this size
        trial_results = {"FCFS": [], "SJF": [], "RR-2": [], "RR-5": []}

        for i in range(NUM_TRIALS):
            # 1. Generate one new set of random jobs
            original_jobs = generate_random_jobs(size, MAX_BURST_TIME)

            # 2. Run all 4 algorithms on the *same set* of jobs
            # We use deepcopy() to ensure each algorithm gets a fresh,
            # identical copy of the jobs.

            avg_fcfs = fcfs_scheduler(deepcopy(original_jobs))
            trial_results["FCFS"].append(avg_fcfs)

            avg_sjf = sjf_scheduler(deepcopy(original_jobs))
            trial_results["SJF"].append(avg_sjf)

            # Remember to pass the TIME_SLICE to the RR functions
            avg_rr2 = rr2_scheduler(deepcopy(original_jobs), time_slice=2)
            trial_results["RR-2"].append(avg_rr2)

            avg_rr5 = rr5_scheduler(deepcopy(original_jobs), time_slice=5)
            trial_results["RR-5"].append(avg_rr5)

        # 3. Average the 20 trial results
        results[size]["FCFS"] = sum(trial_results["FCFS"]) / NUM_TRIALS
        results[size]["SJF"] = sum(trial_results["SJF"]) / NUM_TRIALS
        results[size]["RR-2"] = sum(trial_results["RR-2"]) / NUM_TRIALS
        results[size]["RR-5"] = sum(trial_results["RR-5"]) / NUM_TRIALS

        print(f"FCFS: {results[size]['FCFS']:.2f}ms")
        print(f"SJF:  {results[size]['SJF']:.2f}ms")
        print(f"RR-2: {results[size]['RR-2']:.2f}ms")
        print(f"RR-5: {results[size]['RR-5']:.2f}ms")

    return results


def print_results_table(results):
    """Prints the final formatted table for the report."""
    print("\n\n--- Final Performance Analysis Table ---")
    print(
        "====================================================================================="
    )
    print(
        f"| {'Input Size':<12} | {'Avg. Turnaround (FCFS)':<22} | {'Avg. Turnaround (SJF)':<22} | {'Avg. Turnaround (RR-2)':<22} | {'Avg. Turnaround (RR-5)':<22} |"
    )
    print(
        "|--------------|------------------------|------------------------|------------------------|------------------------|"
    )
    for size in JOB_SIZES:
        fcfs = f"{results[size]['FCFS']:.2f} ms"
        sjf = f"{results[size]['SJF']:.2f} ms"
        rr2 = f"{results[size]['RR-2']:.2f} ms"
        rr5 = f"{results[size]['RR-5']:.2f} ms"
        print(f"| {size:<12} | {fcfs:<22} | {sjf:<22} | {rr2:<22} | {rr5:<22} |")
    print(
        "====================================================================================="
    )


if __name__ == "__main__":
    final_results = run_simulation()
    print_results_table(final_results)
