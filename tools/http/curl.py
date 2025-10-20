"""
curl -X 'PATCH' \
  'http://127.0.0.1:8000/api/v1/users/d8c4399d-f3e6-4970-b6c1-1459b079925c' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI1LTEwLTE1VDA4OjA1OjM3Ljk4NjAwNiIsInVzZXJfaWQiOiJkOGM0Mzk5ZC1mM2U2LTQ5NzAtYjZjMS0xNDU5YjA3OTkyNWMifQ.-_9PAzAIQr8M10A1r7WtrUS3647slstnmABiSp6zzgY' \
  -H 'Content-Type: application/json' \
  -d '{

  "lastName": "string1"
}'"""


from httpx import Request, RequestNotRead, Client


from httpx import Request, RequestNotRead


def make_curl_from_request(request: Request) -> str:
    """
    Генерирует команду cURL из HTTP-запроса httpx.

    :param request: HTTP-запрос, из которого будет сформирована команда cURL.
    :return: Строка с командой cURL, содержащая метод запроса, URL, заголовки и тело (если есть).
    """
    # Создаем список с основной командой cURL, включая метод и URL
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    # Добавляем заголовки в формате -H "Header: Value"
    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    # Добавляем тело запроса, если оно есть (например, для POST, PUT)
    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    # Объединяем части с переносами строк, исключая завершающий `\`
    return " \\\n  ".join(result)


# def print_request(request: Request):
#     print(f"Выполняем запрос {request.method}")
#
# client = Client(event_hooks={"request": [print_request]})
# client.get("http://127.0.0.1:8000/api/v1/users")
# client.post("http://127.0.0.1:8000/api/v1/users")
# client.patch("http://127.0.0.1:8000/api/v1/users")
# client.delete("http://127.0.0.1:8000/api/v1/users")
#
