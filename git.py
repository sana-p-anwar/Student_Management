import streamlit as st
from studentt_views import StudentManager
student_instance=StudentManager()
tab1, tab2=st.tabs(["ADD","VEIW"])
with tab1:
    st.title("Add New Student ")
    name=st.text_input("Enter Student Name")
    age=st.text_input("Enter Student Age")
    course=st.text_input("Enter Student Course")
    phone=st.text_input("Enter Phone Number")
    city=st.text_input("Enter City")
    if st.button("Add New Student"):# this is the post method
        student_instance.post(name=name, age=age, course=course, phone=phone, city=city)
        st.success("Student Added Successfully")

with tab2:
    st.title("View Student Details")

