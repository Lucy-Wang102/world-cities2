"""
Home.py — Streamlit main entry page for a multipage app.

Place this file at the repository root. Put your pages (including app.py) inside
the `pages/` folder. Run the app with:

    streamlit run Home.py

The "Go to App" button attempts to navigate to the page by setting the
Streamlit query parameter `page`. If your pages/app.py uses a different visible
page title than "App", update the PAGE_NAME variable below to match that title.
"""

import streamlit as st

# Page config
st.set_page_config(page_title="World Cities — Home", page_icon="🏙️")

# The visible page name used by Streamlit's multipage system.
# By default Streamlit shows the page title derived from the target script.
# If your pages/app.py sets a title (via st.set_page_config or the file name),
# update this variable to match the exact page title shown in the pages sidebar.
PAGE_NAME = "App"  # <-- Change this to the page title shown for pages/app.py if needed

# Page content
st.title("World Cities — Home")
st.markdown(
    """
    Welcome! This is the Home page for the Streamlit multipage app.
    Use the button below to open the App page (pages/app.py).
    """
)

st.write("Quick links:")
col1, col2 = st.columns([1, 3])
with col1:
    if st.button("Go to App"):
        # Set the page query parameter to request the target page and rerun.
        # Streamlit will open the matching page if PAGE_NAME matches the page's title.
        st.experimental_set_query_params(page=PAGE_NAME)
        st.experimental_rerun()
with col2:
    st.markdown(
        f"- Or open the page manually from the left Pages menu.\n"
        f"- Fallback link: [Open '{PAGE_NAME}' page](/?page={PAGE_NAME})"
    )

st.divider()
st.info(
    "Notes: If the button doesn't navigate, confirm the page's visible title in "
    "the Pages sidebar and set PAGE_NAME to that exact value (case-sensitive)."
)
