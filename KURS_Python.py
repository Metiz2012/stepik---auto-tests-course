residence_limit= 90
shengen_constraint=180
visits= [[1,10], [30,54], [60,89], [120,159]]  # ПРОМЕЖУТКИ ПРЕБЫВАНИЯ
total_time_in_es =0                            # начальное значение
for visit in visits:
      total_time_in_es += visit[1]- visit[0]+1

overstay_time=total_time_in_es-residence_limit
print ( 'Вы привысили время прибывания',overstay_time)
assert (overstay_time==10+25+30+40-residence_limit)