import streamlit as st

st.markdown("## Image Embedded Example")
st.image("https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80")

st.markdown("## Image credit: ")
st.markdown("""
Creator: User Neil Iris (@neil_ingham) ......
""")

st.markdown('## Video Embedded example')
st.video("https://www.youtube.com/watch?v=MsXdUtlDVhk")

st.markdown("## Video credit:")
st.markdown("Creator Lady Gaga ")

st.markdown('## Audio File Embedded example')
st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg")

st.markdown("## Audio credit:")
st.markdown("Creator Chopin-valse-opus64 ")