import fastui.components as c
from fastui.events import GoToEvent, PageEvent
from fastui.forms import SelectOption

from config import ICON_SRC, GITHUB
from utils import expiration

def header(*, backend: str) -> c.AnyComponent:
  return c.Div(
    class_name="container mb-5",
    components=[
      c.Div(
        class_name="row",
        components=[
          c.Div(
            class_name="col-2",
            components=[
              c.Div(
                class_name="container",
                components=[
                  c.Div(
                    class_name="row",
                    components=[
                      c.Link(
                        class_name="col-3",
                        on_click=GoToEvent(url="/"),
                        active=True,
                        components=[
                          c.Image(
                            src=ICON_SRC,
                            width="155%"
                          )
                        ]
                      ),
                      c.Link(
                        class_name="col-5 text-decoration-none text-dark",
                        on_click=GoToEvent(url="/"),
                        active=True,
                        components=[c.Heading(text="Pastebin", level=2)]
                      )
                    ]
                  )
                ]
              )
            ]
          ),
          c.Div(
            class_name="col-1",
            components=[
              c.Button(
                class_name="btn btn-outline-success w-100",
                text="+ paste",
                on_click=GoToEvent(url="/")
              )
            ]
          ),
          c.Div(
            class_name="col-1",
            components=[
              c.Button(
                class_name="btn btn-outline-dark w-100",
                text="API",
                on_click=GoToEvent(url=backend + "/apidocs/")
              )
            ]
          ),
          c.Div(
            class_name="col-1",
            components=[
              c.Button(
                class_name="btn btn-outline-dark w-100",
                text="source",
                on_click=GoToEvent(url=GITHUB)
              )
            ]
          )
        ]
      )
    ]
  )


def index_section() -> c.AnyComponent:
  return c.Div(
    class_name="container",
    components=[
      c.Div(
        class_name="row mb-3",
        components=[
          c.Form(
            class_name="col-8",
            submit_url="/api/paste/",
            submit_trigger=PageEvent(name="create_paste"),
            footer=[],
            form_fields=[
              c.forms.FormFieldTextarea(
                class_name="form-control mb-3",
                name="text",
                title="New Paste",
                required=True,
                rows=12
              ),
              c.forms.FormFieldSelect(
                class_name="form-control",
                name="expires",
                title="Expires",
                display_mode="default",
                options=[
                  SelectOption(value=expiration.never, label="Never"),
                  SelectOption(value=expiration.ten_minutes, label="10 Minutes"),
                  SelectOption(value=expiration.hour, label="1 Hour"),
                  SelectOption(value=expiration.day, label="1 Day"),
                  SelectOption(value=expiration.week, label="1 Week"),
                  SelectOption(value=expiration.two_weeks, label="2 Weeks"),
                  SelectOption(value=expiration.month, label="1 Month"),
                  SelectOption(value=expiration.half_year, label="Half-year"),
                  SelectOption(value=expiration.year, label="1 year")
                ],
                initial=expiration.never
              )
            ]
          )
        ]
      ),
      c.Div(
        class_name="row",
        components=[
          c.Div(
            class_name="col-2",
            components=[
              c.Button(
                text="Create new paste",
                on_click=PageEvent(name="create_paste"),
                html_type="submit"
              )
            ]
          )
        ]
      )
    ]
  )


def paste_section(*, text: str) -> c.AnyComponent:
  return c.Div(
    class_name="container",
    components=[
      c.Div(
        class_name="row",
        components=[
          c.Div(
            class_name="col-8",
            components=[
              c.Code(class_name="form-control", text=text)
            ]
          )
        ]
      )
    ]
  )

def error_section(text: str, width: int = 3) -> c.AnyComponent:
    return c.Div(
    class_name="container",
    components=[
      c.Div(
        class_name="row justify-content-center",
        components=[
          c.Div(
            class_name=f"col-{width}",
            components=[
              c.Code(
                class_name="bg-danger-subtle rounded text-center",
                text=text
              )
            ]
          )
        ]
      )
    ]
  )
