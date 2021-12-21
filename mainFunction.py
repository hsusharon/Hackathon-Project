from flask import Flask, render_template, request, redirect, url_for
import urllib.request
import re
import json

twoDaysWeatherSplitStr='"}}]},{"|{"|":"|","|"},{"|":{"|":\[{"|"}]},"|"}},{"|"}}]}]},{"|"}]},|"}]}]},|,|"}]}]}]}|]}]}}'
twoDaysWeatherRemoveStr=['elementValue','value','measures','Wx','dataTime','AT','description','startTime',
'endTime','time','自定義 Wx 文字','自定義 Wx 單位','自定義 CI 文字','elementName','NA','fields','id',
'contentDescription','type','String','id','datasetDescription','locationName','dataid','locationsName','geocode',
'Double','Timestamp','String','location','success','true','result','resource_id','lat','weatherElement','PoP12h',
'lon','records','locations','F-D0047-089','臺灣各縣市鄉鎮未來3天(72小時)逐3小時天氣預報','台灣',
'D0047-089','RH','T','CI','']

todayWeatherSplitStr='"}],"|{"|":"|","|":|":\[|\[|"}|]}|}|"},{"|,|"'
todayWeatherRemoveStr=['datasetDescription','locationName','elementName','startTime','endTime','parameterName',
					'parameterValue','parameterUnit','weatherElement','parameter','id','String','type','Timestamp',
					'records','true','success','fields','result','F-C0032-001','resource_id','time','百分比','C',
					'location','三十六小時天氣預報','']

def decodeUrl(url,SplitStr):
	# Because some HTTP servers only allow requests coming from common browsers as opposed to scripts
	req = urllib.request.Request(
	    url,
	    data=None,
	    headers={
	        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
	    }
	)
	res = urllib.request.urlopen(req)
	datab = res.read()
	data = datab.decode(encoding="utf-8",errors="ignore")
	list=re.split(SplitStr,data)
	return list