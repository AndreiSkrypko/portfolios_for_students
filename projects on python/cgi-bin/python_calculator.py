#!/usr/bin/env python3
"""
CGI-скрипт, который получает данные из формы и возвращает результат вычисления.
Использует функции из calculator.py, чтобы не дублировать логику.
"""

import cgi
import cgitb
import json
import os
import sys


cgitb.enable()  # Показываем подробные ошибки в браузере (полезно при обучении)

# Добавляем корень проекта в PYTHONPATH, чтобы можно было импортировать calculator.py
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from calculator import calculate  # noqa: E402


def build_response():
    """Читает данные формы, вызывает calculate и формирует ответ."""
    form = cgi.FieldStorage()
    a_text = form.getfirst("a", "").strip()
    op = form.getfirst("op", "").strip()
    b_text = form.getfirst("b", "").strip()

    if not a_text or not b_text or not op:
        return {"success": False, "error": "Пожалуйста, заполните все поля."}

    result = calculate(a_text, op, b_text)
    if isinstance(result, str):
        return {"success": False, "error": result}

    return {
        "success": True,
        "result": result,
        "expression": f"{a_text} {op} {b_text}"
    }


if __name__ == "__main__":
    response = build_response()
    print("Content-Type: application/json; charset=utf-8\n")
    print(json.dumps(response, ensure_ascii=False))

