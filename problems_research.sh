#!/bin/bash
cd "$(dirname "$0")"
timeout 10m /home/roshan-yadav/.local/bin/agent "$(cat problems_research.md)" --yolo
