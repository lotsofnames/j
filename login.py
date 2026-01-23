from edupage_api import Edupage
from edupage_api.exceptions import BadCredentialsException, CaptchaException
import streamlit as st

press = False
if "x" not in st.session_state:
    st.session_state.x = False


def send_message(ludia, text):

    edupage.send_message(ludia, text)


def posielanie(ludia, text):
    button = st.button("Poslat spravu")
    if button == True:
        send_message(ludia, text)


def text():
    students = []
    for student in edupage.get_students():

        if student in students:
            fico = 0
            while 1:
                if f"{student.name}{fico}" in students:
                    fico += 1
                else:
                    students.append(f"{student.name}{fico}")
                    break
        else:
            students.append(student.name)
    teachers = []
    for teacher in edupage.get_teachers():
        if teacher in teachers:
            premna = 0
            while 1:
                if f"{teacher.name}{premna}" in teachers:
                    premna += 1
                else:
                    teachers.append(f"{teacher.name}{premna}")
                    break
        else:
            teachers.append(teacher.name)
    option = st.selectbox(
        "Komu chcete poslat spravu?",
        (
            "Učitlia",
            "spolužiaci",
            "cela škola",
            "samostane  ucitelia",
            "samostane spolužiaci",
            "samostane cela škola",
        ),
    )
    if option == "samostane  ucitelia":
        option2 = st.multiselect("vyberte ludi ktorim chcete poslat spravu:", teachers)
        text = st.text_area("Text spravy")
        print(option2)
    elif option == "samostane spolužiaci":
        option2 = st.multiselect("vyberte ludi ktorim chcete poslat spravu:", students)
        text = st.text_area("Text spravy")
        posielanie(option2, text)
    elif option == "samostane cela škola":
        option2 = st.multiselect(
            "vyberte ludi ktorim chcete poslat spravu:", students + teachers
        )
    else:
        text = st.text_area("Text spravy")
    # st.write(option)
    # edupage.send_message(['matus'],"text")


edupage = Edupage()
st.subheader("Meno")
Username = st.text_input("Username")
st.subheader("Heslo")
Password = st.text_input("Password", type="password")
press = st.button("Prihlasit sa")
if press == True:
    st.session_state.x = True
if st.session_state.x == True:
    try:
        edupage.login(Username, Password, "sos-levice")
        st.write("Prihlasenie uspesne!")
        text()
    except BadCredentialsException:
        st.write("Nespravne meno alebo heslo!")
    except CaptchaException:
        st.write("try agen")
