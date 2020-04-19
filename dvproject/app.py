import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go # or plotly.express as px
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pycountry

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson') as response:
    counties = json.load(response)

dataset=pd.read_csv('hotel_bookings.csv')
df = pd.DataFrame(dataset)
list_alpha_2 = [i.alpha_2 for i in list(pycountry.countries)]
list_alpha_3 = [i.alpha_3 for i in list(pycountry.countries)]

df['country'].replace({"CN": "CAN"}, inplace=True)
# df1 = df.groupby(['hotel','adults','children','babies'])['stays_in_weekend_nights'].sum().reset_index(name ='stays_in_weekend_nights')
df1WeekendNights = df.groupby(['hotel'])['stays_in_weekend_nights'].sum().reset_index(name ='stays_in_weekend_nights')
# df1Melted = pd.melt(df1, id_vars =['hotel'], value_vars =['adults','children','babies'])
# df1City = df1Melted.loc[df1Melted['hotel'] == 'City Hotel']
# df1Resort = df1Melted.loc[df1Melted['hotel'] == 'Resort Hotel']
df1Adults = df.groupby(['hotel','stays_in_weekend_nights'])['adults'].sum().reset_index(name ='adults')
df1Adults = df1Adults[df1Adults['stays_in_weekend_nights']>0]
df1AdultsCity = df1Adults.loc[df1Adults['hotel'] == 'City Hotel']
df1AdultsResort = df1Adults.loc[df1Adults['hotel'] == 'Resort Hotel']
adultsCityWeekend = df1AdultsCity['adults'].sum()
adultsResortWeekend = df1AdultsResort['adults'].sum()

df1Children = df.groupby(['hotel','stays_in_weekend_nights'])['children'].sum().reset_index(name ='children')
df1Children = df1Children[df1Children['stays_in_weekend_nights']>0]
df1ChildrenCity = df1Children.loc[df1Children['hotel'] == 'City Hotel']
df1ChildrenResort = df1Children.loc[df1Children['hotel'] == 'Resort Hotel']
childrenCityWeekend = df1ChildrenCity['children'].sum()
childrenResortWeekend = df1ChildrenResort['children'].sum()

df1Babies = df.groupby(['hotel','stays_in_weekend_nights'])['babies'].sum().reset_index(name ='babies')
df1Babies = df1Babies[df1Babies['stays_in_weekend_nights']>0]
df1BabiesCity = df1Babies.loc[df1Babies['hotel'] == 'City Hotel']
df1BabiesResort = df1Babies.loc[df1Babies['hotel'] == 'Resort Hotel']
babiesCityWeekend = df1BabiesCity['babies'].sum()
babiesResortWeekend = df1BabiesResort['babies'].sum()

# df2 = df.groupby(['hotel','adults','children','babies'])['stays_in_week_nights'].sum().reset_index(name ='stays_in_week_nights')
df2WeekNights = df.groupby(['hotel'])['stays_in_week_nights'].sum().reset_index(name ='stays_in_week_nights')
# df2Melted = pd.melt(df2, id_vars =['hotel'], value_vars =['adults','children','babies'])
# df2City = df2Melted.loc[df2Melted['hotel'] == 'City Hotel']
# df2Resort = df2Melted.loc[df2Melted['hotel'] == 'Resort Hotel']
df2Adults = df.groupby(['hotel','stays_in_week_nights'])['adults'].sum().reset_index(name ='adults')
df2Adults = df2Adults[df2Adults['stays_in_week_nights']>0]
df2AdultsCity = df2Adults.loc[df2Adults['hotel'] == 'City Hotel']
df2AdultsResort = df2Adults.loc[df2Adults['hotel'] == 'Resort Hotel']
adultsCityWeek = df2AdultsCity['adults'].sum()
adultsResortWeek = df2AdultsResort['adults'].sum()

df2Children = df.groupby(['hotel','stays_in_week_nights'])['children'].sum().reset_index(name ='children')
df2Children = df2Children[df2Children['stays_in_week_nights']>0]
df2ChildrenCity = df2Children.loc[df2Children['hotel'] == 'City Hotel']
df2ChildrenResort = df2Children.loc[df2Children['hotel'] == 'Resort Hotel']
childrenCityWeek = df2ChildrenCity['children'].sum()
childrenResortWeek = df2ChildrenResort['children'].sum()

df2Babies = df.groupby(['hotel','stays_in_week_nights'])['babies'].sum().reset_index(name ='babies')
df2Babies = df2Babies[df2Babies['stays_in_week_nights']>0]
df2BabiesCity = df2Babies.loc[df2Babies['hotel'] == 'City Hotel']
df2BabiesResort = df2Babies.loc[df2Babies['hotel'] == 'Resort Hotel']
babiesCityWeek = df2BabiesCity['babies'].sum()
babiesResortWeek = df2BabiesResort['babies'].sum()

months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6,
          "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

dfMonth = df.groupby(['arrival_date_month','hotel'])['hotel'].count().reset_index(name ='month')
dfMonth['monthno'] = dfMonth['arrival_date_month'].apply(lambda x: months[x])
dfMonth.sort_values(by=['monthno'], inplace=True)
dfYear = df.groupby(['arrival_date_year','hotel'])['hotel'].count().reset_index(name ='year')
dfWeek = df.groupby(['arrival_date_week_number','hotel'])['hotel'].count().reset_index(name ='week')
dfDay = df.groupby(['arrival_date_day_of_month','hotel'])['hotel'].count().reset_index(name ='day')
dfMonthCity = dfMonth.loc[dfMonth['hotel'] == 'City Hotel']
dfMonthResort = dfMonth.loc[dfMonth['hotel'] == 'Resort Hotel']
dfYearCity = dfYear.loc[dfYear['hotel'] == 'City Hotel']
dfYearResort = dfYear.loc[dfYear['hotel'] == 'Resort Hotel']
dfDayCity = dfDay.loc[dfDay['hotel'] == 'City Hotel']
dfDayResort = dfDay.loc[dfDay['hotel'] == 'Resort Hotel']
dfWeekCity = dfWeek.loc[dfWeek['hotel'] == 'City Hotel']
dfWeekResort = dfWeek.loc[dfWeek['hotel'] == 'Resort Hotel']

dfMeal = df.groupby(['meal','hotel','arrival_date_month'])['hotel'].count().reset_index(name ='mealtype')
# dfMeal['meal'].replace({"Undefined": "Meal not mentioned"}, inplace=True)
dfDeposit = df.groupby(['deposit_type','hotel','arrival_date_month'])['hotel'].count().reset_index(name ='deposit')
dfCustomer = df.groupby(['customer_type','hotel','arrival_date_month'])['hotel'].count().reset_index(name ='customer')
dfMealCity = dfMeal.loc[dfMeal['hotel'] == 'City Hotel']
dfMealResort = dfMeal.loc[dfMeal['hotel'] == 'Resort Hotel']
dfDepositCity = dfDeposit.loc[dfDeposit['hotel'] == 'City Hotel']
dfDepositResort = dfDeposit.loc[dfDeposit['hotel'] == 'Resort Hotel']
dfCustomerCity = dfCustomer.loc[dfCustomer['hotel'] == 'City Hotel']
dfCustomerResort = dfCustomer.loc[dfCustomer['hotel'] == 'Resort Hotel']

dfCountry = df.groupby(['country','hotel'])['hotel'].count().reset_index(name ='countrynumber')
dfCountryCancelled = df.groupby(['country','is_canceled','hotel'])['hotel'].count().reset_index(name ='countrynumber')
dfCountryCancelled = dfCountryCancelled[dfCountryCancelled['is_canceled']>0]

dfBookings = df.groupby(['booking_changes','hotel'])['hotel'].count().reset_index(name ='Number of Booking')

dfBookings.rename(columns={'booking_changes':'Total Booking Changes','hotel':'Hotel'},inplace=True)


def countryNameFunction(df):
    countryName = []
    for index, row in df.iterrows():
        if (row['country'] in list_alpha_3):
            countryName.append(pycountry.countries.get(alpha_3=row['country']).name)
        else:
            countryName.append('Invalid Code')
    return countryName

dfCountry['CountryName'] = countryNameFunction(dfCountry)
dfCountryCity = dfCountry.loc[dfCountry['hotel'] == 'City Hotel']
dfCountryResort = dfCountry.loc[dfCountry['hotel'] == 'Resort Hotel']

# countryName1 = []
# for index, row in dfCountryCancelled.iterrows():
#     if (row['country'] in list_alpha_3):
#       countryName1.append(pycountry.countries.get(alpha_3=row['country']).name)
#     else:
#       countryName1.append('Invalid Code')

dfCountryCancelled['CountryName'] = countryNameFunction(dfCountryCancelled)
dfCountryCancelledCity = dfCountryCancelled.loc[dfCountryCancelled['hotel'] == 'City Hotel']
dfCountryCancelledResort = dfCountryCancelled.loc[dfCountryCancelled['hotel'] == 'Resort Hotel']

def SetColor(x):
    if(x == "City Hotel"):
        return "green"
    else:
        return "red"
fig1 = go.Figure() # or any Plotly Express function e.g. px.bar(...)
fig1.add_trace(go.Bar(
    name='Weekend Nights',
    x=df1WeekendNights['hotel'],
    y=df1WeekendNights['stays_in_weekend_nights'],
    customdata=df1WeekendNights[['stays_in_weekend_nights']],
    hovertemplate = "Number Of stays: %{customdata[0]}",
    marker_color=['rgb(223,101,176)','rgb(223,101,176)'],
    text=df1WeekendNights['stays_in_weekend_nights'])
)
fig1.add_trace(go.Bar(
    name='Weekday Nights',
    x=df2WeekNights['hotel'],
    y=df2WeekNights['stays_in_week_nights'],
    customdata=df2WeekNights[['stays_in_week_nights']],
    hovertemplate = "Number Of stays: %{customdata[0]}",
    marker_color=['#fb9b06','#fb9b06'],
    text=df2WeekNights['stays_in_week_nights'])
)

# Change the bar mode
fig1.update_traces(texttemplate='%{text}', textposition='outside', textfont_size=10,marker_line_color='black',marker_line_width=1.5,hoverlabel={'namelength':0})
fig1.update_layout(barmode='group')
fig1.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
    xaxis = dict(showgrid=False),
    yaxis = dict(showgrid=False),
    yaxis_title="Total Number of Bookings",
    xaxis_title="Type of Hotel",
    title = "Stays on Weekend and Weekday nights",
    margin=dict(l=40, r=40, t=40, b=40),
    plot_bgcolor='rgba(0,0,0,0)'
)
colors = ['rgb(250,164,118)', 'rgb(206,102,147)', 'rgb(113,50,141)']
title = ['Customers in Weekend Nights', 'Customers in Weekday Nights']
labels = ['Adults','Children','Babies']
value1 = np.array(adultsCityWeekend)
value1 = np.append(value1,childrenCityWeekend)
value1 = np.append(value1,babiesCityWeekend)
value2 = np.array(adultsCityWeek)
value2 = np.append(value2,childrenCityWeek)
value2 = np.append(value2,babiesCityWeek)
fig2 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]]);
fig2.add_trace(go.Pie(labels=labels, values=value1, name="Customers in Weekend Nights"),1,1)
fig2.add_trace(go.Pie(labels=labels, values=value2, name="Customers in Week Nights"),1,2)
fig2.update_traces(hoverinfo='label+percent', textfont_size=20, marker=dict(colors=colors,line=dict(color='#000000', width=0.5)),hole=0.4,hoverlabel={'namelength':0})
fig2.update_layout(hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
    legend_title='Customers',
    annotations=[dict(text='Weekend', x=0.185, y=0.5, font_size=20, showarrow=False),
                    dict(text='Nights', x=0.20, y=0.4, font_size=20, showarrow=False),
                 dict(text='Weekday', x=0.82, y=0.5, font_size=20, showarrow=False),
                   dict(text='Nights', x=0.80, y=0.4, font_size=20, showarrow=False)],
    title = "Total Number of customers in City Hotel")

value3 = np.array(adultsResortWeekend)
value3 = np.append(value3,childrenResortWeekend)
value3 = np.append(value3,babiesResortWeekend)
value4 = np.array(adultsResortWeek)
value4 = np.append(value4,childrenResortWeek)
value4 = np.append(value4,babiesResortWeek)
fig3 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]]);
fig3.add_trace(go.Pie(labels=labels, values=value3, name="Customers in Weekend Nights"),1,1)
fig3.add_trace(go.Pie(labels=labels, values=value4, name="Customers in Week Nights"),1,2)
fig3.update_traces(hoverinfo='label+percent', textfont_size=20, marker=dict(colors=colors,line=dict(color='#000000', width=0.5)),hole=0.4,hoverlabel={'namelength':0})
fig3.update_layout(hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
    legend_title='Customers',
    annotations=[dict(text='Weekend', x=0.185, y=0.5, font_size=20, showarrow=False),
                    dict(text='Nights', x=0.20, y=0.4, font_size=20, showarrow=False),
                 dict(text='Weekday', x=0.82, y=0.5, font_size=20, showarrow=False),
                   dict(text='Nights', x=0.80, y=0.4, font_size=20, showarrow=False)],
    title = "Total Number of customers in Resort Hotel")

fig4 = go.Figure()
fig4.add_trace(
    go.Scatter(
        x=dfMonthCity['arrival_date_month'],
        y=dfMonthCity['month'],
        hovertemplate =
        'Month: %{x}'+
        '<br>Value: %{y}<br>',
        mode="markers",
        name="City Hotel",
        opacity=0.5,
        marker=dict(
            size=15,
            color='rgb(241,105,19)',
            line=dict(width=2,color='black')
        ))
)
fig4.add_trace(
    go.Scatter(
        x=dfMonthResort['arrival_date_month'],
        y=dfMonthResort['month'],
        hovertemplate =
        'Month: %{x}'+
        '<br>Value: %{y}<br>',
        mode="markers",
        name="Resort Hotel",
        opacity=0.5,
        marker=dict(
            size=15,
            color='rgb(158,89,135)',
            line=dict(width=2,color='black')
        ))
)
fig4.add_trace(
    go.Scatter(
        x=dfDayCity['arrival_date_day_of_month'],
        y=dfDayCity['day'],
        hovertemplate =
        'Day: %{x}'+
        '<br>Value: %{y}<br>',
        visible=False,
        mode="markers",
        name="City Hotel",
        opacity=0.5,
        marker=dict(
            size=15,
            color='rgb(241,105,19)',
            line=dict(width=2,color='black')
        ))
)
fig4.add_trace(
    go.Scatter(
        x=dfDayResort['arrival_date_day_of_month'],
        y=dfDayResort['day'],
        hovertemplate =
        'Day: %{x}'+
        '<br>Value: %{y}<br>',
        visible=False,
        mode="markers",
        name="Resort Hotel",
        opacity=0.5,
        marker=dict(
            size=15,
            color='rgb(158,89,135)',
            line=dict(width=2,color='black')
        ))
)

fig4.add_trace(
    go.Scatter(
        x=dfYearCity['arrival_date_year'],
        y=dfYearCity['year'],
        hovertemplate =
        'Year: %{x}'+
        '<br>Value: %{y}<br>',
        name="City Hotel",
        visible=False,
        mode="markers",
        opacity=0.5,
        marker=dict(
            size=15,
            color='rgb(241,105,19)',
            line=dict(width=2,color='black')
        ))
)

fig4.add_trace(
    go.Scatter(
        x=dfYearResort['arrival_date_year'],
        y=dfYearResort['year'],
        hovertemplate =
        'Year: %{x}'+
        '<br>Value: %{y}<br>',
        visible=False,
        mode="markers",
        name="Resort Hotel",
        opacity=0.5,
        marker=dict(
            size=15,
            color='rgb(158,89,135)',
            line=dict(width=2,color='black')
        ))
)

fig4.add_trace(
    go.Scatter(
        x=dfWeekCity['arrival_date_week_number'],
        y=dfWeekCity['week'],
        hovertemplate =
        'Week: %{x}'+
        '<br>Value: %{y}<br>',
        visible=False,
        mode="markers",
        name="City Hotel",
        opacity=0.5,
        marker=dict(
            size=15,
            color='rgb(241,105,19)',
            line=dict(width=2,color='black')
        ))
)

fig4.add_trace(
    go.Scatter(
        x=dfWeekResort['arrival_date_week_number'],
        y=dfWeekResort['week'],
        hovertemplate =
        'Week: %{x}'+
        '<br>Value: %{y}<br>',
        visible=False,
        mode="markers",
        name="Resort Hotel",
        opacity=0.5,
        marker=dict(
            size=15,
            color='rgb(158,89,135)',
            line=dict(width=2,color='black'))
        )
)
# fig4.update_traces(hoverlabel={'namelength':0})

fig4.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(label="Month",
                     method="update",
                     args=[{"visible": [True, True, False, False, False, False, False, False]},
                           {    "title":"Count of Customers in a Month",
                               "xaxis":{"title":"Month"}}]),
                dict(label="Day",
                     method="update",
                     args=[{"visible": [False, False, True, True, False, False, False, False]},
                           {"title":"Count of Customers in a Day",
                               "xaxis":{"title":"Day in Month"}}]),
                dict(label="Year",
                     method="update",
                     args=[{"visible": [False, False, False, False, True, True, False, False]},
                           {"title":"Count of Customers in a Year",
                               "xaxis":{"title":"Year","tickmode":"array","tickvals":dfYearResort['arrival_date_year'], "ticktext":dfYearResort['arrival_date_year']}}]),
                dict(label="Week",
                     method="update",
                     args=[{"visible": [False, False, False, False, False, False, True, True]},
                           {"title":"Count of Customers in a Week",
                               "xaxis":{"title":"Week Number"}}])
            ]),
        )
    ])
fig4.update_layout(
    hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
    legend_title='Hotel',
    title = "Count of Customers in a Month",
    xaxis_title="Month",
    yaxis_title="Number of Customers",
    margin=dict(l=40, r=40, t=40, b=40),
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=True
)


fig6 = go.Figure()
fig6.add_trace(go.Choroplethmapbox(geojson=counties, locations=dfCountryCity['country'], z=dfCountryCity['countrynumber'],featureidkey="properties.ISO_A3",
                                    colorscale="Agsunset", zmin=0, zmax=12, marker_line_width=1,colorbar=dict(title='Bookings'),text=dfCountryCity['CountryName'],hovertemplate = 'Country: %{text}'+'<br>Value: %{z}<br>',name="Bookings"))
fig6.add_trace(go.Choroplethmapbox(geojson=counties, locations=dfCountryCancelledCity['country'], z=dfCountryCancelledCity['countrynumber'],featureidkey="properties.ISO_A3",
                                    colorscale="Agsunset", zmin=0, zmax=12, marker_line_width=1,visible=False,colorbar=dict(title='Cancellations'),text=dfCountryCancelledCity['CountryName'],hovertemplate = 'Country: %{text}'+'<br>Value: %{z}<br>',name="Cancellations",))

fig6.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(label="Bookings",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title":"Number of Bookings"}]),
                dict(label="Cancellations",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title":"Number of Cancellations"}])
            ]),
        )
    ])

fig6.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig6.update_layout(hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
    title = "Number of Bookings",margin={"r":40,"t":40,"l":40,"b":40},autosize=False,
    width= 1400,
    height=800)


fig7 = go.Figure()
fig7.add_trace(go.Choroplethmapbox(geojson=counties, locations=dfCountryResort['country'], z=dfCountryResort['countrynumber'],featureidkey="properties.ISO_A3",
                                    colorscale="Agsunset", zmin=0, zmax=12, marker_line_width=1,colorbar=dict(title='Booking Count'),text=dfCountryResort['CountryName'],hovertemplate = 'Country: %{text}'+'<br>Value: %{z}<br>',name="Bookings"))
fig7.add_trace(go.Choroplethmapbox(geojson=counties, locations=dfCountryCancelledResort['country'], z=dfCountryCancelledResort['countrynumber'],featureidkey="properties.ISO_A3",
                                    colorscale="Agsunset", zmin=0, zmax=12, marker_line_width=1,visible=False,colorbar=dict(title='Cancellation Count'),text=dfCountryCancelledResort['CountryName'],hovertemplate = 'Country: %{text}'+'<br>Value: %{z}<br>',name="Cancellations",))

fig7.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(label="Bookings",
                     method="update",
                     args=[{"visible": [True, False]},
                           {"title":"Number of Bookings"}]),
                dict(label="Cancellations",
                     method="update",
                     args=[{"visible": [False, True]},
                           {"title":"Number of Cancellations"}])
            ]),
        )
    ])

fig7.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=1, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig7.update_layout(hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),
    title = "Number of Bookings",margin={"r":40,"t":40,"l":40,"b":40},autosize=False,
    width=1400,
    height=800)

fig5 = px.bar(dfBookings, x="Hotel", y="Number of Booking", color="Hotel",
  animation_frame="Total Booking Changes",color_discrete_map = {"City Hotel": "rgb(238,138,130)", "Resort Hotel": "rgb(160,89,160)"} )
fig5.update_traces(marker_line_color='black',marker_line_width=1.5,hoverlabel={'namelength':0})
fig5.update_layout(sliders = {'transition' : {'duration': 10000}},hoverlabel=dict(
        bgcolor="white",
        font_size=16,
        font_family="Rockwell"
    ),legend_title='Hotel',
    title = "Booking Changes",margin={"r":40,"t":40,"l":40,"b":40},plot_bgcolor='rgba(0,0,0,0)')
fig5.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 2000
fig5.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1200


# external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = dash.Dash()
# Boostrap CSS.
colors = {
    'background': 'rgb(224,224,223)',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.Div([
            html.H1(children="Hotel Booking Demand",style={
                'textAlign': 'center'
            }),
            html.Div(children='This visualization shows the pattern of bookings and cancellations done by a customer. Two types of hotel has been showcased in this - City Hotel and Resort Hotel. The graphs shown in the visualization capture only some aspects of the dataset because of its large size', style={
                'textAlign': 'center'
            }),
        ]),
        html.Br([]),
        html.Div([
            html.H3(children="Number of Bookings and Cancellations"),
            html.Div(children='This plot shows the count of bookings and cancellations done by guests of a particular nationality. Two tabs have been included to show these numbers for City as well as Resort Hotel'),
        ]),
        html.Div([
            dcc.Tabs([
                dcc.Tab(label='City Hotel', children=[
                    dcc.Graph(figure=fig6)
                ]),
                dcc.Tab(label='Resort Hotel', children=[
                    dcc.Graph(figure=fig7)
                ]),
            ])
        ]),
        html.Div([
            html.H3(children="Arrival of customers according to day,month,week,year"),
            html.Div(
                children='This scatter plot shows at which time a customer usually arrives in a City hotel or a Resort hotel. It depicts number of customers on daily, monthly, yearly and weekly basis'
                ),
        ]),
        html.Div([
            dcc.Graph(figure=fig4)
        ]),
        html.Div([
            html.H3(children="Customers staying on Weekend and Weekday nights"),
            html.Div(
                children='This chart shows the count of customers booking for a weekend of a weekday night in both type of hotels. The pie chart depicts the bifurcation of these customers into adults, children and babies for City as well as Resort hotel'
                ),
        ]),
        html.Div([
            dcc.Graph(figure=fig1)
        ]),
        html.Div([
            dcc.Graph(figure=fig2)
        ]),
        html.Div([
            dcc.Graph(figure=fig3)
        ]),
        html.Div([
            html.H3(children="Booking Changes for City and Resort Hotels"),
            html.Div(
                children='This animated bar chart shows how often the booking changes are made by a customer for both type of hotels. It also depicts how many guests made these booking changes.'
                ),
        ]),
        html.Div([
            dcc.Graph(figure=fig5)
        ])
])

app.run_server(debug=True)  # Turn off reloader if inside Jupyter
