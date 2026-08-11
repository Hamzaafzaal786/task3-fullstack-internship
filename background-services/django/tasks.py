# For Django with Celery
from celery import shared_task
import time

@shared_task
def process_data(data):
    """Background task for Django"""
    print(f"Processing: {data}")
    time.sleep(5)  # Simulate long processing
    print(f"Completed: {data}")
    return f"Processed {data}"

# Sample scheduled task
@shared_task
def scheduled_cleanup():
    """This runs on a schedule (every hour)"""
    print("Running scheduled cleanup task...")
    return "Cleanup completed"

# Sample cron job
@shared_task
def daily_report():
    """Run daily at midnight"""
    print("Generating daily report...")
    return "Daily report generated"