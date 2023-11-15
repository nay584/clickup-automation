from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
import ssl

from webhookHandler.taskWebhookHandler import taskWebhookRouter
from webhookManager.webhookManager import webhookManagerRouter
from authentication.login import loginRouter

app = FastAPI()
app.include_router(loginRouter)
app.include_router(taskWebhookRouter)
app.include_router(webhookManagerRouter)

if __name__ == "__main__":
    load_dotenv()
    # Paths to your SSL certificate and private key files
    ssl_cert_path = os.getenv("SSL_CERT")
    ssl_key_path = os.getenv("SSL_KEY")

    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5001,
                # ssl_keyfile=ssl_key_path, ssl_certfile=ssl_cert_path
                )