import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.set_page_config(layout='wide', page_title='Startup Analysis')
df = pd.read_csv('Startup_Funding_Cleaned.csv')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year


colors = ["#E78CAE", "#926580", "#926580", "#707EA0", "#34495E"]
custom_palette = sns.color_palette(colors)

def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['AmountInUSD'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('StartupName')['AmountInUSD'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('StartupName')['AmountInUSD'].sum().mean()
    # total funded startup
    num_startups = df['StartupName'].nunique()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total', str(total) + 'cr')
    with col2:
        st.metric('Max', str(max_funding) + 'cr')
    with col3:
        st.metric('Avg', str(round(avg_funding)) + ' cr')
    with col4:
        st.metric('Funded Startups', num_startups)

    col1, col2 = st.columns(2)
    with col1:
        tp10fund=df.groupby('StartupName')['AmountInUSD'].sum().sort_values(ascending=False)
        st.subheader("Top 10 Funded Startups")
        st.dataframe(tp10fund.head(10))

    col1, col2 = st.columns(2)
    with col1:
        st.image('Images/wordcloud1.png',use_column_width="auto")
    
    with col2:
        st.image('Images/wordcloud2.png',use_column_width="auto")
        

    col1,col2 = st.columns(2)
    with col1:
        st.image('Images/Companies with most number of investors.png', caption='Companies with most number of investors',use_column_width="auto")
    
    with col2:
        st.image('Images/Density estimation for number of investors.png', caption='Density estimation for number of investors',use_column_width="auto")

    
    st.subheader("Top Investors by funding on multiple days")
    st.image('Images/top Investors by funding on multiple days.png',use_column_width="auto")
    
    st.image('Images/Top Investors by funding on multiple days wordcloud.png',caption="Top Investors by funding on multiple days wordcloud",use_column_width="auto")
    
    st.subheader("Top 10 Most funded Investors")
    st.image('Images/Top 10 Most funded Investors.png',use_column_width="auto")
    
    st.subheader("Industry sector opted by top investors")
    st.image('Images/Industry sector opted by top investors.png',use_column_width="auto")
    
    st.subheader("In which sector there are most Startups")
    st.image('Images/in which sector there are most startups.png',use_column_width="auto")
    
    st.subheader("Most funded Industry")
    st.image('Images/Most funded Industry.png',use_column_width="auto")
    
    st.subheader("Most preferrable cities as per Investment on startups")
    st.image('Images/Most preferrable cities as per Investment on startups.png',use_column_width="auto")

    
def load_year_wise():
    st.title("Year-wise Funding Analysis")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('Total funding in 2015', '12065784954' + ' cr')
    with col2:
        st.metric('Total funding in 2016', '8724735319' + ' cr')
    with col3:
        st.metric('Total funding in 2017', '7747185034' + ' cr')
        
    col1,col2=st.columns(2)

    with col1:
        st.image('Images/Total Funding Amound.png',caption="Investment in period between January-2015 to Jan-2017 ",use_column_width="auto")
    
    with col2:
        st.image('Images/Average Funding Amount.png',use_column_width="auto")
        
    st.markdown("""
                ### Total funding was most in 2015 and decreased
            """)
    
    st.image('Images/Pie_Variation.png',use_column_width="auto")
    
    st.image("Images/Total variation of funding amount per month in period of 2015-2017.png",caption="Variation of funding amount per month in period of 2015-2017",use_column_width="auto")
    
    
    
    
    option = st.selectbox('Select Type', ['Year','2015', '2016', '2017','Quaterwise'])
    
    if option == '2015':
        st.image('Images/Insights of 2015.png',use_column_width="auto")
        st.markdown(
            """
            - Below we can visualize that total funding reached to its peak between the months of june - july and Aug - Sep
            - End week of july was most attracted to investments
            - Quarter 3 was seen as the most funded quarter of 2015
            """
            )
        
    elif option == '2016':
        st.image('Images/Insights of 2016.png',use_column_width="auto")
        st.markdown(
            """
            #### It seems to be July and  August was the most funding month in year 2016.

            - A sudden increase is witnessed in the month of july - August

            - June seems to be the decline in funding may be  due to goverment administration

            - Further after September  uniform low funding due to demonetization of indian currency

            - Early weeeks of augest seems to be the most funding time

            - An inverse relation among funding by  Quarter
            """
            )
    elif option == '2017':
        st.image('Images/Insights of 20171.png',use_column_width="auto")
        st.image('Images/Insights of 2017.png',use_column_width="auto")
        st.markdown(
            """
            - Month of March and second Week of May had seen peak funding scenarios
            
            - Quarter 2 has most funding  
            """
            )
    elif option == 'Quaterwise':
        st.markdown(
            """
            -  Quaterly funding is found to be normally distributed

            -  Funding is highest in 3rd Quarter of 2015
            """
        )
        st.image('Images/Quaterly_funding.png',use_column_width="auto")
        st.image('Images/Quaterly_funding_Variation.png',caption='Quaterly variation in Funding Amount',use_column_width="auto")
        
        st.markdown(
            """
            - In 2015 and 2016 the average funding was in the starting and mid quarters
            
            - but in 2017 the average funding changed to mid to last quarters

            - the pattern of average funding in 2015 vs 2017 is totally opposite
            """
        )

############################_________________________________###############################################

def load_investment_type():
    st.title('Investment Type Analysis')
    st.subheader("Private equity is seen to be most favourable Investment Mode for high funding amount per startup")
    
    st.image("Images/Investmenttype_vs_Amount.png",use_column_width="auto")
    
    option = st.selectbox('Select Year', ['Year','2015', '2016', '2017'])
    
    if option == '2015':
        st.image("Images/Investment_type_2015.png",use_column_width="auto")
        
        st.markdown(
            """
            - Private equity is more dispersed according to amount funded and more amount is invested through private equity per startup on the otherhand seed funding is less dispersed according to amount funded and low amount is funded using this but frequency of seed funding is more as compared to private equity.
            
            - No debt funding occured in 2015.
            """
        )
    
    elif option == '2016':
        st.image("Images/Investment_type_2016.png",use_column_width="auto")
        
        st.markdown(
            """
            - Private equity is more dispersed according to amount funded and more amount is invested through private equity per startup on the otherhand seed funding is less dispersed         according to amount funded and low amount is funded using this but frequency of seed funding is more as compared to private equity.

            - As compared to 2015 seed funding has slightly more deviated.
            
            - No dept funding and crowd funding occured in 2016.
            
            - Snapdeal and makemytrip was funded most via private equity.
            """
        )
    
    elif option == '2017':
        st.image("Images/Investment_type_2017.png",use_column_width="auto")
        st.markdown(
            """
            - Private Equity is not so dispersed as compared to previous two years.

            - Debt funding slightly taken place.
            """
        )

##########################_________________________________###############################################

def load_conclusion():
    st.header("Conclusion")
    st.markdown(
        """
        * Funding startups are highly dispersed as investors are highly specific about choosing startups.
        * There were more than 2000 new startups funded in the year between 2015-2017.
        * Paytm and Flipkart were funded most.
        * Top 10 investments are made through private equity.
        * Paytm was mostly funded on different days by single investor.
        * Swiggy was invested by most number of investor.
        * As per startups 2 and 3 were most frequent combination of investors.
        * There were 50% relation between funded amount and number of investors per startup.
        * There were more than 1900 unique investors.
        * Steadview capital and existing investors invested highest amount.
        * E.ventures Investor  funded 115 times the most.
        * Ola was Funded most frequent number of times.
        * Consumer internet was the top most choice for all investors.
        * Top investors funded ecommerce and consumer internet most in terms of amount.
        * Most funding came through private equity.
        * Crowd funding and dept funding were less preferred by the investors.
        * Seed funding was less dispersed but private equity is choosen to made large investments per startup.
        * Consumer internet sector got most ammount of funding and attracted the most investors.
        * Banglore had the most average funding <br>
        * Maximum Total  funding was generated  in the  year 2015 and then it slowly decreased with increase in years<br>
        * Average funding was most in 2017<br>
        * In 2015 the period of june-oct was funded most and quarter 3 was funded most<br>
        * In 2016 period of june and september were most funded and quterly funding decreased with increase in time<br>
        * In 2017 the period between march- may had recieved most fundings<br>
        * 3rd quarter  of 2015 was invested most and funding amount was normally distributed<br>
        * Starting months of 2015,mid of 2016 and 3rd Quarter of 2017 were funded most as per individual investment<br>
        * 2016 had highest amount of investments<br>
        * In 2015 there was slight fund generated through crowd funding<br>
        * In 2016 there was slight variation in seed funding by amount.
        * In 2017 there dept funding witnessed for first time but in less fraction as Ahmedabad seems to be an anomaly as it only witnessed the debt funding.
        * Amount Distribution in 2017 (left skewed) was totally opposite  to 2015(right skewed) in terms of Date. 2016's Amount distribution was normally distributed.
        """
    )
##########################_________________________________###############################################

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One', ['Overall Analysis','Year-wise Analysis', 'Investment Type Analysis','Conclusion'])

if option == 'Overall Analysis':
    load_overall_analysis()


elif option == 'Year-wise Analysis':
    load_year_wise()

elif option == 'Investment Type Analysis':
    load_investment_type()
   
else:
    load_conclusion()