# Maxwell's demon of test enviroment

## page/page.py
```python
from j2htmx import Component


class Page(Component):
    ...
```

## page/i.html
```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
</head>
<body id="{{ component }}">
   {{ param_text }}
</body>
</html>
```

## main.py

```python
from aiohttp import web
from aiohttp.web_request import Request

from page.page import Page

routes = web.RouteTableDef()

app = web.Application()


async def root_page(request: Request) -> web.Response:
    return web.Response(text=await Page().finalize(
        param_text='Hi'
    ), headers={'Content-type': 'text/html; charset=utf-8'})


app.add_routes([
    web.get('/', root_page)
])

if __name__ == "__main__":
    web.run_app(app)
```
