#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
# -----------------------------------------------------------
# @file: Calculator.py
# @Author: Timotej Tabacek(xtabac03)
# @brief: Calculator application interface
# -----------------------------------------------------------
"""
Calculator application interface built with flet library.
supports basic operations and some special functions.
Part of the application is a custom-built math library with an interpreter package.
"""
# -----------------------------------------------------------
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

import math_lib
import math_interface
from evaluate_rec import Evaluate


# set constants
HEIGHT = 500
WIDTH = 360

HINT_MESSAGE = "Usage hint: \n" \
               "1. Use ^ for power,where the exponent is a positive integer e.g. 2^3 = 8\n" \
               "2. Use √ for root, e.g. 2√4 = 2\n" \
               "3. Use ! for factorial, e.g. 5! = 120\n" \
               "4. Use / for division, e.g. 4/2 = 2\n" \
               "5. Use * for multiplication, e.g. 4*2 = 8\n" \
               "6. Use - for subtraction, e.g. 4-2 = 2\n" \
               "7. Use + for addition, e.g. 4+2 = 6\n" \
               "Calculator supports parenthesis and the expression length is limited to screen size\n"
BG_GRADIENT = ft.LinearGradient(
    begin=ft.alignment.top_center,
    end=ft.alignment.bottom_center,
    stops=[0.0, 0.58, 1.0],
    colors=["#51108c", "#1c144f", "#100149"]
)
DISPLAY_GRADIENT = ft.LinearGradient(
    begin=ft.alignment.bottom_left,
    end=ft.alignment.top_right,
    colors=["#51108c", "#0c0038"]
)


class CalculatorApp(UserControl):
    """
    @brief: Calculator application.
    @param library: math library compliant with math interface
    @return: Calculator application
    """
    def __init__(self, library: math_interface.MathInterface):
        super().__init__()
        self.m = library
        self.result = None
        self.expression = None
        self.hint_states = ["Zero Division", "Syntax error", " 0"]

    def build(self):
        self.result = Text(value=" 0", width=300, text_align=ft.TextAlign.END, no_wrap=True, color=colors.WHITE, size=40)
        self.expression = Text(value="0", width=260, text_align=ft.TextAlign.END, no_wrap=True, color=colors.WHITE, size=20)

        result_field = Container(
            width=330,
            height=100,
            expand=1,
            opacity=0.8,
            padding=5,
            border_radius=10,
            gradient=DISPLAY_GRADIENT,
            content=Row(
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

        )

        numpad_parentheses = Row(
            controls=[
                        ElevatedButton(
                            text="(",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="(",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text=")",
                            bgcolor="#e28600",
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
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="AC",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="1/x",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="1/x",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="x!",
                            bgcolor=colors.WHITE24,
                            color=colors.WHITE,
                            data="!",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            content=ft.Icon(name=ft.icons.BACKSPACE, color=colors.WHITE),
                            bgcolor="#e28600",
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
                            bgcolor="#0c0038",
                            elevation=5,
                            color=colors.WHITE,
                            data="7",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="8",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="8",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="9",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="9",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="+",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="+",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="-",
                            bgcolor="#e28600",
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
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="4",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="5",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="5",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="6",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="6",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="*",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="*",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="/",
                            bgcolor="#e28600",
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
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="1",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="2",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="2",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="3",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="3",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="xⁿ",
                            bgcolor="#e28600",
                            color=colors.WHITE,
                            data="^",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text="√",
                            bgcolor="#e28600",
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
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data="0",
                            on_click=self.button_clicked,
                            expand=1,
                        ),
                        ElevatedButton(
                            text=".",
                            bgcolor="#0c0038",
                            color=colors.WHITE,
                            data=".",
                            on_click=self.button_clicked,
                            expand=2,
                        ),
                        ElevatedButton(
                            text="=",
                            bgcolor="#e28600",
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
            gradient=BG_GRADIENT,
            expand=True,
            padding=10,
            border_radius=ft.border_radius.all(10),
            content=Column(
                expand=True,
                controls=[result_field,
                          numpad]
            )
        )

        # application's root control (i.e. "view") containing all other controls
        return calculator

    def check_expression(self, expression: str) -> bool:
        """
        @brief: Checks if the expression is valid
        @param expression: The expression to check in string format
        @return: True if the expression is invalid, False otherwise
        """
        for char in expression:
            if char not in "0123456789.+-*/^√()!":
                return True
        lpar = expression.count("(")
        rpar = expression.count(")")
        if lpar != rpar:
            return True
        return False

    def parse_expression(self, expression):
        """
        @brief: Parses the expression and returns the result
        @param expression: The expression to parse in string format
        @return: The result of the expression in string format

        """
        try:
            evaluated_expression = Evaluate(expression, self.m).evaluate()
        except ZeroDivisionError:
            return "Zero Division"
        except ValueError:
            return "Syntax error"
        except AttributeError:
            return "Syntax error"

        result = str(evaluated_expression)
        if result == "None":
            result = "0"
        elif len(result) > 13:
            return '{:.2e}'.format(float(result))
        if result[-2:] == ".0":
            return result[:-2]
        else:
            return result

    def calculate_result(self):
        """
        @brief: Calculates the result of the expression

        Method used for setting the calculator's display information
        """
        self.result.value = self.result.value.strip()
        if self.check_expression(self.result.value):
            self.result.value = "Syntax error"
        else:
            self.expression.value = self.result.value
            self.result.value = self.parse_expression(self.result.value)
            self.expression.value += "="

    def button_clicked(self, e):
        """
        @brief: Button click event handler
        @param e: The event object
        """
        # delete all
        if e.control.data == "AC":
            self.result.value = " 0"

        # backspace
        elif e.control.data == "BACKSPACE":
            self.result.value = self.result.value[:-1]

        # evaluate expression
        elif e.control.data == "=":
            self.calculate_result()
        # inverse
        elif e.control.data == "1/x":
            if len(self.result.value) == 1:
                self.result.value = f"1/{self.result.value}"
            else:
                self.result.value = f"1/({self.result.value})"

        # base hint
        else:
            if self.result.value in self.hint_states:
                self.result.value = ""
            self.result.value += e.control.data
        self.update()

def main(page: Page):
    mathlib = math_lib.MathLib()
    # create application instance
    calc = CalculatorApp(mathlib)

    key_map = {
        "0": ")",
        "1": "!",
        "6": "^",
        "8": "*",
        "9": "(",
    }
    numpad_keys = ["Numpad 0", "Numpad 1", "Numpad 2", "Numpad 3", "Numpad 4", "Numpad 5", "Numpad 6", "Numpad 7",
                   "Numpad 8", "Numpad 9", "Numpad Add", "Numpad Decimal", "Numpad Divide",
                   "Numpad Equal", "Numpad Multiply", "Numpad Subtract"]
    numpad_map = {"Numpad 0": "0",
                  "Numpad 1": "1",
                  "Numpad 2": "2",
                  "Numpad 3": "3",
                  "Numpad 4": "4",
                  "Numpad 5": "5",
                  "Numpad 6": "6",
                  "Numpad 7": "7",
                  "Numpad 8": "8",
                  "Numpad 9": "9",
                  "Numpad Add": "+",
                  "Numpad Decimal": ".",
                  "Numpad Divide": "/",
                  "Numpad Equal": "=",
                  "Numpad Multiply": "*",
                  "Numpad Subtract": "-"}

    def set_page_params():
        """
        @brief: Sets the page parameters
        """
        page.window_width = WIDTH
        page.window_height = HEIGHT + 80
        page.window_min_width = WIDTH
        page.window_min_height = HEIGHT + 80
        page.window_max_width = WIDTH
        page.window_max_height = HEIGHT + 80

        page.window_maximizable = False
        page.window_minimizable = False

        page.update()
        page.bgcolor = "#0c0038"

        page.window_frameless = True
        page.window_title_bar_hidden = True
        page.window_title_bar_buttons_hidden = True
        page.window_opacity = 0.9

        page.window_left = 400
        page.window_top = 200
        page.update()

    def page_resize(e):
        page.window_width = WIDTH
        page.window_height = HEIGHT + 80
        page.update()

    def key_pressed(e):
        """
        @brief: Key press event handler
        @param e: The event object

        Method used for handling the key press events
        """
        hint_states = ["Zero Division", "Syntax error", " 0"]
        if e.key == "Escape":
            e.page.window_close()
        elif e.key == "Delete":
            calc.result.value = " 0"
        elif e.key == "Backspace":
            calc.result.value = calc.result.value[:-1]
        elif e.key == "Enter" or e.key == "Numpad Enter":
            calc.calculate_result()
        elif e.key in "0123456789-+^*()/!." or e.key in numpad_keys:
            if calc.result.value in hint_states:
                calc.result.value = ""
            if e.key in numpad_keys:
                calc.result.value += numpad_map[e.key]
            elif e.key in key_map.keys() and e.shift:
                calc.result.value += key_map[e.key]
            else:
                calc.result.value += e.key
        calc.update()

    # set page parameters
    set_page_params()
    page.on_resize = page_resize

    page.title = "Calculator"
    page.on_keyboard_event = key_pressed

    # add application's root control to the page
    # container for the title bar of the app
    page.add(Container(
        width=360,
        height=100,
        expand=1,
        opacity=0.8,
        padding=5,
        border_radius=10,
        bgcolor="#51108c",
        content=ft.WindowDragArea(
            Row(
                expand=1,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=255,
                controls=[
                    ft.IconButton(ft.icons.MENU_BOOK_ROUNDED,
                                  tooltip=HINT_MESSAGE,
                                  icon_color=colors.WHITE,
                                  ),
                    ft.IconButton(ft.icons.CLOSE, icon_color=colors.WHITE, on_click=lambda _: page.window_close()),
                ]
            )
        )
    ))
    page.add(calc)


ft.app(target=main)
