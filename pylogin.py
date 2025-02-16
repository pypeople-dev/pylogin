import uvicorn
import logging
import os
import sys
import subprocess
import signal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)

pylogin = FastAPI()

# Load environment variables
PID_FILE = os.getenv("PID_FILE", "pylogin.pid")
origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# Add CORS middleware
pylogin.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def start():
    if os.path.exists(PID_FILE):
        print("Pylogin is already running!")
        sys.exit(0)

    # Run process in the background
    if os.name == "nt":
        process = subprocess.Popen([sys.executable, __file__, "run"],
                                   creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
    else:
        process = subprocess.Popen([sys.executable, __file__, "run"],
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL,
                                   preexec_fn=os.setsid)

    # Save the PID to a file
    with open(PID_FILE, "w") as f:
        f.write(str(process.pid))
    print(f"pylogin started with PID {process.pid}.")


def stop():
    if not os.path.exists(PID_FILE):
        print("No running instance found.")
        return

    with open(PID_FILE, "r") as f:
        pid = int(f.read())
    
    try:
        if os.name == "nt":
            subprocess.call(["taskkill", "/F", "/PID", str(pid)])
        else:
            os.killpg(pid, signal.SIGTERM)
        print(f"pylogin with PID {pid} has been stopped.")
    except ProcessLookupError:
        print("Process already terminated.")
    
    os.remove(PID_FILE)

def run():
    server_port = int(os.getenv('PORT', 5001))
    logging.info("pylogin server started on port " + str(server_port))

    uvicorn.run(
        "pylogin:pylogin",
        host="0.0.0.0", 
        port=server_port, 
        reload=True
    )

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        run()
    elif len(sys.argv) > 1 and sys.argv[1] == "stop":
        stop()
    elif len(sys.argv) > 1 and sys.argv[1] == "start":
        start()
    else:
        print("Invalid command. Use 'start', 'stop', or 'run'.")