import streamlit as st
import streamlit.components.v1 as stc
import recommendation_module as rec

menu = ["Home","About"]

choice = st.sidebar.selectbox("Main Menu",menu)


if __name__ == "__main__":
    # Title for the App
    st.markdown(
        '''
        <div style="border: 2px solid blue; padding: 10px; background-color: white; border-radius: 5px;">
            <h1 style="margin: 0;color:black;">COURSE RECOMMENDATION SYSTEM</h1>
        </div>
        ''',
        unsafe_allow_html=True
    )
    st.write("")

    if choice == "Home":
        with st.form("search_form"):
            search_query = st.text_input("Enter your course",key ="search_input",placeholder="search for the course")

            col1,col2 = st.columns([5,1])

            with col1:
                st.write("")

            with col2:
                st.write("")
                search_button = st.form_submit_button("Search")
        
        recom_num = st.sidebar.number_input("Number of recommendation",3,10,5)
        st.subheader("Best Courses for you")
        if search_query is not None:
            result = rec.recommand(search_query,recom_num)

            # Getting the required features
            for row in result.iterrows():
                title = row[1][0]
                subscribers = row[1][3]
                price = row[1][2]
                link = row[1][1]

                 # Apply specific styling to the recommended course template
                st.markdown(
                    f'''
                    <div style="width: 70%; height: 100%; margin: 1px; padding: 5px; position: relative;  box-shadow: 0 0 15px 5px #ccc; background-color: #CF9FFF; border-left: 5px solid #6c6c6c;">
                        <h4 style="margin: 5px 0;">{title}</h4>
                        <p style="margin: 0; color: blue;">🧑‍🏫 Subscribers: {subscribers}</p>
                        <p style="margin: 0; color: blue;">💲 Price: {price}</p>
                        <div style="flex-grow: 1;"></div>
                        <div style="text-align: right;">
                        <p style="margin: 0; color: blue; display: inline-block;">
                        <a href="{link}" style="color: blue; text-decoration: none; background-color: rgb(49, 51, 63); color: white; padding: 5px; border-radius: 5px;">View Course</a>
                        </p>
                        </div>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )
                st.write("")


        
    # About the course
    elif choice == "About":
        st.subheader("About the App")

        st.markdown(
        """
        <div style="background-color:  #ADD8E6; padding: 20px; border-radius: 10px;">
        <h2>Welcome to the Course Recommendation App!</h2>
        <p>This app is designed to help you discover the perfect courses 
        on Udemy based on your interests and preferences.</p>

        <h3>Features:</h3>
        <ul>
        <li>Personalized Recommendations: Our advanced recommendation system analyzes your preferences and suggests courses tailored just for you.</li>
        <li>User-Friendly Interface: Our intuitive interface makes it easy to find and explore courses without any hassle.</li>
        </ul>

        <h3>How to Use:</h3>
        <ol>
        <li>Select Your Interests: Choose your preferred topics and areas of interest.</li>
        <li>Get Recommendations: Click the "Search" button to receive personalized course suggestions.</li>
        <li>Explore and Learn: Browse through the recommended courses using View Course button, read reviews, and start your learning journey!</li>
        </ol>

        <p>I hope you enjoy using the app and find it valuable for your learning goals.</p>

        <h3>About Me:</h3>
        <p>Name: Shreyas Sutar  Roll No: </p>
        </div>
        """,
        unsafe_allow_html=True
    )



    
    