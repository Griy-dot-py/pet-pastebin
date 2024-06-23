from typing import Annotated

import components as c
from aiohttp import ClientSession
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui.components import FireEvent, Page
from fastui.events import GoToEvent
from fastui.forms import fastui_form
from forms import NewPasteForm

from config import BACKEND_BASE_URL

app = FastAPI()


@app.get("/api/error", response_model=FastUI, response_model_exclude_none=True)
def error_page() -> list[AnyComponent]:
    err_text = (
        "An error occured on the server. We are trying to fix it as soon as possible"
    )
    return [
        Page(
            components=[
                c.header(backend=BACKEND_BASE_URL),
                c.error_section(
                    text=err_text,
                    width=8,
                ),
            ]
        )
    ]


@app.post("/api/paste/")
async def post_paste(form: Annotated[NewPasteForm, fastui_form(NewPasteForm)]):
    async with ClientSession(BACKEND_BASE_URL) as session:
        async with session.post(
            "/api/paste/", json=form.model_dump(exclude_none=True)
        ) as resp:
            if resp.status == 201:
                hash = (await resp.json())["hash"]
            else:
                print((await resp.content.read()).decode())
                return [FireEvent(event=GoToEvent(url="/error"))]

    return [FireEvent(event=GoToEvent(url=f"/paste/{hash}"))]


@app.get("/api/paste/{hash}", response_model=FastUI, response_model_exclude_none=True)
async def get_paste(hash: str) -> list[AnyComponent]:
    components = [c.header(backend=BACKEND_BASE_URL)]

    async with ClientSession(BACKEND_BASE_URL) as session:
        async with session.get(f"/api/paste/{hash}") as resp:
            if resp.status == 404:
                components.append(c.error_section(text="404 Paste not found :("))
            elif resp.status == 200:
                components.append(c.paste_section(text=(await resp.json())["text"]))
            else:
                print((await resp.content.read()).decode())
                return [FireEvent(event=GoToEvent(url="/error"))]

    return [Page(components=components)]


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def index() -> list[AnyComponent]:
    return [Page(components=[c.header(backend=BACKEND_BASE_URL), c.index_section()])]


@app.get("/{path:path}")
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="Pastebin"))
