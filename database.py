import sqlite3
import hashlib
import requests


def log_in(password) -> str:
    pw_hash = hashlib.new("sha512")
    pw_hash.update(password.encode())
    pw_hex = pw_hash.hexdigest()
    return pw_hex


def get_connection():
    try:
        con = sqlite3.connect("./database.db")
        return con
    except Exception as e:
        print(e)
        raise e


def create_table(
    stmt: str,
    is_commitable: bool = False,
):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute(stmt)
    if is_commitable:
        con.commit()
    cursor.close()
    con.close()


def add(stmt: str, values: tuple = (), is_commitable: bool = False):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute(stmt, values)
    if is_commitable:
        con.commit()
    cursor.close()
    con.close()


def select(
    stmt: str,
    values: tuple = (),
    is_commitable: bool = False,
):
    con = get_connection()
    cursor = con.cursor()
    res = None
    cursor.execute(stmt, values)
    res = cursor.fetchall()
    if is_commitable:
        con.commit()
    cursor.close()
    con.close()
    return res


def find_coordinates(url: str, lon: float, lat: float, api_key: str) -> dict:
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
    }
    response = requests.get(url=url, params=params)
    return response.json()


def find_city(url: str, q: str, api_key: str) -> dict:
    params = {
        "q": q,
        "appid": api_key,
    }
    response = requests.get(url=url, params=params)
    return response.json()
