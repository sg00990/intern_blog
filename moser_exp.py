import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit_survey as ss

survey = ss.StreamlitSurvey("survey")
pages = survey.pages(1, on_submit=lambda: st.success("success"))

pages.submit_button = lambda pages: st.button("Soumettre", type="primary", use_container_width=True)

with pages:
    if pages.current == 0:
        survey.text_area("test")

# set graph size
plt.rcParams["figure.figsize"] = (10,5)

# add Moser logo
col1, col2, col3 = st.columns(3)
with col1:
    st.image("MOS-Logo_RGB.png")
with col2:
    st.write(' ')
with col3:
    st.write(' ')

# add centered title
st.markdown("<h1 style='text-align: center'>My Internship Experience at Moser Consulting</h1>", unsafe_allow_html=True)

# add 'about me' section
st.markdown("<h3 style='color: #6C97AE'>About Me</h3>", unsafe_allow_html=True)

# add photo and text
col4, col5 = st.columns(2)
with col4:
    st.image("image002.jpg")
with col5:
    st.write("Hello!")
    st.write("My name is Sarah Graddy and I completed my 8-week internship experience at Moser Consulting in fall 2023.")
    st.write("I graduated from Kennesaw State University in May 2023 with a degree in computer science and concentration in data science.")
    st.write("I worked in Data & Analytics where I learned all kinds of tools such as Power BI, Streamlit and Python.")

# add tools section
st.markdown("<h3 style='color: #6C97AE'>Tools I Learned</h3>", unsafe_allow_html=True)

# add chart showing tools used
df = pd.DataFrame({
    'Tools': ['Power BI', 'Tableau', 'Snowflake', 'Streamlit', 'JIRA', 'Python', 'SQL', 'Agile Methodology'],
    'Weeks Spent Learning': [6, 3, 3, 2, 5, 3, 3, 2]
})
color_code = ['#6C97AE', '#99C130']
bar = df.plot(x = "Tools", y = "Weeks Spent Learning", kind="bar", color=color_code)
font = {'size': 12, 'weight': 'bold'}
bar.set_xlabel("Tools", fontdict=font)
bar = bar.figure
st.pyplot(bar)

# add project section
st.markdown("<h3 style='color: #6C97AE'>Projects</h3>", unsafe_allow_html=True)
col6, col7, col8 = st.columns(3)
with col6:
    st.markdown("<h6 style='text-align: left'>Power BI Demo Reports</h5>", unsafe_allow_html=True)
    st.write("I spent most of my internship creating demo reports in Power BI that Moser can show to existing and future clients. I learned how to create parameters, bookmarks and dynamic axes.")
with col7:
     st.markdown("<h6 style='text-align: left'>Data Masking in Python</h5>",unsafe_allow_html=True)
     st.write("I created a Python file that can be used to mask sensitive information in data such as names and IDs. It reads in an Excel workbook and utilizes libraries such as Faker and FastDataMask.")
with col8:
     st.markdown("<h6 style='text-align: left'>Interactive Resume in Tableau</h5>",unsafe_allow_html=True)
     st.write("Using Tableau and Google Sheets, I was able to create an interactive resume. I included different charts to display experiences and added clickable links.")

# add blog section
st.markdown("<h3 style='color: #6C97AE'>Moser Blog</h3>", unsafe_allow_html=True)
st.write("I was given the opportunity to contribute to Moser's blog. The homepage can be found here: https://www.moserit.com/blog")
st.write("Influenced by the Hands-On Essentials courses on Snowflake Academy, I created a tutorial on how to use Streamlit with Snowflake. The tasks included downloading a database from Snowflake's marketplace, connecting a GitHub repository to Streamlit and adding charts from queries.")

st.markdown("<h3 style='color: #6C97AE'>Reflection</h3>", unsafe_allow_html=True)
st.write("Overall, I had a fantastic time at Moser Consulting! I learned a LOT in my 8 weeks there and was able to gain experience in both data analysis and data engineering.")
st.write("My mentor hosted weekly sessions on various topics such as SQL basics and DAX in Power BI. She also answered any questions I had and inspired me to participate in challenges like the Tableau interactive resume project!")
st.write("Though I was originally interested in data visualization, my manager encouraged me to try my hand at masking data in Python. It was more on the data engineering side of things, but I enjoyed it nonetheless. I am definitely motivated to take up projects like that in the future.")
st.write("One of the highlights of my internship was discovering the 'Moser Pets' page on Slack. It brightened my day whenever I saw a cute cat or dog!")

# line break
st.markdown("""---""")

# add social links
col9, col10, col11 = st.columns(3)
with col9:
    div1, div2, div3 = st.columns(3)
    with div2:
     st.image('linkedin.png', width = 50)
     st.write('[LinkedIn](https://www.linkedin.com/in/sarah-graddy/)')
with col10:
    div4, div5, div6 = st.columns(3)
    with div5:
        st.image('github.png', width = 50)
        st.write('[GitHub](https://github.com/sg00990)')
with col11:
    div7, div8, div9 = st.columns(3)
    with div8:
        st.image('tableau.png', width = 50)
        st.write('[Tableau](https://public.tableau.com/app/profile/sarah.graddy)')
