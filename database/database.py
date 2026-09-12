import sqlite3
from pathlib import Path

DB_PATH = Path("data/researchbench.db")


def initialize_database():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            upload_date TEXT NOT NULL,
            text TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_memories (
            id TEXT PRIMARY KEY,
            type TEXT NOT NULL,
            question TEXT,
            answer TEXT,
            source_document_id TEXT,
            source_evidence TEXT,
            timestamp TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personal_memories (
            id TEXT PRIMARY KEY,
            type TEXT NOT NULL,
            content TEXT NOT NULL,
            linked_document_id TEXT,
            linked_protocol_id TEXT,
            timestamp TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS protocol_steps (
            id TEXT PRIMARY KEY,
            protocol_id TEXT NOT NULL,
            step_number INTEGER NOT NULL,
            title TEXT,
            instruction TEXT,
            completed INTEGER DEFAULT 0,
            timestamp TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS connections (
            id TEXT PRIMARY KEY,
            source_id TEXT NOT NULL,
            source_type TEXT NOT NULL,
            target_id TEXT NOT NULL,
            target_type TEXT NOT NULL,
            reason TEXT,
            timestamp TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id TEXT PRIMARY KEY,
            content TEXT NOT NULL,
            linked_document_id TEXT,
            linked_protocol_id TEXT,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
