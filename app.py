import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(
     page_title="Essentials price Analysis",
     page_icon="📊",
     layout="centered",
 )

# col_00,col_01=st.columns(2)
# col_00.write("Checkout my [Github page](https://github.com/aadityarock2000)")
# col_01.write("Checkout my [LinkedIn](https://www.linkedin.com/in/aaditya-parthasarathy/)")
# adding the navbar

places=["CHENNAI","DELHI","LUCKNOW","SHIMLA","MUMBAI","AHMEDABAD","KOLKATA","PATNA","GUWAHATI","PORT BLAIR","HYDERABAD"]

st.title('An Analysis on the Prices of Essential Commodities in Indian cities')


st.markdown("""
<img src="https://images.unsplash.com/photo-1572402123736-c79526db405a" width="100%">
""", unsafe_allow_html=True)


st.markdown("""

I have been hearing about Inflation for the past few Months, and I have been curious as to how much the prices
of essential commodities have actually increased. Therefore, I decided to put my analytical skills to the test as an aspiring Data scientist
to come up with some hypothesis and answer them myself, verifying the hypothesis in the process. I have learned some interesting facts about the
city I have been living all my life, and also this analysis has broken some of my preconceived notions. Go thourugh some of the questions I answered in my analysis
in the tabs below.


### Questions I have on the dataset:
1. Which is more costly? Living in a tier 1 city (Chennai, Delhi, Mumbai) or a hill station or a island like port blair? How much is it better than the rest of the country? (quantify it)
    
2. How does the value of petrol affect the cost of prices of various kind?
    
3. What are the effects of pre and post covid rates? 
    
4. Which food item has the highest variation of cost beteen cities on average? Did it increase over the years, or is it getting smaller?

    4.1. Which commodity has increased in price by a lot? (quantify it)

5. Which of the vegetables (potato, tomato, onion) has a lot of fluctuations? Is it city dependent? (Coming Soon!)

#### Click on the tabs below to view my analysis to answer the above questions, and verify my hypothesis.
""")

#dfferent tabs for different Questions
tab_titles=["Dataset Extraction","Question 1", "Question 2", "Question 3","Question 4"]
tabs=st.tabs(tab_titles)

with tabs[0]:
    st.header('Extraction of dataset')
    st.markdown("""
    
    For this analysis, we would require the use of both the prices dataset and the fuel prices for the years 2014 to 2022. 
    Below follows a brief description of the extraction process.

    ---

    """)

    #About commodity dataset
    col_1a,col_1b=st.columns(2)
    col_1a.markdown("""
    <img src="https://images.unsplash.com/photo-1489806149968-aee262986b40" width="100%">
    """, unsafe_allow_html=True)
    col_1b.markdown("""
    ## The Essential Commodity Price Dataset
    """)
    st.text("")
    st.markdown("""

    There is a database provided by the [Department of Consumer Affairs](https://consumeraffairs.nic.in/), 
    jointly developed by the [National Informatics Center](https://www.nic.in/). This database has a collection of commodity prices
    from vaious cities in India, from roughy 2010s, but has sufficient data from about the year 2014 and above.

    We use the [website](https://fcainfoweb.nic.in/reports/report_menu_web.aspx) to view and extract the 
    data from the years 2014 to 2022 (till present). As they do not provide a way to download datasets, we would have to 
    scrape the website, using the python's requests library.

    The code used to extract the dataset used in the analysis can be found [here](https://github.com/aadityarock2000/Price-history-analysis/blob/master/notebooks/price-history-v2.ipynb).
    
    The dataset consists of 22 commodities, listed below. I acknolwdge that the rate here is provided by the government, 
    and hence, most of the packed essentials in the shelves of super markets would not reflect these.

    ##### Commmodities discussed in the analysis.
    """)

    column_list=['Rice','Wheat','Atta (Wheat)','Gram Dal','Tur/Arhar Dal','Urad Dal','Moong Dal','Masoor Dal','Sugar',
            'Milk','Groundnut Oil (Packed)','Mustard Oil (Packed)','Vanaspati (Packed)','Soya Oil (Packed)','Sunflower Oil (Packed)',
            'Palm Oil (Packed)','Gur','Tea Loose','Salt Pack (Iodised)','Potato','Onion','Tomato']
    st.write(column_list)
    st.markdown("---")
    # About fuel Dataset
    col_1c,col_1d=st.columns(2)
    col_1c.markdown("## The Indian Fuel Price Dataset")
    col_1d.markdown("""
    <img src="https://images.unsplash.com/photo-1611807527279-f6ac568cd4f8?" width="100%">
    """, unsafe_allow_html=True)
    st.text('')
    st.markdown("""
    A lot of talk about inflation is frequenctly followed by the discussion on fuel prices. Hence, I would also 
    like to take that into account. However, similar to the commodity dataset, there is no ready made dataset for
    fuel prices in India. So, I used selenium to extract prices from [this website](https://www.mypetrolprice.com/5/Petrol-price-in-Chennai)

    This website is used to extract prices of petrol in the Chennai region from 2014, and since most often,
    the prices didn't vary to a large extent (it varied mostly in terms of less than a rupee, so not that significant), 
    we can impute the data using interpolation on both sides.
    
    **Click on the tabs above to move to different questions and view my analysis**
    
    """)
   
with tabs[1]:

    st.header('Question 1')
    st.info("""**Living in which place is costlier? There are various places all across India selected for this analysis. 
    How much does the cheaper city *cheaper* than the most expensive one?**""")
    
    st.markdown("""
    <img src="https://images.unsplash.com/photo-1561784493-88b0a3ce0c76" width="100%">
    """, unsafe_allow_html=True)
    st.caption('An ariel View of Chennai City.')
    
    st.markdown("""
    #### My Initial Hypothesis:
    - My initial Hypothesis is that a tier 1 city(metro cities) would be costly to live in than a tier 2 city(non metro cities)
    - Living in Islands should be costlier than being in the main land.
    - Hill stations would be equivalent/ expensive when compared to tier 1 cities   
    """)
    st.markdown("""

    
    ### The Approach:

    There are different products with different price points, so it is difficult to measure the "costliness" with just a simple sum/average of the products. 
    Different products can have different ranges of values, hence, it is better to normalise it. 

    """)

    df=pd.read_csv('data/combined_data.csv')
    df_scaled = df.copy()
    df_scaled.iloc[:,1:23] = MinMaxScaler().fit_transform(df_scaled.iloc[:,1:23])

    places=["CHENNAI","DELHI","LUCKNOW","SHIMLA","MUMBAI","AHMEDABAD","KOLKATA","PATNA","GUWAHATI","PORT BLAIR","HYDERABAD"]
    df_new=pd.read_csv('data/df_new.csv')
    df_new['Date'] =  pd.to_datetime(df_new['Date'], format="%Y/%m/%d")

    #plotting the average
    fig,ax=plt.subplots()
    for i in range(len(places)):
        ax.plot(df_new['Date'],df_new[places[i]],label=places[i])

    ax.axvline(x=pd.to_datetime('2020-04-01', format = "%Y/%m/%d"))
    ax.legend()

    fig.set_figheight(10)
    fig.set_figwidth(15)
    st.pyplot(fig)

    st.markdown("""

    This above plot shows the scaled sum of commodities among various cities 
    for the past 8 years. We can see a clear increasing trend of prices from 2018, 
    and then an un precedented increase in the past 2 years, since the advent of the unpredictable COVID-19.

    > ##### Look at the *line* in the chart dividing the pre and the post Covid-era for the stark difference in pricing.

    We can make a lot of observations from this chart at a glance. 

    1. Port Blair is consistently costly over the years, as it is the most remote of the cities in the list.
    2. Shimla, being a hill station, is not that expensive when compared to the rest. This is suprising, considering the hypothesis of Hill stations being costlier.
    3. Ahmedabad is the cheapest for most of this duration of 8 years. 
    4. Mumbai is the second most expensive of the list, and it has approached levels of Port Blair in terms of cost in the last 2 years.
    5. Covid-19 seemed to have an immediate impact in pricing, which we will discuss later, in a further question
    """)

    col_a,col_b=st.columns(2)

    col_a.markdown("""
    We now can also view as to the order of the expensiveness of the cities.
    Select a year below to see the average scaled prices of commodities of that year. There is a lot 
    of fluctuations over the years, so a yearwise comparison seems to be fair.
    """)

    #set up a button for the year
    year = col_b.selectbox(
        'Which year would you like to analyse?',
        ('2014', '2015','2016','2017','2018','2019','2020','2021','2022'))

    st.markdown("### Chart of the average Scaled Prices for the year selected")
    df_test=df_new[df_new['Date'].dt.to_period('Y')==year]
    l=df_test.mean().to_frame().reset_index()
    l.columns=['City','Avg. Scaled Prices']
    l=l.sort_values('Avg. Scaled Prices')
    fig1, ax1 =plt.subplots()
    ax1.barh(l['City'],l['Avg. Scaled Prices'])
    fig.set_figheight(10)
    fig.set_figwidth(15)

    percentage_costly=round(100*((l.iloc[-1,1]-l.iloc[0,1])/l.iloc[0,1]),2)
    col1,col2,col3=st.columns(3)

    col1.metric("Difference between the extremes",str(percentage_costly)+"%")
    col2.metric("Costliest City",l.iloc[-1,0])
    col3.metric("Cheapest City",l.iloc[0,0])

    st.pyplot(fig1)
    #st.dataframe(l)
    st.markdown("""
    It can also be observed that the gap between Mumbai and Port Blair is decreasing over the years, with 2022
    being the most brutal, where it almost toched the same price.

    #### Reviewing Our Hypothesis:
    1. Statement 1 of tier of cities being important to judge expensiveness **holds true** for the most part.
    2. Statement 2 of island cities being expensive is **also true**, but I didn't expect such a wide gap between the number 1 and number 2 city to be this large. 
        This shows how much land transport is important in a country like India, to maintain uniform pricing over cities.
    3. Statement 3 of Hill station(shimla) being more expensive turns out to be **completely false**. It is actually cheaper than living in the tier 1 metro cities 
        and even some tier 2 cities over the years.
    """)

with tabs[2]:
    st.header('Question 2')
    st.info("""**How does the value of petrol / gas prices affect the cost of essential items of various kind?**""")
    
    st.markdown("""
    
    #### My Initial Hypothesis: 
    - Fuel prices have increased over the years, but the pandemic had drastically sky rocketed the cost of petrol. So, most of the commodities should follow the trend as well.
    - If the cost of commodity is well aligned with the cost of fuel, then fuel prices most likely cause/inflence the cost of commodities.
    
    """)
    st.markdown("""

    ### The Approach:
    This can be breaken into 2 sub-tasks
    1. Finding if the total prices depend on fuel prices
    2. Find out which quantities are more related to fuel prices.

    #### Task 1: 

    Let us use the petrol prices extracted earlier and compare it with the total costs chart that we plotted before.
    
    """)
    df1=pd.read_csv('data/Chennaipetrol.csv')
    df1['Date'] =  pd.to_datetime(df1['date'], format='%Y-%m-%d')

    # removing a duplicate row at index 2019-11-1 (has 2 different petrol values)
    #df1[df1['date']=='2019-11-1']
    df1.drop(555,inplace=True)
    df_CHENNAI=pd.read_csv('data/prices_CHENNAI.csv')
    df_CHENNAI=df_CHENNAI.iloc[368:,:]
    df_CHENNAI=df_CHENNAI.reset_index(drop=True)
    #reset the index to make it clean
    df1=df1.reset_index()
    df1.drop(['index','date','city'], axis=1, inplace=True)
    
    #create the Date column

    df_CHENNAI['23'] =  pd.to_datetime(df_CHENNAI['23'], format='%d/%m/%Y')
    df2=df_CHENNAI[['23']]
    df2.columns=['Date']
    
    #creating the Petrol_price Data Frame
    petrol_price=df2.merge(df1, how='left', on='Date')
    petrol_price['rate'] = petrol_price['rate'].interpolate(limit_direction='both')


    #plotting the prices of Petrol and Chennai total prices side by side

    col_3,col_4=st.columns(2)

    #plotting the petrol price in column 1

    #plotting the average
    fig_a,ax_a=plt.subplots()
    
    ax_a.plot(petrol_price['Date'],petrol_price['rate'])
    ax_a.axvline(x=pd.to_datetime('2020-01-01', format = "%Y/%m/%d")) # draw a line for denoting Covid -19
    col_3.pyplot(fig_a)
    col_3.caption('Petrol prices in Chennai from 2014 to August 2022')


    # plotting chennai prices in column 2
    fig_b,ax_b=plt.subplots()
    ax_b.plot(df_new['Date'],df_new[places[2]],label=places[i])
    ax_b.axvline(x=pd.to_datetime('2020-01-01', format = "%Y/%m/%d")) # draw a line for denoting 2020 Jan 1
    col_4.pyplot(fig_b)
    col_4.caption('Scaled commodity prices in Chennai from 2014 to August 2022')

    st.markdown("""
    
    > The line denotes the start of 2020, which can be seen as the start of Covid pandemic

    From the graphs, we can see that there is an increase of both fuel and food, specially in the last 2 years
    , so there is a **clear correlation** between the both. However we can't ascertain that the fuel prices have
    directly affected food prices in India, as there are various factors that the pandmic has brought up.
    
    #### Task 2:
    We can now analyse as to what products are highly correlated to fuel prices.
    Select a Product to see for yourself.
    """)

    col_5,col_6=st.columns(2)


    col_5.markdown("""
        <img src="https://images.unsplash.com/photo-1527018601619-a508a2be00cd" width="100%">
        """, unsafe_allow_html=True)
    col_5.caption('A Fuel Station')


    col_6.write("Select a commodity and a city to view its change in rate over the years, and compare it with the figure on the side")
    column_list=['Rice','Wheat','Atta (Wheat)','Gram Dal','Tur/Arhar Dal','Urad Dal','Moong Dal','Masoor Dal','Sugar',
            'Milk','Groundnut Oil (Packed)','Mustard Oil (Packed)','Vanaspati (Packed)','Soya Oil (Packed)','Sunflower Oil (Packed)',
            'Palm Oil (Packed)','Gur','Tea Loose','Salt Pack (Iodised)','Potato','Onion','Tomato']
    commodity = col_6.selectbox(
        'Which commodity would you like to analyse?', column_list )
    place=col_6.selectbox(
        'Which city would you like to view?', places )

 


    #plotting the prices for the selected commodity
    
    #commodity='Sunflower Oil (Packed)'
    fig_3,ax_3=plt.subplots()
    ax_3.plot(df_new['Date'],100*df_scaled[df_scaled["City"]==place][commodity].reset_index(drop=True),label='Scaled Commodity Price')
    ax_3.plot(petrol_price['Date'],petrol_price['rate'],label='Fuel Price')
    #ax_3.axvline(x=pd.to_datetime('2020-04-01', format = "%Y/%m/%d"))
    ax_3.legend()

    fig_3.set_figheight(10)
    fig_3.set_figwidth(15)
    st.pyplot(fig_3)
    st.caption('Change in price of '+commodity+' in '+place+' over the years')
    
    
    st.markdown("""

    > Note: There are a lot of combinations to work on, and plotting all the cities in the same plot makes it hard to analyse. Hence I have enabled you to view the carts individually.
    
    There are a lot of products analysed side by side with the fuel prices, and there are some commodities
    that show a positive correlation with fuel prices. Most of the high gains out of the ordinary inflation comes
    from various oils, that seem to have skyrocketed over the last 2 years, from 2019 end to 2022. Let us take a quick look at them.
    
    Look at the plots for some of the commmodities and fuel plots

    """)

    labels=['0','2014', '2015','2016','2017','2018','2019','2020','2021','2022','2023']
    f, ((ax_5, ax_6), (ax_7, ax_8)) = plt.subplots(2, 2)
    
    ax_5.plot(df_new['Date'],100*df_scaled[df_scaled["City"]=="CHENNAI"][column_list[12]].reset_index(drop=True),label='Scaled Commodity Price')
    ax_5.plot(petrol_price['Date'],petrol_price['rate'],label='Fuel Price')
    ax_5.set_xticklabels(labels=labels,rotation=90)
    ax_5.set_title(column_list[12])
    
    ax_6.plot(df_new['Date'],100*df_scaled[df_scaled["City"]=="MUMBAI"][column_list[13]].reset_index(drop=True),label='Scaled Commodity Price')
    ax_6.plot(petrol_price['Date'],petrol_price['rate'],label='Fuel Price')
    ax_6.set_xticklabels(labels=labels,rotation=90)
    ax_6.set_title(column_list[13])
    
    ax_7.plot(df_new['Date'],100*df_scaled[df_scaled["City"]=="CHENNAI"][column_list[14]].reset_index(drop=True),label='Scaled Commodity Price')
    ax_7.plot(petrol_price['Date'],petrol_price['rate'],label='Fuel Price')
    ax_7.set_xticklabels(labels=labels,rotation=90)
    ax_7.set_title(column_list[14])
    
    ax_8.plot(df_new['Date'],100*df_scaled[df_scaled["City"]=="CHENNAI"][column_list[15]].reset_index(drop=True),label='Scaled Commodity Price')
    ax_8.plot(petrol_price['Date'],petrol_price['rate'],label='Fuel Price')
    ax_8.set_xticklabels(labels=labels,rotation=90)
    ax_8.set_title(column_list[15])
    
    f.set_figheight(10)
    f.set_figwidth(15)
    st.pyplot(f)

    st.markdown("""
    
    These products are the only ones that have some correlation with the increasing fuel prices. Note something in common?
    > They all seem to be cooking oils. 

    Moreover, some of the products do not have any correlation with the fuel prices at all. 
    One such example is moong dal, which funnily is almost the exact opposite of fuel price trend. Take a look
    at the chart below.
    
    """)

    #plotting Moong Dal to show inverse petrol relation
    fig_10,ax_10=plt.subplots()
    ax_10.plot(df_new['Date'],100*df_scaled[df_scaled["City"]=="CHENNAI"][column_list[6]].reset_index(drop=True),label='Scaled Commodity Price')
    ax_10.plot(petrol_price['Date'],petrol_price['rate'],label='Fuel Price')
    #ax_3.axvline(x=pd.to_datetime('2020-04-01', format = "%Y/%m/%d"))
    ax_10.legend()
    ax_10.set_title(column_list[6])
    st.pyplot(fig_10)
    st.caption('Change in price of '+column_list[6]+' has no relation to fuel prices.')

    
    col_2a,col_2b=st.columns(2)
    col_2a.markdown("""
        <img src="https://media.istockphoto.com/photos/pile-mung-dal-or-moong-dal-a-lot-of-with-copy-space-for-text-concept-picture-id931337404" width="100%">
        """, unsafe_allow_html=True)
    col_2a.caption('Moong Dal')
    col_2b.markdown("""
    Hence, fuel prices are not a major factor in deciding the price of commodities, according to the data, 
    and it is mostly oils for some strange reason connnected to fuel prices in India. Let us now look back at our hypothesis 
    """)
    
    
    st.markdown("""
    #### Reviewing our Hypothesis:
    1. Fuel prices have increase, and so is the cost of essential commodities. They do share a common trend, but do not cause each other. As they say, " Correlation does not imply causation"
    2. Statement 2 is not completely True, and is most likely false. The data goes agaist pre conceived notion that fuel prices increases the cost of goods, but it seems like it doesn't, atleast accoring to the data. 
    """)

    st.markdown("""
    There is little to no provable relation between fuel prices and commodities. Some of the similarities we saw amounts to
    just a coincidence, due to the pandemic. We will look at pandemic specifically in the next Question (Question 3)  
    
    """)

with tabs[3]:
    st.header('Question 3')
    st.info("""**What are the effects of pre and post covid rates? To narrow down the question, Let us answer about the quantities that have
    drastically changed in price since 2020, which wasn't seen in the past 6 years.**""")

    st.markdown("""
    #### My Initial Hypothesis: 
    - Prices have definitely increased (I am obviously not living under a rock!), but I assume it has taken a hit in all the products.
    - There is regular inflation, but I have no idea as to how much prices have changed in the essential commodity segment. I predict that most of the products have increased in prices.
    
    """)
    
    st.markdown("""
    <img src="https://images.unsplash.com/photo-1584483766114-2cea6facdf57" width="100%">
    """, unsafe_allow_html=True)
    st.caption('COVID-19')
    
    

    #df_month.head()

    #make input for choosing the city and commodity
    st.write("Select a commodity and a city to view its change in rate over the years")
    # column_list=['Rice','Wheat','Atta (Wheat)','Gram Dal','Tur/Arhar Dal','Urad Dal','Moong Dal','Masoor Dal','Sugar',
    #         'Milk','Groundnut Oil (Packed)','Mustard Oil (Packed)','Vanaspati (Packed)','Soya Oil (Packed)','Sunflower Oil (Packed)',
    #         'Palm Oil (Packed)','Gur','Tea Loose','Salt Pack (Iodised)','Potato','Onion','Tomato']
    # commodity1 = st.selectbox(
    #     'Select a commodity', column_list )
    # place1=st.selectbox(
    #     'Select city to view?', places )

    #getting the monthly prices of a specific commodity
    
    #st.write(temp)


    col_11, col_12,col_13=st.columns(3)


    column_list=['Rice','Wheat','Atta (Wheat)','Gram Dal','Tur/Arhar Dal','Urad Dal','Moong Dal','Masoor Dal','Sugar',
            'Milk','Groundnut Oil (Packed)','Mustard Oil (Packed)','Vanaspati (Packed)','Soya Oil (Packed)','Sunflower Oil (Packed)',
            'Palm Oil (Packed)','Gur','Tea Loose','Salt Pack (Iodised)','Potato','Onion','Tomato']
    commodity1 = col_11.selectbox(
        'Select a commodity', column_list )
    place1=col_11.selectbox(
        'Select city to view?', places )


    commodity=column_list[12]
    df_month=df.groupby([pd.PeriodIndex(df['Date'], freq="Y"),'City'])[commodity1].mean()
    df_month=pd.DataFrame(df_month)
    df_month=df_month.reset_index()


    temp=df_month[df_month['City']==place1]
    temp['diff']=100*(temp[commodity1].diff()/temp[commodity1])
    temp['Date']=np.array(['2014', '2015','2016','2017','2018','2019','2020','2021','2022'])


    pre_cov_percentage=round(100*(temp.iloc[6,2]-temp.iloc[0,2])/temp.iloc[0,2],2)
    pre_cov=round(temp.iloc[6,2]-temp.iloc[0,2],2)
    col_12.metric('Pre-Covid Increase',pre_cov,str(pre_cov_percentage)+'%')
    post_cov_percentage=round(100*(temp.iloc[8,2]-temp.iloc[6,2])/temp.iloc[6,2],2)
    post_cov=round(temp.iloc[8,2]-temp.iloc[6,2],2)
    col_13.metric('Post-Covid Increase',post_cov,str(post_cov_percentage)+'%')


    #plotting prive increase over the years
    fig_11,ax_11=plt.subplots()
    ax_11.bar(temp['Date'],temp['diff'])
    ax_11.set_title(commodity1)
    st.pyplot(fig_11)
    st.caption('Change in price of '+commodity1+' over the years')


    st.markdown("""    
    Now, let us see an example of Lucknow city, and analyse the difference in the pre and post COVID rates.
    """)
    temp_inflation_rates=pd.read_csv('data/temp_inflation_rates.csv')
    temp_inflation_rates=temp_inflation_rates.sort_values('diff')

    fig_12,ax_12=plt.subplots()
    #st.write(temp_inflation_rates)
    ax_12.barh(temp_inflation_rates['commodity'],temp_inflation_rates['diff'])
    ax_12.set_title('Variation between pre and post COVID inflation')
    #ax_12.set_xticklabels(labels=temp_inflation_rates['commodity'].tolist(),rotation=90)
    ax_12.set_xlabel("Percentage")
    st.pyplot(fig_12)
    st.caption('Variation of Prices in Lucknow City for during the pre and post COVID eras')

    col_3a, col_3b=st.columns(2)

    col_3b.markdown("""
    <img src="https://images.unsplash.com/photo-1531501824979-4813e568563e" width="100%">""", unsafe_allow_html=True)
    col_3b.caption('Sunflowers')
    
    col_3a.markdown("""
    These results show that like what we saw in question 2, oils are the main culprit for the high rates duing the covid era. 
    Another interesting find is that "Masoor Dal", whose value seem to have skyrocketed after 2020. We can hence conclude our question
    from the Section 2, and conclude that the price increase is not fuel dependent, but was primarily due to the issues caused by the
    pandemic.
    
    """)
    st.markdown("""
    
    #### Reviewing my Hypothesis:
    1. There is certainly inflation, but it does have seem to have affected certain products like cooking oils and Masoor Dal.
    2. Not all products have record High inflation. Some products have come down in cost. This particualry seems the case due to high costs in the start of 2019, which has then subsided after a sudden shock in these 2 years
    """)

with tabs[4]:
    st.header('Question 4')
    st.info("""**Which food item has the highest variation of cost beteen cities on average? Did it increase over the years, or is it getting smaller? Also, Which commodity has increased in price by a lot? 
    To answer the question, let us compare the yearly avarage prices of commodities for the last 8 years**""")


    st.markdown("""
    #### My Initial Hypothesis: 
    
    
    """)
    
    
    yearly_std_dev=pd.read_csv('data/yearly_std_dev.csv')
    
    #plotting the standard deviation data.
    fig_13,ax_13=plt.subplots()
    column_list=['Rice','Wheat','Atta (Wheat)','Gram Dal','Tur/Arhar Dal','Urad Dal','Moong Dal','Masoor Dal','Sugar',
            'Milk','Groundnut Oil (Packed)','Mustard Oil (Packed)','Vanaspati (Packed)','Soya Oil (Packed)','Sunflower Oil (Packed)',
            'Palm Oil (Packed)','Gur','Tea Loose','Salt Pack (Iodised)','Potato','Onion','Tomato']
    for i in range(len(column_list)):
        ax_13.plot(yearly_std_dev["Year"],yearly_std_dev[column_list[i]],label=column_list[i])



    ax_13.axhspan(15,40,facecolor='#d62728',alpha=0.4)
    ax_13.axhspan(0,17,facecolor='#2ca02c',alpha=0.4)
    ax_13.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, shadow=True)
    ax_13.set_title("Standard deviation of commodities between cities")
    st.pyplot(fig_13)
    st.caption('Change in price of commodities between cities over the years. ')


    col_4c,col_4d=st.columns(2)
    col_4c.markdown("""
    <img src="https://images.unsplash.com/photo-1597003837092-f733b086d5aa" width="100%">""", unsafe_allow_html=True)
    col_4c.caption('A palm tree')

    col_4d.markdown("""
    This chart shows the variation of the prices of commodities between the cities over the years. 
    
    As we can see, the prices can be categorised into 2 parts, where the standard deviation is less than 15 and another is 
    from 15 to 40.

    Over the years, we can see that the deviation has started to reduce and has geared towards the under 20 mark.
    The culprit is again Oils in this case. Seems like Tea prices vary a lot, being the outlier in the case.
        
    """)

    st.subheader(' Variation in prices over the years')
    st.markdown("""
    Now, lets look at the actual increase in prices of commodities, and calcualte which is the 
    one that increased in price by al lot from 2014 to 2022.
    
    
    """)
    diff_list=pd.read_csv('data/diff_list.csv')
    diff_list=diff_list.sort_values('Increase Percentage')

    #metrics Plot
    col_4a,col_4b=st.columns(2)

    col_4a.metric("Lowest Increase",diff_list.iloc[0]['Commodity'],str(round(diff_list.iloc[0]['Increase Percentage'],2))+"%")
    col_4b.metric("Highest Increase",diff_list.iloc[-1]['Commodity'],str(round(diff_list.iloc[-1]['Increase Percentage'],2))+"%")


    #increase percentage plots
    fig14, ax14 =plt.subplots()
    
    ax14.barh(diff_list['Commodity'],diff_list['Increase Percentage'])

    ax14.set_title('Commodities and their Price Increase over 8 years')
    #ax_12.set_xticklabels(labels=temp_inflation_rates['commodity'].tolist(),rotation=90)
    ax14.set_xlabel("Increase Percentage")
    st.pyplot(fig14)
    #st.caption('Variation of Prices in Lucknow City for during the pre and post COVID eras')

    st.markdown("""
    As expected, oils are the major culprit, and have had the higest increase over the years.   
    """)

