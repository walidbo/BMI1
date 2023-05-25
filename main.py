# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # import the streamlit library
    import streamlit as st

    # give a title to our app
    st.title('Welcome to BMI Calculator')
    # TAKE WEIGHT INPUT in kgs
    weight = st.number_input("Enter your weight (in kgs)")
    # TAKE HEIGHT INPUT
    # radio button to choose height format
    status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))
    if (status == 'cms'):
        height = st.number_input('Centimeters')

        try:
            bmi = weight / ((height / 100) ** 2)
        except:
            st.text("Enter some value of height")
    elif (status == 'meters'):
        # take height input in meters
        height = st.number_input('Meters')

        try:
            bmi = weight / (height ** 2)
        except:
            st.text("Enter some value of height")
    else:
        height = st.number_input('Feet')
            # 1 meter = 3.28
        try:
            bmi = weight / (((height / 3.28)) ** 2)
        except:
            st.text("Enter some value of height")
    if (st.button('Calculate BMI')):

        # print the BMI INDEX
        st.text("Your BMI Index is {}.".format(bmi))

        # give the interpretation of BMI index
        if (bmi < 16):
            st.error("You are Extremely Underweight")
        elif (bmi >= 16 and bmi < 18.5):
            st.warning("You are Underweight")
        elif (bmi >= 18.5 and bmi < 25):
            st.success("Healthy")
        elif (bmi >= 25 and bmi < 30):
            st.warning("Overweight")
        elif (bmi >= 30):
            st.error("Extremely Overweight")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
