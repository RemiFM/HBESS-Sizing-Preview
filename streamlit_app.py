import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
from PIL import Image


st.set_page_config(
    page_title="HBESS Sizing Tool",
    page_icon="🔋", #🔋⚡
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': "mailto:remi.decoster@flandersmake.be?subject=[HBESS Sizing Tool] - Subject",
        'Report a bug': "mailto:remi.decoster@flandersmake.be?subject=[HBESS Sizing Tool] - Subject",
        'About': "The HBESS Sizing Tool was developed by Flanders Make in 2023 as part of the SEABAT project."
    }
)


#####HEADER######
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)
###########



#st.title('HBESS Sizing Tool')
st.subheader('Hybrid Battery Energy Storage System (HBESS) Sizing Tool')

tab1, tab2, tab3, tab4 = st.tabs(["Define inputs", "Proposed configuration", "System comparison", "More information"])

with tab1:
    #col1, col2 = st.columns([1, 3])
    col1, col2, col3 = st.columns([2,3,1], gap="medium")

    with col1:




        coleen, coltwee = st.columns(2)
        with coleen:
            option1 = st.selectbox(
                'High Energy (HE) Cell',
                ('LTO Toshiba 23 Ah', 'NMC Samsung 94 Ah', 'Custom'), help='Coming soon', index=0)

        with coltwee:
            option2 = st.selectbox(
                'High Power (HP) Cell',
                ('LTO Toshiba 23 Ah', 'NMC Samsung 94 Ah', 'Custom'), help='Coming soon', index=1)

        coldrie = st.columns(1)

        # genre = st.radio(
        # "Number of load profiles",
        # ('1', '2', '3', '4', '5'), horizontal=True, disabled=True, help='This feature is coming soon')

        load_profile = st.selectbox(
            'Load profile',
            ('Tug boat 1', 'Tug boat 2', 'Other boat', 'Custom'), help='Coming soon'
        )

        option3 = st.selectbox(
            'Energy Management Strategy',
            ('Split', 'Power', 'Gradient', 'Cost'), help='Coming soon', index=2)




        col11, col22 = st.columns(2)

        with col11:
            soc_slider2 = st.slider('Initial State of Charge (SoC)', 0, 100, 90, key=3)
            ref_voltage_field = st.number_input('Target voltage (V)', min_value = 12, max_value = 10000, value = 1000, step=10)
            cycles_field = st.number_input('Number of cycles per year', min_value=1, max_value=10000, value = 365, step = 10)

        with col22:
            dod_slider2 = st.slider('Depth of Discharge (DoD)', 0, 100, 80, key=2)
            number = st.number_input('Charging time (hours)', min_value = 0.0, max_value = 240.0, value=1.0, step=0.1)
            lifetime_field = st.number_input('Expected lifetime (years)', min_value=1, max_value=200, value=20, step=1)

        cola = st.columns(1)


        with st.expander("Upload custom files"):
            ##
            uploaded_file = st.file_uploader("Custom Load Profile", key=1)
            if uploaded_file is not None:
                # To read file as bytes:
                bytes_data = uploaded_file.getvalue()
                st.write(bytes_data)

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                st.write(stringio)

                # To read file as string:
                string_data = stringio.read()
                st.write(string_data)

                # Can be used wherever a "file-like" object is accepted:
                dataframe = pd.read_csv(uploaded_file)
                st.write(dataframe)

            ##
            uploaded_file = st.file_uploader("Custom HE Cell", key=12)
            if uploaded_file is not None:
                # To read file as bytes:
                bytes_data = uploaded_file.getvalue()
                st.write(bytes_data)

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                st.write(stringio)

                # To read file as string:
                string_data = stringio.read()
                st.write(string_data)

                # Can be used wherever a "file-like" object is accepted:
                dataframe = pd.read_csv(uploaded_file)
                st.write(dataframe)

            ##
            uploaded_file = st.file_uploader("Custom HP Cell", key=123)
            if uploaded_file is not None:
                # To read file as bytes:
                bytes_data = uploaded_file.getvalue()
                st.write(bytes_data)

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                st.write(stringio)

                # To read file as string:
                string_data = stringio.read()
                st.write(string_data)

                # Can be used wherever a "file-like" object is accepted:
                dataframe = pd.read_csv(uploaded_file)
                st.write(dataframe)


    with col2:
        #st.subheader('Load Profile & Energy Management Strategy')
        kcol1, kcol2, kcol3, kcol4 = st.columns(4)
        kcol1.metric("Required Energy", "150 kWh")
        kcol2.metric("Maximum Power", "794 kW")
        kcol3.metric("Average Power", "237 kW")
        kcol4.metric("Peak-to-Average Power Ratio", "6.23 dB")

        chart_data = pd.DataFrame((794/2.5) * np.random.randn(50, 3) + 237, columns=['Load profile', 'High Energy Pack', 'High Power Pack'])
        st.line_chart(chart_data, height=560, use_container_width=True)

    with col3:
        st.write('**High Energy (HE) Cell**')

        dict_a = {'Parameter':['Chemistry', 'Capacity', 'Voltage', 'C-rates', 'Weight', 'Cost'],
        'Value':['NMC', 50, 3.65, '1/1', 0.885, 150],
        'Unit':['-', 'Ah', 'V', '-', 'kg', '€/kWh']}
        df_a = pd.DataFrame(dict_a)
        st.table(df_a)

        st.write('**High Power (HP) Cell**')

        dict_b = {'Parameter':['Chemistry', 'Capacity', 'Voltage', 'C-rates', 'Weight', 'Cost'],
        'Value':['LTO', 23, 2.3, '4/4', 0.550, 380],
        'Unit':['-', 'Ah', 'V', '-', 'kg', '€/kWh']}
        df_b = pd.DataFrame(dict_b)
        st.table(df_b)






with tab2:
    tab2col1, tab2col2 = st.columns([1, 2])
    with tab2col1:

        st.subheader("Proposed HBESS Configuration")

        col1, col2, col3 = st.columns(3)
        col1.metric("Required Energy", "150 kWh")
        col1.metric("Number of HE Cells", "144")
        col1.metric("HE Pack Energy", "110 kWh")
        col2.metric("Maximum Power", "800 kW")
        col2.metric("Number of HP Cells", "128")
        col2.metric("HP Pack Energy", "80 kWh")
        col3.metric("Average Power", "230 kW")
        col3.metric("Total Cost", "€4,800")
        col3.metric("Total Energy", "190 kWh")
        #col4.metric("Total Energy", "212 kWh", "9%")
        #col5.metric("Total Cost", "48.3 x 10^3€", "-50%")

        st.write("")
        st.subheader("Breakdown of Battery Packs")

        tab2col1div1, tab2col1div2 = st.columns(2)
        with tab2col1div1:
            st.write('**High Energy (HE) Pack**')

            S_HE, P_HE, E_HE, V_HE, C_HE, V_HE_L, V_HE_H, I_HE = 24, 6, 110, 987.07, 2600, 942.12, 1006.22, 64.23
            st.write(
            '- Cells in series: ', S_HE, '\n',
            '- Cells in parallel: ', P_HE, '\n',
            '- Total energy: ', E_HE, ' kWh', '\n',
            '- Nominal voltage: ', V_HE, ' V', '\n',
            '- Minimum voltage: ', V_HE_L, ' V', '\n'
            '- Maximum voltage: ', V_HE_H, ' V', '\n'
            '- Maximum current: ', I_HE, ' A', '\n'
            '- Cost: ', C_HE, ' €')
        with tab2col1div2:
            st.write('**High Power (HP) Pack**')

            S_HE, P_HE, E_HE, V_HE, C_HE, V_HE_L, V_HE_H, I_HE = 16, 8, 80, 1005.28, 2200, 986.25, 1023.75, 91.88
            st.write(
            '- Cells in series: ', S_HE, '\n',
            '- Cells in parallel: ', P_HE, '\n',
            '- Total energy: ', E_HE, ' kWh', '\n',
            '- Nominal voltage: ', V_HE, ' V', '\n',
            '- Minimum voltage: ', V_HE_L, ' V', '\n'
            '- Maximum voltage: ', V_HE_H, ' V', '\n'
            '- Maximum current: ', I_HE, ' A', '\n'
            '- Cost: ', C_HE, ' €')


    with tab2col2:
        tab2col2par1, tab2col2par2 = st.columns(2)

        with tab2col2par1:
            chart_data = pd.DataFrame(
            np.random.randn(50, 2)+5, columns=['HE Pack', 'HP Pack'])

            st.write('**Load profile**')
            st.area_chart(chart_data, height=300, use_container_width=True)

            st.write('**State of Charge (SoC)**')
            st.line_chart(chart_data, height=300, use_container_width=True)

        with tab2col2par2:

            chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

            st.write('**Voltage**')
            st.line_chart(chart_data, height=300, use_container_width=True)

            st.write('**Current**')
            st.bar_chart(chart_data, height=300, use_container_width=True)

with tab3:
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Cost of HBESS", "€4,800")
    col2.metric("Cost of Monotype HE", "€5,344", "+11.33%", delta_color="inverse")
    col3.metric("Cost of Monotype HP", "€7,321", "+52.52%", delta_color="inverse")
    col4.metric("Lifetime of HBESS", "24.3 years")
    col5.metric("Lifetime of Monotype HE", "22.5 years", "-5.80%")
    col6.metric("Lifetime of Monotype HP", "19.4 years", "-14.26%")

    st.write("")
    tab3col1, tab3col2, tab3col3 = st.columns([1, 1, 2])
    with tab3col1:
        st.subheader("Monotype HE Storage System")

        S_HE, P_HE, E_HE, V_HE, C_HE, V_HE_L, V_HE_H, I_HE = 24, 12, 220, 1005.28, 5344, 986.25, 1023.75, 128.46
        st.write(
        '- Cells in series: ', S_HE, '\n',
        '- Cells in parallel: ', P_HE, '\n',
        '- Total energy: ', E_HE, ' kWh', '\n',
        '- Nominal voltage: ', V_HE, ' V', '\n',
        '- Minimum voltage: ', V_HE_L, ' V', '\n'
        '- Maximum voltage: ', V_HE_H, ' V', '\n'
        '- Maximum current: ', I_HE, ' A', '\n'
        '- Cost: ', C_HE, ' €')

        st.write("")
        chart_data = pd.DataFrame(np.random.randn(20, 1), columns=['State of Charge'])
        st.line_chart(chart_data, height=250)

    with tab3col2:
        st.subheader("Monotype HP Storage System")

        S_HE, P_HE, E_HE, V_HE, C_HE, V_HE_L, V_HE_H, I_HE = 16, 16, 160, 1005.28, 7321, 986.25, 1023.75, 183.66
        st.write(
        '- Cells in series: ', S_HE, '\n',
        '- Cells in parallel: ', P_HE, '\n',
        '- Total energy: ', E_HE, ' kWh', '\n',
        '- Nominal voltage: ', V_HE, ' V', '\n',
        '- Minimum voltage: ', V_HE_L, ' V', '\n'
        '- Maximum voltage: ', V_HE_H, ' V', '\n'
        '- Maximum current: ', I_HE, ' A', '\n'
        '- Cost: ', C_HE, ' €')

        st.write("")
        chart_data = pd.DataFrame(np.random.randn(20, 1), columns=['State of Charge'])
        st.line_chart(chart_data, height=250)



    with tab3col3:
        st.subheader("Hybryd Storage System (HBESS)")
        tab3col3par1, tab3col3par2 = st.columns(2)
        with tab3col3par1:
            S_HE, P_HE, E_HE, V_HE, C_HE, V_HE_L, V_HE_H, I_HE = 24, 6, 110, 987.07, 2600, 942.12, 1006.22, 64.23
            st.write(
            '- HE Cells in series: ', S_HE, '\n',
            '- HE Cells in parallel: ', P_HE, '\n',
            '- Total HE energy: ', E_HE, ' kWh', '\n',
            '- Nominal HE voltage: ', V_HE, ' V', '\n',
            '- Minimum HE voltage: ', V_HE_L, ' V', '\n'
            '- Maximum HE voltage: ', V_HE_H, ' V', '\n'
            '- Maximum HE current: ', I_HE, ' A', '\n'
            '- HE Cost: ', C_HE, ' €')
        with tab3col3par2:
            S_HE, P_HE, E_HE, V_HE, C_HE, V_HE_L, V_HE_H, I_HE = 16, 8, 80, 1005.28, 2200, 986.25, 1023.75, 91.88
            st.write(
            '- HP Cells in series: ', S_HE, '\n',
            '- HP Cells in parallel: ', P_HE, '\n',
            '- Total HP energy: ', E_HE, ' kWh', '\n',
            '- Nominal HP voltage: ', V_HE, ' V', '\n',
            '- Minimum HP voltage: ', V_HE_L, ' V', '\n'
            '- Maximum HP voltage: ', V_HE_H, ' V', '\n'
            '- Maximum HP current: ', I_HE, ' A', '\n'
            '- HP Cost: ', C_HE, ' €')

        st.write("")
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['HE SOC', 'HP SOC'])
        st.line_chart(chart_data, height=250)


with tab4:
    tab4col1, tab4col2 = st.columns([3, 8], gap="medium")
    with tab4col1:
        image = Image.open('parallel_hbess.png')
        st.image(image, caption='Parallel HBESS')

    with tab4col2:
        st.subheader('Hybrid Battery Energy Storage Systems')
        st.write('''
            Hybrid Battery Energy Storage Systems or HBESS in short are battery systems consisting of two or more battery cell types. The complementary features of the two cell types make the hybrid battery system outperform any monotype battery system.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed hendrerit libero eu urna scelerisque, eget dictum eros viverra. Maecenas diam odio, dictum sit amet orci nec, rutrum faucibus erat. Nulla elit lacus, vulputate a ex id, porta consectetur arcu. Cras aliquet quam vel quam scelerisque dignissim. Etiam vehicula gravida odio nec interdum. Aliquam rutrum tincidunt ligula et finibus. Vivamus a libero et massa vehicula mattis. Vestibulum pulvinar sit amet dui in faucibus. Vestibulum eu euismod est, ac venenatis erat. Nullam sit amet malesuada massa. Mauris massa neque, sodales vel lacus id, vehicula posuere augue.

            In aliquam, leo in volutpat malesuada, metus augue ultricies nisl, quis vehicula velit lacus nec nunc. Maecenas id lobortis mauris. Etiam pellentesque turpis cursus est sollicitudin, sit amet malesuada sapien tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent pretium sapien risus, ac tincidunt tortor lacinia at. Nunc laoreet volutpat venenatis. Sed at aliquet erat. Proin purus mi, consectetur a faucibus et, tempor non massa. Nulla varius enim id augue placerat scelerisque. Nulla facilisi. Quisque a tincidunt neque. Nullam nunc enim, venenatis eget massa sed, tincidunt semper felis. Donec maximus tortor semper augue pharetra egestas.
        ''')

    tab4col3 = st.columns(1)
    with st.expander("Energy Management Strategies"):
        st.write('Coming soon')
    with st.expander("References"):
        st.write('Coming soon')








#FOOTER#
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
height: 10%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p></p>
<p>Developed by <a href="https://www.flandersmake.be/en">Flanders Make</a> as part of the <a href="https://www.seabat-h2020.eu">SEABAT</a> project</p>
</div>
"""
#<p>Developed by Flanders Make as part of the SEABAT project <a style='display: block; text-align: center;' href="https://www.flandersmake.be" target="_blank">Flanders Make</a></p>
st.markdown(footer,unsafe_allow_html=True)
