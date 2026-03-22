#!/usr/bin/env python3
"""Fetch public LLM leaderboard data and write to data/leaderboard/.

Sources:
  - Arena AI (formerly LMSYS Chatbot Arena) via public API
  - HuggingFace Open LLM Leaderboard archived dataset
"""
import json
import os
from datetime import datetime, timezone

import requests

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'leaderboard')
os.makedirs(DATA_DIR, exist_ok=True)


def fetch_arena_ai(limit=20):
    """Fetch top models from Arena AI (formerly LMSYS Chatbot Arena)."""
    # Public API endpoint - no auth required
    url = 'https://api.wulong.dev/arena-ai-leaderboards/v1/leaderboard?name=text'
    entries = []
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            models = data.get('models', data) if isinstance(data, dict) else data
            if isinstance(models, list):
                for m in models[:limit]:
                    entries.append({
                        'model': m.get('model', m.get('name', 'Unknown')),
                        'vendor': m.get('vendor', m.get('organization', None)),
                        'elo_score': m.get('score', m.get('elo', None)),
                        'rank': m.get('rank', None),
                        'source': 'arena-ai',
                        'url': 'https://arena.ai/',
                    })
            print(f'[leaderboard] Fetched {len(entries)} models from Arena AI')
        else:
            print(f'[leaderboard] Arena AI returned {resp.status_code}')
    except Exception as e:
        print(f'[leaderboard] Error fetching Arena AI: {e}')
    return entries


def fetch_arena_ai_raw(limit=20):
    """Fallback: fetch from raw GitHub JSON of arena-ai-leaderboards."""
    url = 'https://raw.githubusercontent.com/oolong-tea-2026/arena-ai-leaderboards/main/data/latest.json'
    entries = []
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            # Navigate to text leaderboard
            if isinstance(data, dict):
                text_data = data.get('text', data)
                models = text_data.get('models', []) if isinstance(text_data, dict) else []
                for m in models[:limit]:
                    entries.append({
                        'model': m.get('model', m.get('name', 'Unknown')),
                        'vendor': m.get('vendor', None),
                        'elo_score': m.get('score', m.get('elo', None)),
                        'rank': m.get('rank', None),
                        'source': 'arena-ai-github',
                        'url': 'https://arena.ai/',
                    })
            print(f'[leaderboard] Fetched {len(entries)} models from Arena AI (GitHub raw)')
        else:
            print(f'[leaderboard] Arena AI GitHub raw returned {resp.status_code}')
    except Exception as e:
        print(f'[leaderboard] Error fetching Arena AI raw: {e}')
    return entries


def fetch_open_llm_leaderboard(limit=20):
    """Fetch from archived Open LLM Leaderboard dataset on HuggingFace."""
    # The leaderboard was archived in March 2025; dataset still accessible
    url = 'https://datasets-server.huggingface.co/rows?dataset=open-llm-leaderboard%2Fresults&config=default&split=train&offset=0&length=50'
    entries = []
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            rows = data.get('rows', [])
            for row in rows[:limit]:
                r = row.get('row', {})
                entries.append({
                    'model': r.get('model_name', r.get('fullname', 'Unknown')),
                    'average_score': r.get('average', r.get('Average', None)),
                    'parameters': r.get('params', r.get('#Params (B)', None)),
                    'source': 'open-llm-leaderboard-archived',
                    'url': f"https://huggingface.co/{r.get('model_name', r.get('fullname', ''))}",
                })
            print(f'[leaderboard] Fetched {len(entries)} models from Open LLM Leaderboard dataset')
        else:
            print(f'[leaderboard] Open LLM Leaderboard dataset returned {resp.status_code}, skipping')
    except Exception as e:
        print(f'[leaderboard] Error fetching Open LLM Leaderboard: {e}')
    return entries


def main():
    timestamp = datetime.now(timezone.utc).isoformat()
    all_entries = []

    # Arena AI (primary source - actively maintained)
    arena = fetch_arena_ai(limit=20)
    if not arena:
        # Fallback to raw GitHub data
        arena = fetch_arena_ai_raw(limit=20)
    all_entries.extend(arena)

    # Open LLM Leaderboard (archived but still useful reference data)
    open_llm = fetch_open_llm_leaderboard(limit=20)
    all_entries.extend(open_llm)

    if not all_entries:
        print('[leaderboard] WARNING: No leaderboard data fetched from any source')
        output = {'fetched_at': timestamp, 'sources': [], 'entries': []}
    else:
        sources = list(set(e.get('source', '') for e in all_entries))
        output = {
            'fetched_at': timestamp,
            'sources': sources,
            'total_entries': len(all_entries),
            'entries': all_entries,
        }

    output_path = os.path.join(DATA_DIR, 'llm_leaderboard.json')
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f'[leaderboard] Wrote {len(all_entries)} entries to {output_path}')

    summary_path = os.path.join(DATA_DIR, 'latest_summary.json')
    summary = {
        'fetched_at': timestamp,
        'arena_ai_count': len(arena),
        'open_llm_leaderboard_count': len(open_llm),
        'top_models': [e.get('model', '') for e in all_entries[:10]],
    }
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'[leaderboard] Wrote summary to {summary_path}')


if __name__ == '__main__':
    main()
