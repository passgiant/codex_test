from __future__ import annotations

"""Flask application providing a simple calculator web interface."""

from decimal import Decimal, InvalidOperation, getcontext
from typing import Callable, Dict, Tuple

from flask import Flask, render_template, request

# Configure decimal arithmetic for predictable rounding behaviour
getcontext().prec = 28

app = Flask(__name__)

Operation = Callable[[Decimal, Decimal], Decimal]


class CalculationError(Exception):
    """Raised when a calculation cannot be completed."""


def add(left: Decimal, right: Decimal) -> Decimal:
    return left + right


def subtract(left: Decimal, right: Decimal) -> Decimal:
    return left - right


def multiply(left: Decimal, right: Decimal) -> Decimal:
    return left * right


def divide(left: Decimal, right: Decimal) -> Decimal:
    if right == 0:
        raise CalculationError("0으로 나눌 수 없습니다.")
    return left / right


OPERATIONS: Dict[str, Tuple[str, Operation]] = {
    "add": ("덧셈", add),
    "subtract": ("뺄셈", subtract),
    "multiply": ("곱셈", multiply),
    "divide": ("나눗셈", divide),
}


def parse_decimal(value: str) -> Decimal:
    try:
        return Decimal(value)
    except InvalidOperation as exc:  # pragma: no cover - defensive branch
        raise CalculationError("숫자를 올바르게 입력해 주세요.") from exc


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    operand1 = request.form.get("operand1", "")
    operand2 = request.form.get("operand2", "")
    operation_key = request.form.get("operation", "add")

    if request.method == "POST":
        try:
            left = parse_decimal(operand1)
            right = parse_decimal(operand2)
            try:
                label, operation = OPERATIONS[operation_key]
            except KeyError as exc:  # pragma: no cover - defensive branch
                raise CalculationError("알 수 없는 연산입니다.") from exc

            result_value = operation(left, right)
            result = f"{label}: {result_value.normalize()}"
        except CalculationError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        operations=OPERATIONS,
        selected_operation=operation_key,
        operand1=operand1,
        operand2=operand2,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
