class JSExecuteScript:
    """
    Пример написания JS скрипта
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    или ==
    browser.execute_script(JSExecuteScript.SCROLL_TO_ELEMENT_TOP_OF_SCREEN, button)
    """
    COLOR_RED = "arguments[0].style.setProperty('color', 'red', 'important');"
    BORDER_3PX_SOLID_RED = "arguments[0].style.setProperty('border', '3px', 'red', 'solid', 'important');"
    COLOR_RED_and_BORDER_3PX_SOLID_RED = "arguments[0].style.setProperty('color', 'red', 'important');arguments[0].style.setProperty('border', '3px', 'red', 'solid', 'important');"
    DISPLAY_NONE = "arguments[0].style.display = 'none';"
    DISPLAY_BLOCK = "arguments[0].style.display = 'block';"
    SCROLL_TO_ELEMENT_TOP_OF_SCREEN = "return arguments[0].scrollIntoView(true);"