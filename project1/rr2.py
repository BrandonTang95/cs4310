"""
CS 4310 Project 1: Simulating Job Scheduler
Part 2: Implementation - Round-Robin (Time Slice = 2)

This program simulates the Round-Robin (RR) scheduling algorithm
with a fixed time slice of 2.

Usage: python rr2.py <input_file>
Example: python rr2.py job.txt
"""

import sys
from collections import deque


class Job:
    """A simple class to store job data."""

    def __init__(self, job_id, burst_time):
        self.id = job_id
        self.burst_time = burst_time
        # --- Tracking ---
        self.remaining_time = burst_time
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


def rr_scheduler(job_list, time_slice):
    """
    Simulates the Round-Robin (RR) scheduling algorithm.
    All jobs arrive at time 0.
    """
    current_time = 0
    total_turnaround_time = 0
    jobs_completed = 0
    total_jobs = len(job_list)

    # Use a deque for the ready queue
    ready_queue = deque(job_list)

    # print(f"--- Round-Robin (TimeSlice={time_slice}) Simulation ---")
    # print("Job execution order and details:\n")

    while jobs_completed < total_jobs:
        job = ready_queue.popleft()

        start_time = current_time

        if job.remaining_time > time_slice:
            # Job runs for a full slice, does not finish
            current_time += time_slice
            job.remaining_time -= time_slice

            # Put job back at the end of the queue
            ready_queue.append(job)

            # Print execution details [cite: 22]
            # print(
            #     f"  Time {start_time:02d} - {current_time:02d}: {job.id} (Remaining: {job.remaining_time})"
            # )

        else:
            # Job will finish in this turn
            current_time += job.remaining_time
            job.remaining_time = 0
            job.completion_time = current_time
            job.turnaround_time = job.completion_time  # Since arrival_time is 0

            total_turnaround_time += job.turnaround_time
            jobs_completed += 1

            # Print execution details [cite: 22]
            # print(
            #     f"  Time {start_time:02d} - {current_time:02d}: {job.id} *** FINISHED ***"
            # )

    # Calculate and print the final average
    average_turnaround_time = total_turnaround_time / total_jobs

    # print(f"\n--- RR (TimeSlice={time_slice}) Results ---")
    # print(f"Total jobs: {total_jobs}")
    # print(f"Total time: {current_time} ms")
    # print(f"Average Turnaround Time: {average_turnaround_time:.2f} ms")

    return average_turnaround_time


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python rr2.py <input_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    jobs = parse_input_file(input_filename)

    TIME_SLICE = 2  # [cite: 17]

    if jobs:
        rr_scheduler(jobs, TIME_SLICE)


if __name__ == "__main__":
    main()
