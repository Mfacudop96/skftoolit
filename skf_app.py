import base64
import warnings
import streamlit as st
import plotly.express as px
import pandas as pd
from IPython.display import display, HTML

import gspread
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials

warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

############################ GOOGLE DRIVE API #########################################

# Connect to Google
# Scope: Enable access to specific links
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials_mf.json", scope)
client = gspread.authorize(credentials)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

#--link sheet=https://docs.google.com/spreadsheets/d/12w8jPcwNsosODuMZo2SGuj8ZMMuTK-i5ibHquZRb-ek/edit?pli=1#gid=0

########################################################################################

index_tool = ['<=250', '<=500', '<=1000', '<=2000', '<=3000', '<=4000', '<=5000', '<=6000', '<=7000', '<=8000', '<=9000', '<=10000', '<=12000', '<=14000', '<=16000', '<=18000', '<=20000', '<=24000', '<=28000', '<=32000', '<=36000', '<=48000', '<=48001']
data = {'ISO32':  ['ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF'],
        'ISO46':  ['ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3135DSL/17L',	'ROBX3135DSL/17L',	'ROBX3135DSL/17L',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF'],
        'ISO68':  ['ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3135DSL/17M',	'ROBX3135DSL/17M',	'ROBX3135DSL/17M',	'ROBX3145DSL/17M',	'ROBX3145DSL/17M',	'ROBX3145DSL/17M',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF'],
        'ISO100': ['ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3125DSL/17M',	'ROBX3125DSL/17M',	'ROBX3135DSL/17M',	'ROBX3135DSL/17M',	'ROBX3135DSL/17M',	'ROBX3145DSL/17M',	'ROBX3145DSL/17M',	'ROBX3155DSL/17L',	'ROBX3155DSL/17L',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF'],
        'ISO150': ['ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3125DSL/17S',	'ROBX3125DSL/17S',	'ROBX3135DSL/17M',	'ROBX3135DSL/17M',	'ROBX3145DSL/17M',	'ROBX3145DSL/17M',	'ROBX3155DSL/17M',	'ROBX3155DSL/17M',	'ROBX3165DSL/17M',	'ROBX3165DSL/17M',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF'],
        'ISO220': ['ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3125DSL/17S',	'ROBX3125DSL/17S',	'ROBX3135DSL/17M',	'ROBX3135DSL/17M',	'ROBX3145DSL/17M',	'ROBX3145DSL/17M',	'ROBX3155DSL/17M',	'ROBX3165DSL/17M',	'ROBX3165DSL/17M',	'ROBX3175DSL/17M',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF'],
        'ISO320': ['ROBX3115DSL/17S',	'ROBX3115DSL/17S',	'ROBX3125DSL/17S',	'ROBX3135DSL/17S',	'ROBX3145DSL/17S',	'ROBX3155DSL/17S',	'ROBX3165DSL/17S',	'ROBX3175DSL/17S',	'ROBX3185DSL/17S',	'Contact SKF',      'Contact SKF' ,     'Contact SKF',      'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF'],
        'ISO460': ['ROBX3115DSL/17S',	'ROBX3125DSL/17S',	'ROBX3135DSL/17S',	'ROBX3155DSL/17S',	'ROBX3175DSL/17S',	'ROBX3185DSL/17S',	'Contact SKF',      'Contact SKF',      'Contact SKF' ,     'Contact SKF',      'Contact SKF' ,     'Contact SKF',      'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF'],
        'ISO720': ['Contact SKF',       'Contact SKF',      'Contact SKF',      'Contact SKF',      'Contact SKF',      'Contact SKF',      'Contact SKF',      'Contact SKF',      'Contact SKF' ,     'Contact SKF',      'Contact SKF' ,     'Contact SKF',      'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF',	'Contact SKF']}

ref_df = pd.DataFrame(data, index=index_tool)


@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("ReconOil_landing_2.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}


[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
visibility: hidden;
right: 2rem;
}}

[data-testid="stSidebarNav"] {{
                color: red;
                top: 0;
            }}
</style>
"""

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.markdown(page_bg_img, unsafe_allow_html=True)




with st.sidebar:
    
    st.sidebar.image("logo2.png", use_column_width="auto")
    # Add the sidebar title
    st.title(":gear: Calculadora RencondOil Box")

    with st.form("my_form"):

        dist_name_input = st.text_input(
            "Nombre de Distribuidor",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder="Nombre Completo"
        )

        clien_name_input = st.text_input(
            "Nombre de Cliente Final",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder="Nombre Completo"
        )

        sector_name_input = st.text_input(
            "Sector",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder="Sector"
        )

        tip_act_input = st.text_input(
            "Tipo de Activo",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder="Tipo de Activo"
        )

        oil_name_input = st.text_input(
            "Nombre del Aceite",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder="Nombre del Acite"
        )

        vol_oil_input = st.number_input(
            "Volumen de Aceite (Lt)", 
            value=0)

        tem_oil_input = st.number_input(
            "Temperatura de Aceite (C°)", 
            value=0)

        viscocidad = data.keys()
        volumen = index_tool

        #vol_oil_input  = st.number_input("Volumen de Aceite (Lt)")
        rang_vol_oil_input = st.selectbox("Rango de volumen de Aceite (Lt)",
                                          list(volumen),
                                          index=0,
                                          placeholder="Select contact method...",
                                          label_visibility=st.session_state.visibility,
                                          disabled=st.session_state.disabled
                                         )


        #LTc_oil_input = st.number_input("Viscosidad del Aceite (ISO VG)")
        visc_oil_input = st.selectbox("Viscosidad del Aceite (ISO VG)",
                                      list(viscocidad),
                                      index=0,
                                      placeholder="Select contact method...",
                                      label_visibility=st.session_state.visibility,
                                      disabled=st.session_state.disabled
                                      )
        
        col1, col2, col3 = st.columns(3)

        button1 = col1.form_submit_button("Save", type="primary", use_container_width=True)
        button2 = col3.form_submit_button("Compute", type="primary", use_container_width=True)


    if button2:
        cod_robx_input = ref_df[visc_oil_input].loc[rang_vol_oil_input]
        st.write(f"Código ROBX es **{cod_robx_input}**")

    if button1:

        ########################################################################################
        #
        # Create a blank spreadsheet (Note: We're using a service account, so this spreadsheet is LTible only to this account)
        #sheet = client.create("NewDatabase")
        # To access newly created spreadsheet from Google Sheets with your own Google account you must share it with your email
        # Sharing a Spreadsheet
        #sheet.share('frank2207a@gmail.com', perm_type='user', role='writer')
        ########################################################################################
        # open a google sheet
        gs = client.open_by_key('12w8jPcwNsosODuMZo2SGuj8ZMMuTK-i5ibHquZRb-ek')
        # select a work sheet from its name
        worksheet = gs.worksheet('Sheet1')

        cod_robx_input = ref_df[visc_oil_input].loc[rang_vol_oil_input]
        new_data = {'DISTRIBUIDOR_NOMBRE': dist_name_input, 
                    'CLIENTE_NOMBRE': clien_name_input, 
                    'SECTOR': sector_name_input, 
                    'TIPO_ACTIVO': tip_act_input, 
                    'ACEITE': oil_name_input, 
                    'VOLUMEN_ACEITE': vol_oil_input,
                    'TEMPERATURA_ACEITE': vol_oil_input,
                    'RANGO_VOLUMEN_ACEITE': rang_vol_oil_input, 
                    'VISCOCIDAD_ACEITE': visc_oil_input,
                    'ROBX_COD': cod_robx_input}
        
        new_df = pd.DataFrame(new_data, index=[0])
        
        # write to dataframe
        df_values = new_df.values.tolist()
        gs.values_append('Sheet1', {'valueInputOption': 'RAW'}, {'values': df_values})

        st.write("Se guardo los datos exitosamente")
    




    