import subprocess
import time

def run_script(script_name):
    """Runs a Python script using subprocess."""
    try:
        print(f"[*] Starting {script_name}...")
        process = subprocess.Popen(['python', script_name])
        return process
    except FileNotFoundError:
        print(f"[!] Error: {script_name} not found.")
        return None
    except Exception as e:
        print(f"[!] An error occurred while running {script_name}: {e}")
        return None

if __name__ == "__main__":
    server_process = run_script('tsvpn_server_client.py')
    client_process = run_script('tsvpn_gui.py')

    if server_process and client_process:
        print("[*] TS VPN (simplified) is running. Close the terminal windows or the GUI to stop.")
        try:
            # Keep the main script running until the user interrupts (Ctrl+C)
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[*] Stopping TS VPN...")
            if server_process.poll() is None:
                server_process.terminate()
                server_process.wait()
                print("[*] Server stopped.")
            if client_process.poll() is None:
                client_process.terminate()
                client_process.wait()
                print("[*] Client GUI stopped.")
    else:
        print("[!] Failed to start one or both scripts.")