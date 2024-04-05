# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie!

    """)


name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your smoothie will be:', name_on_order)


#option = st.selectbox(
    #'What is your favourite Fruit?',
    #('Banana', 'Strawberries', 'Peaches'))

#st.write('You selected:', option)


# Display the Fruit Options List in Your Stramlit in Snowflake(Sis) APP
session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)



ingredients_list = st.multiselect(
    'Choose upto 5 ingredients:',
    my_dataframe,max_selections=5)


if ingredients_list:
    #st.write(ingredients_list) # Improving the string output
    #st.text(ingredients_list) ## Improving the string output
    ingredients_string=''



    
#To convert the LIST to a STRING we can add an FOR LOOP block. A FOR LOOP will repeat once FOR every value in the LIST.
    for fruit_chosen in ingredients_list:
        ingredients_string+=fruit_chosen + ' '
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values('""" + ingredients_string + """','""" + name_on_order + """')"""


    #st.write(ingredients_string)

# Improving the string output
#Build a SQL Insert Statement & Test It
 

    #st.write(my_insert_stmt)
    #st.stop
## Add a Submit Button:
    time_to_insert=st.button('Submit Order')

#Make the second IF Block dependent not on the string having a value, 
#but on the submit button being clicked by the customer.
#Once you have submitted an order, check the Snowflake table. 



# Inserting the Order into Snowflake
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!' , icon="✅")
