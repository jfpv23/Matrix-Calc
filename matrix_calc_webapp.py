import streamlit as st
import addingbackend as add
import multiplyingbackend as mult
import numpy as np

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://c4.wallpaperflare.com/wallpaper/397/672/855/the-matrix-neo-wallpaper-preview.jpg");
    background-size: 60vw 100vh;  #This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-size: 80px'>THE MATRIX CALC</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: left; font-size: 20px'>By: John Frank Valenzona</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <h1 style="font-size: 30px; text-align: center">
        Enter the size of the matrices:
        </h1>
    """, unsafe_allow_html=True)
with col2:
    try:
        row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
    except ValueError:
        st.error("Please enter a valid integer for the number of rows.")
with col3:
    try:
        column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')
    except ValueError:
        st.error("Please enter a valid integer for the number of columns.")

col4, col5 = st.columns(2)
with col4:
    st.markdown("""
            <h1 style="font-size: 24px; text-align: center">
            Matrix A
            </h1>
        """, unsafe_allow_html=True)
    for row_index in range(row):
        columns = st.columns(column)
        for col_index, col in enumerate(columns):
            with col:
                try:
                    st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')
                except ValueError:
                    st.error("Please enter valid numerical values.")
with col5:
    st.markdown("""
                <h1 style="font-size: 24px; text-align: center">
                Matrix B
                </h1>
            """, unsafe_allow_html=True)
    for row_index in range(row):
        columns = st.columns(column)
        for col_index, col in enumerate(columns):
            with col:
                try:
                    st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
                except ValueError:
                    st.error("Please enter valid numerical values.")

matA = np.zeros((row, column))
matB = np.zeros((row, column))

for i in range(row):
    for j in range(column):
        value = st.session_state.get(f'Arow{i+1}Acol{j+1}', '')
        if value:
            try:
                matA[i, j] = float(value)
            except ValueError:
                st.error("Please enter valid numerical values for Matrix A.")

for i in range(row):
    for j in range(column):
        value = st.session_state.get(f'Brow{i+1}Bcol{j+1}', '')
        if value:
            try:
                matB[i, j] = float(value)
            except ValueError:
                st.error("Please enter valid numerical values for Matrix B.")


st.markdown("<h1 style='text-align: center; font-size: 30px'>SELECT OPERATION BELOW:</h1>", unsafe_allow_html=True)

col6, col7, col8 = st.columns(3)
with col6:

    calculate_sum = st.button("A + B (ADD)", key='AplusB')
    calculate_inverse = st.button("Inverse of A and B", key='inverse')
with col7:

    calculate_product = st.button("A * B (MULTIPLY)", key='AmultB')
    calculate_determinant = st.button("Determinant of A and B", key='determinant')
with col8:

    calculate_transpose = st.button("Transpose of A and B", key='transpose')
    if st.button("Reset"):
        st.session_state.clear()
        st.experimental_rerun()

if calculate_sum or calculate_product or calculate_transpose or calculate_inverse or calculate_determinant:
    if np.count_nonzero(matA) == 0 or np.count_nonzero(matB) == 0:
        st.error("Please enter values for both Matrix A and Matrix B.")
    else:
        if calculate_sum:
            matrix_Result = add.get_sumOfMatrices(matA, matB)
            col6, col7, col8 = st.columns(3)
            with col7:
                st.markdown("""
                                    <h1 style='text-align: center; font-size: 24px'>
                                    Matrix Result (Addition)
                                    </h1>
                                """, unsafe_allow_html=True)
                for row_index in range(row):
                    columns = st.columns(column)
                    for col_index, col in enumerate(columns):
                        with col:
                            st.text_input("", value=matrix_Result[row_index][col_index],
                                          key=f'Rrow{row_index + 1}Rcol{col_index + 1}')

        if calculate_product:
            matrix_Result = mult.get_productOfMatrices(matA, matB)
            col6, col7, col8 = st.columns(3)
            with col7:
                st.markdown("""
                                                    <h1 style='text-align: center; font-size: 24px'>
                                                    Matrix Result (Multiplication)
                                                    </h1>
                                                """, unsafe_allow_html=True)
                for row_index in range(row):
                    columns = st.columns(column)
                    for col_index, col in enumerate(columns):
                        with col:
                            st.text_input("", value=matrix_Result[row_index][col_index],
                                          key=f'Rrow{row_index + 1}Rcol{col_index + 1}')

        if calculate_transpose:
            col6, col7, col8 = st.columns(3)
            with col7:
                st.markdown("<h1 style='text-align: center; font-size: 24px'>Matrix Result (Transpose)</h1>",
                            unsafe_allow_html=True)

            col8, col9, col10, col11, col12 = st.columns(5)
            with col9:
                st.markdown("### Matrix A")
                st.write(np.transpose(matA))

            with col11:
                st.markdown("### Matrix B")
                st.write(np.transpose(matB))

        if calculate_inverse:
            col6, col7, col8 = st.columns(3)
            with col7:
                st.markdown("<h1 style='text-align: center; font-size: 24px'>Matrix Result (Inverse)</h1>",
                            unsafe_allow_html=True)

            col8, col9, col10, col11, col12 = st.columns(5)
            with col9:
                st.markdown("### Matrix A")
                try:
                    st.write(np.linalg.inv(matA))
                except np.linalg.LinAlgError:
                    st.error("Inverse does not exist for Matrix A (singular matrix)")
            with col11:
                st.markdown("### Matrix B")
                try:
                    st.write(np.linalg.inv(matB))
                except np.linalg.LinAlgError:
                    st.error("Inverse does not exist for Matrix B (singular matrix)")

        if calculate_determinant:
            col6, col7, col8 = st.columns(3)
            with col7:
                with col7:
                    st.markdown("<h1 style='text-align: center; font-size: 24px'>Matrix Result (Determinant)</h1>",
                                unsafe_allow_html=True)

            col8, col9, col10, col11, col12 = st.columns(5)
            with col9:
                st.markdown("### Matrix A")
                st.write(np.linalg.det(matA))
            with col11:
                st.markdown("### Matrix B")
                st.write(np.linalg.det(matB))