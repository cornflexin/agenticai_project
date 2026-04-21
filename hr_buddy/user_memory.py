"""
user_memory.py — Profile persistence for HR Policy Bot.
Tracks employee name, department, and query history so the agent
remembers context across turns even after the sliding window trims old messages.
"""

import json
import os
from datetime import datetime

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "profiles")
os.makedirs(PROFILES_DIR, exist_ok=True)

HR_TOPICS = [
    "Annual Leave and Casual Leave Policy",
    "Sick Leave and Medical Leave Policy",
    "Maternity and Paternity Leave",
    "Work From Home and Hybrid Work Policy",
    "Salary Structure, Payroll, and Payslip",
    "Performance Appraisal and Increment Policy",
    "Code of Conduct and Workplace Ethics",
    "Resignation, Notice Period, and Full and Final Settlement",
    "Reimbursements: Travel, Food, and Business Expenses",
    "Onboarding, Probation, and Confirmation",
    "Training, Learning, and Development Policy",
    "Grievance Redressal and HR Helpdesk",
]

DEFAULT_PROFILE = {
    "name": "",
    "user_id": "",
    "department": "",
    "created_at": "",
    "last_active": "",
    "questions_asked": 0,
    "sessions": 0,
    "recent_topics": [],
    "frequently_asked": {},
}


def _path(user_id: str) -> str:
    safe = "".join(c if c.isalnum() or c in "_-" else "_" for c in user_id)
    return os.path.join(PROFILES_DIR, f"{safe}.json")


def load_profile(user_id: str) -> dict:
    fpath = _path(user_id)
    if os.path.exists(fpath):
        try:
            with open(fpath, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    profile = dict(DEFAULT_PROFILE)
    profile["user_id"] = user_id
    profile["created_at"] = datetime.now().isoformat(timespec="seconds")
    return profile


def save_profile(profile: dict) -> None:
    profile["last_active"] = datetime.now().isoformat(timespec="seconds")
    try:
        with open(_path(profile.get("user_id", "unknown")), "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2)
    except OSError as e:
        print(f"[user_memory] Could not save profile: {e}")


def record_topic(profile: dict, topic: str) -> dict:
    recent = profile.get("recent_topics", [])
    if topic not in recent:
        recent.insert(0, topic)
    profile["recent_topics"] = recent[:5]
    freq = profile.get("frequently_asked", {})
    freq[topic] = freq.get(topic, 0) + 1
    profile["frequently_asked"] = freq
    profile["questions_asked"] = profile.get("questions_asked", 0) + 1
    return profile


def get_all_profiles() -> list:
    profiles = []
    for fname in os.listdir(PROFILES_DIR):
        if fname.endswith(".json"):
            try:
                with open(os.path.join(PROFILES_DIR, fname), encoding="utf-8") as f:
                    profiles.append(json.load(f))
            except (json.JSONDecodeError, OSError):
                pass
    return sorted(profiles, key=lambda p: p.get("last_active", ""), reverse=True)
