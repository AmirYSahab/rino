'''
Created on Jan 4, 2021

@author: amir
'''
from rinexReader import __rinex__ 
import datetime

if __name__ == '__main__':
    year = input('year />:')#2002
    month = input('month />:')
    day = input('day />:')
    n_days = input('number of days you need to download />:')
    email = input('Input the registered email to ftps://gdc.cddis.eosdis.nasa.gov/ />:')
    # read rinex
    dtime = datetime.datetime.strptime('{}-{}-{}'.format(year,month,day),"%Y-%m-%d")
    
    rinex = __rinex__()
    
    rnxData = [None]*n_days
    for day_ in range(n_days):
        d = dtime + datetime.timedelta(days = day_)
        
        # read rinex
        url = rinex.generate_url(leo = 'champ', date = (d.year,d.month,d.day))
        rinex.download(url=url, email = email)
        
        file_path = '{}/{}'.format(rinex.download_path,url.split(sep='/')[-1])
        rinex.unzip(file_path)
        
        rinex.hatanaka2rinex()
        
        rinex.read(rinex.path)
        
        rnxData[day_] = rinex.data.observations
        
        rinex_interval = rinex.data.header['interval']
        
    print('rinex data is downloaded and read in rnxData for {} day/s'.format(len(rnxData)))
    print('rinex.data.observations has keys: {}'.format(rinex.data.observations.keys()))
    print('rinex.data.observations["help"]:{}'.format(rinex.data.observations['help']))