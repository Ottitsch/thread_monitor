import psutil
import time

def monitor_all_processes():
    known_threads = {}

    # Initialize known threads for all processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            known_threads[proc.pid] = {t.id for t in psutil.Process(proc.pid).threads()}
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    print("Monitoring all processes for new threads...")

    while True:
        time.sleep(1)
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                current_threads = {t.id for t in psutil.Process(proc.pid).threads()}
                new_threads = current_threads - known_threads.get(proc.pid, set())

                if new_threads:
                    for tid in new_threads:
                        print(f"Process: {proc.info['name']} (PID {proc.pid}) spawned a new thread (TID {tid})")
                    known_threads[proc.pid] = current_threads
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

if __name__ == "__main__":
    monitor_all_processes()