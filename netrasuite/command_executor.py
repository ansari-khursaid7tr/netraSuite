import subprocess

def run_command(cmd: str):
    try:
        process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return process.stdout + (process.stderr if process.stderr else "")
    except Exception as e:
        return f"Command execution failed: {e}"
