#!/bin/bash
cd "$(dirname "$0")"
timeout 50m /home/roshan-yadav/.local/bin/agent "$(cat innovations_research.md)" --yolo
