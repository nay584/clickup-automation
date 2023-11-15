from fastapi import APIRouter, Request

taskWebhookRouter = APIRouter()


@taskWebhookRouter.post("/taskStatusUpdatedWebhook")
async def task_status_updated_webhook(request: Request):
    data = await request.json()
    print(data)
    return {}
