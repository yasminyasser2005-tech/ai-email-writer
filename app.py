import streamlit as st
from email_writer import generate_reply

st.set_page_config(page_title="AI Email Writer", page_icon="✉️")
st.title("✉️ AI Customer Complaint → Professional Reply")

company_name = st.text_input("Company name", value="Our Company")
tone = st.selectbox(
    "Reply tone",
    ["professional and empathetic", "warm and casual", "formal and concise"]
)

complaint = st.text_area("Paste the customer complaint here", height=150)

if st.button("Generate Reply") and complaint.strip():
    with st.spinner("Writing reply..."):
        reply = generate_reply(complaint, tone=tone, company_name=company_name)
    st.subheader("Generated Reply")
    st.write(reply)
    st.text_area("Copy this reply:", value=reply, height=200)