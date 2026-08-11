from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI(title="FastAPI Background Tasks")

def process_data(data: dict):
    """Background task function"""
    print(f"Processing: {data}")
    time.sleep(5)  # Simulate long processing
    print(f"Completed: {data}")

@app.get("/")
async def root():
    return {"message": "FastAPI Background Tasks Demo"}

@app.post("/process/{item_id}")
async def process_item(item_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_data, {"item": item_id})
    return {"message": f"Item {item_id} is being processed in background"}