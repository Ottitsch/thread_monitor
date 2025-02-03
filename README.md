# Process Thread Monitor

## Overview
This Python script monitors all running processes on a system and detects when a new thread is spawned. It utilizes the `psutil` library to efficiently track processes and their threads in real-time.

## Features
- Continuously monitors all active processes.
- Detects and reports newly created threads.
- Provides process name, PID, and new thread ID when a new thread is detected.
- Handles process access restrictions and zombie processes gracefully.

## Requirements
- Python 3.x
- `psutil` library

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/process-thread-monitor.git
   cd process-thread-monitor
   ```
2. Install dependencies:
   ```sh
   pip install psutil
   ```

## Usage
Run the script using:
```sh
python monitor_threads.py
```
The script will continuously monitor all processes and print a message when a new thread is detected.

## Example Output
```
Monitoring all processes for new threads...
Process: chrome.exe (PID 1234) spawned a new thread (TID 5678)
Process: python.exe (PID 9101) spawned a new thread (TID 1121)
```
https://github.com/user-attachments/assets/a6d59660-0c16-4c9a-b4de-1167082a3971

## Notes
- The script requires appropriate permissions to access process details. Run with administrator privileges if necessary.
- Handles exceptions for processes that may terminate or become inaccessible during execution.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.

## Author
Developed by Ottitsch. Contributions are welcome!

