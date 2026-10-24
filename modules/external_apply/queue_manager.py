import json
import os
import threading
from datetime import datetime

QUEUE_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "external_jobs_queue.json")
_lock = threading.Lock()


def _load_queue() -> list[dict]:
    if not os.path.exists(QUEUE_FILE):
        return []
    try:
        with open(QUEUE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []


def _save_queue(queue: list[dict]) -> None:
    temp_file = QUEUE_FILE + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2, ensure_ascii=False)
    os.replace(temp_file, QUEUE_FILE)


def enqueue_external_job(job_id: str, title: str, company: str, job_link: str, external_link: str) -> bool:
    """Add a discovered external job to the queue if not already present."""
    if not external_link or not external_link.startswith("http"):
        return False

    with _lock:
        queue = _load_queue()
        for item in queue:
            if item.get("job_id") == job_id or item.get("external_link") == external_link:
                return False  # Already queued

        entry = {
            "job_id": str(job_id),
            "title": str(title),
            "company": str(company),
            "job_link": str(job_link),
            "external_link": str(external_link),
            "discovered_at": datetime.now().isoformat(),
            "status": "pending",  # pending | in_progress | applied | failed | needs_human
            "attempts": 0,
            "last_error": None,
            "applied_at": None,
        }
        queue.append(entry)
        _save_queue(queue)
        return True


def get_pending_jobs() -> list[dict]:
    """Retrieve all jobs that are still pending or need human action."""
    with _lock:
        queue = _load_queue()
        return [j for j in queue if j.get("status") in ("pending", "needs_human")]


def update_job_status(job_id: str, status: str, error: str | None = None) -> None:
    """Update status of a specific job in the queue."""
    with _lock:
        queue = _load_queue()
        for j in queue:
            if j.get("job_id") == str(job_id):
                j["status"] = status
                j["attempts"] = j.get("attempts", 0) + 1
                if error:
                    j["last_error"] = str(error)
                if status == "applied":
                    j["applied_at"] = datetime.now().isoformat()
                break
        _save_queue(queue)


def get_queue_stats() -> dict:
    with _lock:
        queue = _load_queue()
        stats = {"total": len(queue), "pending": 0, "applied": 0, "failed": 0, "needs_human": 0}
        for j in queue:
            s = j.get("status", "pending")
            stats[s] = stats.get(s, 0) + 1
        return stats
