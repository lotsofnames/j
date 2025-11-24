import qrcode
import streamlit as st
st.title("QR Code")

content = st.text_input("Enter the content of qr code:",
        placeholder="qr code content here")
if st.button("Generate QR Code"):
    qrcode.make(content).save("qrcode.png")
    st.image("qrcode.png")
    with open("qrcode.png", "rb") as f:
        st.download_button(label="Download QR Code", data=f, file_name="qrcode.png",mime="image/png")