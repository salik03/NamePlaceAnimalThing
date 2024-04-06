import streamlit as st
import random
import time

def generate_random_alphabet(used_alphabets):
    remaining_alphabets = [chr(i) for i in range(65, 91) if chr(i) not in used_alphabets]
    if remaining_alphabets:
        return random.choice(remaining_alphabets)
    else:
        return None

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def main():
    st.title("Name Place Animal Thing")
    
    used_alphabets = set()
    
    if 'used_alphabets' not in st.session_state:
        st.session_state.used_alphabets = set()
    
    if 'current_alphabet' not in st.session_state:
        st.session_state.current_alphabet = None
    
    if st.button("Generate Random Alphabet"):
        countdown_placeholder = st.empty()
        for i in range(5, 0, -1):
            countdown_placeholder.write(f"Generating in {i}...")
            time.sleep(1)
        countdown_placeholder.empty()
        
        new_alphabet = generate_random_alphabet(st.session_state.used_alphabets)
        if new_alphabet:
            st.session_state.current_alphabet = new_alphabet
            st.session_state.used_alphabets.add(new_alphabet)
    
    st.markdown("---")
    
    if st.session_state.current_alphabet:
        st.markdown(f"<h1 style='text-align: center; font-size: 272px; text-transform: uppercase;'>{st.session_state.current_alphabet}</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.write("Alphabets Left:")
    highlighted_alphabets = [chr(i) for i in range(65, 91) if chr(i) not in st.session_state.used_alphabets]
    st.write(" ".join(highlighted_alphabets))
    
    st.markdown("<footer style='text-align: center; margin-top: 50px;'>Made by Salik03<br>"
                "<a href='https://github.com/salik03' target='_blank'><img src='https://www.svgrepo.com/show/475654/github-color.svg' width='30' style='margin-right: 10px;'></a>"
                "<a href='https://www.linkedin.com/in/salik-uddin' target='_blank'><img src='https://cdn-icons-png.flaticon.com/512/3536/3536505.png ' width='30'></a></footer>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
