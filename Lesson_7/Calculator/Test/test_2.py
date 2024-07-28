from Lesson_7.Calculator.Pages.calcmainpage import CalcMain


def test_calculator_assert(chrome_browser):
    calcmain = CalcMain(chrome_browser)
    calcmain.insert_time()
    calcmain.click_buttons()
    assert "15" in calcmain.wait_button_txt()