"""
CS 4310 Project 1: Simulating Job Scheduler
Part 2: Implementation - First-Come-First-Serve (FCFS)

This program simulates the FCFS scheduling algorithm based on a list
of jobs read from an input file. It prints the execution details
and calculates the average turnaround time.

Usage: python fcfs.py <input_file>
Example: python fcfs.py job.txt
"""

import sys


class Job:
    """A simple class to store job data."""

    def __init__(self, job_id, burst_time):
        self.id = job_id
        self.burst_time = burst_time
        # --- Metrics ---
        self.completion_time = 0
        self.turnaround_time = 0


def parse_input_file(filename):
    """
    Parses the input job file.
    The file format is:
    Job<id>
    <burst_time>
    ...
    """
    jobs = []
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines), 2):
                job_id = lines[i].strip()
                burst_time = int(lines[i + 1].strip())
                jobs.append(Job(job_id, burst_time))
    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid content in '{filename}'. Check file format.")
        sys.exit(1)
    return jobs


def fcfs_scheduler(job_list):
    """
    Simulates the FCFS scheduling algorithm.
    All jobs arrive at time 0.
    """
    current_time = 0
    total_turnaround_time = 0

    # print("--- FCFS Scheduling Simulation ---")
    # print("Job execution order and details (Gantt Chart style):\n")

    for job in job_list:
        start_time = current_time

        # Process the entire job
        job.completion_time = current_time + job.burst_time
        job.turnaround_time = job.completion_time  # Since arrival_time is 0
        current_time = job.completion_time

        total_turnaround_time += job.turnaround_time

        # Print execution details [cite: 22]
        # print(
        #     f"  Time {start_time:02d} - {current_time:02d}: {job.id} (Burst: {job.burst_time})"
        # )

    # Calculate and print the final average
    average_turnaround_time = total_turnaround_time / len(job_list)

    # print("\n--- FCFS Results ---")
    # print(f"Total jobs: {len(job_list)}")
    # print(f"Total time: {current_time} ms")
    # print(f"Average Turnaround Time: {average_turnaround_time:.2f} ms")

    return average_turnaround_time


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python fcfs.py <input_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    jobs = parse_input_file(input_filename)

    if jobs:
        fcfs_scheduler(jobs)


if __name__ == "__main__":
    main()
