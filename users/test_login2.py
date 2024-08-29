import re
from playwright.sync_api import Playwright, sync_playwright, expect

from configuration import BASE_URL


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    if page.get_by_role("link", name="Cerrar Sesión").is_visible():
        page.get_by_role("link", name="Cerrar Sesión").click()
    page.get_by_role("link", name="Iniciar Sesión").click()
    page.get_by_label("Nombre de usuario").click()
    page.get_by_label("Nombre de usuario").fill("pepe")
    page.get_by_label("Contraseña").click()
    page.get_by_label("Contraseña").fill("1234")
    page.get_by_role("button", name="Iniciar Sesión").click()
    expect(page.get_by_text("Por favor, introduzca un")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)