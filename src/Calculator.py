import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    colors,
)
import pyparsing as pp
import math_lib
import math_interface
from evaluate_rec import Evaluate

HEIGHT = 500
WIDTH = 360


class CalculatorApp(UserControl):
    def __init__(self, library):
        super().__init__(library)
        self.m = library
        self.result = None
        self.expression = None
        self.operator_map = {
            "+": self.m.add,
            "-": self.m.subtract,
            "*": self.m.multiply,
            "/": self.m.divide,
            "^": self.m.power,
            "√": self.m.root,
            "1/x": self.m.reciprocal_func,
            "!x": self.m.factorial
        }

    def build(self):
        self.result = Text(value="0", color=colors.WHITE, size=40)
        self.expression = Text(value="0", color=colors.WHITE, size=20)

        result_field = Row(
            expand=1,
            alignment=ft.MainAxisAlignment.END,
            controls=[
                Column(
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                    controls=[
                        self.expression,
                        self.result,
                    ]
                )
            ]
        )

        numpad_parentheses = Row(
            controls=[
                        ElevatedButton(
                            text="(",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            data="(",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text=")",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            data=")",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                    ]
        )
        numpad_1 = Row(
            controls=[
                        ElevatedButton(
                            text="AC",
                            bgcolor=colors.BLUE_GREY_100,
                            color=colors.BLACK,
                            data="AC",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="1/x",
                            bgcolor=colors.BLUE_GREY_100,
                            color=colors.BLACK,
                            data="1/x",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="!x",
                            bgcolor=colors.BLUE_GREY_100,
                            color=colors.BLACK,
                            data="!",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            content=ft.Icon(name=ft.icons.BACKSPACE, color=colors.WHITE),
                            bgcolor=colors.ORANGE,
                            data="BACKSPACE",
                            on_click=self.button_clicked,
                            expand=2,
                        ),
                    ]
        )
        numpad_2 = Row(
            controls=[
                        ElevatedButton(
                            text="7",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="7",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="8",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="8",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="9",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="9",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="+",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            data="+",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="-",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            data="-",
                            on_click=self.button_clicked,
                            expand=1,
                        ),

                    ]
        )
        numpad_3 = Row(
            controls=[
                        ElevatedButton(
                            text="4",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="4",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="5",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="5",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="6",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="6",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="*",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            data="*",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="/",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            data="/",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                    ]
        )
        numpad_4 = Row(
            controls=[
                        ElevatedButton(
                            text="1",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="1",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="2",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="2",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="3",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="3",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="xⁿ",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            data="^",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="√",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            data="√",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                    ]
        )
        numpad_5 = Row(
            controls=[
                        ElevatedButton(
                            text="0",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="0",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text=".",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data=".",
                            on_click=self.button_clicked,
                            expand=2,
                        ),
                        ElevatedButton(
                            text="=",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            data="=",
                            on_click=self.button_clicked,
                            expand=2,
                        )
                    ]
        )

        numpad = Container(
            width=WIDTH,
            expand=2,
            content=Column(
                controls=[
                    numpad_parentheses,
                    numpad_1,
                    numpad_2,
                    numpad_3,
                    numpad_4,
                    numpad_5,
                ]
            )
        )

        calculator = Container(
            width=WIDTH,
            height=HEIGHT,
            bgcolor=colors.BLACK,
            padding=10,
            border_radius=ft.border_radius.all(10),
            content=Column(
                controls=[result_field,
                          numpad]
            )
        )

        # application's root control (i.e. "view") containing all other controls
        return calculator

    def parse_expression(self, expression):
        evaluated_expression = Evaluate(expression, self.m).evaluate()
        return evaluated_expression

    def button_clicked(self, e):
        if e.control.data == "AC":
            self.result.value = "0"
        elif e.control.data == "BACKSPACE":
            self.result.value = self.result.value[:-1]
        elif e.control.data == "=":
            self.expression.value = self.result.value
            self.result.value = self.parse_expression(self.result.value)
            self.expression.value += "="

        else:
            if self.result.value == "0":
                self.result.value = ""
            self.result.value += e.control.data
        self.update()


def set_page_params(page: Page):
    page.window_width = WIDTH
    page.window_height = HEIGHT - 10
    page.window_maximizable = False

    page.window_opacity = 0.9
#   page.window_title_bar_hidden = True
    page.window_left = 400
    page.window_top = 200


def main(page: Page):
    set_page_params(page)
    page.title = "Calc App"
    mathlib = math_lib.MathLib()
    # create application instance
    calc = CalculatorApp(mathlib)

    # add application's root control to the page
    page.add(calc)


ft.app(target=main)
