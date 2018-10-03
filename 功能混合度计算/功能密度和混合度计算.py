import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#df=pd.read_excel('entropy1000.xlsx')
"""
计算功能混合度和密度，待优化封装
"""
def calPOI(begin,count,df):
    df_cal=df.iloc[:,range(begin-1,begin-1+count)]
    df_cal['sum']=df_cal.apply(lambda x:x.sum(),axis=1)
    df_cal['entropy']=0
    for j in range(len(df_cal)):
        entropy=0
        for i in range(begin-1,begin-1+count):
#            num=df_cal.iloc[j,i]
            if df_cal.iloc[j,i]:
                p=df_cal.iloc[j,i]/df_cal['sum'].loc[j]
                lnp=np.log(p)
                sin_etp=-p*lnp
            else:
                continue
            entropy+=sin_etp
        df_cal['entropy'].loc[j]=entropy
        print('正在计算第{}行，值为{}'.format(j+1,entropy))
    return df_cal


"""
绘制散点图
"""
def plot_scatter():
    fig_scatter=plt.figure(figsize=(8,4))
    df_plot=df[df['average']>0][['average','公司企']]
    fig_q1_1 = plt.figure(figsize = (8,4))
    plt.scatter(df_plot['average'],df_plot['公司企'])
    plt.show()

if __name__=='__main__':

	"""
	基本参数修改
	"""

	#文件名修改(xx.xlsx)
	filename=''
	#表名(Sheet1)
	sheetname='Sheet1'
	#待计算列(包头不包尾，从0开始)
	begin=1
	end=13
	#输出文件名
	outputname='功能.xlsx'

	"""
	开始计算
	"""

    df=pd.read_excel(filename,sheetname=sheetname)
    df_cal=calPOI(begin,end,df)
    df['sum']=df_cal['sum']
    df['entropy']=df_cal['entropy']
    df.to_excel(outputname)
    
    










