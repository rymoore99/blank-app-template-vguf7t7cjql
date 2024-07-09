
import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("⚾ Acme Card Co 🏈")
pn = st.text_input('Search for a card')


@st.cache_resource
def init_connection():
    conn = st.connection("postgresql", type="sql")

    return conn

conn = init_connection()

if len(pn) > 0:
    card = pn
    df = conn.query(f'select *, SIMILARITY(search_string, \'{card}\') as sim from "ACMETRADING_checklist_pre1970" where SIMILARITY(search_string, \'{card}\') > 0.1 ORDER BY sim DESC limit 20', ttl="10m")

    # Print results.
    st.dataframe(df[['search_string', 'parallel', 'sim', 'url_full']], use_container_width=True, hide_index=True,
    column_config={
        "search_string": "Card",
        "parallel": 'Parallel',
                    "sim": "Score",
                  "url_full": st.column_config.LinkColumn()
                  })

