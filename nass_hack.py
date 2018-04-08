"""nasscom-hack"""
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from weather import Weather, Unit
from wordcloud import WordCloud

sns.set()
df_path="M:\\Madhuri\\NASSCOM\\Nasscom_hack-master\\cleaned_series.xlsx"
imgpath = "M:\\Madhuri\\NASSCOM\\Kisan Nxt\\Kisan Nxt\\Images"

df=pd.read_excel(df_path)

def gen_charts(state):
    #word-cloud
    img_pth ={}
    df["StateName"]=df["StateName"].apply(lambda x: x.lower())
    df_tamil=df[df["StateName"]==state.lower()]
    df["StateName"]=df["StateName"].apply(lambda x: x.title())
    wordcloud2 = WordCloud().generate(' '.join(df_tamil['QueryText']))
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud2)
    plt.axis("off")
    print("ooo",imgpath)
    plt.savefig(imgpath+"\\wordcloud.jpg")
    plt.close()
    plt.clf()
    img_pth['plot1']=imgpath+"\\wordcloud.jpg"
    #bar-chart
    temp=df_tamil["DistrictName"].value_counts().to_frame().reset_index()
    g=sns.barplot(x="index",y="DistrictName",data=temp)
    loc, labels = plt.xticks()
    g.set_xticklabels(labels,rotation=90)
    plt.xlabel("Districts")
    plt.ylabel("Query Count")
    plt.title("Query Count for "+state)
    plt.tight_layout()
    plt.savefig(imgpath+"\\bar_chart.jpg")
    #plt.show()
    plt.clf()
    img_pth['plot2']=imgpath+"\\bar_chart.jpg"
    #fig.show()
    #fig.close()
    #line-chart
    temp=df_tamil[["CreatedYear","CreatedMonth","Season"]].groupby(["CreatedYear","CreatedMonth"]).count().reset_index()
    temp.set_index("CreatedMonth",inplace=True)
    temp.index = pd.CategoricalIndex(temp.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
    temp=temp.sort_index()
    temp.reset_index(inplace=True)
    k=sns.pointplot(x="CreatedMonth",y="Season",data=temp)
    
    #fig1.show()
    plt.xlabel("Months")
    plt.ylabel("Query Count")
    plt.title("Month wise Trend")
    plt.tight_layout()
    plt.savefig(imgpath+"\\line_chart.jpg")
    #plt.show()
    plt.clf()
    img_pth['plot3']=imgpath+"\\line_chart.jpg"
    #fig.close()
    print("charts are saved")
    #general-heatmap
    temp=df[["StateName","Sector","Season"]].groupby(by=["StateName","Sector"]).count().reset_index()
    result = temp.pivot(index='StateName', columns='Sector', values='Season')
    g=sns.heatmap(result,cmap="RdBu_r")
    loc, labels = plt.yticks()
    g.set_yticklabels(labels,rotation=90)
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Sectorwise & Statewise Query Count')
    plt.tight_layout()
    plt.savefig(imgpath+"\\heatmap.jpg")
    img_pth['plot4']=imgpath+"\\heatmap.jpg"
    return img_pth
    
    #plt.show()


def weather_by_city(city):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    condition = location.condition
    current_condition=condition.text
    current_temp=location.print_obj["item"]["condition"]["temp"]
    forecasts = location.forecast
    weather_df={}
    weather_df['Text']=current_condition
    weather_df['Temp']=current_temp
    #for forecast in forecasts:
     #   weather_df[forecast.date]={}
      #  weather_df[forecast.date]['Text']=forecast.text
       # weather_df[forecast.date]['Min']=forecast.low
        #weather_df[forecast.date]['Max']=forecast.high
    return weather_df
