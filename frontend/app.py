import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="Banking Management System")
st.title("🏦 Banking Management System")

# -------------------------------
# CREATE ACCOUNT
# -------------------------------
st.subheader("➕ Create Account")

name = st.text_input("Name")
email = st.text_input("Email")
balance = st.number_input("Initial Balance", min_value=0.0)

if st.button("Create Account"):
    payload = {
        "name": name,
        "email": email,
        "balance": balance
    }

    response = requests.post(f"{API}/accounts", json=payload)

    if response.status_code in (200, 201):
        st.success("✅ Account created successfully")
        st.rerun()
    else:
        st.error("❌ Failed to create account")
        st.text(response.text)


st.divider()

# -------------------------------
# FETCH ACCOUNTS (SAFE)
# -------------------------------
st.subheader("📋 All Accounts")

try:
    response = requests.get(f"{API}/accounts")

    if response.status_code != 200:
        st.error("❌ Backend error")
        st.text(response.text)
        st.stop()

    accounts = response.json()

except requests.exceptions.RequestException as e:
    st.error("🚫 Backend not running")
    st.text(str(e))
    st.stop()

except ValueError:
    st.error("❌ Backend did not return JSON")
    st.text(response.text)
    st.stop()

if not accounts:
    st.info("No accounts found")
    st.stop()

st.table(accounts)

st.divider()

# -------------------------------
# UPDATE ACCOUNT
# -------------------------------
st.subheader("✏️ Update Account")

ids = [a["id"] for a in accounts]
uid = st.selectbox("Select Account ID", ids)

new_name = st.text_input("New Name")
new_email = st.text_input("New Email")

if st.button("Update Account"):
    response = requests.put(
        f"{API}/accounts/{uid}",
        json={"name": new_name, "email": new_email},
    )

    if response.status_code == 200:
        st.success("✅ Account updated")
        st.rerun()
    else:
        st.error(response.text)

st.divider()

# -------------------------------
# DELETE ACCOUNT
# -------------------------------
st.subheader("🗑 Delete Account")

did = st.selectbox("Select Account ID to Delete", ids)

if st.button("Delete Account"):
    response = requests.delete(f"{API}/accounts/{did}")

    if response.status_code == 200:
        st.success("✅ Account deleted")
        st.rerun()
    else:
        st.error(response.text)
