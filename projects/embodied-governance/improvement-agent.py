#!/usr/bin/env python3
"""
Symbiosis Charter Continuous Improvement Agent
共生宪章持续改进代理

Background daemon that continuously improves the governance framework.
后台守护进程，持续改进治理框架。
"""

import os
import sys
import time
import subprocess
import signal
from datetime import datetime
from pathlib import Path

# Configuration
WORK_DIR = Path("/Users/pcofmarcus/.openclaw/workspace/unserious_studio/projects/embodied-governance")
LOG_FILE = WORK_DIR / ".improvement.log"
LOCK_FILE = WORK_DIR / ".improvement.lock"
ITERATION_DELAY = 60  # seconds between iterations

class ImprovementDaemon:
    def __init__(self):
        self.iteration = 0
        self.running = True
        
    def log(self, message):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    
    def check_lock(self):
        """Check if another instance is running"""
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                # Check if process exists
                os.kill(pid, 0)
                self.log(f"Another instance is already running (PID: {pid})")
                return False
            except (ValueError, OSError, ProcessLookupError):
                # Stale lock file
                LOCK_FILE.unlink()
        return True
    
    def create_lock(self):
        """Create lock file with current PID"""
        with open(LOCK_FILE, "w") as f:
            f.write(str(os.getpid()))
    
    def remove_lock(self):
        """Remove lock file on exit"""
        if LOCK_FILE.exists():
            LOCK_FILE.unlink()
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        self.log(f"Received signal {signum}, shutting down...")
        self.running = False
    
    def check_git_status(self):
        """Check git status and commit if needed"""
        try:
            os.chdir(WORK_DIR)
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                self.log(f"Uncommitted changes found, committing...")
                subprocess.run(["git", "add", "-A"], check=True)
                subprocess.run(
                    ["git", "commit", "-m", f"auto: continuous improvement iteration #{self.iteration}"],
                    check=True
                )
                subprocess.run(["git", "push", "origin", "main"], check=True)
                self.log("Changes committed and pushed successfully")
            else:
                self.log("No uncommitted changes")
                
        except subprocess.CalledProcessError as e:
            self.log(f"Git operation failed: {e}")
    
    def read_improvement_plan(self):
        """Read improvement plan to determine next task"""
        plan_file = WORK_DIR / "IMPROVEMENT_PLAN.md"
        if plan_file.exists():
            self.log("Reading improvement plan...")
            # TODO: Parse plan and determine next task
            return True
        return False
    
    def execute_improvement(self):
        """Execute one improvement iteration"""
        self.iteration += 1
        self.log(f"=== Iteration #{self.iteration} starting ===")
        
        # 1. Check git status
        self.check_git_status()
        
        # 2. Read improvement plan
        self.read_improvement_plan()
        
        # 3. TODO: Execute specific improvement tasks
        # This is where the actual improvement logic goes
        # - Read current files
        # - Identify improvement opportunities
        # - Make changes
        # - Commit
        
        self.log(f"=== Iteration #{self.iteration} complete ===")
    
    def run(self):
        """Main daemon loop"""
        # Setup signal handlers
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)
        
        # Check lock
        if not self.check_lock():
            sys.exit(1)
        
        # Create lock
        self.create_lock()
        
        try:
            self.log("=" * 50)
            self.log("Improvement Daemon Started")
            self.log(f"Working directory: {WORK_DIR}")
            self.log(f"Iteration delay: {ITERATION_DELAY}s")
            self.log(f"PID: {os.getpid()}")
            self.log("=" * 50)
            
            while self.running:
                self.execute_improvement()
                
                # Sleep with interrupt handling
                for _ in range(ITERATION_DELAY):
                    if not self.running:
                        break
                    time.sleep(1)
                    
        finally:
            self.remove_lock()
            self.log("Daemon stopped")

def main():
    """Entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Symbiosis Charter Improvement Daemon")
    parser.add_argument("--once", action="store_true", help="Run one iteration and exit")
    parser.add_argument("--status", action="store_true", help="Check daemon status")
    parser.add_argument("--stop", action="store_true", help="Stop running daemon")
    
    args = parser.parse_args()
    
    if args.status:
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, 0)
                print(f"Daemon is running (PID: {pid})")
                if LOG_FILE.exists():
                    print("\nRecent log entries:")
                    with open(LOG_FILE, "r") as f:
                        lines = f.readlines()
                        for line in lines[-10:]:
                            print(line.rstrip())
            except:
                print("Daemon is not running (stale lock file)")
        else:
            print("Daemon is not running")
        return
    
    if args.stop:
        if LOCK_FILE.exists():
            try:
                with open(LOCK_FILE, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, signal.SIGTERM)
                print(f"Sent stop signal to daemon (PID: {pid})")
            except Exception as e:
                print(f"Failed to stop daemon: {e}")
        else:
            print("Daemon is not running")
        return
    
    daemon = ImprovementDaemon()
    
    if args.once:
        daemon.execute_improvement()
    else:
        daemon.run()

if __name__ == "__main__":
    main()
