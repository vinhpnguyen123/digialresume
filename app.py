import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests


selected = option_menu(
    menu_title= None,
    options=["About", "Portfolio", "Contact"],
    icons=["house", "book", "envolope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)


if selected == "About":
    st.title("About Me")
    avatar_col, intro_col = st.columns(2,  gap="large")

    with avatar_col:
        image_path ='/Users/vinhnguyen/Downloads/meo.jpg'
        st.image(image_path, width=300)

    with intro_col:
        st.markdown('<h1 style="color: white;">Who am I?</h1>', unsafe_allow_html=True)
        st.write("")
        st.write("Study at [High School for the Gifted](https://ptnk.edu.vn/)")
        st.write("")
        st.write("I am a student")
        st.markdown("---")
        cv_path = '/Users/vinhnguyen/Downloads/Quang Vinh _CV.docx.pdf'

        
        # Open the CV file in binary mode
        with open(cv_path, "rb") as file:
                btn = st.download_button(
                    label="Download CV",
                    data=file,
                    file_name="Quang Vinh _CV.docx.pdf",
                    mime="application/pdf"
                )
        st.write("✉️"," ","nguyenphamquangvinh1210@gmail.com")


        icon_col1, icon_col2, icon_col3=  st.columns(3, gap="small")

            # Facebook icon
        with icon_col1:
            st.markdown("""
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
                """, unsafe_allow_html=True)

            # HTML and CSS for the Facebook link with icon
            facebook_link = """
                <style>
                .facebook-icon {
                    color: #3b5998;
                    font-size: 30px;
                    margin-right: 10px;
                    text-decoration: none;
                
                }
                .facebook-icon:hover {
                    color: #2d4373;
                }
                </style>
                <a href="https://www.facebook.com/kriknaknoe" target="_blank" class="facebook-icon">
                    <i class="fab fa-facebook"></i>
                </a>
                <a href="https://www.facebook.com/kriknaknoe" target="_blank" class="facebook-link"></a>

            """

            # Display the Facebook link with icon
            st.markdown(facebook_link, unsafe_allow_html=True)
        with icon_col2: 
            st.markdown("""
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
                """, unsafe_allow_html=True)

            # HTML and CSS for the Facebook link with icon
            Github_link = """
                <style>
                .github-icon {
                    color: #2b3137;
                    font-size: 30px;
                    margin-right: 10px;
                    text-decoration: none;

                }
                .github-icon:hover {
                    color: #2d4373;
                }
                </style>
                <a href="https://github.com/vinhpnguyen123" target="_blank" class="github-icon">
                    <i class="fab fa-github"></i>
                </a>

            """

            # Display the Facebook link with icon
            st.markdown(Github_link, unsafe_allow_html=True)
            
        with icon_col3: 
            st.markdown("""
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
                """, unsafe_allow_html=True)

            # HTML and CSS for the Facebook link with icon
            Linkedin_link = """
                <style>
                
                .Linkedin-icon {
                    color: #0077B5;
                    font-size: 30px;
                    margin-right: 10px;
                    text-decoration: none;

                }
                .Linkedin-icon:hover {
                    color: #2d4373;
                }
                </style>
                <a href="https://www.linkedin.com/in/vinh-undefined-141aa1250/" target="_blank" class="Linkedin-icon">
                    <i class="fa-brands fa-linkedin-in"></i>

                </a>

            """

            # Display the Facebook link with icon
            st.markdown(Linkedin_link, unsafe_allow_html=True)
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

    python = load_lottieurl("https://lottie.host/493ce4ce-7e7f-495d-ad1d-1096b26be2a7/1nS91EtizC.json")
    git = load_lottieurl("https://lottie.host/286708e0-8dc2-4dd9-ab2f-b900172154d9/yjsDNzdvdH.json")
    tf = load_lottieurl("https://lottie.host/d453722a-c5ff-479f-abfb-5ea16c87ee48/MrdGuoYDzU.json")
    html = load_lottieurl("https://lottie.host/ce0c8c60-4223-4093-8e50-b4a9cd10396d/xx2d5BvSGG.json")
    css = load_lottieurl("https://lottie.host/755259ad-ac4d-4808-97f4-77521a6c81a3/5gEV6sSxEO.json")
    st.write('\n')
    with st.container():
        st.subheader('Programming Language')
        st.write("---")
        col1, col2, col3,col4, col5= st.columns([1, 1, 1, 1, 1])
        with col1:
            st_lottie(python, height=90,width=90, key="python", speed=2.5)
        with col2:
            st_lottie(git, height=90,width=90, key="git", speed=2.5)
        with col3:
            st_lottie(tf, height=90,width=90, key="tf", speed=2.5)
        with col4:
            st_lottie(html, height=90,width=90, key="ht", speed=2.5)
        with col5:
            st_lottie(css, height=90,width=90, key="cs", speed=2.5)
if selected == "Portfolio":
    st.title("My latest work and portfolio")
    tab1, tab2, tab3 = st.tabs(["Shoes category", "Personal info", "Sign in Page"])
    
    with tab1:
        st.header("Shoes")
        st.video("/Users/vinhnguyen/Desktop/Screen Recording 2024-07-12 at 21.54.50.mov")

    with tab2:
        st.header("Personal web")
        st.video("/Users/vinhnguyen/Desktop/Screen Recording 2024-07-12 at 21.53.37.mov")

    with tab3:
        st.header("Sign in page ")
        st.video("/Users/vinhnguyen/Desktop/Screen Recording 2024-07-12 at 21.58.14.mov")
    
    st.write("---")
    st.title("Intern at Tri Viet english center")
    st.write("---")
    st.title("Intern at Codezx")
    st.write("---")
    st.title("blabla")


if selected == "Contact":
    divide_col1, divide_col2 = st.columns(2, gap="large")
    with divide_col1:
        st.header("Leave a message")

    # Create the contact form
        with st.form(key='contact_form'):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            
            # Create a submit button
            submit_button = st.form_submit_button(label='Submit')

        # Handle the form submission
        if submit_button:
            st.write("Thank you for reaching out!")
    with divide_col2:
        st.header("Contact Me")
        col1, col2, col3=  st.columns(3, gap="large")
            # Facebook icon
        with col1:
            st.markdown("""
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
                """, unsafe_allow_html=True)

            # HTML and CSS for the Facebook link with icon
            facebook_link = """
                <style>
                .facebook-icon {
                    color: #3b5998;
                    font-size: 30px;
                    margin-right: 10px;
                    text-decoration: none;
                    margin-left: 10px;
                }
                .facebook-icon:hover {
                    color: #2d4373;
                }
                </style>
                <a href="https://www.facebook.com/kriknaknoe" target="_blank" class="facebook-icon">
                    <i class="fab fa-facebook"></i>
                </a>
                <a href="https://www.facebook.com/kriknaknoe" target="_blank" class="facebook-link"></a>

            """

            # Display the Facebook link with icon
            st.markdown(facebook_link, unsafe_allow_html=True)
        with col2: 
            st.markdown("""
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
                """, unsafe_allow_html=True)

            # HTML and CSS for the Facebook link with icon
            Github_link = """
                <style>
                .github-icon {
                    color: #2b3137;
                    font-size: 30px;
                    margin-right: 10px;
                    text-decoration: none;
                    margin-left: 10px;
                }
                .github-icon:hover {
                    color: #2d4373;
                }
                </style>
                <a href="https://github.com/vinhpnguyen123" target="_blank" class="github-icon">
                    <i class="fab fa-github"></i>
                </a>

            """

            # Display the Facebook link with icon
            st.markdown(Github_link, unsafe_allow_html=True)
            
        with col3: 
            st.markdown("""
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
                """, unsafe_allow_html=True)

            # HTML and CSS for the Facebook link with icon
            Linkedin_link = """
                <style>
                
                .Linkedin-icon {
                    color: #0077B5;
                    font-size: 30px;
                    margin-right: 10px;
                    text-decoration: none;
                    margin-left: 10px;
                }
                .Linkedin-icon:hover {
                    color: #2d4373;
                }
                </style>
                <a href="https://www.linkedin.com/in/vinh-undefined-141aa1250/" target="_blank" class="Linkedin-icon">
                    <i class="fa-brands fa-linkedin-in"></i>

                </a>

            """

            # Display the Facebook link with icon
            st.markdown(Linkedin_link, unsafe_allow_html=True)
        st.write("")
        st.write("")
        contact1,contact2 = st.columns(2, gap="small")
        with contact1:
            container = st.container(border=True)
            container.write("Contact")
            container.write("0942985751")
        with contact2:
            container = st.container(border=True)
            container.write("Email")
            container.write("nguyenphamquangvinh1210@gmail.com")
        cv_path = '/Users/vinhnguyen/Downloads/Quang Vinh _CV.docx.pdf'

        
        # Open the CV file in binary mode
        with open(cv_path, "rb") as file:
                btn = st.download_button(
                    label="Download CV",
                    data=file,
                    file_name="Quang Vinh _CV.docx.pdf",
                    mime="application/pdf"
                )       


