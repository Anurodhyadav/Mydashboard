import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from bokeh.io import show,output_file
from bokeh.plotting import figure
from bokeh.models import HoverTool,CategoricalColorMapper
from bokeh.layouts import widgetbox,row
from bokeh.transform import cumsum
from bokeh.palettes import Category20c
import math
from operator import add

def main():
    st.title('Diseases in Nepal from 2011/12 to 2013/14')
    st.sidebar.title('Diseases in Nepal')
    st.markdown('View diseases in Nepal')
    year=['2011/12','2012/13','2013/14']
    
    @st.cache(persist=True)
    def load_data():
        data=pd.read_csv("https://github.com/Anurodhyadav/DiesesNepalVizualization/raw/master/dieses.csv")
        return data
    df=load_data()
  

    Dieses=list(set(df['Sub-Indicator']))
    Dieses.sort()
    Mountain_2011=np.zeros(14)
    Hill_2011=np.zeros(14)
    Terai_2011=np.zeros(14)
    Mountain_2012=np.zeros(14)
    Hill_2012=np.zeros(14)
    Terai_2012=np.zeros(14)
    Mountain_2013=np.zeros(14)
    Hill_2013=np.zeros(14)
    Terai_2013=np.zeros(14)

    @st.cache(persist=True)   
    def nepal_total_bar():
        for i,j in enumerate(Dieses):
            for index,row in df.iterrows():
                if (row['Ecological Belt']=='Mountain' and row['Year (AD)']=='2011/12'  and row['Sub-Indicator']==j):
                    Mountain_2011[i]=Mountain_2011[i]+row['Value']
                elif (row['Ecological Belt']=='Hill' and row['Year (AD)']=='2011/12'  and row['Sub-Indicator']==j):
                    Hill_2011[i]=Hill_2011[i]+row['Value']
                elif(row['Ecological Belt']=='Terai' and row['Year (AD)']=='2011/12'  and row['Sub-Indicator']==j):
                    Terai_2011[i]=Terai_2011[i]+row['Value']
        
        for i,j in enumerate(Dieses):
            for index,row in df.iterrows():
                if (row['Ecological Belt']=='Mountain' and row['Year (AD)']=='2012/13'  and row['Sub-Indicator']==j):
                    Mountain_2012[i]=Mountain_2012[i]+row['Value']
                elif (row['Ecological Belt']=='Hill' and row['Year (AD)']=='2012/13'  and row['Sub-Indicator']==j):
                    Hill_2012[i]=Hill_2012[i]+row['Value']
                elif(row['Ecological Belt']=='Terai' and row['Year (AD)']=='2012/13'  and row['Sub-Indicator']==j):
                    Terai_2012[i]=Terai_2012[i]+row['Value']

        for i,j in enumerate(Dieses):
            for index,row in df.iterrows():
                if (row['Ecological Belt']=='Mountain' and row['Year (AD)']=='2013/14'  and row['Sub-Indicator']==j):
                    Mountain_2013[i]=Mountain_2013[i]+row['Value']
                elif (row['Ecological Belt']=='Hill' and row['Year (AD)']=='2013/14'  and row['Sub-Indicator']==j):
                    Hill_2013[i]=Hill_2013[i]+row['Value']
                elif(row['Ecological Belt']=='Terai' and row['Year (AD)']=='2013/14'  and row['Sub-Indicator']==j):
                    Terai_2013[i]=Terai_2013[i]+row['Value']

        Mountain_2011_total=Mountain_2011.sum()
        Hill_2011_total=Hill_2011.sum()
        Terai_2011_total=Terai_2011.sum()

        Mountain_2012_total=Mountain_2012.sum()
        Hill_2012_total=Hill_2012.sum()
        Terai_2012_total=Terai_2012.sum()

        Mountain_2013_total=Mountain_2013.sum()
        Hill_2013_total=Hill_2013.sum()
        Terai_2013_total=Terai_2013.sum()

        Mountain_total=[Mountain_2011_total,Mountain_2012_total,Mountain_2013_total]
        Hill_total=[Hill_2011_total,Hill_2012_total,Hill_2013_total]
        Terai_total=[Terai_2011_total,Terai_2012_total,Terai_2013_total]

        return Mountain_total,Hill_total,Terai_total,Mountain_2011,Hill_2011,Terai_2011,Mountain_2012,Terai_2012,Hill_2012,Mountain_2013,Hill_2013,Terai_2013
    
    Mountain_total,Hill_total,Terai_total,Mountain_2011,Hill_2011,Terai_2011,Mountain_2012,Terai_2012,Hill_2012,Mountain_2013,Hill_2013,Terai_2013=nepal_total_bar()

    if st.checkbox('Show Plot of diseases from 2011/12 to 2013/14',False):
        st.subheader('*Total number of diseases found in nepal from 2011 to 2014')
        year=['2011/12','2012/13','2013/14']
        plt.figure(figsize=(20,10))
        ax=plt.gca()
        myx=np.arange(3)
        width=0.3 
        rects1=ax.bar(myx-width/2,Mountain_total,width,label='Mountain')
        rects2=ax.bar(myx+width/2,Hill_total,width,label='Hill')
        rects3=ax.bar(myx+width/2+width,Terai_total,width,label='Terai')
        ax.legend()
        ax.set_xlabel('Year',fontsize=20)
        ax.set_ylabel('Total number of diseases',fontsize=20)
        ax.set_xticks(myx)
        ax.set_title('Total number of diseases found in nepal from 2011 to 2014',fontsize=25)
        ax.set_xticklabels(year)

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


        autolabel(rects1)
        autolabel(rects2)
        autolabel(rects3)
        st.pyplot()
    
    
    a=list(map(add,Mountain_2011,Hill_2011))
    Nepal_pie_2011=list(map(add,a,Terai_2011))
    
    b =list(map(add,Mountain_2012,Hill_2012))
    Nepal_pie_2012=list(map(add,b,Terai_2012))
    
    c=list(map(add,Mountain_2013,Hill_2013))
    Nepal_pie_2013=list(map(add,c,Terai_2013))
    
     
    st.sidebar.subheader('Diseases distribution per year')
    st.sidebar.markdown('Show by distribution of diseases in given year')
    piechart=st.sidebar.multiselect('**More than one can be selected',("Nepal_pie_2011","Nepal_pie_2012","Nepal_pie_2013"))
   
    if "Nepal_pie_2011" in piechart:
        st.subheader('*Diseases in Nepal in 2011')
        st.markdown('**Hover over to see the data')
        e=dict(zip(Dieses,Nepal_pie_2011))
        data = pd.Series(e).reset_index(name='value').rename(columns={'index':'dieses'})
        data['value'] = pd.to_numeric(data['value'],errors='coerce')
        data['angle'] = data['value'].astype(float)/data['value'].astype(float).sum()*2*math.pi
        data['color'] = Category20c[len(e)]
        data['percentage']=data['value'].astype(float)/data['value'].astype(float).sum()

        p = figure(plot_height=500,plot_width=800, title="Diseases in Nepal in 2011/12", toolbar_location=None,
           tools="hover", tooltips="@dieses: @value:Percentage:@percentage{%0.2f}", x_range=(-0.5, 1.0))

        p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color',legend='dieses',source=data)

        p.legend.location='bottom_right'
        p.axis.axis_label=None
        p.axis.visible=False
        p.grid.grid_line_color = None
        st.bokeh_chart(p)

    if "Nepal_pie_2012" in piechart:
        st.subheader('*Diseases in Nepal in 2012')
        st.markdown('**Hover over to see the data')
        e=dict(zip(Dieses,Nepal_pie_2012))
        data = pd.Series(e).reset_index(name='value').rename(columns={'index':'dieses'})
        data['value'] = pd.to_numeric(data['value'],errors='coerce')
        data['angle'] = data['value'].astype(float)/data['value'].astype(float).sum()*2*math.pi
        data['color'] = Category20c[len(e)]
        data['percentage']=data['value'].astype(float)/data['value'].astype(float).sum()

        p = figure(plot_height=500,plot_width=800, title="Diseases in Nepal in 2012/13", toolbar_location=None,
           tools="hover", tooltips="@dieses: @value:Percentage:@percentage{%0.2f}", x_range=(-0.5, 1.0))

        p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color',legend='dieses',source=data)

        p.legend.location='bottom_right'
        p.axis.axis_label=None
        p.axis.visible=False
        p.grid.grid_line_color = None
        st.bokeh_chart(p)

    if "Nepal_pie_2013" in piechart:
        st.subheader('*Diseases in Nepal in 2013')
        st.markdown('**Hover over to see the data')
        e=dict(zip(Dieses,Nepal_pie_2013))
        data = pd.Series(e).reset_index(name='value').rename(columns={'index':'dieses'})
        data['value'] = pd.to_numeric(data['value'],errors='coerce')
        data['angle'] = data['value'].astype(float)/data['value'].astype(float).sum()*2*math.pi
        data['color'] = Category20c[len(e)]
        data['percentage']=data['value'].astype(float)/data['value'].astype(float).sum()

        p = figure(plot_height=500,plot_width=800, title="Dieses in Nepal in 2013/14", toolbar_location=None,
           tools="hover", tooltips="@dieses: @value:Percentage:@percentage{%0.2f}", x_range=(-0.5, 1.0))

        p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color',legend='dieses',source=data)

        p.legend.location='bottom_right'
        p.axis.axis_label=None
        p.axis.visible=False
        p.grid.grid_line_color = None
        st.bokeh_chart(p)
    myDieses=['None Selected']+Dieses
    st.sidebar.subheader('Diseases found across years')
    alldieses = st.sidebar.selectbox("Show by Dieses across Nepal",myDieses)

    if alldieses is not 'None Selected':
        My_Mountain=np.zeros(3)
        My_Mountain_2011=0
        My_Mountain_2012=0
        My_Mountain_2013=0
        My_Hill=np.zeros(3)
        My_Hill_2011=0
        My_Hill_2012=0
        My_Hill_2013=0
        My_Terai=np.zeros(3)
        My_Terai_2011=0
        My_Terai_2012=0
        My_Terai_2013=0
        for index,row in df.iterrows():
            if(row['Ecological Belt']=='Mountain' and row['Year (AD)'] =='2011/12'  and row['Sub-Indicator']==alldieses):
                My_Mountain_2011 = My_Mountain_2011 + row['Value']
    
            elif(row['Ecological Belt']=='Mountain' and row['Year (AD)'] =='2012/13'  and row['Sub-Indicator']==alldieses):
                My_Mountain_2012 = My_Mountain_2012 + row['Value']
    
            elif(row['Ecological Belt']=='Mountain' and row['Year (AD)']=='2013/14' and row['Sub-Indicator']==alldieses):
                My_Mountain_2013 = My_Mountain_2013 + row['Value']

        My_Mountain=[My_Mountain_2011,My_Mountain_2012,My_Mountain_2013]

        for index,row in df.iterrows():

            if(row['Ecological Belt']=='Hill' and row['Year (AD)']=='2011/12'  and row['Sub-Indicator']==alldieses):
                My_Hill_2011 = My_Hill_2011 + row['Value']
    
            elif(row['Ecological Belt']=='Hill' and row['Year (AD)']=='2012/13'  and row['Sub-Indicator']==alldieses):
                My_Hill_2012 = My_Hill_2012 + row['Value']
    
            elif(row['Ecological Belt']=='Hill' and row['Year (AD)']=='2013/14' and row['Sub-Indicator']==alldieses):
                My_Hill_2013 = My_Hill_2013 + row['Value']

        My_Hill=[My_Hill_2011,My_Hill_2012,My_Hill_2013]


        for index,row in df.iterrows():

            if(row['Ecological Belt']=='Terai' and row['Year (AD)']=='2011/12'  and row['Sub-Indicator']==alldieses):
                My_Terai_2011 = My_Terai_2011 + row['Value']
    
            elif(row['Ecological Belt']=='Terai' and row['Year (AD)']=='2012/13'  and row['Sub-Indicator']==alldieses):
                My_Terai_2012 = My_Terai_2012 + row['Value']
    
            elif(row['Ecological Belt']=='Terai' and row['Year (AD)']=='2013/14' and row['Sub-Indicator']==alldieses):
                My_Terai_2013 = My_Terai_2013 + row['Value']

        My_Terai=[My_Terai_2011,My_Terai_2012,My_Terai_2013]
        st.subheader('*Total number of {} found in nepal from 2011 to 2014'.format(alldieses))
        plt.figure(figsize=(20,10))
        ax=plt.gca()
        myx=np.arange(3)
        width=0.3
        rects1=ax.bar(myx-width/2,My_Mountain,width,label='In Mountain')
        rects2=ax.bar(myx+width/2,My_Hill,width,label='In Hill')
        rects3=ax.bar(myx+width/2+width,My_Terai,width,label='In Terai')
        ax.legend()
        ax.set_xlabel('Year',fontsize=20)
        ax.set_ylabel('Total number of {} Cases'.format(alldieses),fontsize=20)
        ax.set_xticks(myx)
        ax.set_title('Total number of {} found in nepal from 2011 to 2014'.format(alldieses),fontsize=25)
        ax.set_xticklabels(year)

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)
        autolabel(rects3)
        st.pyplot()

    st.sidebar.subheader('Check Your District')
    district=list(set(df['District Name']))
    district.sort()
    mydistrict=['None Selected']+district
    st.sidebar.text('**Select the district and diseases and then press show to view the data')

    jila = st.sidebar.selectbox("Select the district",mydistrict)
    
    if jila is not 'None Selected':
        rog = st.sidebar.selectbox("Select The diseases",myDieses)
        btn = st.sidebar.button('Show',key='btn')
        if rog is not 'None Selected' and btn:
            myjila=np.zeros(3)
            myjila_2011=0
            myjila_2012=0
            myjila_2013=0
            for index,row in df.iterrows():
                if (row['District Name']== jila  and row['Year (AD)']=='2011/12'  and row['Sub-Indicator']==rog):
                    myjila_2011=row['Value']
                elif (row['District Name']== jila and row['Year (AD)']=='2012/13'  and row['Sub-Indicator']==rog):
                    myjila_2012=row['Value']
                elif (row['District Name']== jila and row['Year (AD)']=='2013/14'  and row['Sub-Indicator']==rog):
                    myjila_2013=row['Value']
            myjila=[myjila_2011,myjila_2012,myjila_2013]

        
            st.subheader('*{} in {} from 2011/12 to 2013/2014'.format(rog,jila))
            st.markdown('Hover over red circle to see the value')
            p=figure(title='District {}'.format(jila),x_range=year,x_axis_label='year',plot_height=800,plot_width=800,y_axis_label='{} Count'.format(rog),tools=[HoverTool(tooltips='@y')])
            p.line(year,myjila,color='black')
            p.circle(year,myjila,size=12,color='red')
            st.bokeh_chart(p)
    
    if st.sidebar.checkbox('**Show the dataset',False):
        st.subheader('Diseases datasets')
        st.write(df)
    
        




            
if __name__ == "__main__":
    main()
