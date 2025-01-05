from src.design.first_page import first_page
from utils.local import checkOneTimeLogin
from src.design.dashboard_user import dashboard
from src.design.dashboard_spv import dashboard as spv_dashboard
import src.design.random

alreadyLogin = checkOneTimeLogin()
if not alreadyLogin: first_page()
else:
    role = alreadyLogin.get("role")
    if role  == "spv": spv_dashboard()
    else: dashboard()