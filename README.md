# EnjoyTagus131
Python-based CLI tool for managing boat trip schedules, handling skipper availability and booking requests. Developed for a university programming course in 2022.

# Boat Trip Scheduler 🚤

## About the Project
This project is a boat trip scheduling management system developed in **Python**. It was created in an academic context on December 18, 2022.

The software manages the agenda for boat tours by processing skippers' availability, existing schedules, and incoming booking requests to determine the final schedule.

## Features
- Parsing of skipper availability.
- Management of current boat schedules.
- Processing of new booking requests against available slots.
- Conflict resolution and schedule updating.

## Prerequisites
- Python 3.11 (or higher)

## Usage
To run the program, execute the `update.py` script providing the paths to the input files in the following order:
1. Skippers file
2. Schedule file
3. Requests file

### Command Structure
```bash
python update.py <path_to_skippers> <path_to_schedule> <path_to_requests>
