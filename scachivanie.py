import requests
flag=True
count=0

while flag :
  if count==0 :
     a = requests.get('https://stepik.org/media/attachments/course67/3.6.3/835329.txt').text
     count+=1
  else :
      link= 'https://stepik.org/media/attachments/course67/3.6.3/'+a

      a=requests.get(link).text
      count +=1
      if 'We' in a :
          print(a)
          break

