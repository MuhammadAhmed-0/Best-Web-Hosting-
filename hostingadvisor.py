# Import necessary libraries
import streamlit as st
import pandas as pd
# Define options dictionary containing different categories and corresponding options with reasons, website links, and features
options = {
    "For beginners": [
        ("Bluehost", "Best choice with excellent support", "https://bluehost.sjv.io/aeducateweb",
         { "SSD Storage": "10 GB", "Free Domain": "Yes", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.5s"}),
        ("Hostinger", "Affordable and user-friendly ", "https://hostinger.sjv.io/aeducateweb",
         {"SSD Storage": "100 GB", "Free Domain": "Yes", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.2s"}),
        ("Interserver", "Great value for diverse hosting needs", "https://www.kqzyfj.com/click-100952366-11145908",
         {"SSD Storage": "Unlimited", "Free Domain": "No", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.8s"})
    ],
    "For budget-conscious users": [
        ("Hostinger", "Budget-friendly and Reliable with Free Domain", "https://hostinger.sjv.io/aeducateweb",
         {"Price": "$2.99/month", "SSD Storage": "100 GB", "Free Domain": "Yes", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.2s"}),
        ("Namecheap", "Affordable domain registration and hosting", "https://namecheap.pxf.io/aeducateweb",
         {"Price": "$2.91/month", "SSD Storage": "10 GB", "Free Domain": "Yes", "24/7 Support": "No", "Uptime": "99.9%", "Load Time": "1.6s"}),
        ("Interserver", "Competitive pricing with good features", "https://www.kqzyfj.com/click-100952366-11145908",
         {"Price": "$2.5/month", "SSD Storage": "Unlimited", "Free Domain": "No", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.8s"})
    ],
    "For performance": [
        ("Cloudways", "Managed cloud hosting with high performance", "https://shareasale.com/r.cfm?b=1080835&u=3355619&m=75038&urllink=&afftrack=",
         {"Price": "Varies", "SSD Storage": "Varies", "Free Domain": "No", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "0.5s"}),
        ("WP Engine", "Optimized for WordPress with top-notch speed", "https://shareasale.com/r.cfm?b=394686&u=3355619&m=41388&urllink=&afftrack=",
         {"Price": "$20.00/month", "SSD Storage": "10 GB", "Free Domain": "No", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.2s"}),
        ("Digital Ocean", "Developer-friendly cloud hosting", "https://digitalocean.pxf.io/aeducateweb",
         {"Price": "$4.00/month", "SSD Storage": "10 GB", "Free Domain": "No", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.0s"})
    ],
    "For e-commerce": [
        ("Bluehost", "E-commerce features with scalable hosting, Highly Recommended", "https://bluehost.sjv.io/aeducateweb",
         {"SSD Storage": "40 GB", "Free Domain": "Yes", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.5s"}),
        ("Hostgator", "Robust platform for online businesses", "https://partners.hostgator.com/aeducateweb",
         {"SSD Storage": "40GB", "Free Domain": "Yes", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.2s"})
    ],
    "For WordPress": [
        ("Bluehost", "Officially Recommended for WordPress", "https://bluehost.sjv.io/aeducateweb",
         {"Price": "$1.95/month", "SSD Storage": "10 GB", "Free Domain": "Yes", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.5s"}),
        ("WP Engine", "Specialized in high-performance WordPress hosting", "https://shareasale.com/r.cfm?b=394686&u=3355619&m=41388&urllink=&afftrack=",
         {"Price": "$20.00/month", "SSD Storage": "10 GB", "Free Domain": "No", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.2s"})
    ],
    "For Blogging": [
        ("Bluehost", "Highly Recommended for Blogging", "https://bluehost.sjv.io/aeducateweb",
         {"Price": "$1.95/month", "Storage": "10 GB", "Free Domain": "Yes", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.5s"}),
        ("Hostinger", "Great Alternative choice for bloggers", "https://hostinger.sjv.io/aeducateweb",
         {"Price": "$2.99/month", "Storage": "100 GB", "Free Domain": "No", "24/7 Support": "Yes", "Uptime": "99.9%", "Load Time": "1.2s"})
    ]
}

# Define function to display options based on the selected category
def display_options(category):
    if category in options:
        st.markdown(f"## Best Options {category}:")
        st.write("---------------------------------")
        for option, reason, link, features in options[category]:
            st.write(f"- **{option}:** {reason}")
            st.write("**Features:**")
            # Create a DataFrame from the features dictionary
            df = pd.DataFrame(features.items(), columns=["Feature", "Details"])
            # Display the DataFrame as a table
            st.table(df)
            if st.button(f"Visit {option}"):
                # Open the corresponding website in a new tab when the button is clicked
                st.markdown(f"<a href='{link}' target='_blank'>Click here to visit {option}</a>", unsafe_allow_html=True)
            st.write("---")
    else:
        st.error("Invalid category selection.")

# Main function to create the Streamlit UI
def main():
    # Set page title and description
    st.title("Web Hosting Advisor")
    st.markdown("""
    Welcome to the **Web Hosting Advisor!**
    
    Select a category from the dropdown menu to explore best hosting options.
    """)

    # Display category selection dropdown
    user_input = st.selectbox("**Select a category:**", list(options.keys()))

    # Check if a category is selected
    if user_input:
        # Display options based on the selected category
        display_options(user_input)

# Run the main function
if __name__ == "__main__":
    main()