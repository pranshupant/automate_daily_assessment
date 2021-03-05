#!/bin/bash
echo "Daily Automation"
pwd
source /home/ppant/anaconda3/bin/activate
conda run -n pytorch_env python3 daily_assessment.py >> /tmp/file
pwd
echo "Assessment Complete"
