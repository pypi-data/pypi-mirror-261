# WebSearch



> Python module allowing you to do various searches for links on the Web.


[![Python application](https://github.com/iTeam-S/WebSearch/actions/workflows/python-test.yml/badge.svg)](https://github.com/iTeam-S/WebSearch/actions/workflows/python-test.yml)
[![Publish](https://github.com/iTeam-S/WebSearch/actions/workflows/pip-upload.yml/badge.svg)](https://github.com/iTeam-S/WebSearch/actions/workflows/pip-upload.yml)

[![PyPI - Version](https://img.shields.io/pypi/v/websearch-python?style=for-the-badge)](https://pypi.org/project/websearch-python/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/websearch-python?label=DOWNLOADS&style=for-the-badge)](https://pypi.org/project/websearch-python/)



## Installation

```s
pip3 install websearch-python
```
**OR** you can install dev version
```s
pip3 install https://github.com/iTeam-S/WebSearch/archive/refs/heads/main.zip
```

## Use

### Quick Start as Module

```python
from websearch import WebSearch as web
for page in web('iTeam-$').pages[:2]:
   print(page)
```

```
[RESULTS]

 https://iteam-s.mg/
 https://github.com/iTeam-S
```


### Quick Start as Webserver

```s
# run webserver 
websearch --host 0.0.0.0 --port 7845
```

**OR**

```s
# run webserver 
python -m websearch --host 0.0.0.0 --port 7845
```

```s
# requests contents
curl http://0.0.0.0:7845/pages/botoravony+arleme
```

 ```json
 [
   "https://portfolio.iteam-s.mg/?id=2",
   "https://portfolio.iteam-s.mg/libs/cv/arleme.pdf",
   "https://madagascar.webcup.fr/team-webcup/iteams"
 ]
```

### Use Deployed Version
```s
curl https://websearch-python.herokuapp.com/pages/botoravony+arleme
```

__________________________

<details>
   <summary style='font-size:24'>  FULL DOCUMENTATION </summary>

### Initialization

```python
from websearch import WebSearch
web = WebSearch('Gaetan Jonathan BAKARY')
```
You can pass a `list` for mutliple keyword.

```python
web = WebSearch(['Gaetan Jonathan BAKARY', 'iTeam-S'])
```
You can also specify a `website` as a reference.

```python
web = WebSearch('Gaetan Jonathan', site='iteam-s.mg')
```


### Webpages results

```python
from websearch import WebSearch
web = WebSearch('Gaetan Jonathan BAKARY')
webpages = web.pages
for wp in webpages[:5]:
   print(wp)
```

```
[RESULTS]

   https://mg.linkedin.com/in/gaetanj
   https://portfolio.iteam-s.mg/?u=gaetan
   https://github.com/gaetan1903
   https://medium.com/@gaetan1903
   https://gitlab.com/gaetan1903
```


### Images results

```python
from websearch import WebSearch
web = WebSearch('Gaetan Jonathan BAKARY')
webimages = web.images
for im in webimages[:5]:
   print(im)
```

```
[RESULTS]

   https://tse3.mm.bing.net/th?id=OIP.-K25y8TqkOi9UG_40Ti8bgAAAA
   https://tse1.mm.bing.net/th?id=OIP.yJPVcDx6znFSOewLdQBbHgHaJA
   https://tse3.mm.bing.net/th?id=OIP.7rO2T_nDAS0bXm4tQ4LKQAHaJA
   https://tse2.mm.bing.net/th?id=OIP.IUIEkGQVzYRKaDA7WeeV7QHaEF
   https://tse3.explicit.bing.net/th?id=OIP.OmvVnMIVu2ZdNZHZzJK_hgAAAA
```


### PDF results

```python
from websearch import WebSearch
web = WebSearch('Math 220')
pdfs = web.pdf
for pdf in pdfs[:5]:
   print(pdf)
```

```
[RESULTS]

   https://www.coconino.edu/resources/files/pdfs/registration/curriculum/course-outlines/m/mat/mat_220.pdf
   https://www.jmu.edu/mathstat/Files/ALEKSmatrix.pdf
   https://www.jjc.edu/sites/default/files/Academics/Math/M220%20Master%20Syllabus%20SP18.pdf
   https://www.sonoma.edu/sites/www/files/2018-19cat-11math.pdf
   https://www.svsd.net/cms/lib5/PA01001234/Centricity/Domain/1009/3.3-3.3B-Practice-KEY.pdf
```

To prevent the search for attachments with format verification, set `verif=False`, which is `True` by default.

Format verification is presented [here](https://github.com/iTeam-S/WebSearch/pull/4)

```python
from websearch import WebSearch
web = WebSearch('Math 220', verif=False)
```


### DOCX results
```python
from websearch import WebSearch:
web = WebSearch('python')
words = web.docx
for word in words[:3]:
   print(word)
```

```
[RESULTS]

   https://www.ocr.org.uk/Images/572953-j277-programming-techniques-python.docx
   https://www.niu.edu/brown/_pdf/physics374_spring2021/l1-19-21.docx
   https://ent2d.ac-bordeaux.fr/disciplines/mathematiques/wp-content/uploads/sites/3/2017/09/de-Scratch-%C3%A0-Python.docx
```


### XLSX results
```python
from websearch import WebSearch:
web = WebSearch('datalist')
excels = web.xlsx
for excel in excels[:3]:
   print(excel)
```

```
[RESULTS]

   https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/979255/Detailed_Single_Data_List_-_2021-2022.xlsx
   https://www.jaist.ac.jp/top/data/list-achievement-research-e.xlsx
   https://img1.wsimg.com/blobby/go/bed8f8d7-d6c2-488d-9aa3-5910e18aa8d2/downloads/Datalist.xlsx
```


### PPTX results
```python
from websearch import WebSearch:
web = WebSearch('Leadership')
powerpoints = web.pptx
for powerpoint in powerpoints[:3]:
   print(powerpoint)
```

```
[RESULTS]

   https://www.plainviewisd.org/cms/lib6/TX01918200/Centricity/Domain/853/Leadership%20Behav.%20Styles.pptx
   https://www.yorksandhumberdeanery.nhs.uk/sites/default/files/leadership_activity_and_msf.pptx
   https://www.itfglobal.org/sites/default/files/node/resources/files/Stage%203.1%20Powerpoint.pptx
```


### ODT results
```python
from websearch import WebSearch
web = WebSearch('Finance')
documents = web.odt
for doc in documents[:2]:
   print(doc)
```

```
[RESULTS]
   https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/970748/Green_Finance_Report.odt
   https://iati.fcdo.gov.uk/iati_documents/3678707.odt
  
```

### ODS results
```python
from websearch import WebSearch
web = WebSearch('Commerce')
documents = web.ods
for doc in documents[:2]:
   print(doc)
```

```
[RESULTS]
http://www.justice.gouv.fr/art_pix/Stat_RSJ_12.7_Civil_Les_tribunaux_de_commerce.ods
https://www.insee.fr/fr/metadonnees/source/fichier/Precision-principaux-indicateurs-crise-sanitaire-2020.ods
```

### ODP results
```python
from websearch import WebSearch
web = WebSearch('Renaissance')
documents = web.odp
for doc in documents[:2]:
   print(doc)
```

```
[RESULTS]
http://ekladata.com/9sHTcbLYfwbNGKU9cpnZXjlsbfA/17-Art-Renaissance.odp
https://www.college-yvescoppens-malestroit.ac-rennes.fr/sites/college-yvescoppens-malestroit.ac-rennes.fr/IMG/odp/diapo-presentation-voyage-5e.odp
```

### KML results
```python
from websearch import WebSearch
web = WebSearch('Madagascar')
maps = web.kml
for map in maps[:3]:
   print(map)
```

```
[RESULTS]
http://www.hydrosciences.fr/sierem/kmz_files/MGPLGRA.kml
https://www.ngoaidmap.org/downloads?doc=kml&name=association-intercooperation-madagascar-aim_projects&partners%5B%5D=6160&sectors%5B%5D=1&status=active
https://ngoaidmap.org/downloads?doc=kml&name=nemp-madagascar-cyclone-enawo-response_projects&projects%5B%5D=20655&status=active
```

### CUSTOM results

For other extensions, not present, use the `custom` function

Second arg can be taken [here](https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)

```python
from websearch import WebSearch
web = WebSearch('Biologie')
ps_documents = web.custom('ps', 'application/postscript')
for doc in ps_documents[:3]:
   print(doc)
```

```
[RESULTS]

http://irma.math.unistra.fr/~fbertran/Master1_2020_2/L3Court.ps
http://jfla.inria.fr/2002/actes/10-michel.ps
https://www.crstra.dz/telechargement/pnr/ps/environnement/fadel-djamel.ps
```


### Webserver

you can deploy as webserver and send an http request

```s
   python -m websearch --host [host] --port [port]
      [*] default host : 0.0.0.0
      [*] default port : 7845 
```
Exemple for page:
   ```s
   curl http://<host>:<port>/pages/botoravony+arleme

   
   [

      "https://portfolio.iteam-s.mg/?id=2",
      "https://portfolio.iteam-s.mg/libs/cv/arleme.pdf",
      "https://madagascar.webcup.fr/team-webcup/iteams"
   ]
```

Exemple for image:
```s
   curl http://<host>:<port>/images/one+piece


   [
      "https://tse1.mm.bing.net/th?id=OIP.GlNk7idD3RCI_SYLiVzSBAHaE7",
      "https://tse2.mm.bing.net/th?id=OIP.uePUN5rwpB-7wicu1uxQcgHaFj",
      "https://tse2.mm.bing.net/th?id=OIP.dwWBU-A_6KPvvEYsL2nhVgHaFc",
      "https://tse1.mm.bing.net/th?id=OIP.5M8tKIhIWvbqGO1prhUGfAHaJ4",
      .....
      "https://tse4.mm.bing.net/th?id=OIP.uvp3efwHRLDJnUWZ5KLWCwHaE8",
      "https://tse3.mm.bing.net/th?id=OIP.d_uUoc-8R13RZ1bb76yhZgHaKp",
      "https://tse1.mm.bing.net/th?id=OIP.cBWDvspBM036p6h4DS6RTAHaFj"
   }
```

Search by extension : `curl http://<host>:<port>/<extension>/<query>`

Where extension is from this list: 

```
swf, pdf, ps, dwf, kml, kmz, gpx, hwp, htm, html, xls, xlsx,
ppt, pptx, doc, docx, odp, ods, odt, rtf, svg, tex, txt, text,
bas, c, cc, cpp, cxx, h, hpp, cs, java, pl, py, wml, wap, xml
```

Exemple : 
```s
   curl http://<host>:<port>/kml/madagascar+antananarivo


   [
      "https://ifl.francophonelibre.org/atelier/ActionOSMMG2019/wms/kml?layers=ActionOSMMG2019:MG_Antananarivo_pharmacy_point_OSM_20190427"
   ]
```

You can use the parameter `limit` to limit results
```
   curl http://<host>:<port>/images/one+piece?limit=4


   [
      "https://tse1.mm.bing.net/th?id=OIP.GlNk7idD3RCI_SYLiVzSBAHaE7",
      "https://tse2.mm.bing.net/th?id=OIP.uePUN5rwpB-7wicu1uxQcgHaFj",
      "https://tse2.mm.bing.net/th?id=OIP.dwWBU-A_6KPvvEYsL2nhVgHaFc",
      "https://tse1.mm.bing.net/th?id=OIP.5M8tKIhIWvbqGO1prhUGfAHaJ4"
   ]

```
##### Note: `site` and `verif` parameter in module can be given in url parameter
`curl http://<host>:<port>/pdf/statut?verif=false&site=iteam-s.mg`


 </details>

   
_____________________________________________________________________  
   
   
## Show your support
 Give a star 🌟 if this project helped you!
   
 [!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/gaetan1903) 
   
 
## License

MIT License

Copyright (c) 2021 [iTeam-$](https://iteam-s.mg)


___________________________________________________________________
   
 ## Contributors
![contributors GitHub](https://contrib.rocks/image?repo=iTeam-S/WebSearch)

