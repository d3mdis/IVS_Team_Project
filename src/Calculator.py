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
import pyparsing
import math_lib
import math_interface

HEIGHT = 500
WIDTH = 360


class CalculatorApp(UserControl):
    def __init__(self, math_library):
        super().__init__(math_library)

    def parse_expression(self, expression):
        pass

    def build(self):
        result = Text(value="0", color=colors.WHITE, size=40)
        result_field = Row(controls=[result],
                           expand=1,
                           alignment=ft.MainAxisAlignment.END)
        numpad_parentheses = Row(
            controls=[
                        ElevatedButton(
                            text="(",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text=")",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
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
                            expand=1,
                        ),
                        ElevatedButton(
                            text="1/x",
                            bgcolor=colors.BLUE_GREY_100,
                            color=colors.BLACK,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="!x",
                            bgcolor=colors.BLUE_GREY_100,
                            color=colors.BLACK,
                            expand=1,
                        ),
                        ElevatedButton(
                            content=ft.Icon(name=ft.icons.BACKSPACE, color=colors.WHITE),
                            bgcolor=colors.ORANGE,
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
                            expand=1,
                        ),
                        ElevatedButton(
                            text="8",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="9",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="+",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="-",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
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
                            expand=1,
                        ),
                        ElevatedButton(
                            text="5",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="6",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="*",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="/",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
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
                            expand=1,
                        ),
                        ElevatedButton(
                            text="2",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="3",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="xⁿ",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="√",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
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
                            expand=1,
                        ),
                        ElevatedButton(
                            text=".",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            expand=2,
                        ),
                        ElevatedButton(
                            text="=",
                            bgcolor=colors.ORANGE,
                            color=colors.WHITE,
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
        #numpad.alignment = ft.alignment.center
        # application's root control (i.e. "view") containing all other controls
        return calculator


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
