from fastapi import APIRouter, Depends
from pydantic import BaseModel
import requests
import os

from authentication.login import login_for_access_token, get_current_user

webhookManagerRouter = APIRouter(
    tags=["webhookManager"],
    dependencies=[Depends(get_current_user)]
)



@webhookManagerRouter.post("/getWebhooks")
async def get_webhooks(team_id: str):
    url = "https://api.clickup.com/api/v2/team/" + team_id + "/webhook"

    headers = {"Authorization": os.getenv("API_KEY")}

    response = requests.get(url, headers=headers)

    data = response.json()
    return data

class WebhookRegisterInfo(BaseModel):
    team_id: str
    endpoint: str
    event_types: list[str]
    space_id: str | None
    folder_id: str | None
    list_id: str | None
    task_id: str | None

@webhookManagerRouter.post("/setWebhook")
async def set_webhooks(webhookRegisterInfo: WebhookRegisterInfo):
    url = "https://api.clickup.com/api/v2/team/" + webhookRegisterInfo.team_id + "/webhook"

    payload = {
        "endpoint": webhookRegisterInfo.endpoint,
        "events": [ webhookRegisterInfo.event_types],
        "space_id": webhookRegisterInfo.space_id,
        "folder_id": webhookRegisterInfo.folder_id,
        "list_id": webhookRegisterInfo.list_id,
        "task_id": webhookRegisterInfo.task_id
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": os.getenv("API_KEY")
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    return data

class WebhookUpdateInfo(BaseModel):
    webhook_id: str
    endpoint: str
    event_types: list[str]
    space_id: str | None
    folder_id: str | None
    list_id: str | None
    task_id: str | None

@webhookManagerRouter.post("/updateWebhook")
async def update_webhook(webhookUpdateInfo: WebhookUpdateInfo):
    url = "https://api.clickup.com/api/v2/webhook/" + webhookUpdateInfo.webhook_id

    payload = {
        "endpoint": webhookUpdateInfo.endpoint,
        "events": webhookUpdateInfo.event_types,
        "status": "active"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": os.getenv("API_KEY")
    }

    response = requests.put(url, json=payload, headers=headers)

    data = response.json()
    return data

@webhookManagerRouter.post("/deleteWebhook")
async def delete_webhook(webhook_id: str):
    url = "https://api.clickup.com/api/v2/webhook/" + webhook_id

    headers = {"Authorization": os.getenv("API_KEY")}

    response = requests.delete(url, headers=headers)

    data = response.json()
    return data