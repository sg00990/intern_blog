import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    st.write("My name is Sarah Graddy and I completed my 12-week internship experience at Moser Consulting in fall 2023.")
    st.write("I graduated from Kennesaw State University in May 2023 with a degree in computer science and concentration in data science.")
    st.write("I worked in Data & Analytics where I learned all kinds of tools such as Power BI, Streamlit and Python.")

# add tools section
st.markdown("<h3 style='color: #6C97AE'>Tools I Learned</h3>", unsafe_allow_html=True)

# add chart showing tools used
df = pd.DataFrame({
    'Tools': ['Power BI', 'Tableau', 'Snowflake', 'Streamlit', 'JIRA', 'Python', 'SQL', 'Agile Methodology'],
    'Weeks Spent Learning': [8, 3, 6, 6, 5, 9, 4, 2]
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
     st.markdown("<h6 style='text-align: left'>Streamlit Apps</h5>",unsafe_allow_html=True)
     st.write("Using Streamlit, I was able to create applications for both internal and external use. I learned how to feed data to Snowflake databases, embed Power BI reports and create user-friendly surveys with conditional formatting.")

# add blog section
st.markdown("<h3 style='color: #6C97AE'>Moser Blog & Podcast</h3>", unsafe_allow_html=True)
st.write("I was given the opportunity to contribute to Moser's blog. The post can be found [here](https://www.moserit.com/blog/creating-a-web-app-with-snowflake-and-streamlit).")
st.write("Influenced by the Hands-On Essentials courses on Snowflake Academy, I created a tutorial on how to use Streamlit with Snowflake. The tasks included downloading a database from Snowflake's marketplace, connecting a GitHub repository to Streamlit and adding charts from queries.")
st.write("In addition to the blog post, I was also able to participate in a podcast about Streamlit.")

st.markdown("<h3 style='color: #6C97AE'>DataViz Quarterly Challenge</h3>", unsafe_allow_html=True)
st.write("During my time at Moser, I was presented with the opportunity to participate in our DataViz group's quarterly challenge! The goal was to create an interactive resume on either Tableau or Power BI, so I chose Tableau.")
st.write("Someone from HR judged each entry and I won! It was a lot of fun to participate in this challenge. Check my resume out [here](https://public.tableau.com/views/SarahGraddy-InteractiveResume/InteractiveResume?:language=en-US&:display_count=n&:origin=viz_share_link).")


st.markdown("<h3 style='color: #6C97AE'>Reflection</h3>", unsafe_allow_html=True)
st.write("Overall, I had a fantastic time at Moser Consulting! I learned a LOT in my 12 weeks there and was able to gain experience in both data analysis and data engineering.")
st.write("My mentor hosted weekly sessions on various topics such as SQL basics and DAX in Power BI. She also answered any questions I had and inspired me to participate in challenges like the Tableau interactive resume project!")
st.write("Though I was originally interested in data visualization, my manager encouraged me to try my hand at masking data in Python. It was more on the data engineering side of things, but I enjoyed it nonetheless. I am definitely motivated to take up projects like that in the future.")
st.write("I also had a great time learning Streamlit. It was super easy to use (especially because I know Python) and it was a nice blend of front-end and back-end development.")
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
